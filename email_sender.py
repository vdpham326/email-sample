import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # allows access to index.html file


html = Template(Path('index.html').read_text()) # html variable and set it to be index.html and use read_text method to read as a string
email = EmailMessage()
email['from'] = 'VP'
email['to'] = 'phamv0326@gmail.com'
email['subject'] = 'You won a million dollars!'

email.set_content(html.substitute({'name':'TinTin'}), 'html') #this set the contents of the email

#setting up your email server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() # encryption mechanism
    smtp.login('abc@gmail.com', 'abc123') #login credentials for dummy email 
    smtp.send_message(email) # send the email object created above
    print('all good boss!!')