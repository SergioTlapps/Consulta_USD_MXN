# ----------------------------------------------------
# report_service.py
# ----------------------------------------------------


import pandas as pd #as equivale a import y pd pandas


class ReportService:
    @staticmethod
    def json_to_dataframe(datos_json): 
        dataframe = pd.DataFrame( 
            datos_json["value"] 
        )
        
        return dataframe

    # ------------------------------------------------
    # Calcular Totales
    # ------------------------------------------------

    @staticmethod
    def calcular_totales(dataframe):
        totales ={                      
            "No Vencido": dataframe["No Vencido"].sum(), 
            
            "0 - 15 Días": dataframe["0 - 15 Días"].sum(),
            
            "16 - 30 Días": dataframe["16 - 30 Días"].sum(),
            
            "31 - 45 Días": dataframe["31 - 45 Días"].sum(),
            
            "46 - 60 Días": dataframe["46 - 60 Días"].sum(),
            
            "61 - 90 Días": dataframe["61 - 90 Días"].sum(),
            
            "+91 Días": dataframe["+91 Días"].sum(), 
            
            "Saldo Total Pendiente":dataframe["Saldo Total Pendiente"].sum()
        }
        return totales