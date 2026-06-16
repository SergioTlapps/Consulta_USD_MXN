# ----------------------------------------------------
# connection.py
# ----------------------------------------------------
 
import requests 

#Importamos config del sistama
from Config.settings import (
    SAP_URL,
    SAP_COMPANY,
    SAP_USER,
    SAP_PASSWORD,
)

class SAPConnection: 
    @staticmethod
    def login():
        datos = { #Credenciales para poder hacer login
            "CompanyDB": SAP_COMPANY,
            "UserName": SAP_USER,
            "Password": SAP_PASSWORD
        }
        
        #Peticion POST hacia el endpoint de login
        respuesta = requests.post (
            f"{SAP_URL}/b1s/v1/Login",
            json=datos,
            verify=False, 
            timeout=30
        )
           
        respuesta.raise_for_status()
        
        resultado = respuesta.json()  
        print(resultado)
        session_id = resultado["SessionId"]
        
        return session_id