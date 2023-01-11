import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("nisaldilesh14@gmail.com", "xfxhrzyampkdkpzq")
 
# message to be sent
message = "Messdfsage_you_need_to_send"
 
# sending the mail
s.sendmail("nisaldilesh14@gmail.com", "hasindusithmin64@gmail.com", message)
 
# terminating the session
s.quit()