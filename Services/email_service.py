# ----------------------------------------------------
# email_service.py
# ----------------------------------------------------

import os

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 


from Config.settings import(
    EMAIL_USER,
    EMAIL_PASSWORD
)

class EmailService:
    @staticmethod
    def enviar_correo(
        destinatario,
        asunto,
        html,
        archivo_adjunto  
    ):
        mensaje = MIMEMultipart() 
        mensaje["From"] = EMAIL_USER 
        mensaje["To"] = destinatario 
        mensaje["Subject"] = asunto 
        # Agregar HTML
        mensaje.attach(
            MIMEText(
                html,
                "html"
            )
        )
        
        #Adjuntar excel
        with open(
            archivo_adjunto,
            "rb"  
        )as archivo: 
            parte = MIMEBase( 
                "application",
                "octet-stream" 
            )
            
            parte.set_payload( 
                archivo.read()
            )

        encoders.encode_base64(
            parte 
        )

        parte.add_header(
            "Content-Disposition",
            f"attachment; filename={archivo_adjunto}"
            
        )
                
        mensaje.attach(
            parte
        )
        
        #Conexion SMTP
        servidor = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )
        
        servidor.starttls() 
        
        
        servidor.login( 
            EMAIL_USER,
            EMAIL_PASSWORD
        )
        
        servidor.send_message( 
            mensaje
        )
        
        servidor.quit()
        

        
        
        