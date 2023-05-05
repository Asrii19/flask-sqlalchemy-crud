from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI

# Importamos la librería Flask para crear nuestra aplicación web
from flask import Flask

# Creamos la instancia de nuestra aplicación
app = Flask(__name__)

# Asignamos una clave secreta para nuestra aplicación
app.secret_key = 'mysecret'

# Imprimimos la conexión a la base de datos que tenemos configurada
print(DATABASE_CONNECTION_URI)

# Configuramos la base de datos que vamos a utilizar para nuestra aplicación
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Configuramos el tiempo máximo de caché a 0 para evitar problemas de actualización
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Inicializamos la conexión a nuestra base de datos utilizando la librería SQLAlchemy
SQLAlchemy(app)

# Registramos la ruta y las funciones de nuestro blueprint 'contacts'
app.register_blueprint(contacts)

