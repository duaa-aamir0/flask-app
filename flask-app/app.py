from flask import Flask, render_template, request, jsonify
import sqlite3
import hashlib
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY  # hardcoded in config (Codacy will flag this)

# --- Database setup ---
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT,
                        password TEXT
                    )''')
    conn.commit()
    conn.close()

# --- Home route ---
@app.route('/')
def index():
    return render_template('index.html')

# --- Register route ---
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password required!'}), 400

    hashed_pass = hashlib.md5(password.encode()).hexdigest()  # insecure hashing (Codacy will flag)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{hashed_pass}')")  # SQL injection risk
    conn.commit()
    conn.close()

    return jsonify({'message': f'User {username} registered successfully!'})

# --- Get users route ---
@app.route('/users')
def get_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    users = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify({'users': users})


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
