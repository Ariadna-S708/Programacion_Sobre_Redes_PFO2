import sqlite3
import bcrypt
from flask import Flask, request, jsonify

app = Flask(__name__)


# Configuraccion de la base de datos
DB_NAME = 'usuarios.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

init_db()


# Endpoint de registro de usuario
@app.post('/registro')
def registro():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validar campos
    if not username or not password:
        return jsonify({'error': 'Faltan campos. El usuario y la contraseña son obligatorios.'}), 400
    
    # Verificar usuario existente
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE username = ?', (username,))
        if cursor.fetchone():
            return jsonify({'error': 'El usuario ya existe.'}), 400
    
    # Encriptar contraseña
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Guardar usuario
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, password_hash))
            conn.commit()
            return jsonify({'mensaje': 'Usuario registrado exitosamente.'}), 201
    except sqlite3.Error:
        return jsonify({'mensaje': 'Error al registrar el usuario.'}), 500


# Endpoint de login
@app.post('/login')
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validar campos
    if not username or not password:
        return jsonify({'error': 'Faltan campos. El usuario y la contraseña son obligatorios.'}), 400
    
    # Verificar usuario existente
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE username = ?', (username,))
        usuario = cursor.fetchone()

    if not usuario:
        return jsonify({'error': 'Usuario no encontrado.'}), 404

    # Verificar contraseña
    if not bcrypt.checkpw(password.encode('utf-8'), usuario[2]):
        return jsonify({'error': 'Contraseña incorrecta.'}), 401
    
    return jsonify({'mensaje': 'Login exitoso'}), 200


# Endpoint de tareas
@app.get('/tareas')
def tareas():
    return """
    <html>
        <body>
            <h1>Bienvenido a la gestión de tareas</h1>
            <p>¡Aquí puedes administrar tus tareas!</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)