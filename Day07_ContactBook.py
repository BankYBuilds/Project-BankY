contacts = {
    "John": "08012345678",
    "Sarah": "08123456789",
    "David": "09034567890",
    "Grace": "07045678901",
    "Daniel": "09156789012"
}


searchContact = input("Enter a contact name:\n").strip()


matched_key = None

for name, numbers in contacts.items():
    if name.lower() == searchContact.lower():
        matched_key = name
        print(f"{matched_key}: {numbers}")
        break
if matched_key is None:
    print("Contact not found")

    choice = input("Would you like to add it? (Y/N):\n ")

    if choice.lower() == "y":
        phone_no = input("Enter phone number: ")

        contacts[searchContact.title()] = phone_no

        print("Contact added successfully!")
        for name, numbers in contacts.items():
            print(f"{name}: {numbers}")