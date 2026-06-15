# ----------------------------------------------------
# report_template.py
# ----------------------------------------------------
# Esta clase se encarga únicamente de construir
# el HTML que se enviará por correo.
#
# Responsabilidades:
#
# - Crear diseño HTML
# - Mostrar totales
# - Mostrar moneda del reporte

from datetime import datetime

class ReportTemplate:

    @staticmethod
    def generar_html(
        totales,
        moneda
        
    ):
        fecha_actual = datetime.now().strftime(
            "%d/%m/%Y"
        )

        html = f"""
        <html>

        <body style="
            font-family: Arial;
            background-color:#f4f4f4;
            padding:20px;
        ">

        <div style="
            max-width:800px;
            margin:auto;
            background:white;
            padding:30px;
            border-radius:10px;
        ">

        <h1 style="
            text-align:center;
            color:#0d6efd;
        ">
            REPORTE DE ANTIGÜEDAD DE SALDOS
        </h1>
        
        <p style="font-size:18px;">
            Corte al {fecha_actual}
        </p>

        <h3 style="
            text-align:center;
            color:#555;
        ">
            Moneda: {moneda}
        </h3>

        <table
            width="100%"
            border="1"
            cellspacing="0"
            cellpadding="10"
        >

            <tr style="
                background:#0d6efd;
                color:white;
            ">
                <th>Concepto</th>
                <th>Total</th>
            </tr>

            <tr>
                <td>No Vencido</td>
                <td>${totales["No Vencido"]:,.2f}</td>
            </tr>

            <tr>
                <td>0 - 15 Días</td>
                <td>${totales["0 - 15 Días"]:,.2f}</td>
            </tr>

            <tr>
                <td>16 - 30 Días</td>
                <td>${totales["16 - 30 Días"]:,.2f}</td>
            </tr>

            <tr>
                <td>31 - 45 Días</td>
                <td>${totales["31 - 45 Días"]:,.2f}</td>
            </tr>

            <tr>
                <td>46 - 60 Días</td>
                <td>${totales["46 - 60 Días"]:,.2f}</td>
            </tr>

            <tr>
                <td>61 - 90 Días</td>
                <td>${totales["61 - 90 Días"]:,.2f}</td>
            </tr>

            <tr>
                <td>+91 Días</td>
                <td>${totales["+91 Días"]:,.2f}</td>
            </tr>

            <tr style="
                background:#f2f2f2;
                font-weight:bold;
            ">
                <td>Saldo Total Pendiente</td>
                <td>
                    ${totales["Saldo Total Pendiente"]:,.2f}
                </td>
            </tr>

        </table>

        <br>

        <p>
            Se adjunta archivo Excel con el detalle
            completo de clientes.
        </p>
        
        <hr>
        <hr>

        <p style="color:#777;">
            Este correo fue generado automáticamente por el sistema de cobranza.
        </p>

        <p style="color:#777;">
            TLapps | Departamento TI
        </p>

        </div>

        </body>

        </html>
        """

        return html