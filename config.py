from dotenv import load_dotenv
import os

#CARGA LAS VARIABLES DE ENTORNO DEL .env
load_dotenv()

#SE ALMACENAN EN VARIABLES
user = os.environ["USER"]
password = os.environ["PASSWORD"]
host = os.environ["HOST"]
database = os.environ["DATABASE"]
server = os.environ["SERVER"]

#SE GENERA EL URI PARA ENTRAR AL PROYECTO
DATABASE_CONNECTION_URI = f'{server}://{user}:{password}@{host}/{database}'