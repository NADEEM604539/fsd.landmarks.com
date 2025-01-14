import sqlite3

# Create database and table for storing landmarks
def create_db():
    conn = sqlite3.connect('landmarks.db')
    cursor = conn.cursor()

    # Create the landmarks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS landmarks (
            id INTEGER PRIMARY KEY,
            image_filename TEXT,
            name TEXT,
            latitude REAL,
            longitude REAL,
            description TEXT
        )
    ''')

    # Add some sample data
    cursor.executemany('''
        INSERT INTO landmarks (image_filename, name, latitude, longitude, description)
        VALUES (?, ?, ?, ?, ?)
    ''', [
        ('landmark1.png', 'Landmark 1', 31.4337, 73.0858, 'IQBAL STADIUM. International Cricket Stadium where many historic matches played.'),
        ('landmark2.png', 'Landmark 2', 31.4187, 73.0791, 'Clock Tower of Faisalabad. Manchester of Pakistan.'),
        ('landmark3.png', 'Landmark 3', 31.418715, 73.079109, 'Canal Road. showing how standard roads and markets along with Resturants'),
        ('landmark4.png', 'Landmark 4', 31.418715,  73.079109, 'Very famous chowk of Faisalabad giving a beautiful view in the center of city.'),
        ('landmark5.png', 'Landmark 5', 31.4294 , 73.0750, 'Agriculte university the Asia\'s lagest city.')
    ])

    conn.commit()
    conn.close()

# Run the function to create the database
create_db()
