import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor SMTP
#lembrando que precisa colocar as opções no google de login de baixa segurança
email_origem = 'email de origem'
senha = 'email de origem'
servidor_smtp = 'smtp.gmail.com'
porta = 587

# Criar um objeto SMTP
smtp = smtplib.SMTP(host=servidor_smtp, port=porta)
smtp.starttls()  # Iniciar o modo TLS para criptografar a conexão

# Fazer login no servidor SMTP
smtp.login(email_origem, senha)

# Construir a mensagem de e-mail
destinatario = 'email de destinatario'
assunto = 'Teste de e-mail com Python'
corpo = 'Olá, este é um e-mail de teste enviado usando Python e smtplib.'

mensagem = MIMEMultipart()
mensagem['From'] = email_origem
mensagem['To'] = destinatario
mensagem['Subject'] = assunto

mensagem.attach(MIMEText(corpo, 'plain'))

# Enviar o e-mail
smtp.sendmail(email_origem, destinatario, mensagem.as_string())

# Fechar a conexão SMTP
smtp.quit()

print('E-mail enviado com sucesso!')