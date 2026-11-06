# 1. Customer/User  Requirements
# 2. Prototype/ Design / (Final by the User)
# 3. Development (1 week)
# 4. Testing (1 week) - get back to Customer and show and review
# Loops 1 - 4
# 5. Final Testing and release the website/App

# Requirement for Notes App:

# 1. People notes on it based on Subject Title   : Dictionaries key
# 2. Multiple Notes   : Dictionaries Data Types
# 3. Search the Notes by Subject Title   :   Dictionaries key
# 4. Add Notes    : Add into Dictionaries
# 5. Edit Notes   :  Edit into Dictionaries
# 6. Delete/Remove Notes :  Remove into Dictionaries
# 7. Organize the Notes by Alphabets

# Template
# Note App
# 1. Add notes
# 2. Edit notes
# 3. Search notes
# 4. View notes
# 5. Delete notes
# 6. Exit notes

# Nested Container Data Types:
note = {
    "category": [],
    "title": [],
    "content": [],
    "date": []
}
#notes_app = {"Category" : "" }    # Collect all Notes you wan to Create   # SET
def addnote():
    title = input("Enter the title: ").strip()        # String
    content = input("Enter the content: ").strip()
    date = datetime.date.today().strftime("%m/%d/%Y")

    note["title"].append(title)
    note["content"].append(content)
    note["date"].append(date)
    print("Notes Added Successfully")
    print(note)

def save_file():
    with open("notes1.json", "w") as file:
        json.dump(notes, file, indent = 6)
    print("Save into file")

def load_file():
    with open('notes1.json', 'r') as file:
        loaded_data = json(file)

def addnote():
    new_title = input("Enter the title: ")
    new_content = input("Enter the content: ")
    notes["title"].append(new_title)
    notes["content"].append(new_content)
    save_notes(notes)
    print("Added Successfully")
def editnote():
    pass

def deletenote():
    pass

def searchnote():
    pass
def viewnote():
    for note in notes
        for value in notes[note]:
            print(values)
def Main_NotesApp():

    print("Notes App")
    print("-" * 25)
    while True:
        try:
            print("""
                1. Add Notes
                2. Edit Notes
                3. Search Notes
                4. Delete Notes
                5. View Notes
                6. Exit
            """)
            choice = int(input("Choose the option: ").strip())

            if choice == 1:
                print("Add Notes:")
                addnote()
            elif choice == 2:
                print("Edit Notes:")
                editnote()
            elif choice == 3:
                print("Search Notes")
                searchnote()
            elif choice == 4:
                print("Delete Notes")
                deletenote()
            elif choice == 5:
                print("View Notes")
                viewnote()
            elif choice == 6:
                print("Exit")
                break
            else:
                print("Invalid Choice, Choose between 1-6 !!!")
                continue
        except Exception as e:
            print(f"Invalid Choice, Try Again!!! {e}")
            continue

save_file()
Main_NotesApp()     # Call the Functions
