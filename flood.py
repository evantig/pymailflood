import sys
import smtplib
import json
from time import sleep

i1 = 0
i2 = 0
usr_err = []
message = ''
s = ''
sendfrom = ''
mails = 0
error = ''
try:
    with open('config.json') as config_file:
        try:
            data = json.load(config_file)
            usrs = data['accounts']['usrs']
            pwds = data['accounts']['pwds']
            if len(usrs) != len(pwds):
                error = 'Error: Length of user list does match length of password list'
        except:
            error = 'Error: Invalid JSON file'
except:
    error = 'Error: Could not open JSON file'

def update():
    global message
    global i1
    message = '''Subject: hi ''' + str(i1) + '''

    hello. this is nigerian diplomat david mathew. please send money and you receive free 2 billion dollar from donald trump wealth distriution'''
    i1 += 1

def login(uname, pwd, svr = 'smtp.gmail.com', port = 587):
    print('Run login(' + uname + ', ' + pwd + ', ' + svr + ', ' + str(port) + ')')
    global s
    global sendfrom
    sendfrom = uname
    s = smtplib.SMTP(svr, port)
    s.ehlo()
    s.starttls()
    s.login(uname, pwd)

if error == '':

    while len(usr_err) < len(usrs):
        usr_err.append(0)

    sendto = input('To: ')
    login(usrs[0], pwds[0])

    while i2 < len(usrs):
        try:
            update()
            s.sendmail(sendfrom, sendto, message)
            mails += 1
            print('Email #' + str(mails) + ' sent from ' + usrs[i2])
        except:
            print('Email could not be sent. Trying next account...')
            usr_err[i2] = 1
            i2 += 1
            if i2 < len(usrs):
                login(usrs[i2], pwds[i2])
    print('No more accounts to try')
else:
    print(error)