import smtplib

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='rajatsingh1853@gmail.com'
receiver='savintom@rediffmail.com'
msg="hii,whats up"
s.login(sender,'password')
s.sendmail(sender,receiver,msg)
print("msg sent successfuly")
s.quit()