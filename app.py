import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def send_email(subject, body, to_email):
    from_email = "harizonelopez23@gmail.com"
    password = "207[jksy8392]#"
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def generate_report():
    # For the sake of example, let's just return a simple string
    return "Daily report for " + str(datetime.date.today())

if __name__ == "__main__":
    report = generate_report()
    send_email("Daily Report", report, "recipient_email@gmail.com")
