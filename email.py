import smtplib
from email.mime.text import MIMEText

smtp = smtplib.SMTP("stmp.live.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.login("leeky940926@gmail.com", "dlrldyd5608")

msg = MIMEText("message test")
msg["Subject"] = "subject test"
msg["To"] = "kiyong.lee@athenaslab.com"
smtp.send_message("leeky940926@gmail.com", "kiyong.lee@athenaslab.com")

smtp.quit()