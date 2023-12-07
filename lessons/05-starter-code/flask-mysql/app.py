from flask import Flask
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db_config = {
    'host': 'db',
    'user': 'user',
    'password': 'password',
    'database': 'db'
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