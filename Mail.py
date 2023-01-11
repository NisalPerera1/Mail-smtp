import smtplib
from email.mime.text import MIMEText

sender = 'nisaldilesh14@gmail.com'
receiver = 'hasindusithmin64@gmail.com'

msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'nisaldilesh14@gmail.com'
msg['To'] = 'methsara31@gmail.com'


# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("nisaldilesh14@gmail.com", "xfxhrzyampkdkpzq")
 
# message to be sent
message = "Message_you_need_to_send"
 
# sending the mail
s.sendmail("nisaldilesh14@gmail.com", "hasindusithmin64@gmail.com", msg.as_string())
 
# terminating the session
s.quit()
