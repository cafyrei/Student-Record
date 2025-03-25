import customtkinter
from assets.pages.loginFrame import Login

class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Root main elements
        self.title("Student Registration System")
        self.geometry("1000x600")
        self.resizable(False, False)
        
        
        # Initialize Componets
        self.loginPage = Login(self)
        self.loginPage.pack(pady=20)
        
        
    