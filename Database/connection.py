# ----------------------------------------------------
# connection.py
# ----------------------------------------------------
#Esta es el encargado de conectarse a SAP
#
#Lo que vamos a realizar aqio es el 
#-LOGIN , OBTENER SESION ID
#POR EL PRINCIPIO DE SOLID

#Libreria para realizar peticion a HTTP, algo similar a postman 
import requests

#Importamos config del sistama
from Config.settings import (
    SAP_URL,
    SAP_COMPANY,
    SAP_USER,
    SAP_PASSWORD,
)

#Clase para autenticacion sap
#LOGIN SAP si al autenticarse uno, si las credenciales son correctas devuelve el session id
#DEspues ese session id sera utlizado para exponer vistar y realizar consultas

#Y el class, es un molde que nos va ayudar para organizar codigo y datos relazionados
class SAPConnection: 
    @staticmethod
    def login():
        
            # Datos que SAP espera recibir
            # exactamente igual que en postman
        datos = {

            #DB SAP
            "CompanyDB": SAP_COMPANY,
            #useR SAP
            "UserName": SAP_USER,
            #Contraseña SAP
            "Password": SAP_PASSWORD
        }
        
        #Aqui es la peticion POST hacia el endpoint de login
        respuesta = requests.post (
            f"{SAP_URL}/b1s/v1/Login", #ENDPOINT login SAP
            
            #Enviar datos en formato Json
            json=datos,
            
            # Ignora validaciones SSL internas
            verify=False,
            
            #Tiempo max espera
            timeout=30
        )
    
        #Si SAp devuelve 200 - continua
        #si es 401 -> Error de AUTEN
        #Y 500 error del server
        
        #Exepcion autotomatica de protocolos
        respuesta.raise_for_status()
        
        resultado = respuesta.json() #Convertir la respuesta a json
        # Ejemplo de respuesta:
        #
        # {
        #     "SessionId":
        #     "f2ef5555-6555-5551-8000..."
        # }
        print(resultado)
        session_id = resultado[
            "SessionId"
        ]
        
        #Regresar al sessionid
        return session_id