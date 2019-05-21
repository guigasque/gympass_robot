# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 10:34:45 2018

@author: joao.galhianne
"""


#def carregaParametrosJson(nomeJason):
#    
#    import json
#
#    with open('../' + nomeJason, encoding='utf-8-sig') as f:    
#        arquivo_json_de_parametros = json.load(f)
#        
#    return(arquivo_json_de_parametros);
    

    
def copy():
    
    #from twilio.rest import Client
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    import gc
    import os
  
# =============================================================================
#     carrega parametros
# =============================================================================
    #usuario = paramentrosJson["usuario_gympass"][parametroDeUsuario]["usuario"]
    #senha = paramentrosJson["usuario_gympass"][parametroDeUsuario]["senha"]
    usuario = " "" " + cpf + " "" "
    senha = " "" " + senha + " "" "
    
# =============================================================================

    #chrome_options = webdriver.ChromeOptions()
    #prefs = {'download.default_directory' : enderecoDownload}
    #chrome_options.add_experimental_option('prefs', prefs)
    #driver = webdriver.Chrome(options=chrome_options)
    #driver = webdriver.Chrome('../')
    driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
    
# =============================================================================
#     Login
# =============================================================================
    
    url_login="https://www.gympass.com/pessoas/entrar"
    
    driver.get(url_login)
        
    inputElement = driver.find_element_by_id("person_search_info")
    inputElement.send_keys(usuario)
    
    driver.find_element_by_name('commit').click()
    
    inputElement = driver.find_element_by_id("person_password")
    inputElement.send_keys(senha)
    
    driver.find_element_by_name('button').click()
    
# =============================================================================
#     Muda para a página para copiar o daily token
# =============================================================================
    
    url_copiar="https://www.gympass.com/end-user/br/daily-token"
    driver.get(url_copiar)

    token = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/main/nav/div/div/div/strong').text
    #time.sleep(20)
    
    print(token)
    
# =============================================================================
#     account_sid = 'ACacf25c7d4a3730e3e7392022aee5c345'
#     auth_token = '874e1163afab8d6e3b36d1a01856e4f1'
#     client = Client(account_sid, auth_token)
# 
#     message = client.messages \
#                 .create(
#                      body="Para utilizar o gympass, mostre este número na recepção:" + token,
#                      from_='+13143288890',
#                      to='+55199982305051'
#                  )
# 
#     print(message.sid)
# =============================================================================
    
    
    import requests
    TWILIO_SID = "ACacf25c7d4a3730e3e7392022aee5c345"
    TWILIO_AUTHTOKEN = "874e1163afab8d6e3b36d1a01856e4f1"
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
    to_number = "whatsapp:+5519982305051"
    #to_number = "whatsapp:+5519993550113"
    #to_number = "whatsapp:+5519981806636"
    
    appointment_msg = "Para utilizar o gympass, mostre este número na recepção: " + token
    msg = send_whatsapp_message(to_number, appointment_msg)
    print(msg['sid']) # SM5xxxafa561e34b1e84c9d22351ae08a0
    print(msg['status']) # queued
    
    
#    from twilio.rest import Client 
#     
#    account_sid = 'ACacf25c7d4a3730e3e7392022aee5c345' 
#    auth_token = '874e1163afab8d6e3b36d1a01856e4f1' 
#    client = Client(account_sid, auth_token) 
#     
#    message = client.messages.create( 
#                                  from_='whatsapp:+14155238886',  
#                                  body='Your appointment is coming up on July 21 at 3PM' + token,      
#                                  to='whatsapp:+5519981806636' 
#                              ) 
#     
#    print(message.sid)
    
    gc.collect()
    
    driver.quit();
    
    return(token)

