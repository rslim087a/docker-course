from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# Configure MySQL connection
db_config = {
    'host': os.getenv('DATABASE_HOST'),
    'user': os.getenv('DATABASE_USER'),
    'password': os.getenv('DATABASE_PASSWORD'),
    'database': os.getenv('DATABASE_NAME')
}


@app.route('/', methods=['GET'])
def index():
    # Prepare a message with the database connection details
    connection_details = f"Database Host: {db_config['host']}, User: {db_config['user']}, Database: {db_config['database']}"

    try:
        conn = mysql.connector.connect(**db_config)
        conn.close()
        return f"Success! Connected to MySQL. {connection_details}"
    except mysql.connector.Error as e:
        return f"Failed to connect to MySQL. {connection_details} Error: {e}"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=3000)