import ssl
import sys
import smtplib
from email.message import EmailMessage
from email_info import email_password, smtp_port, smtp_server

if len(sys.argv) == 2:
    command = sys.argv[1]
    if command == 'send_email':
        email_sender = input('What email would you like to use? ')
        email_receiver = input('To whom would you like to send this email? ')

        subject = input('What would you like your subject to be? ')
        body = input('What would you like to include in the body? ')

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as smtp:
                print('Connecting to server...')
                smtp.login(email_sender, email_password)
                print('Connected to server.')

                print()
                print(f'Sending email to {email_receiver}...')
                smtp.sendmail(email_sender, email_receiver, em.as_string())

                print(f'Email sent successfully to {email_receiver}')
        except Exception as e:
            print(e)

    else:
        print('unknown command')
