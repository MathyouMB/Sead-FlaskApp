def returnText(name):
    #file = open("demoText.txt", "w")
    #file.write(name)
    text = open("demoText.txt","r").readlines()
    print(text)
    return (text)

def returnNotes(notes):
    print(notes)
    return notes
