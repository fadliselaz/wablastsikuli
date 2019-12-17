

import os
import random

new = "new.png"

search = "search.png"

sel = Pattern("sel.png").targetOffset(-3,96)
notFound = "notFound.png"
def send():


    #buka datam member
    with open('openFile/testDatabase.txt', 'r') as db:
        db = db.read().splitlines()

    #buka datam member
    with open('openFile/msg.txt', 'r') as msg:
        msg = msg.read().splitlines()
    
    
        
    x = len(db)
    
    for i in range(x):

        pesan = random.choice(msg)
        contact = db[i].split(',')
        name = contact[0]
        pang = name.replace("LNG - ", "")
        email = contact[1]
        phone = contact[2]
        #print('{} {} 0{}'.format(name, email, phone))
        wait(2)
        print(pesan + " " +pang)
        click(new)
        wait(1)
        click(search)
        paste(phone)
        
        
        wait(2)

        if exists(notFound):
            click("1576557551483.png")
        else:
            click(sel)
            wait(2)
            type("a",Key.CMD)
            type(Key.DELETE)
            #paste(pesan + " " + "*{}*".format(pang))
            #type(Key.ENTER)
            wait(3)
        
        
        
        i += 1

send()

                               




                                                                                