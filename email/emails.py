import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "hihi@gmail.com"  # Enter your address
receiver_email = "leeky940926@gmail.com"  # Enter receiver address
password = "password"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context, timeout=3) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)