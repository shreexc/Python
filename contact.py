def view_contacts(contacts):
    print("-"*8,"view_contacts","-"*8)
    for a, (name, num) in enumerate (contacts, 1):
        print(f"{a} {name} {num}")

def add_contacts(contacts):
    print("-"*8,"add_contact","-"*8)
    name = str(input("Enter contact name: "))
    num = str(input("Enter contact number: "))
    contacts.append((name, num))
    print(f"{name} - {num} has been added to the contacts.")

def delete_contact(contacts):
    print("-"*8,"delete_contact","-"*8)
    for a, (name, num) in enumerate (contacts, 1):
        print(f"{a} {name} {num}")
    dele = int(input("Enter the ID of the contact to delete: "))
    rem = contacts.pop(dele - 1)
    print(f"Deleting: Record {a} of {name} {num}")

def main(contacts=[("Stish", "123"), ("Rita", "321")]):
    while True:
        user = str(input("Select an operation:\n v View contacts\n a Add contacts\n d Delete contacts\n q Quit\n Enter choice(v/a/d/q- to quit): "))

        if user == "v":
            view_contacts(contacts)

        elif user == "a":
            add_contacts(contacts)

        elif user == "d":
            delete_contact(contacts)

        elif user == "q":
            print("-"*8,"goodbye","-"*8)
            break
        
        else: print("-"*8,"invalid_choice","-"*8,"\n","Try again...\n")

if __name__ == '__main__':
    main()
