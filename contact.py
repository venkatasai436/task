import json
import os

# The filename where contacts will be stored
FILENAME = "contacts.json"

def load_contacts():
    """Loads contacts from the JSON file into a dictionary."""
    if not os.path.exists(FILENAME):
        return {}  # Return an empty dictionary if file doesn't exist
    
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return {} # Return empty if file is corrupt or unreadable

def save_contacts(contacts):
    """Saves the current dictionary of contacts to the JSON file."""
    try:
        with open(FILENAME, 'w') as file:
            json.dump(contacts, file, indent=4)
        print("✓ Changes saved successfully.")
    except IOError as e:
        print(f"Error saving data: {e}")

def add_contact(contacts):
    name = input("Enter Name: ").strip()
    if name in contacts:
        print(f"Contact '{name}' already exists.")
        return

    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    # Store in dictionary
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    save_contacts(contacts)
    print(f"Contact '{name}' added.")

def search_contact(contacts):
    name = input("Enter Name to search: ").strip()
    contact = contacts.get(name)

    if contact:
        print(f"\n--- Details for {name} ---")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("--------------------------")
    else:
        print(f"Contact '{name}' not found.")

def update_contact(contacts):
    name = input("Enter Name to update: ").strip()
    if name not in contacts:
        print(f"Contact '{name}' not found.")
        return

    print(f"Updating {name}. Leave blank to keep current value.")
    current_phone = contacts[name]['phone']
    current_email = contacts[name]['email']

    new_phone = input(f"Enter new phone ({current_phone}): ").strip()
    new_email = input(f"Enter new email ({current_email}): ").strip()

    # Update only if user provided input; otherwise keep old value
    contacts[name]['phone'] = new_phone if new_phone else current_phone
    contacts[name]['email'] = new_email if new_email else current_email
    
    save_contacts(contacts)
    print(f"Contact '{name}' updated.")

def delete_contact(contacts):
    name = input("Enter Name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")

def list_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- All Contacts ---")
        for name, info in contacts.items():
            print(f"{name} | {info['phone']} | {info['email']}")
        print("--------------------")

def main():
    # Load data once at the start
    contacts = load_contacts()

    while True:
        print("\n=== CONTACT BOOK ===")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List All Contacts")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            list_contacts(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()