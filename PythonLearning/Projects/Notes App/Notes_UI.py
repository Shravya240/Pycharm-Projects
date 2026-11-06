import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Notes Manager")
root.geometry("600x600")

#notes = load_notes()    # Unclear

# Widgets
frame1 = tk.Frame(root)
frame1.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

listbox = tk.Listbox(frame1, width=30)
listbox.pack(fill=tk.BOTH, expand=True)

btn_frame = tk.Frame(frame1)
btn_frame.pack(fill=tk.X)

tk.Button(btn_frame, text="Load", command="").pack(side=tk.LEFT, fill=tk.X, expand=True)
tk.Button(btn_frame, text="Delete", command="").pack(side=tk.LEFT, fill=tk.X, expand=True)
tk.Button(btn_frame, text="Toggle Done", command="").pack(side=tk.LEFT, fill=tk.X, expand=True)

# Right side (Editor)
editor_frame2 = tk.Frame(root)
editor_frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

title_entry = tk.Entry(editor_frame2, font=("Arial", 14))
title_entry.pack(fill=tk.X)

text_area = tk.Text(editor_frame2, wrap=tk.WORD, font=("Arial", 14))
text_area.pack(fill=tk.BOTH, expand=False)

tk.Button(editor_frame2, text="Save Note", command="").pack(fill=tk.X)

#refresh_list()

#
root.mainloop()