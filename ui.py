# Import the required libraries
import tkinter as tk
from tkinter import ttk
import mysql.connector  

# Import custom classes and modules
from Lis_fxns import TestElement, InsertResult
import results_db

# Connect to the MySQL server
conn = mysql.connector.connect(
host= "localhost",
user= "root",
password= "timothy69"    
)

# Initialize and configure the database
results_db.initialize_database()

# Define the main application class using Tkinter
class App(tk.Tk):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        
        # create a main window
        self.menu = tk.Menu()
        self.title("LITE LIS")
        self.state("zoomed")

        # style a modern style button
        style = ttk.Style()
        style.configure("Modern.TButton",font=("Helvetica", 16), background="#4CAF50", foreground="black", padding=10)

        # create themed results entry and printing buttons
        self.results_entry_btn= ttk.Button(self, text="Results Entry", style="Modern.TButton", command=self.results_entry)
        self.print_results_btn = ttk.Button(self, text="Print Results", style="Modern.TButton", command=self.print_results)
        
        # place buttons at the centre of the window
        self.results_entry_btn.place(relx=0.5, rely=0.4, anchor="center")
        self.print_results_btn.place(relx=0.5, rely=0.6, anchor="center")

        # Initialize variables for patient data
        self.patient_name = None
        self.patient_id = None
        self.age = None
        self.sex = None
        self.date = None
        self.t_bil = None
        self.d_bil = None
        self.alt = None
        self.ast = None
        self.alp = None
        self.ggt = None
        self.tp = None
        self.alb = None
    
    # Function to open the results entry window
    def results_entry(self):
        # create toplevel window
        patient_form = tk.Toplevel(self)
        patient_form.title("Results Entry")
        patient_form.geometry("800x600")

        #create frame to hold patient details
        top_frame = ttk.Frame(patient_form)
        top_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        # Create patient details fields and labels
        ttk.Label(top_frame, text="Patient Name:").grid(row=0, column=0, padx=5, pady=5)    
        patient_name = ttk.Entry(top_frame)
        patient_name.grid(row=0, column=1, padx=5, pady=5)
        self.patient_name = patient_name

        # patient_id field
        ttk.Label(top_frame, text="Patient ID:").grid(row=0, column=2, padx=5, pady=5)
        patient_id = ttk.Entry(top_frame)
        patient_id.grid(row=0, column=3, padx=5, pady=5)
        self.patient_id = patient_id

        #patient age field
        ttk.Label(top_frame, text="Age:").grid(row=0, column=4, padx=5, pady=5)
        age = ttk.Entry(top_frame)
        age.grid(row=0, column=5, padx=5, pady=5)
        self.age = age

        #patient sex field
        ttk.Label(top_frame, text="Sex:").grid(row=1, column=0, padx=5, pady=5)
        sex = ttk.Combobox(top_frame, values=["Male", "Female", "Other"])
        sex.grid(row=1, column=1, padx=5, pady=5)
        self.sex = sex

        #date field
        ttk.Label(top_frame, text="Date:").grid(row=1, column=2, padx=5, pady=5)
        date = ttk.Entry(top_frame)
        date.grid(row=1, column=3, padx=5, pady=5)
        self.date = date

        #create middle frame
        middle_frame = ttk.Frame(patient_form)
        middle_frame.pack(padx=10, pady=10, fill=tk.BOTH)
        
        # create results entry headings
        ttk.Label(middle_frame, text="Test", font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, columnspan=4)
        ttk.Label(middle_frame, text="Result", font=("Helvetica", 12, "bold")).grid(row=0, column=4, padx=50, pady=5, columnspan=4)
        ttk.Label(middle_frame, text="Unit", font=("Helvetica", 12, "bold")).grid(row=0, column=8, padx=10, pady=5, columnspan=2)
        ttk.Label(middle_frame, text="Reference range", font=("Helvetica", 12, "bold")).grid(row=0, column=10, padx=20, pady=5)

        # create Total bilirubin entry points
        self.t_bil = TestElement(parent_frame=middle_frame,row=1, test_name="Total bilirubin", r_range="0 - 10", unit="umol/l")
        self.t_bil.create_widgets()
         
        # create Direct bilirubin entry points
        self.d_bil = TestElement(parent_frame=middle_frame,row=2, test_name="Direct bilirubin", r_range="0 - 5", unit="umol/l")
        self.d_bil.create_widgets()    

        # create ALT entry points
        self.alt = TestElement(parent_frame=middle_frame, row=3, test_name="ALT", r_range="10 - 45", unit="U/L")
        self.alt.create_widgets()
        
        # create AST entry  points
        self.ast = TestElement(parent_frame=middle_frame, row=4, test_name="AST", r_range="10 - 35", unit="U/L")
        self.ast.create_widgets()
        
        # create ALP entry points
        self.alp = TestElement(parent_frame=middle_frame, row=5, test_name="ALP", r_range="38 - 126", unit="U/L")
        self.alp.create_widgets()
        
        # create ggt entry points
        self.ggt = TestElement(parent_frame=middle_frame, row=6, test_name="GGT", r_range="12 - 58", unit="U/L")
        self.ggt.create_widgets()
        
        # create total protein entry points
        self.tp = TestElement(parent_frame=middle_frame, row=7, test_name="Total Protien", r_range="63 - 82", unit="g/L")
        self.tp.create_widgets()
        
        # create albumin entry points
        self.alb = TestElement(parent_frame=middle_frame, row=8, test_name="Albumin", r_range="35 - 50", unit="g/L")
        self.alb.create_widgets()
        

        #create frame to hold buttons
        bottom_frame = ttk.Frame(patient_form)
        bottom_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        #create save button
        self.button = ttk.Button(bottom_frame, text="Save", style="Modern.TButton", command=self.save_data)
        self.button.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        #create clear button
        self.button = ttk.Button(bottom_frame, text="Clear", style="Modern.TButton", command= self.clear_form)
        self.button.grid(row=0, column=2, padx=10, pady=10, sticky='e')     

    # Function to clear the form 
    def clear_form(self):
    # Reset all the input fields to empty or default values
        self.patient_name.delete(0, tk.END)
        self.patient_id.delete(0, tk.END)
        self.age.delete(0, tk.END)
        self.sex.set("")  # Clear the selected sex
        self.date.delete(0, tk.END)
        self.t_bil.entry_widget.delete(0, tk.END)
        self.d_bil.entry_widget.delete(0, tk.END)
        self.alt.entry_widget.delete(0, tk.END)
        self.ast.entry_widget.delete(0, tk.END)
        self.alp.entry_widget.delete(0, tk.END)
        self.ggt.entry_widget.delete(0, tk.END)
        self.tp.entry_widget.delete(0, tk.END)
        self.alb.entry_widget.delete(0, tk.END)
    # Function to save entered data to the database
    def save_data(self):
        insert_handler = InsertResult(self.conn)
        insert_handler.insert_data(
            self.patient_id.get(),
            self.patient_name.get(),
            int(self.age.get()),
            self.sex.get(),
            self.date.get(),
            float(self.t_bil.get_value()),
            float(self.d_bil.get_value()),
            float(self.alt.get_value()),
            float(self.ast.get_value()),
            float(self.alp.get_value()),
            float(self.ggt.get_value()),
            float(self.tp.get_value()),
            float(self.alb.get_value())
        )

        #clear the form
        self.clear_form()

    
    def clear_entries(self):
        # Clear the contents of the entry widgets
            self.name_entry.delete(0, tk.END)
            self.id_entry.delete(0, tk.END)
    
    # print results from database
    def print_results(self):
        # create a new top level
        print_window= tk.Toplevel(self)
        print_window.title("Print Results")
        print_window.geometry("800x600")

        # create frame to hold widgets
        frame = tk.Frame(print_window, background="lightblue")
        frame.place(relx=0.5, rely=0.5, anchor='center') 

        # Label and Entry for name 
        ttk.Label(frame, text="Name:", style="Modern.TButton").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(frame, style="Modern.TButton")
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Label and Entry for Patient ID
        ttk.Label(frame, text="Patient ID:", style="Modern.TButton").grid(row=1, column=0, padx=5, pady=5)
        self.id_entry = ttk.Entry(frame, style="Modern.TButton")
        self.id_entry.grid(row=1, column=1, padx=5, pady=5)

        # Add search and clear buttons
        ttk.Button(frame, text="Search").grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(frame, text="Clear", command=self.clear_entries).grid(row=2, column=1, padx=5, pady=5)

        


# Entry point of the program
if __name__ == '__main__':
    # Create an instance of the App class and start the GUI event loop
    app = App(conn)
    app.mainloop()