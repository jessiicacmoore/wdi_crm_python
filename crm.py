from contact import Contact


class CRM:
    def main_menu(self):
        while True:  # repeat indefinitely
            self.print_main_menu()
            user_selected = int(input())
            self.call_option(user_selected)

    def print_main_menu(self):
        print("[1] Add a new contact")
        print("[2] Modify an existing contact")
        print("[3] Delete a contact")
        print("[4] Display all the contacts")
        print("[5] Search by attribute")
        print("[6] Exit")
        print("Enter a number: ")

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
        print("Enter first name:")
        first_name = input()
        print("Enter last name:")
        last_name = input()
        print("Enter email:")
        email = input()
        print("Enter note:")
        note = input()

        new_contact = Contact.create(
            first_name=first_name, last_name=last_name, email=email, note=note
        )

    def modify_existing_contact(self):
        print("Please enter the id of the contact you would like to modify")
        modify_id = int(input())
        mod_contact = Contact.get(id=modify_id)

        print("Please enter the attribute you would like to modify")
        print("[1] Change first name")
        print("[2] Change last name")
        print("[3] Change email")
        print("[4] Change note")
        print("Enter a number: ")
        attribute_input = int(input())
        # options = {1: mod_contact.first_name, 2: mod_contact.last_name, 3: mod_contact.email, 4: mod_contact.note}
        # selected_attribute = options[attribute_input] #couldn't use this method to modify?

        print("Please enter your modification")
        modification = input()

        if attribute_input == 1:
            mod_contact.first_name = modification
            mod_contact.save()
        elif attribute_input == 2:
            mod_contact.last_name = modification
            mod_contact.save()
        elif attribute_input == 3:
            mod_contact.email = modification
            mod_contact.save()
        elif attribute_input == 4:
            mod_contact.note = modification
            mod_contact.save()

    def delete_contact(self):
        print("Please enter the id of the contact you would like to delete")
        delete_id = int(input())
        contact = Contact.get(id=delete_id)
        contact.delete_instance()

    def display_all_contacts(self):
        print()
        for contact in Contact.select():
            print(
                f"({contact.id}) {contact.first_name} {contact.last_name} - {contact.email}"
            )
        print()

    def search_by_attribute(self):
        print("[1] Search by first name")
        print("[2] Search by last name")
        print("[3] Search by email")
        print("Enter a number: ")
        options = {1: Contact.first_name, 2: Contact.last_name, 3: Contact.email}
        attribute_input = int(input())
        selected_attribute = options[attribute_input]

        print("Enter your search: ")
        search_input = input()

        query = Contact.select().where(selected_attribute == search_input)

        print()
        for contact in query:
            print(
                f"({contact.id}) {contact.first_name} {contact.last_name} - {contact.email}"
            )
        print()


a_crm_app = CRM()
a_crm_app.main_menu()
