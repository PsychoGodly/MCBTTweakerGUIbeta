import os
import shutil
import tkinter as tk
from tkinter import messagebox

def apply_permissions_and_replace_files():
    try:
        # Set permissions for Windows.ApplicationModel.Store.dll inside System32
        os.system('icacls "%SystemRoot%\\System32\\Windows.ApplicationModel.Store.dll" /grant Everyone:(F)')
        
        # Set permissions for Windows.ApplicationModel.Store.dll inside SysWOW64
        os.system('icacls "%SystemRoot%\\SysWOW64\\Windows.ApplicationModel.Store.dll" /grant Everyone:(F)')
        
        # Move or replace files
        shutil.copyfile("System32\\Windows.ApplicationModel.Store.dll", os.path.join(os.environ['SystemRoot'], "System32\\Windows.ApplicationModel.Store.dll"))
        shutil.copyfile("SysWOW64\\Windows.ApplicationModel.Store.dll", os.path.join(os.environ['SystemRoot'], "SysWOW64\\Windows.ApplicationModel.Store.dll"))
        
        messagebox.showinfo("Success", "Your Minecraft Successfully Tweaked")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create GUI
root = tk.Tk()
root.title("Permissions and Files Replacement")
root.geometry("300x100")

apply_button = tk.Button(root, text="Apply", command=apply_permissions_and_replace_files)
apply_button.pack(pady=20)

root.mainloop()
