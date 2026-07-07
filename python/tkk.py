# import tkinter as tk

# root = tk.Tk() 
# root.title("My First App") 
# root.geometry("300x200")

# label = tk.Label(root, text="Hello world!")  
# label.pack()  

# root.mainloop()



import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as tkmb
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

x = ctk.CTk()
x.title("Login Page")
def login():
    username = "shifali"
    password = "@shifali098"

    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo("Login Successful", "You have logged in successfully!")
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showerror("Wrong Username", "Please check your username.")
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showerror("Wrong Password", "Please enter the correct password.")
    else:
        tkmb.showerror("Login Failed", "Invalid username and password.")

frame = ctk.CTkFrame(master=x)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = ctk.CTkLabel(frame, text="Login Window", font=("Arial", 20))
label.pack(pady=10)

user_entry = ctk.CTkEntry(frame, placeholder_text="Username")
user_entry.pack(pady=10)

user_pass = ctk.CTkEntry(frame, placeholder_text="Password", show="*")
user_pass.pack(pady=10)
btn = ctk.CTkButton(frame, text="Login", command=login)
btn.pack(pady=10)

x.mainloop()