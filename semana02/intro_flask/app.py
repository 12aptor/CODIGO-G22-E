# Importación de la clase Flask
from flask import Flask, request

# Instancia de la aplicación Flask
app = Flask(__name__)

# Creación de una ruta
@app.route('/')
def home():
    return 'Hola Flask 😎!'

@app.route('/json')
def send_json():
    return {'name': 'Flask'}

@app.route('/html')
def send_html():
    return '<button>Hola Flask 😎!</button>'

# Recibe un parámetro de la ruta
@app.route('/user/<username>')
# @app.route('/user/<int:age>') # string, int, float, path, uuid
def user(username):
    return f'Hola {username}'

@app.route('/users', methods=['GET', 'POST']) # DELETE, PUT, PATCH, OPTIONS
def users():
    method = request.method
    if method == 'GET':
        return [
            {
                'id': 1,
                'name': 'John Doe'
            },
            {
                'id': 2,
                'name': 'Jane Doe'
            }
        ]
    elif method == 'POST':
        json = request.get_json()
        return json
    
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    print(file)
    return 'Uploaded!'

# Ejecución de la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)