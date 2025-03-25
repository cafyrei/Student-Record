import customtkinter

# Create the root window
root = customtkinter.CTk()

# Root Elements
root.title("Student Registration System")
root.geometry("1000x600")
root.resizable(False, False)

entry = customtkinter.CTkEntry(root, placeholder_text="CTkEntry")

root.mainloop()