import customtkinter

class Login(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.admin_label = customtkinter.CTkLabel(self, text="Administrator Login", fg_color="transparent")
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter Account Number")
        