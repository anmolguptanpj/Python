phoneDirectory=[]

def addContact(name,number):
    for contact in phoneDirectory:
        if contact["name"].lower() == name.lower():
            print("contact with this name exists already")
            return
        
    contact = {
        "name" : name.title().replace(" ",""),
        "number" : number
    }
    phoneDirectory.append(contact)
    print("Contact added Successfully")

addContact("Anmol","9876543210")
addContact("Clusturn","655565565")
addContact("Tony","8785454565")
addContact("pinky",5656565645)
print(phoneDirectory)

