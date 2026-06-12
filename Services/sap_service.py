# ----------------------------------------------------
# sap_service.py
# ----------------------------------------------------
#esta clase se encarga de interactuar con las vistas de sap
#
#-Exponer vistas
#-Cosultar vistas
#-Obtener info mxn y usd

import requests


#Configuracion del sistema 
from Config.settings import SAP_URL
#from Config.views import (
#    VISTAS_USD, VISTAS_MXN
#    ) 

# ------------------------------------------------
    # Exponer Vista SAP
    # ------------------------------------------------
    # SAP requiere exponer una vista antes de poder
    # consultarla.
    #
    # Esto automatiza exactamente la petición POST
    # que realizábamos manualmente en Postman:
    #
    # POST
    # /b1s/v1/SQLViews('NOMBRE_VISTA')/Expose
    #
    # Recibe:
    #
    # session_id -> sesión obtenida en Login
    # view_name -> nombre de la vista SAP
    #
    # No devuelve información.
    # Si algo falla genera excepción.
    # ------------------------------------------------

class SAPService:
    @staticmethod
    def expose_view(session_id, view_name):
        #SAP recibe la sesion por medio de la Cookie que se llama B1SESSION
        headers = {
            "Cookie": f"B1SESSION={session_id}"
        }
        #Expose post
        respuesta = requests.post(
            f"{SAP_URL}/b1s/v1/SQLViews('{view_name}')/Expose",
            headers=headers,
            verify=False,
            timeout=30
        )
        
        #Si SAP devuelve un error 401,400,500, etc
        #Se genera un aexepxion en automatico
        respuesta.raise_for_status
        
        
        
    #--------------------------------
    #obtener datos sap GET
    #--------------------------------
    
    #Una vez expuesta la vista podemos hacer una consulta tipo GET
    @staticmethod
    def get_view_data(session_id, view_name):
        #Al hacer el get, sap vuelve a consultar la cookie 
        headers = {
            "Cookie": f"B1SESSION={session_id}"
        }
        
        respuesta = requests.get(
            f"{SAP_URL}/b1s/v1/view.svc/{view_name}",
            headers=headers,
            verify=False,
            timeout=30
        )
        
        respuesta.raise_for_status
        resultado = respuesta.json()
        
        return resultado
    