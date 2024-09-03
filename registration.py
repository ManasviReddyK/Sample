import tkinter as tk
from tkinter import messagebox

# Function to handle the registration
def register():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    
    if not name or not email or not phone:
        messagebox.showerror("Error", "All fields are required!")
    else:
        # Here you would typically handle the registration logic (e.g., save to a database)
        # For now, we'll just show a success message
        messagebox.showinfo("Success", f"Registration successful!\nName: {name}\nEmail: {email}\nPhone: {phone}")

# Create the main window
root = tk.Tk()
root.title("Event Registration Form")

# Create and place the labels and entries for the form
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Phone").grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_phone = tk.Entry(root)
entry_phone.grid(row=2, column=1, padx=10, pady=10)

# Create and place the submit button
button_submit = tk.Button(root, text="Register", command=register)
button_submit.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
