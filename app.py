from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

# Database connection settings (replace with your actual details)
server = 'sql-hello-cloud-devops-ngiamour.database.windows.net'
database = 'sqldb-hello-cloud-devops'
username = 'sqladmin'
password = 'StrongPassword123!'
driver = '{ODBC Driver 18 for SQL Server}'

def get_db_connection():
    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    conn = pyodbc.connect(connection_string)
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT Name FROM Products')
    products = [row[0] for row in cursor.fetchall()]
    conn.close()
    
    return render_template('index.html', products=products)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/devops')
def devops():
    return render_template('devops.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
