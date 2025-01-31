from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

DATABASE_CONFIG = {
    'dbname': 'flask-postgres',
    'user': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': 5432
}

def get_db_connection():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    return conn

def create_user_table():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        cursor.close()
        conn.close()
        print('Table user created successfully')
    except Exception as e:
        print(f'Error creating table: {e}')

create_user_table()

@app.get('/users')
def get_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        column_names = [desc[0] for desc in cursor.description]

        users = []
        for row in cursor.fetchall():
            # user = dict(zip(column_names, row))
            user = {
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'created_at': str(row[3])
            }
            users.append(user)

        cursor.close()
        conn.close()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({ 'error': str(e) }), 500
    
@app.post('/users')
def create_user():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO users(name, email) VALUES (%s, %s);',
            (name, email)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({ 'message': 'User created successfully' }), 201
    except Exception as e:
        return jsonify({ 'error': str(e) }), 500

if __name__ == '__main__':
    app.run(debug=True)