import smtplib

try:
		msgFrom = str(input("Informe o e-mail de destino: "))
		smtpObj = smtplib.SMTP('smtp.outlook.com', 587)
		smtpObj.ehlo()
		smtpObj.starttls()
		msgTo = 'email@example.com'
		toPass = 'mypass'
		smtpObj.login(msgTo, toPass)
		msg = '''
		Funcionou
		'''
		smtpObj.sendmail(msgTo,msgFrom,'Subject: Teste keylogger\n{}'.format(msg))
		smtpObj.quit()
		print("Email enviado com sucesso!")
except:
		print("Erro ao enviar e-mail")

