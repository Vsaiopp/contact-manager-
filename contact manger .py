class ContactManager:
    def __init__(self) :

        self.contact_dict = {}
    
        
      

    def view_contacts(self) :
            if not self.contact_dict:
                print("No contacts found.")
            else:
                for name, number in self.contact_dict.items():
                    print(f"{name.title()} : {number}")


    def add_contacts(self) :
        name = input('Enter the name ').lower()
        number = input('add the number ')
        self.contact_dict[name] = number
        print("Contact added successfully.")

    def remove_contact(self) :
        name = input('Enter a name to remove: ').lower()
        if name in self.contact_dict:
            self.contact_dict.pop(name)
            print("Contact removed successfully.")
        else:
            print("Contact not found.")


if __name__ == '__main__' :
    manager = ContactManager()
    is_running = True 


    while is_running :
        print('Welcome to the contact manager  select an operation\n'
    '1.View contacts \n'
    '2.Add contact \n'
    '3.Remove Contact')
        try:
            choice = int(input())
            if  choice == 1 :
                manager.view_contacts()

            elif choice == 2 :
                 manager.add_contacts()

            elif choice == 3 :
                manager.remove_contact()
            
            else :
                print('Not a valid selection ')
            while True :
                exitoption = input('Press q to quit and c to continue ').lower()

                if exitoption == 'q' :
                    print('Exiting ')
                    is_running = False
                    break
                elif exitoption == 'c' :
                     print('started again')
                     break
                else :
                    print("not a valid option ")

               


        except ValueError :
             print('Not a valid operation')