"""Contact Book

A small command-line app for managing contacts.
Contacts are saved to a JSON file (contacts.json) next to this script,
so they are still there the next time you run it.

Run it with:  python contacts.py
"""

import json
import os

# --- Settings ---------------------------------------------------------------

# Build the file path from the script's own location, so the app works
# no matter which folder you run it from.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "contacts.json")

MENU = """
==============================
        CONTACT BOOK
==============================
  1. Add a contact
  2. View contacts
  3. Delete a contact
  4. Quit
------------------------------"""


# --- Saving and loading -----------------------------------------------------

def load_contacts():
    """Read the contact list from the JSON file.

    Returns an empty list if the file doesn't exist yet or is corrupted.
    """
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("The contacts file was corrupted, starting with an empty list.")
        return []


def save_contacts(contacts):
    """Write the whole contact list to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        # indent=2 keeps the file readable; ensure_ascii=False keeps
        # characters like ö and é instead of turning them into \u codes.
        json.dump(contacts, f, indent=2, ensure_ascii=False)


# --- Menu actions -----------------------------------------------------------

def add_contact():
    """Ask for a name and phone number, then save the new contact."""
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()

    if not name:
        print("A contact needs a name.")
        return

    contacts = load_contacts()                         # 1. load the list
    contacts.append({"name": name, "phone": phone})    # 2. add to it
    save_contacts(contacts)                            # 3. save it back
    print(f"Saved {name}.")


def view_contacts():
    """Print all contacts as a numbered list."""
    contacts = load_contacts()

    if not contacts:
        print("No contacts yet.")
        return

    print("\nYour contacts:")
    # enumerate(..., start=1) numbers the list from 1 instead of 0.
    for number, contact in enumerate(contacts, start=1):
        print(f"  {number}. {contact['name']} - {contact['phone']}")


def delete_contact():
    """Remove a contact chosen by its number in the list."""
    contacts = load_contacts()

    if not contacts:
        print("No contacts to delete.")
        return

    view_contacts()

    try:
        number = int(input("\nNumber of the contact to remove: "))
        if number <= 0:
            # Without this check, 0 would become index -1, which in Python
            # means "the last item", and delete the wrong contact.
            raise ValueError
        removed = contacts.pop(number - 1)             # list positions start at 0
    except (ValueError, IndexError):
        # ValueError: not a number (or <= 0). IndexError: number too big.
        print("Invalid contact number.")
        return

    save_contacts(contacts)
    print(f"Removed {removed['name']}.")


# --- Main program -----------------------------------------------------------

def main():
    """Show the menu again and again until the user chooses to quit."""
    while True:
        print(MENU)
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1, 2, 3 or 4.")


# This runs main() only when the file is executed directly,
# not when it is imported by another script.
if __name__ == "__main__":
    main()
