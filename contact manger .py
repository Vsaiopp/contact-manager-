class ContactManager:
    def __init__(self , number,name) :
        self.name = name
        self.number = number
      

    def view_contacts() :
        print(contact_dict)

    def add_contacts(number,name) :
        contact_dict.update({name: number})

    def remove_contact(name) :
        contact_dict.pop(name)

is_running = True 
contact_dict = {}

if __name__ == '__main__' :


    while is_running :
        print('Welcome to the contact manager  select an operation\n'
    '1.View contacts \n'
    '2.Add contact \n'
    '3.Remove Contact')
        try:
            choice = int(input())
            if  choice == 1 :
                ContactManager.view_contacts()

            elif choice == 2 :
                 name = input('Enter the name ').lower()
                 number = input('add the number ')
                 ContactManager.add_contacts(number,name)

            elif choice == 3 :
                name = input('Enter a name to remove : ').lower()
                ContactManager.remove_contact(name)
            
            else :
                print('Not a valid selection ')
            
            exitoption = input('Press q to quit and c to continue ').lower()

            if exitoption == 'q' :
                print('Exiting ')
                is_running = False
            elif exitoption == 'c' :
                print('started again')
            else :
                print("not a valid option ")

               


        except ValueError :
             print('Not a valid operation')