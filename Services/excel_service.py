# ----------------------------------------------------
# excel_service.py
# ----------------------------------------------------

class ExcelService:
    @staticmethod
    def generar_excel(dataframe, nombre_archivo):
        ruta = f"Reports/{nombre_archivo}"
        dataframe.to_excel(
            ruta,
            index=False
        ) 
        return ruta
    