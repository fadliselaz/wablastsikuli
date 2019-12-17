import random
translateArea = "translateArea.png"
voice = "voice.png"
removeText = "removeText.png"

def translate():
    #buka datam member
    with open('testDatabase.txt', 'r') as db:
        db = db.read().splitlines()
        
    x = 300
    
    for i in range(20):
        
        ct = random.choice(db)
        contact = ct.split(',')
        
        name = contact[0]
        name = name.replace("LNG - ", "")
        email = contact[1]
        phone = contact[2]
        
        doubleClick(translateArea)
        paste(name)
        wait(1)
        click(voice)
        wait(3)
        click(removeText)

        

        x += 1
    

                

translate()