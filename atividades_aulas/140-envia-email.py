from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'danton@email'
minha_senha = 'senha'

with open('arquivos/template_mail.html', 'r', encoding='UTF-8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Danton', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Danton'
msg['to'] = 'danton@email'  # Cliente
msg['subject'] = 'Teste E-mail Python'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

#ENVIO DE IMAGEM EM ANEXO
with open('arquivos/imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)
