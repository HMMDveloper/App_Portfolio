import streamlit as st
from pages.test import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("your email address ")
    message = st.text_area("Enter your message:")
    message = message + "\n" + user_email
    button = st.form_submit_button("Submit")
    if button:
        success = send_email(
            sender_email="digitallinkcraft@gmail.com",
            app_password="gantgyubaitausxn",
            receiver_email="digitallinkcraft@gmail.com",
            subject="Contact Form Submission",
            body=message,
        )
        if success:
            st.success("Email sent successfully!")
        else:
            st.error("Failed to send email. Please try again.")
