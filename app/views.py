from email.mime.image import MIMEImage
from django.shortcuts import render
from seagull import settings
from .forms import CallbackForm
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime, os
from email.mime.base import MIMEBase
from email import encoders

def attach_logo_as_inline_image(email_msg):
    logo_path = os.path.join(os.path.dirname(__file__), 'logo.jpg')
    with open(logo_path, 'rb') as logo_file:
        img = MIMEBase('image', 'jpeg', filename='logo.jpg')
        img.set_payload(logo_file.read())
        encoders.encode_base64(img)
        img.add_header('Content-ID', '<logo>')
        img.add_header('Content-Disposition', 'inline', filename='logo.jpg')
        email_msg.attach(img)

def index(request):
    success = None
    error = None

    if request.method == "POST":
        form = CallbackForm(request.POST)

        if form.is_valid():
            try:
                # Extract data safely
                full_name = form.cleaned_data['full_name']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                
                # Prepare email content for user
                user_email_subject = "We Received Your Request"
                user_email_body = f"""
                                    <html>
                                        <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f8f9fa;">
                                            <div style="max-width: 600px; margin: auto; padding: 20px; background: #ffffff; border: 1px solid #dddddd;">
                                                <!-- Logo positioned at the top left with border-radius -->
                                                <div style="text-align: left; padding-bottom: 20px;">
                                                    <img src="cid:logo" alt="Company Logo" style="width: 50px; border-radius: 50%;">
                                                </div>
                                                <h2 style="color: #333333;">Dear {full_name},</h2>
                                                <p style="color: #555555; font-size: 16px;">
                                                    We received your request with the following details:
                                                </p>
                                                <ul style="color: #555555; font-size: 16px; line-height: 1.5;">
                                                    <li><strong>Phone Number:</strong> {phone}</li>
                                                    <li><strong>Message:</strong> {message}</li>
                                                </ul>
                                                <p style="color: #555555; font-size: 16px;">
                                                    We will get back to you soon. Thank you!
                                                </p>
                                                <p style="color: #888888; font-size: 12px; text-align: center; padding-top: 20px;">
                                                    &copy; {datetime.datetime.now().year} Seagull Tech Vision. All rights reserved.
                                                </p>
                                            </div>
                                        </body>
                                    </html>
                                    """

                # Prepare email content for admin
                admin_email_subject = "User Requested a Call Back"
                admin_email_body = f"""
                                    <html>
                                        <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f8f9fa;">
                                            <div style="max-width: 600px; margin: auto; padding: 20px; background: #ffffff; border: 1px solid #dddddd;">
                                                <!-- Logo positioned at the top left with border-radius -->
                                                <div style="text-align: left; padding-bottom: 20px;">
                                                    <img src="cid:logo" alt="Company Logo" style="width: 50px; border-radius: 50%">
                                                </div>
                                                <h2 style="color: #333333;">New Callback Request</h2>
                                                <p style="color: #555555; font-size: 16px;">
                                                    You have received a callback request with the following details:
                                                </p>
                                                <ul style="color: #555555; font-size: 16px; line-height: 1.5;">
                                                    <li><strong>Full Name:</strong> {full_name}</li>
                                                    <li><strong>Phone:</strong> {phone}</li>
                                                    <li><strong>Email:</strong> {email}</li>
                                                    <li><strong>Message:</strong> {message}</li>
                                                </ul>
                                                <p style="color: #555555; font-size: 16px;">
                                                    Please follow up with the user as soon as possible.
                                                </p>
                                                <p style="color: #888888; font-size: 12px; text-align: center; padding-top: 20px;">
                                                    &copy; {datetime.datetime.now().year} Seagull Tech Vision. All rights reserved.
                                                </p>
                                            </div>
                                        </body>
                                    </html>
                                    """
                # SMTP Configuration
                context = ssl._create_unverified_context()
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
                    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

                    # Send email to user
                    user_email = MIMEMultipart()
                    user_email['From'] = settings.EMAIL_HOST_USER
                    user_email['To'] = email
                    user_email['Subject'] = user_email_subject
                    user_email.attach(MIMEText(user_email_body, 'html'))

                    # Attach logo as inline image
                    attach_logo_as_inline_image(user_email)

                    server.send_message(user_email)

                    # Send email to admin
                    admin_email = MIMEMultipart()
                    admin_email['From'] = settings.EMAIL_HOST_USER
                    admin_email['To'] = "seagulltechhr@gmail.com"
                    admin_email['Subject'] = admin_email_subject
                    admin_email.attach(MIMEText(admin_email_body, 'html'))

                    server.send_message(admin_email)

                success = "Request submitted successfully. You’ll receive a confirmation email shortly."

            except Exception as e:
                print(f"Error in sending email: {e}")
                error = "An unexpected error occurred. Please try again."
        else:
            error = "Invalid form submission. Please correct the fields and submit again."

    else:
        form = CallbackForm()

    return render(
        request,
        'index.html',
        {'form': form, 'success': success, 'error': error}
    )

