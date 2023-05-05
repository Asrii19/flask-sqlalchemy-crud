# Importar los módulos necesarios para la aplicación
from flask import Blueprint, render_template, request, redirect, url_for, flash

# Importar el modelo Contact desde el archivo contact.py
from models.contact import Contact

# Importar el objeto db desde el archivo db.py
from utils.db import db

# Crear el objeto blueprint llamado 'contacts'
contacts = Blueprint("contacts", __name__)

# Crear una ruta que renderice la página principal de la aplicación y muestre todos los contactos almacenados en la base de datos
@contacts.route('/')
def index():
    contacts = Contact.query.all() # Obtener todos los contactos de la base de datos
    return render_template('index.html', contacts=contacts) # Renderizar la página principal y pasar los contactos como argumento

# Crear una ruta que permita agregar un nuevo contacto a la base de datos
@contacts.route('/new', methods=['POST'])
def add_contact():
    if request.method == 'POST':

        # Obtener los datos del formulario enviado
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']

        # Crear un nuevo objeto Contact con los datos recibidos del formulario
        new_contact = Contact(fullname, email, phone)

        # Agregar el nuevo contacto a la base de datos y confirmar la operación
        db.session.add(new_contact)
        db.session.commit()

        # Mostrar un mensaje de éxito en la siguiente petición
        flash('Contact added successfully!')

        # Redirigir a la página principal
        return redirect(url_for('contacts.index'))

# Crear una ruta que permita actualizar un contacto existente en la base de datos
@contacts.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    # Obtener el contacto correspondiente al id recibido como argumento
    contact = Contact.query.get(id)

    if request.method == "POST":
        # Obtener los nuevos datos del contacto desde el formulario y actualizarlos en la base de datos
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()

        # Mostrar un mensaje de éxito en la siguiente petición
        flash('Contact updated successfully!')

        # Redirigir a la página principal
        return redirect(url_for('contacts.index'))

    # Renderizar la página de actualización del contacto y pasar el objeto Contact como argumento
    return render_template("update.html", contact=contact)

# Crear una ruta que permita eliminar un contacto de la base de datos
@contacts.route("/delete/<id>", methods=["GET"])
def delete(id):
    # Obtener el contacto correspondiente al id recibido como argumento
    contact = Contact.query.get(id)

    # Eliminar el contacto de la base de datos y confirmar la operación
    db.session.delete(contact)
    db.session.commit()

    # Mostrar un mensaje de éxito en la siguiente petición
    flash('Contact deleted successfully!')

    # Redirigir a la página principal
    return redirect(url_for('contacts.index'))

# Crear una ruta que renderice la página Acerca de
@contacts.route("/about")
def about():
    return render_template("about.html")
