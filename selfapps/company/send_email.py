import smtplib,ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "anything2552extra@gmail.com"
    password = "tomvipasbqmxypad"

    receiver = "rockyrocks246810@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)