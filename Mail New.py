Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


from fastapi import FastAPI
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
... app.add_middleware(
...     CORSMiddleware,
...     allow_origins=["*"],
...     allow_credentials=True,
...     allow_methods=["*"],
...     allow_headers=["*"],
... )
... 
... 
... @app.get('/')
... async def root():    
...     return 200
... 
... class Mail(BaseModel):
...     subject:str
...     message:str
...     
... 
... @app.post('/')
... async def send_mail(mail:Mail):
...     sender = 'nisaldilesh14@gmail.com'
...     receiver = 'hasindusithmin64@gmail.com'
...     
...     msg = MIMEText(mail.message)
... 
...     msg['Subject'] = mail.subject
...     msg['From'] = 'nisaldilesh14@gmail.com'
...     msg['To'] = 'hasindusithmin64@gmail.com'
... 
... 
...     # creates SMTP session
...     s = smtplib.SMTP('smtp.gmail.com', 587)
...     
...     # start TLS for security
...     s.starttls()
...     
...     # Authentication
...     s.login("nisaldilesh14@gmail.com", "xfxhrzyampkdkpzq")
...     
...     # sending the mail
...     s.sendmail("nisaldilesh14@gmail.com", "hasindusithmin64@gmail.com", msg.as_string())
...     
...     # terminating the session
...     s.quit()
...     
...     return "success"
