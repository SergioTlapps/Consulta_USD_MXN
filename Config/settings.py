# ----------------------------------------------------
# settings.py
# ----------------------------------------------------
#En este arcivho  centrliza toda la informacion del 
#Proyectoo.
#Se funcion es leer las variables almacenadas en el
#archivo .env, para que el resto del sistema pueda
#utilizarlas
#Y al igual si mañana cambia un URL, USuario o 
#Contraseña, unicamente modificamos el archjivo 
#.env y no el codigo fuente.

#-------------------------------------------------

import os # Nos permite "acceder" a las varibles del sistema y del archivo .envv
from dotenv import load_dotenv # nos permite cargar las variables del archivo.env

#cargar variablles .env
load_dotenv()
# ----------------------------------------------------
# Configuración SAP Service Layer
# ----------------------------------------------------
#URL principal de SAP
SAP_URL = os.getenv(
    "SAP_URL"
)

#DB SAP
SAP_COMPANY = os.getenv(
    "SAP_COMPANY"
)

#USER SAP
SAP_USER = os.getenv(
    "SAP_USER"
)

#PASSWORD SAP
SAP_PASSWORD = os.getenv(
    "SAP_PASSWORD"
)

# ----------------------------------------------------
# Configuración Correo
# ----------------------------------------------------

#CORREO DONDE SE ENVIARAN LOS REPORTES
EMAIL_USER = os.getenv(
    "EMAIL_USER"
)

#CONTRASEÑA O APP PASSWORD DEL CORREO 
EMAIL_PASSWORD = os.getenv(
    "EMAIL_PASSWORD"
)

#CORREO QUE RECIBIRA ALERTAR DE ERRORES
MONITOR_EMAIL = os.getenv(
    "MONITOR_EMAIL"
)