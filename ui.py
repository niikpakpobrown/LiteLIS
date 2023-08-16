import tkinter as tk
from tkinter import ttk
from TestElement import TestElement 

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # create a main window
        self.menu = tk.Menu()
        self.title("LITE LIS")
        self.state("zoomed")

        # style a modern style button
        style = ttk.Style()
        style.configure("Modern.TButton",font=("Helvetica", 16), background="#4CAF50", foreground="black", padding=10)

        # create themed results entry and printing buttons
        self.results_entry_btn= ttk.Button(self, text="Results Entry", style="Modern.TButton", command=self.results_entry)
        self.print_results_btn = ttk.Button(self, text="Print Results", style="Modern.TButton")
        
        # place buttons at the centre of the window
        self.results_entry_btn.place(relx=0.5, rely=0.4, anchor="center")
        self.print_results_btn.place(relx=0.5, rely=0.6, anchor="center")

    # results entry window
    def results_entry(self):
        # create toplevel window
        patient_form = tk.Toplevel(self)
        patient_form.title("Results Entry")
        patient_form.geometry("800x600")
        #style = ttk.Style()
        #style.configure("My.Style", background="lightblue", borderwidth=10, relief="solid")

        #create frame to hold patient details
        top_frame = ttk.Frame(patient_form)
        top_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        # patient name field
        ttk.Label(top_frame, text="Patient Name:").grid(row=0, column=0, padx=5, pady=5)    
        patient_name = ttk.Entry(top_frame)
        patient_name.grid(row=0, column=1, padx=5, pady=5)
        
        # patient_id field
        ttk.Label(top_frame, text="Patient ID:").grid(row=0, column=2, padx=5, pady=5)
        patient_id = ttk.Entry(top_frame)
        patient_id.grid(row=0, column=3, padx=5, pady=5)

        #patient age field
        ttk.Label(top_frame, text="Age:").grid(row=0, column=4, padx=5, pady=5)
        age = ttk.Entry(top_frame)
        age.grid(row=0, column=5, padx=5, pady=5)
        
        #patient sex field
        ttk.Label(top_frame, text="Sex:").grid(row=1, column=0, padx=5, pady=5)
        sex = ttk.Combobox(top_frame, values=["Male", "Female", "Other"])
        sex.grid(row=1, column=1, padx=5, pady=5)

        #date field
        ttk.Label(top_frame, text="Date:").grid(row=1, column=2, padx=5, pady=5)
        date = ttk.Entry(top_frame)
        date.grid(row=1, column=3, padx=5, pady=5)

        #create middle frame
        middle_frame = ttk.Frame(patient_form)
        middle_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        # create results entry headings
        ttk.Label(middle_frame, text="Test", font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, columnspan=4)
        ttk.Label(middle_frame, text="Result", font=("Helvetica", 12, "bold")).grid(row=0, column=4, padx=50, pady=5, columnspan=4)
        ttk.Label(middle_frame, text="Reference range", font=("Helvetica", 12, "bold")).grid(row=0, column=8, padx=10, pady=5, columnspan=2)
        ttk.Label(middle_frame, text="Unit", font=("Helvetica", 12, "bold")).grid(row=0, column=10, padx=20, pady=5)

        # create Total bilirubin entry points
        t_bil = TestElement(parent_frame=middle_frame,row=1, test_name="Total bilirubin", r_range="0 - 10", unit="umol/l")
        t_bil.create_widgets()

        # create Direct bilirubin entry points
        d_bil = TestElement(parent_frame=middle_frame,row=2, test_name="Direct bilirubin", r_range="0 - 5", unit="umol/l")
        d_bil.create_widgets()

        # create ALT entry points
        alt = TestElement(parent_frame=middle_frame, row=3, test_name="ALT", r_range="10 - 45", unit="U/L")
        alt.create_widgets()

        # create AST entry  points
        ast = TestElement(parent_frame=middle_frame, row=4, test_name="AST", r_range="10 - 35", unit="U/L")
        ast.create_widgets()
    
        # create ALP entry points
        alp = TestElement(parent_frame=middle_frame, row=5, test_name="ALP", r_range="38 - 126", unit="U/L")
        alp.create_widgets()

        # create ggt entry points
        ggt = TestElement(parent_frame=middle_frame, row=6, test_name="GGT", r_range="12 - 58", unit="U/L")
        ggt.create_widgets()

        # create total protein entry points
        tp = TestElement(parent_frame=middle_frame, row=7, test_name="Total Protien", r_range="63 - 82", unit="g/L")
        tp.create_widgets()

        # create albumin entry points
        alb = TestElement(parent_frame=middle_frame, row=8, test_name="Albumin", r_range="35 - 50", unit="g/L")
        alb.create_widgets()

if __name__ == '__main__':
    app = App()
    app.mainloop()