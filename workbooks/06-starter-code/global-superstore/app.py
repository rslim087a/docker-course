from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os
from datetime import datetime
import uuid
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Constants
CATEGORIES = ["Furniture", "Office Supplies", "Technology"]

# Database configuration
db_config = {
    'host': os.getenv('DATABASE_HOST'),
    'dbname': os.getenv('DATABASE_NAME'),
    'user': os.getenv('DATABASE_USER'),
    'password': os.getenv('DATABASE_PASSWORD')
}

def get_db_connection():
    return psycopg2.connect(**db_config)

def create_items_table(retries=5, delay=5):
    for _ in range(retries):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS items (
                    id VARCHAR(255) PRIMARY KEY,
                    category VARCHAR(255),
                    name VARCHAR(255),
                    price DECIMAL,
                    discount DECIMAL,
                    date TIMESTAMP
                )
            ''')
            conn.commit()
            cursor.close()
            conn.close()
            print("Database initialized successfully")
            break
        except psycopg2.OperationalError as err:
            print("Database connection failed. Retrying...")
            time.sleep(delay)
    else:
        print("Failed to connect to the database after several attempts.")



create_items_table()

class Item:
    def __init__(self, category=None, name=None, price=None, discount=None, date=None, id=None):
        self.id = id if id else str(uuid.uuid4())
        self.category = category
        self.name = name
        self.price = float(price) if price else 0.0
        self.discount = float(discount) if discount else 0.0
        self.date = datetime.strptime(date, '%Y-%m-%d') if date else datetime.now()

    def save_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO items (id, category, name, price, discount, date) 
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO UPDATE 
            SET category = EXCLUDED.category, name = EXCLUDED.name, price = EXCLUDED.price, discount = EXCLUDED.discount, date = EXCLUDED.date
        ''', (self.id, self.category, self.name, self.price, self.discount, self.date))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_all_items():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, category, name, price, discount, date FROM items')
        items = [Item(id=row[0], category=row[1], name=row[2], price=row[3], discount=row[4], date=row[5].strftime('%Y-%m-%d')) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return items

    @staticmethod
    def get_item_by_id(item_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, category, name, price, discount, date FROM items WHERE id = %s', (item_id,))
        row = cursor.fetchone()
        item = Item(id=row[0], category=row[1], name=row[2], price=row[3], discount=row[4], date=row[5].strftime('%Y-%m-%d')) if row else None
        cursor.close()
        conn.close()
        return item

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        form_data['date'] = form_data['date'] if form_data['date'] else datetime.now().strftime('%Y-%m-%d')
        item = Item(**form_data)
        item.save_to_db()
        return redirect(url_for('inventory'))

    item_id = request.args.get('id')
    item = Item.get_item_by_id(item_id) if item_id else Item()
    return render_template('form.html', item=item, categories=CATEGORIES)

@app.route('/inventory', methods=['GET'])
def inventory():
    items = Item.get_all_items()
    return render_template('inventory.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