def about(request):
    return render(request, 'about.html')

def contact(request):
    success = None
    error = None

    if request.method == "POST":
        form = CallbackForm(request.POST)

        if form.is_valid():
            try:
                # Extract data safely
                full_name = form.cleaned_data['full_name']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                
                # Prepare email content for user
                user_email_subject = "We Received Your Request"
                user_email_body = f"""
                                    <html>
                                        <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f8f9fa;">
                                            <div style="max-width: 600px; margin: auto; padding: 20px; background: #ffffff; border: 1px solid #dddddd;">
                                                <!-- Logo positioned at the top left with border-radius -->
                                                <div style="text-align: left; padding-bottom: 20px;">
                                                    <img src="cid:logo" alt="Company Logo" style="width: 50px; border-radius: 50%;">
                                                </div>
                                                <h2 style="color: #333333;">Dear {full_name},</h2>
                                                <p style="color: #555555; font-size: 16px;">
                                                    We received your request with the following details:
                                                </p>
                                                <ul style="color: #555555; font-size: 16px; line-height: 1.5;">
                                                    <li><strong>Phone Number:</strong> {phone}</li>
                                                    <li><strong>Message:</strong> {message}</li>
                                                </ul>
                                                <p style="color: #555555; font-size: 16px;">
                                                    We will get back to you soon. Thank you!
                                                </p>
                                                <p style="color: #888888; font-size: 12px; text-align: center; padding-top: 20px;">
                                                    &copy; {datetime.datetime.now().year} Seagull Tech Vision. All rights reserved.
                                                </p>
                                            </div>
                                        </body>
                                    </html>
                                    """

                # Prepare email content for admin
                admin_email_subject = "User Requested a Call Back"
                admin_email_body = f"""
                                    <html>
                                        <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f8f9fa;">
                                            <div style="max-width: 600px; margin: auto; padding: 20px; background: #ffffff; border: 1px solid #dddddd;">
                                                <!-- Logo positioned at the top left with border-radius -->
                                                <div style="text-align: left; padding-bottom: 20px;">
                                                    <img src="cid:logo" alt="Company Logo" style="width: 50px; border-radius: 50%">
                                                </div>
                                                <h2 style="color: #333333;">New Callback Request</h2>
                                                <p style="color: #555555; font-size: 16px;">
                                                    You have received a callback request with the following details:
                                                </p>
                                                <ul style="color: #555555; font-size: 16px; line-height: 1.5;">
                                                    <li><strong>Full Name:</strong> {full_name}</li>
                                                    <li><strong>Phone:</strong> {phone}</li>
                                                    <li><strong>Email:</strong> {email}</li>
                                                    <li><strong>Message:</strong> {message}</li>
                                                </ul>
                                                <p style="color: #555555; font-size: 16px;">
                                                    Please follow up with the user as soon as possible.
                                                </p>
                                                <p style="color: #888888; font-size: 12px; text-align: center; padding-top: 20px;">
                                                    &copy; {datetime.datetime.now().year} Seagull Tech Vision. All rights reserved.
                                                </p>
                                            </div>
                                        </body>
                                    </html>
                                    """
                # SMTP Configuration
                context = ssl._create_unverified_context()
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
                    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

                    # Send email to user
                    user_email = MIMEMultipart()
                    user_email['From'] = settings.EMAIL_HOST_USER
                    user_email['To'] = email
                    user_email['Subject'] = user_email_subject
                    user_email.attach(MIMEText(user_email_body, 'html'))

                    # Attach logo as inline image
                    attach_logo_as_inline_image(user_email)

                    server.send_message(user_email)

                    # Send email to admin
                    admin_email = MIMEMultipart()
                    admin_email['From'] = settings.EMAIL_HOST_USER
                    admin_email['To'] = "neelrajsinhzala27@gmail.com"
                    admin_email['Subject'] = admin_email_subject
                    admin_email.attach(MIMEText(admin_email_body, 'html'))

                    server.send_message(admin_email)

                success = "Request submitted successfully. You’ll receive a confirmation email shortly."

            except Exception as e:
                print(f"Error in sending email: {e}")
                error = "An unexpected error occurred. Please try again."
        else:
            error = "Invalid form submission. Please correct the fields and submit again."

    else:
        form = CallbackForm()

    return render(
        request,
        'contact.html',
        {'form': form, 'success': success, 'error': error}
    )


def do(request):
    return render(request, 'do.html')

def internship_apply_4_weeks(request):
    return render(request, 'internship_apply_4_weeks.html')

def internship_apply_6_weeks(request):
    return render(request, 'internship_apply_6_weeks.html')

def internship_apply_8_weeks(request):
    return render(request, 'internship_apply_8_weeks.html')

def portfolio(request):
    return render(request, 'portfolio.html')
