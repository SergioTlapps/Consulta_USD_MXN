# ----------------------------------------------------
# excel_service.py
# ----------------------------------------------------
# Esta clase se encarga de generar archivos Excel
# a partir de DataFrames.
#
# Responsabilidades:
#
# - Crear archivos Excel
# - Guardarlos en disco
class ExcelService:
    @staticmethod
    def generar_excel(dataframe, nombre_archivo):
        #Ruta donde se guarde el excel
        ruta = f"Reports/{nombre_archivo}"
        
        #Exportar dataframe a excel
        dataframe.to_excel(
            ruta,
            index=False
        ) 
        #poenmos index false para que pandas no o agregue
        
        return ruta
    