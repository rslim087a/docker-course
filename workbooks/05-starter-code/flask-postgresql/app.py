from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Configure PostgreSQL connection
db_config = {
    'host': os.getenv('DATABASE', 'default_host'),
    'user': os.getenv('USER', 'default_user'),
    'password': os.getenv('PASSWORD', 'default_password'),
    'dbname': os.getenv('DATABASE', 'default_db')
}

@app.route('/', methods=['GET'])
def index():
    try:
        conn = psycopg2.connect(**db_config)
        conn.close()
        return "This app is successfully connected to PostgreSQL."
    except psycopg2.Error as e:
        return "Failed to connect this application to PostgreSQL."

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
