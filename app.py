from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('landmarks.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route for the homepage displaying images
@app.route('/')
def home():
    conn = get_db_connection()
    landmarks = conn.execute('SELECT * FROM landmarks').fetchall()
    conn.close()
    return render_template('index.html', landmarks=landmarks)

# Route for the map page
@app.route('/map')
def map_page():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
