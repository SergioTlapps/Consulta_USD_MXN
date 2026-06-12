# ----------------------------------------------------
# report_service.py
# ----------------------------------------------------
# Esta clase se encarga de procesar la información
# obtenida desde SAP.
#Por ejemplo convertir de JSON a DataFrame por medio pandas
#Calculos totales
#preparar excel 
#preparar indo correo


import pandas as pd #as equivale a import y pd pandas


class ReportService:
    @staticmethod
    def json_to_dataframe(datos_json): #parametro json, recibe la info
        dataframe = pd.DataFrame( # en dataframe se guarda la tabla creada
            datos_json["value"] #llaves del diccionario osea de la vista y devuelve cliente ; c001 example
            #INVESTIGRRRRRRRRR---------------------
        )
        
        return dataframe

    # ------------------------------------------------
    # Calcular Totales
    # ------------------------------------------------
    # Este método recibe un DataFrame y calcula
    # la suma total de todas las columnas
    @staticmethod
    def calcular_totales(dataframe):
        totales ={
            "No Vencido": dataframe["No Vencido"].sum(), #Entre lso corchetes es como crear un diccionario 
            
            "0 - 15 Días": dataframe["0 - 15 Días"].sum(),
            
            "16 - 30 Días": dataframe["16 - 30 Días"].sum(),
            
            "31 - 45 Días": dataframe["31 - 45 Días"].sum(),
            
            "46 - 60 Días": dataframe["46 - 60 Días"].sum(),
            
            "61 - 90 Días": dataframe["61 - 90 Días"].sum(),
            
            "+91 Días": dataframe["+91 Días"].sum(),
            
            "Saldo Total Pendiente":dataframe["Saldo Total Pendiente"].sum()
        }
        return totales