# A. Command Line : user input - Print on Console
# B. User Interface:  Design the screen (GUI/UI) - user input  - Print on the screen


# APP (Application)
# User Interface (Front View)    -   Functionality (Back Side)   - Database/File (Permanent Storage)
#                                -   Create a Notes
#                                -   Save a Notes
#                                -   Delete a Notes
#                                -   View a Notes

import tkinter as tk   # Lib - Access the Class TK()    - Alias (Another Name) to lib

# 1. Create the Main Window
notes_ui = tk.Tk()     # Object of that TK Class
notes_ui.title("Notes App - Akku")    # Set Title of that Objects
notes_ui.geometry("800x600")    # Set the Window Size to 800 Pixels * 600 Pixels

# 2. Add the Elements in the Main Window:
# 2.1 Add the Label Elements
label1  = tk.Label(notes_ui, text = "My Notes")
label1.pack()

# 2.2 Add the ListBox Elements
nlist = tk.Listbox(notes_ui)
nlist.pack(pady = 10)

# 2.3 Add the Text Area Elements
text_area = tk.Text(notes_ui, width = 50, height = 1, font=("Arial", 12))
text_area.pack(padx =10 , pady = 10)

# 2.4 Add the Button Elements
btn_frame = tk.Frame(notes_ui)
btn_frame.pack(padx = 5 ,pady = 5)

create_btn = tk.Button(btn_frame, text = "Create" )
create_btn.grid(padx = 10)
create_btn.pack()

save_btn = tk.Button(btn_frame, text = "Save" )
#save_btn.grid(padx = 10)
save_btn.pack()

view_btn = tk.Button(btn_frame, text = "View" )

view_btn.pack()

delete_btn = tk.Button(btn_frame, text = "Delete" )

delete_btn.pack()

# 3. Start the Tkinter Event Loop - Show the Window
notes_ui.mainloop()
