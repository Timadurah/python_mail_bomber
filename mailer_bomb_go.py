import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mailer_sender(sender, receiver, password__, subject, message_html, host__, port__):
    sender_email = sender
    receiver_email = receiver
    password = password__

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message

    html = message_html

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host__, port__, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    json_returner = '{"mail":receiver_email, "response":"sent"}'
    return json_returner

#
# html__ = """\
  #  <html>
    #  <body>
      #  <p>Hi,<br>
          # How are you?<br>
          # <a href="http://www.realpython.com">Real Python</a> 
          # has many great tutorials.
      #  </p>
    #  </body>
  #  </html>
  #  """
# mailer_sender("dev@topkonnect.net", "durallite@gmail.com", "EmzSbQ6F8CSKRRC",
              # "python mail distributor project", html__, "mail.topkonnect.net", 465)
# 