import random
import string
import tkinter as tk
from tkinter import messagebox



def generate_password(min_length, uppercase=True, lowercase=True, numbers=True, special_charaters=True):
#Defining Characters

    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

  
# Combine Character sets

    characters = ""
    if uppercase:
        characters += uppercase_letters
    if lowercase:
        characters += lowercase_letters
    if numbers:
        characters += digits
    if special_charaters:
        characters += special

    if not characters:
        raise ValueError("At least one character type must be selected to generate the password")



    password = ""
    meets_criteria = False
  

    while not meets_criteria or len(password) < min_length: 
        password = ""
        has_uppercase = has_lowercase = has_digits = has_special = False 

        while len(password) < min_length:
            new_char = random.choice(characters)
            password += new_char

        
            if new_char in uppercase_letters:
                has_uppercase = True
            if new_char in lowercase_letters:
                has_lowercase = True
            if new_char in digits:
                has_digits = True
            if new_char in special:
                has_special = True

        meets_criteria = True
        if uppercase and not has_uppercase:
            meets_criteria = False
        if lowercase and not has_lowercase:
            meets_criteria = False
        if numbers and not has_digits:
            meets_criteria = False
        if special_charaters and not has_special:
            meets_criteria = False

    return password

#Function to save code as file
def save_password_as_file(password):
    try:
        with open("passwords.txt", "a") as file:
            file.write(password + "\n")
    except Exception as e:
        messagebox.showerror("File Error", f"Failed to save your password: {e}")


#Graphical User Interface Logic
def on_generate():
    try:
        length = int(entry_length.get())
        if length <=0:
            raise ValueError("Passwrod length must be a postve integer.")
    
        use_upper = var_upper.get()
        use_lower = var_lower.get()
        use_digits = var_numbers.get()
        use_special = var_special.get()

        if not(use_upper or use_lower or use_digits or use_special):
            messagebox.showwarning("Input Error", "Select at least one charcater.")
            return


        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        output_var.set(password)
        save_password_as_file(password)

        messagebox.showinfo("Password Generated", f"Password generated and saved:\n{password}")

    except ValueError:
        messagebox.showinfo("Password Generated", f"Password generated and saved:\n{password}")

#Graphical User INterface Windwo Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Minimum Pssword Length:").pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack()

#Checboxes to Select Character Options
var_upper = tk.BooleanVar(value=True)
var_lower =tk.BooleanVar(value=True)
var_numbers =tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Uppercase Leters", variable=var_upper).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Lowercase Leters", variable=var_lower).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Numbers", variable=var_numbers).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Special Characters", variable=var_special).pack(anchor="w", padx=20)

#Output dispaly and Genertae Button
output_var = tk.StringVar()
tk.Label(root, text="Generate_Password").pack(pady=10)
tk.Entry(root, textvariable=output_var, width=60, state="readonly").pack()

tk.Button(root, text="generate password", command=on_generate).pack(pady=20)

root.mainloop()


