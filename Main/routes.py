from flask import render_template, redirect, request, url_for, flash
from Main import app, db
from Main.models import Contact
#for email
import smtplib
from email.message import EmailMessage
# To load the email user and passkey
import os
from dotenv import load_dotenv
load_dotenv()

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
def email_alerts(subject, body, to):
    passkey=EMAIL_PASS
    user = EMAIL_USER

    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, passkey)
    server.send_message(msg)
    

    server.quit()

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/about')
def aboutus_page():
    return render_template('about.html')
@app.route('/contact', methods=['POST', 'GET'])
def contact_page():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        feedback = request.form['message']
        
        contact_to_submit = Contact(name=name, email=email, phone=phone, feedback=feedback)
        db.session.add(contact_to_submit)
        db.session.commit()
        print("successfully submitted.")
        # flash("Thanks for Contacting.", category='info')
        subject = f"Hello {contact_to_submit.name}, Thanks for Contacting Us!"
        body = (
            f"Dear {contact_to_submit.name},\n\n"
            "Thank you for reaching out and feedback. We have received your message with the following details:\n\n"
            f"📧 Email: {contact_to_submit.email}\n"
            f"📞 Phone: {contact_to_submit.phone}\n"
            "We will get back to you as soon as possible.\n\n"
            "Best regards,\nShree Panch"
        )
        subject_admin = "New Contact Submission on Shree Panch Website"
        body_admin = (
    f"Hey Bigyan,\n\n"
    f"{contact_to_submit.name} just contacted the team through the website.\n"
    f"Here are the details:\n\n"
    f"📧 Email: {contact_to_submit.email}\n"
    f"📞 Phone: {contact_to_submit.phone}\n"
    f"🏠 Feedback: {contact_to_submit.feedback}\n\n"
    
    "Check the admin dashboard or follow up if needed."
)

        email_alerts(subject, body, contact_to_submit.email)
        email_alerts(subject_admin, body_admin, 'bigyanmishra022@gmail.com')
        flash(f"Thanks for contacting! {contact_to_submit.name}", category='success')
        return redirect(url_for('home_page'))
    
    return render_template('contact.html')

@app.route('/hackathons')
def hackathon_page():
    return render_template('hackathon.html')
@app.route('/teams')
def teams_page():
    return render_template('teams.html')
@app.route('/gallery')
def gallery_page():
    return render_template('gallery.html')