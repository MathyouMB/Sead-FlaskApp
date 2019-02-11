import time
def returnText(name):
    file = open("demoText.txt", "w")
    file.write(name.replace("\n",""))
    file.close()
    text = open("demoText.txt","r").readlines()
    return (text)

def returnNotes(notes):
    text = open("demoText.txt","r").readlines()
    return (text)
