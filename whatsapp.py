## -*- coding: utf-8 -*-
#"""
#Created on Sun Jan 20 20:07:13 2019
#
#@author: guilherme.gasque
#"""
#
#
#import requests
#TWILIO_SID = "ACacf25c7d4a3730e3e7392022aee5c345"
#TWILIO_AUTHTOKEN = "874e1163afab8d6e3b36d1a01856e4f1"
#TWILIO_MESSAGE_ENDPOINT = "https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json".format(TWILIO_SID=TWILIO_SID)
#TWILIO_NUMBER = "whatsapp:+14155238886"
#def send_whatsapp_message(to, message):
#    message_data = {
#        "To": to,
#        "From": TWILIO_NUMBER,
#        "Body": message,
#    }
#    response = requests.post(TWILIO_MESSAGE_ENDPOINT, data=message_data, auth=(TWILIO_SID, TWILIO_AUTHTOKEN))
#    
#    response_json = response.json()
#    
#    
#    return response_json
#to_number = "whatsapp:+5519982305051"
##to_number = "whatsapp:+5519993550113"
##to_number = "whatsapp:+5519981806636"
#
#appointment_msg = "Para utilizar o gympass, mostre este número na recepção: " #+ token
#msg = send_whatsapp_message(to_number, appointment_msg)
#print(msg['sid']) # SM5xxxafa561e34b1e84c9d22351ae08a0
#print(msg['status']) # queued
#    


from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACacf25c7d4a3730e3e7392022aee5c345'
auth_token = '874e1163afab8d6e3b36d1a01856e4f1'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+5519982305051'
                          )

print(message.sid)