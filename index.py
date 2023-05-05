from app import app
from utils.db import db

#COGE EL CONTEXTO DE LA APP Y CREA LA BASE DE DATOS
with app.app_context():
    db.create_all()

#MÉTODO MAIN (corre el programa en modo debug)
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
