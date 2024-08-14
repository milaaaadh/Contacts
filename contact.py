import json
import re


def load_contacts():
    file_name = input("Enter the name Json Contacs File: ")
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []



def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    if not re.match(r"^(0\d{10}|9\d{9})$", phone):
        print("Phone number Have 10 or 11 digits")
        return False
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format.")
        return False

    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")
    return True

def save_contacts(contacts):
    with open(file_name, "w") as file:
        json.dump(contacts, file, indent=4)


def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    for contact in contacts:
        if contact["name"] == name:
            print(f"Editing contact: {name}")
            contact["phone"] = input("Enter new phone number: ")
            contact["email"] = input("Enter new email: ")
            print("Contact updated successfully!")
            return
    print("Contact not found.")


def delete_contact(contacts):
    base 
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def display_contacts(contacts):
    if not contact:
        print("No contact found.")
        return
    
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def sort_contacts(contacts):
    base = input("On what basis should the contacts be sorted? (Options: name,email,phone ")
    contacts.sort(key=lambda x: x[f'{base}'])
    print(f"Contacts sorted by {base}.")
