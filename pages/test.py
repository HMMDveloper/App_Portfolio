import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, app_password, receiver_email, subject, body):
    # Email server settings
    host = "smtp.gmail.com"
    port = 465

    # Create message container
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Create secure SSL context
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(sender_email, app_password)
            server.send_message(message)
        return True
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False

# Example usage
if __name__ == "__main__":
    sender_email = "digitallinkcraft@gmail.com"  # Replace with your Gmail address
    app_password = "gantgyubaitausxn"      # Replace with your App Password
    receiver_email = "digitallinkcraft@gmail.com"
    subject = "Hi!"
    body = "How are you?\nBye!"

    success = send_email(sender_email, app_password, receiver_email, subject, body)
    if success:
        print("Email sent successfully!")
    else:
        print("Failed to send email.")
