# ----------------------------------------------------
# settings.py
# ----------------------------------------------------


import os 
from dotenv import load_dotenv 

load_dotenv()
# ----------------------------------------------------
# Configuracion SAP Service Layer
# ----------------------------------------------------

SAP_URL = os.getenv(
    "SAP_URL"
)


SAP_COMPANY = os.getenv(
    "SAP_COMPANY"
)


SAP_USER = os.getenv(
    "SAP_USER"
)


SAP_PASSWORD = os.getenv(
    "SAP_PASSWORD"
)

# ----------------------------------------------------
# Configuracion Correo
# ----------------------------------------------------


EMAIL_USER = os.getenv(
    "EMAIL_USER"
)


EMAIL_PASSWORD = os.getenv(
    "EMAIL_PASSWORD"
)



EMAIL_DESTINO = os.getenv(
    "EMAIL_DESTINO"
)