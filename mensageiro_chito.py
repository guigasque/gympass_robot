def chito_mansageiro(whatsapp = ""):
    import requests
    whatsapp = 'whatsapp:+55' + whatsapp + ''
    TWILIO_SID = "#########################################"
    TWILIO_AUTHTOKEN = ""#########################################""
    TWILIO_MESSAGE_ENDPOINT = "https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json".format(TWILIO_SID=TWILIO_SID)
    TWILIO_NUMBER = "whatsapp:+14155238886"
    def send_whatsapp_message(to, message):
        message_data = {
            "To": to,
            "From": TWILIO_NUMBER,
            "Body": message,
        }
        response = requests.post(TWILIO_MESSAGE_ENDPOINT, data=message_data, auth=(TWILIO_SID, TWILIO_AUTHTOKEN))
        
        response_json = response.json()
            
        return response_json
    to_number = whatsapp
    
    appointment_msg = 'Olá, meu nome é Mensageiro Chito e gostaria de informá-lo que seu código terminou de rodar. Poderia me dar um docinho de recompensa?'
    msg = send_whatsapp_message(to_number, appointment_msg)
    print(to_number)
    print(msg['sid']) # SM5xxxafa561e34b1e84c9d22351ae08a0
    print(msg['status']) # queued  
