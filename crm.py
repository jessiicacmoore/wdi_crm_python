from contact import Contact

class CRM:

  def main_menu(self):
    while True: # repeat indefinitely
      self.print_main_menu()
      user_selected = int(input())
      self.call_option(user_selected)

  
  def print_main_menu(self):
    print('[1] Add a new contact')
    print('[2] Modify an existing contact')
    print('[3] Delete a contact')
    print('[4] Display all the contacts')
    print('[5] Search by attribute')
    print('[6] Exit')
    print('Enter a number: ')
  
  def call_option(self, user_selected):
    if user_selected == 1:
      self.add_new_contact()
    elif user_selected == 2:
      self.modify_existing_contact()  
    elif user_selected == 3:
      self.delete_contact()
    elif user_selected == 4:
      self.display_all_contacts()  
    elif user_selected == 5:
      self.search_by_attribute()  
    elif user_selected == 6:
      self.display_all_contacts() 
    else:
      print("Sorry, I don't recognize that command") 
  
  
  def add_new_contact(self):
    print('Enter first name:')
    first = input()
    print('Enter last name:')
    last = input()
    print('Enter email:')
    email = input()
    print('Enter note:')
    note = input()

    Contact.create(first, last, email, note)
  
  def modify_existing_contact(self):
    print("Please enter the id of the contact you would like to delete")
    modify_id = input()

    print("Please enter the attribute you would like to modify")
    modify_attribute = input()

    print("Please enter your modification")
    modification = input()

    contact = Contact.find(modify_id)
    contact.update(modify_attribute, modification)

  
  def delete_contact(self):
    print("Please enter the id of the contact you would like to delete")
    delete_id = int(input())
    contact = Contact.find(delete_id)
    contact.delete()
  
  def display_all_contacts(self):
    print(Contact.all())

  def search_by_attribute(self):
    print("[1] Search by first name")
    print("[2] Search by last name")
    print("[3] Search by email")
    print('Enter a number: ')
    attribute_input = int(input())
    print('Enter your search: ')
    search_input = input()
    options = {1: "first_name", 2: "last_name", 3: "email"}
    selected_attr = options[attribute_input]

    search_result = Contact.find_by(selected_attr, search_input)

    print(f"ID: {search_result.id}\nName: {search_result.full_name()}\nEmail: {search_result.email}\nNote: {search_result.note}")
    return search_result
    


a_crm_app = CRM()
a_crm_app.main_menu()