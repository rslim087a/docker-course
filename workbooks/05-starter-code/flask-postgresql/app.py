from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Configure PostgreSQL connection
db_config = {
    'host': os.getenv('DATABASE_HOST'),
    'user': os.getenv('DATABASE_USER'),
    'password': os.getenv('DATABASE_PASSWORD'),
    'dbname': os.getenv('DATABASE_NAME')
}

# Check for missing environment variables
for key, value in db_config.items():
    if value is None:
        raise RuntimeError(f"Environment variable for '{key}' is not set.")

@app.route('/', methods=['GET'])
def index():
    # Prepare a message with the database connection details
    connection_details = f"Database Host: {db_config['host']}, User: {db_config['user']}, Password: {db_config['password']}, Database: {db_config['dbname']}"

    try:
        conn = psycopg2.connect(**db_config)
        conn.close()
        return f"Success! Connected to an instance of PostgreSQL. You are using the env variables: {connection_details}"
    except psycopg2.Error as e:
        return f"Failed to connect to an instance of PostgreSQL. You are using the env variables: {connection_details}"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=3000)
