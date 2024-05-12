import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_messages():
    # Email configuration
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'abdhakeem123abd@gmail.com'
    EMAIL_HOST_PASSWORD = 'qlycvymkilkkrfbc'

    # Read data from Excel
    try:
        df = pd.read_excel('data.xlsx')
    except FileNotFoundError:
        print("Error: 'data.xlsx' file not found.")
        return

    # Iterate over rows and send emails
    for index, row in df.iterrows():
        name = row['name']
        email = row['email']
        subject = row['subject']
        message = row['message']

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = email

        html = f"Hello {name},<br> {message}."
        msg.attach(MIMEText(html, 'html'))

        # Connect to SMTP server and send email
        try:
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
                server.starttls()
                server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
                server.send_message(msg)
            print(f"Message sent successfully to {email}")
        except Exception as e:
            print(f"Failed to send message to {email}: {e}")

if __name__ == "__main__":
    send_messages()
