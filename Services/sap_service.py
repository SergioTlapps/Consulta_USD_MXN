# ----------------------------------------------------
# sap_service.py
# ----------------------------------------------------
import requests
from Config.settings import SAP_URL

# ------------------------------------------------
    # Exponer vista SAP
    # ------------------------------------------------

class SAPService:
    @staticmethod
    def expose_view(session_id, view_name):
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

        respuesta.raise_for_status
        
    #--------------------------------
    #obtener datos sap GET
    #--------------------------------
    
    @staticmethod
    def get_view_data(session_id, view_name):
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
    