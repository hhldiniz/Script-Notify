import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    @staticmethod
    def send_email(sender_email, sender_password, recipient_email, subject, body):
        # Create message container
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        server = None

        # Create SMTP session
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)

            # Send email
            text = message.as_string()
            server.sendmail(sender_email, recipient_email, text)
            print("Email sent successfully")

        except Exception as e:
            print(f"Error sending email: {str(e)}")

        finally:
            if server:
                server.quit()
