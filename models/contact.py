from utils.db import db  # importamos la instancia de SQLAlchemy

class Contact(db.Model):  # creamos la clase Contact, heredando de db.Model
    id = db.Column(db.Integer, primary_key=True)  # definimos las columnas de la tabla
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, fullname, email, phone):  # definimos el constructor de la clase
        self.fullname = fullname  # asignamos los valores recibidos a los atributos de la instancia
        self.email = email
        self.phone = phone
