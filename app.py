
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
# Clase encargada de autenticarse en SAP
from Database.connection import SAPConnection

# Clase encargada de exponer y consultar vistas SAP
from Services.sap_service import SAPService

# Nombres de las vistas configuradas
from Config.views import (
    VISTA_USD,
    VISTA_MXN
)

# Clase encargada de trabajar con Pandas
from Services.report_service import ReportService

# Clase encargada de generar Excel
from Services.excel_service import ExcelService

# Clase encargada de generar HTML
from Templates.report_template import ReportTemplate

# Clase encargada de enviar correos
from Services.email_service import EmailService



# ----------------------------------------------------
# MANEJO GLOBAL DE ERRORES
# ----------------------------------------------------
# Cualquier error que ocurra dentro del sistema
# sera capturado aqui.
# ----------------------------------------------------

try:


    # ----------------------------------------------------
    # LOGIN SAP
    # ----------------------------------------------------
    # SAP devuelve un SessionId que será utilizado
    # durante todo el proceso.
    # ----------------------------------------------------

    session_id = SAPConnection.login()

    print(
        f"\nSesion obtenida: {session_id}"
    )


    # ----------------------------------------------------
    # EXPONER VISTA USD
    # ----------------------------------------------------
    # Antes de consultar una vista SAP requiere
    # que esta sea expuesta.
    # ----------------------------------------------------

    SAPService.expose_view(
        session_id,
        VISTA_USD
    )

    print(
        "\nVista USD expuesta correctamente"
    )

    # ----------------------------------------------------
    # EXPONER VISTA MXN
    # ----------------------------------------------------
    SAPService.expose_view(
        session_id,
        VISTA_MXN
    )
    print(
        "Vista MXN expuesta correctamente"
    )

    # ----------------------------------------------------
    # OBTENER DATOS USD
    # ----------------------------------------------------
    # Se realiza la consulta GET hacia SAP.
    # ----------------------------------------------------

    datos_USD = SAPService.get_view_data(
        session_id,
        VISTA_USD
    )

    print(
        "\nConsulta SAP realizada correctamente USD"
    )

    # ----------------------------------------------------
    # OBTENER DATOS MXN
    # ----------------------------------------------------
    datos_MXN = SAPService.get_view_data(
        session_id,
        VISTA_MXN
    )
    print(
        "\nConsulta SAP realizada correctamente MXN"
    )

    # ----------------------------------------------------
    # CONVERTIR JSON A DATAFRAME
    # ----------------------------------------------------
    # SAP devuelve JSON.
    # ----------------------------------------------------

    dataframeUSD = ReportService.json_to_dataframe(
        datos_USD
    )

    dataframeMXN = ReportService.json_to_dataframe(
        datos_MXN
    )
    # ----------------------------------------------------
    # CALCULAR TOTALES
    # ----------------------------------------------------
    # Se suman todas las columnas necesarias para
    # construir el reporte ejecutivo.
    # ----------------------------------------------------

    totales_USD = ReportService.calcular_totales(
        dataframeUSD
    )

    #print(
    #    "\n==== TOTALES USD ===="
    #)

    #for concepto, valor in totales.items():
    #
    #    print(
    #        f"{concepto}: {valor:,.2f}"
    #    )
        
    # --------- MXN ---------------
    # ----
    totales_MXN = ReportService.calcular_totales(
        dataframeMXN
    )


    # ----------------------------------------------------
    # GENERAR HTML
    # ----------------------------------------------------
    # Se genera el cuerpo del correo utilizando
    # una plantilla HTML.
    # ----------------------------------------------------

    html_USD = ReportTemplate.generar_html(
        totales_USD,
        "USD"
    )

    print(
        "\nHTML generado correctamente de USD"
    )

    #--------------- MNX HTML -----------------
    html_MXN = ReportTemplate.generar_html(
        totales_MXN,
        "MXN"
    )

    print(
        "\nHTML generado correctamente de MXN"
    )

    # ----------------------------------------------------
    # GENERAR EXCEL
    # ----------------------------------------------------
    # Se genera el archivo Excel que sera adjuntado
    # en el correo
    # ----------------------------------------------------

    ruta_excel_USD = ExcelService.generar_excel(
        dataframeUSD,
        "Reporte_USD.xlsx"
    )

    print(
        f"\nExcel generado: {ruta_excel_USD}"
    )

    # -------------- MXN Excel ---------------------
    ruta_excel_MXN = ExcelService.generar_excel(
        dataframeMXN,
        "Reporte_MXN.xlsx"
    )
    print(
        f"\nExcel generado: {ruta_excel_MXN}"
    )


    # ----------------------------------------------------
    # ENVIAR CORREO USD 
    # ----------------------------------------------------
    # Se envia:
    #
    # - HTML generado
    # - Excel adjunto
    #
    # ----------------------------------------------------

    EmailService.enviar_correo(

        destinatario="shekosantana@gmail.com",

        asunto="Reporte Antiguedad de Saldos USD",

        html=html_USD,

        archivo_adjunto=ruta_excel_USD

    )

    print(
        "\nCorreo enviado correctamente USD"
    )

    # --------------- CORREO MXN --------------------
    EmailService.enviar_correo(
        destinatario="shekosantana@gmail.com",
        asunto="Reporte de Antiguedad MXN",
        html= html_MXN,
        archivo_adjunto=ruta_excel_MXN
    )
    print(
        "\nCorreo enviado correctamente MXN"
    )

except Exception as error:

    print(
        f"\nERROR EN EL SISTEMA: {error}"
    )