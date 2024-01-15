from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# Configure MySQL connection
db_config = {
    'host': os.getenv('DATABASE', 'default_host'),
    'user': os.getenv('USER', 'default_user'),
    'password': os.getenv('PASSWORD', 'default_password'),
    'database': os.getenv('DATABASE', 'default_db')
}


@app.route('/', methods=['GET'])
def index():
    try:
        conn = mysql.connector.connect(**db_config)
        conn.close()
        return "This app is successfully connected to MySQL."
    except mysql.connector.Error as e:
        return "You need to connect this application to MYSQL"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')