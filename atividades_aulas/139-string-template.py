from string import Template
from datetime import datetime

with open('arquivos/template_mail.html', 'r', encoding='UTF-8') as html:
    template = Template(html.read ())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='Danton', data=data_atual)

print(corpo_msg)
