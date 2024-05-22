import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

async def send_email(recepient_email: str, otp: int):
    message = Mail(
        from_email='arshnoor@infocusp.com',
        to_emails=recepient_email,
        subject='Verify OTP',
        html_content=f'OTP for user verification is shared: {otp}'
    )
    try:
        SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

        sg = SendGridAPIClient(SENDGRID_API_KEY)

        sg.send(message)
        
    except Exception as e:
        print(str(e))
