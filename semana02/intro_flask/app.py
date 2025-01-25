# Importación de la clase Flask
from flask import Flask

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

# Ejecución de la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)