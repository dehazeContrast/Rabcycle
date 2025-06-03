import tkinter as tk
from tkinter import messagebox
import csv

#Should prompt the user to enter their input and then click the button to
#continue the program
def grab_inputs(user_response, output_response, root):
    email_inputs = user_response.get().strip()
    #A check to make sure a proper email is actually put in
    output_response.config(text="")
    if not "@" in email_inputs or not "." in email_inputs:
       output_response.config(text="Please enter a vaild email addresss", fg="red")
    else:
        output_response.config(text="Email verified, Welcome to RabCycle", fg="green")
        #Will store this data on a csv file for now(will switch to the sql server)
        with open ("account.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow({email_inputs})
        root.after(1000, root.destroy) #closes the window after the entry updated
        #prevents duplicate emails from being added 

def main():
    root = tk.Tk()
    root.geometry('400x150') #sets the size of the window
    #(we can change this however we want to fit the program window)
    
    #Creates the input box for the user to put the email in
    #either it will be good or an error
    tk.Label(root, text="Enter your email address").pack(pady=(10,5))
    email_entries = tk.Entry(root, width=40)
    email_entries.pack(pady=3)
    
    #Creates the text vaild or input 
    message_output = tk.Label(root, text="")
    message_output.pack(pady=5)
    
    #Button creation
    next_button = tk.Button(root, text="Next", command=lambda: grab_inputs(email_entries, message_output, root))
    next_button.pack() #the pady creates space for the formatting of the button 
    #compared to the text box 
    
    root.mainloop()

if __name__ == "__main__":
    main()