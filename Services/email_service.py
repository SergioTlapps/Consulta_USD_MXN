# ----------------------------------------------------
# email_service.py
# ----------------------------------------------------
# Clase encargada exclusivamente
# de enviar correos.
#
# Responsabilidades:
#
# - Crear mensaje
# - Adjuntar archivos
# -- Enviar correo
import os

import smtplib

from email.mime.multipart import MIMEMultipart #Base del cuerpo del correo vacio acepta todo
from email.mime.text import MIMEText #Agregar texto al correo
from email.mime.base import MIMEBase #Archivos adjuntos
from email import encoders #Prepra archivos antes de enviarlos por si vienen en binario


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
        #Crear estructura correoo
        mensaje = MIMEMultipart() #correo vacio
        
        mensaje["From"] = EMAIL_USER #quien envia el correo
        
        mensaje["To"] = destinatario #para quien va
        
        mensaje["Subject"] = asunto #Asunto

        # Agregar HTML
        mensaje.attach( #attach es agregar el contenido html al correo 
            MIMEText( # va ser contenido html
                html,
                "html"
            )
        )
        
        #Adjuntar excel
        with open(
            archivo_adjunto,
            "rb"  #read-bianry
        )as archivo: #guadamos todo en el nombre de archivo
            parte = MIMEBase( #espacio para guardar el archivo
                "application", #Categoria porque dentro viene excel , pdf , etc
                "octet-stream" #Archivo binario generoico, como no se sabe que archivo va a llegar
            )
            
            parte.set_payload( #lee todos los bytes del Excel.
                archivo.read()#esto es que meta el contenido real de excel dentro del espacio
            )

        encoders.encode_base64(
            parte #Adjunta el archivo en el correo , encoer, excel es un binario y por el correo viaja como texto 
            #entonces sencesita convertir
        )

        parte.add_header(#info extra como fehca, remi, destinatario y aparece como adjunto
            "Content-Disposition",#decir que es un archivo adjunto
            f"attachment; filename={archivo_adjunto}" # dice algo parecido a esto Este archivo debe aparecer como ADJUNTO
            
        )
                
        mensaje.attach(
            parte
        )
        
        #Conexion SMTP
        servidor = smtplib.SMTP(
            "smtp.gmail.com",#direccion a gmail y el 587 es su puerto nos vamos a concetar a ese
            587
        )
        
        servidor.starttls() #Coxexion segura al sevidor va a estar cifrado
        
        
        servidor.login( #credenciales
            EMAIL_USER,
            EMAIL_PASSWORD
        )
        
        servidor.send_message( #enviar mensaje
            mensaje
        )
        
        servidor.quit()#cierra conexion al servidor gmail
        
# Crear correo
#mensaje = MIMEMultipart()

# Agregar HTML
#mensaje.attach(...)

# Abrir Excel
#with open(...)

# Adjuntar Excel
#mensaje.attach(...)

# Conectarse a Gmail
#servidor = smtplib.SMTP(...)

# Login
#servidor.login(...)

# Enviar
#servidor.send_message(...)

# Salir
#servidor.quit()
        
        
        
        