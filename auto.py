import requests

#pegar informações que voce quer
requisicao = requests.get(" https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dicionario = requisicao.json()
cotacao = float (requisicao_dicionario['USDBRL']['bid'])
print(cotacao)
#enviar um aviso - email

import smtplib
import email.message

def enviar_email(cotacao):
    corpo_email = f"""
    <p> Dolar está abaixo de R$5.20  precisamos ganhar em dolar e viajar o mundo. Te amo<3 
    Cotação atual: R${cotacao} </p>
     """

    msg = email.message.Message()
    msg['Subject'] = 'Dolar está hoje abaixo de R$ 5.20'
    msg['From'] = 'litzafontana27@gmail.com'
    msg['To'] = 'litzafontana@hotmail.com'
    password = 'wjmkczedprgxlgrt'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s= smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    #login credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'],[msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


#criar a logica quando o dolar estiver abaixo de 5.2
if cotacao < 5.20:
    enviar_email(cotacao)

#deploy-heroku
