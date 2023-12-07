from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Configure PostgreSQL connection
db_config = {
    'host': 'db',
    'user': 'postgres_user',    # Same as in docker-compose.yml
    'password': 'password',     # Same as in docker-compose.yml
    'dbname': 'db'
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
    app.run(debug=True, host='0.0.0.0')