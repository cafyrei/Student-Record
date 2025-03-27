from PIL import Image
import customtkinter as ctk

class Login(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # Main frame Configuration
        self.configure(width=350, 
                       height=350,
                       corner_radius=20)
        self.pack_propagate(False)
        
        # NOTE: Declaration Section
        
        # Frame components
        self.image_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.label_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.login_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.password_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.login_button_frame = ctk.CTkFrame(self, fg_color='transparent')
        
        # Declaring the components
        self.admin_icon = ctk.CTkLabel(self.image_frame)
        self.admin_label = ctk.CTkLabel(self.label_frame)
        self.ID_entry = ctk.CTkEntry(self.login_frame)
        self.ID_password = ctk.CTkEntry(self.password_frame)
        self.submit_button = ctk.CTkButton(self.login_button_frame)
        
        # NOTE: All settings for configuration will be written under this section
        
        administrator_icon = ctk.CTkImage(
            light_image=Image.open(r"assets/img/login_page/administrator.png"), 
            size=(50, 50)
        )
        
        # Components Configuration
        
        self.admin_icon.configure(image=administrator_icon,
                                  text='')
        
        self.admin_label.configure(text='Adminsitrator',
                                   font=('Arial', 18, 'bold'))
        
        self.ID_entry.configure(placeholder_text='Account No.',
                            height=40,
                            width=250)
        
        self.ID_password.configure(placeholder_text='Password',
                                   show="*",
                                   height=40,
                                   width=250)
        
        self.submit_button.configure(height=40,
                                     width=250)
        
        
        # NOTE: This is the where all components will be added to the frame (Pack, Grids)
        
        # Add frames
        self.image_frame.pack()
        self.label_frame.pack(pady=10)
        self.login_frame.pack(pady=10)
        self.password_frame.pack(pady=10)
        self.login_button_frame.pack(pady=10)
        
        # Add components
        self.admin_icon.pack()
        self.admin_label.pack()
        self.ID_entry.pack()
        self.ID_password.pack()
        self.submit_button.pack()        
        
        # Add Components