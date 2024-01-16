from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Configure PostgreSQL connection
db_config = {
    'host': 'DATABASE',
    'user': 'USER',    # Same as in docker-compose.yml
    'password': 'PASSWORD',     # Same as in docker-compose.yml
    'dbname': 'DATABASE'
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