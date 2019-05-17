class Contact:

    contacts = []
    next_id = 1

    def __init__(self, first, last, email, note):
        """This method should initialize the contact's attributes"""
        self.first_name = first
        self.last_name = last
        self.email = email
        self.note = note
        self.id = Contact.next_id
        Contact.next_id += 1

    @classmethod
    def create(cls, first, last, email, note):
        """This method should call the initializer,
    store the newly created contact, and then return it
    """
        contact = Contact(first, last, email, note)
        cls.contacts.append(contact)

        return contact

    @classmethod
    def all(cls):
        """This method should return all of the existing contacts"""
        all_contacts = []
        for contact in cls.contacts:
            all_contacts.append(
                f"{contact.id}. {contact.first_name} {contact.last_name}: {contact.email} - {contact.note}"
            )
        return all_contacts

    @classmethod
    def find(cls, num):
        """ This method should accept an id as an argument
    and return the contact who has that id
    """
        found_contact = Contact.contacts[num - 1]
        return f"{found_contact.first_name} {found_contact.last_name}: {found_contact.email} - {found_contact.note}"

    def update(self, attribute_str, new_value):
        """ This method should allow you to specify
    1. which of the contact's attributes you want to update
    2. the new value for that attribute
    and then make the appropriate change to the contact
    """
        setattr(self, attribute_str, new_value)

    @classmethod
    def find_by(cls, attribute_str, search_value):
        """This method should work similarly to the find method above
    but it should allow you to search for a contact using attributes other than id
    by specifying both the name of the attribute and the value
    eg. searching for 'first_name', 'Betty' should return the first contact named Betty
    """
        for contact in cls.contacts:
            if getattr(contact, attribute_str) == search_value:
                return f"{contact.first_name} {contact.last_name}: {contact.email} - {contact.note}"

    @classmethod
    def delete_all(cls):
        """This method should delete all of the contacts"""
        delete_list = []
        for contact in cls.contacts:
            delete_list.append(contact)

        for contact in delete_list:
            cls.contacts.remove(contact)
            cls.next_id -= 1

    def full_name(self):
        """Returns the full (first and last) name of the contact"""
        return f"{self.first_name} {self.last_name}"

    def delete(self):
        """This method should delete the contact
    HINT: Check the Array class docs for built-in methods that might be useful here
    """
        Contact.contacts.remove(self)
        Contact.next_id -= 1


    # Feel free to add other methods here, if you need them.


contact1 = Contact.create(
    "Betty", "Maker", "bettymakes@bitmakerlabs.com", "Loves Pokemon"
)
contact2 = Contact.create("Bit", "Bot", "bitbot@bitmakerlabs.com", "beep boop")

print(len(Contact.contacts))

print(contact1.id)
print(contact2.id)
print(
    Contact.all()
)  # ['1. Betty Maker: bettymakes@bitmakerlabs.com - Loves Pokemon', '2. Bit Bot: bitbot@bitmakerlabs.com - beep boop']
print(Contact.find(1))  # Betty Maker: bettymakes@bitmakerlabs.com - Loves Pokemon
print(Contact.find(2))  # Bit Bot: bitbot@bitmakerlabs.com - beep boop

contact2.update("note", "This is a new note!")
print(contact2.note)  # This is a new note!

print(Contact.find_by("first_name", "Bit"))

# Contact.delete_all()
print(Contact.all())
print(Contact.next_id)

print(contact1.full_name())

contact2.delete()
print(Contact.all())
