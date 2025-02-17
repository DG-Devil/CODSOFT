# This program is known as "Contact Book" that maintain the contacts and their information

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

contacts = []

def Add():
    print("\n--- Add Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    new_contact = Contact(name, phone, email, address)
    contacts.append(new_contact)
    print("♦ Contact added successfully ♦")

def Search():
    print("\n--- Search Contact ---")
    search_name = input("Enter Name to search: ")
    found = False
    for contact in contacts:
        if contact.name.lower() == search_name.lower():
            print(contact)
            found = True
    if not found:
        print("Contact not found !!!")

def Update():
    print("\n--- Update Contact ---")
    search_name = input("Enter Name of contact to update: ")
    found = False
    for contact in contacts:
        if contact.name.lower() == search_name.lower():
            found = True
            print("What do you want to update : \n1) Name \n2) Phone no. \n3) Email \n4) Address \n0) ALL")
            val = int(input("\n-> "))
            if val == 0:
                contact.name = input("Enter new name : ")
                contact.phone = input("Enter new phone no. : ")
                contact.email = input("Enter new email : ")
                contact.address = input("Enter new address : ")
                print("♦ Contact updated successfully ♦")
                return
            elif val == 1:
                contact.name = input("Enter new name: ")
                print("♦ Contact updated successfully ♦")
            elif val == 2:
                contact.phone = input("Enter new phone no. : ")
                print("♦ Contact updated successfully ♦")
            elif val == 3:
                contact.email = input("Enter new email: ")
                print("♦ Contact updated successfully ♦")
            elif val == 4:
                contact.address = input("Enter new address: ")
                print("♦ Contact updated successfully ♦")
            return
    if not found:
        print("Contact not found !!!")

def Delete():
    print("\n--- Delete Contact ---")
    delete_name = input("Enter Name of the contact to delete: ")
    found = False
    for contact in contacts:
        if contact.name.lower() == delete_name.lower():
            contacts.remove(contact)
            found = True
            print("♦ Contact deleted successfully ♦")
            break
    if not found:
        print("Contact not found !!!")

def Contact_list():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts available!")
    for c in contacts:
        print(c)

def Switch(n):
    if n == 1:
        Add()
    elif n == 2:
        Search()
    elif n == 3:
        Update()
    elif n == 4:
        Delete()
    elif n == 5:
        Contact_list()
    else:
        print("Invalid choice")

def main():
    while True:
        print("\n1) Add Contact \n2) Search Contact \n3) Update Contact \n4) Delete Contact \n5) Contacts \n6) Exit")
        try:
            n = int(input("Enter your choice: \n"))
            if n == 6:
                break
            Switch(n)
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
