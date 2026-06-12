
# ----------------------------------------------------
# app.py
# ----------------------------------------------------
# Punto de entrada principal del sistema.
#
# Desde aquí se ejecutará todo el flujo:
#
# Login
# ↓
# Obtener datos SAP
# ↓
# Generar Excel
# ↓
# Generar correo
# ↓
# Enviar correo
#
#Clase encargada del login
from Database.connection import SAPConnection
#Clase encargada del consultar vistas
from Services.sap_service import SAPService
#Nombre de la vista
from Config.views import VISTA_MXN,VISTA_USD
#Pandas
from Services.report_service import ReportService
from Services.excel_service import ExcelService

# --------------------------------------------
# Obtener SessionId
# --------------------------------------------
session_id = SAPConnection.login()
print(
    f"Sesion obtenida: {session_id}"
)


# --------------------------------------------
# Exponer Vista USD
# --------------------------------------------

SAPService.expose_view (
    session_id,
    VISTA_USD
)
print(
    "Vista USD expuesta correctamente"
)


# --------------------------------------------
# Exponer Vista USD
# --------------------------------------------
datos = SAPService.get_view_data(
    session_id,
    VISTA_USD
)

# Convertir respuesta SAP a DataFrame
dataframe = ReportService.json_to_dataframe(
    datos #investi
)

#Tatales en tabla
totales = ReportService.calcular_totales(
    dataframe
)
print("\n ==== Totales USD ===")

for concepto, valor in totales.items():
    print(
        f"{concepto}: {valor:,.2f}"
    )


#----------------------------------
#Report excel
#----------------------------------
ruta_excel = ExcelService.generar_excel(dataframe,
    "Reporte_USD.xlsx"
)
print(f"\Excel generado: {ruta_excel}")







print(dataframe)


print(
    "Consulta realizada correctamente"
)

#print(
#    datos
#)

print(type(datos))

