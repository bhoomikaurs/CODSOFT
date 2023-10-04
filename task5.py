import json


class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class ContactBook:
    def __init__(self):
        self.contacts_list = []

    def save_contacts_to_file(self):
        with open('contacts.json', 'w') as file:
            json.dump([contact.__dict__ for contact in self.contacts_list], file)

    def add_new_contact(self):
        print("\nAdd Contact")
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contact = Contact(name, phone, email, address)

        self.contacts_list.append(contact)
        self.save_contacts_to_file()
        print(f"{name} has been added to your contacts.")

    def display_all_contacts(self):
        print("\nView Contact List")
        if not self.contacts_list:
            print("Your contact list is empty.")
        else:
            for index, contact in enumerate(self.contacts_list, start=1):
                print(
                    f"{index}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")

    def search_for_contact(self):
        print("\nSearch Contact")
        search_query = input("Enter name or phone number to search: ")

        found_contacts = []

        for contact in self.contacts_list:
            if search_query.lower() in contact.name.lower() or search_query in contact.phone:
                found_contacts.append(contact)

        if found_contacts:
            print("Matching Contacts:")
            for index, contact in enumerate(found_contacts, start=1):
                print(
                    f"{index}. Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("No matching contacts found.")

    def update_existing_contact(self):
        self.display_all_contacts()
        if not self.contacts_list:
            return

        choice = int(input("Enter the number of the contact to update: "))
        if 1 <= choice <= len(self.contacts_list):
            contact = self.contacts_list[choice - 1]
            print(f"Editing Contact: {contact.name}")
            contact.name = input("Enter Updated Name: ")
            contact.phone = input("Enter Updated Phone Number: ")
            contact.email = input("Enter Updated Email: ")
            contact.address = input("Enter Updated Address: ")
            self.save_contacts_to_file()
            print("Contact updated successfully.")
        else:
            print("Invalid choice. Please select a valid contact.")

    def delete_existing_contact(self):
        self.display_all_contacts()
        if not self.contacts_list:
            return

        choice = int(input("Enter the number of the contact to delete: "))
        if 1 <= choice <= len(self.contacts_list):
            contact = self.contacts_list.pop(choice - 1)
            self.save_contacts_to_file()
            print(f"{contact.name} has been deleted from your contacts.")
        else:
            print("Invalid choice. Please select a valid contact.")

    def contact_book_menu(self):
        try:
            with open('contacts.json', 'r') as file:
                self.contacts_list = [Contact(**contact_info)
                                      for contact_info in json.load(file)]
        except FileNotFoundError:
            pass
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_new_contact()
            elif choice == '2':
                self.display_all_contacts()
            elif choice == '3':
                self.search_for_contact()
            elif choice == '4':
                self.update_existing_contact()
            elif choice == '5':
                self.delete_existing_contact()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    contact_book = ContactBook()
    print("Welcome to the Contact Book!")
    contact_book.contact_book_menu()
