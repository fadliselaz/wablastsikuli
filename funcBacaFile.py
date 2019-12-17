import random
import time

def readFile():
    with open('testDatabase.txt', 'r') as rd:
        dataMember = rd.read().splitlines()
    
    with open('msg.txt','r') as msg:
        pesan = msg.read().splitlines()
        
    
    lg = len(dataMember)

    for i in range(lg):
        contact = dataMember[i].split(',')
        nama = contact[0]
        email = contact[1]
        phone = contact[2]
        ps = random.choice(pesan)
        
        # pemecah email
        email = email.replace('@gmail.com','')
        email = email.replace('@yahoo.com','')
        email = email.replace('.',' ')

        # pemecah nama
        nama = nama.replace('LNG - ','')
        nama = nama.lower()

        print("{} {}".format(ps, nama))
        time.sleep(2)
