import requests

def send_simple_message(email):
    return requests.post(
    "https://api.mailgun.net/v3/sandbox9f0065306e9b4c328b260996dd559575.mailgun.org/messages",
    auth=("api", "key-21b381f61471b14cdbde9cb9846993d9"),
    data={"from": "Lisa" "<postmaster@sandbox9f0065306e9b4c328b260996dd559575.mailgun.org>",
    "to": [email],
    "subject": "Thank You for your request!",
    "text": "Hello! We will be in contact with you shortly!"})

send_simple_message("lisa.koschitz@gmail.com")
