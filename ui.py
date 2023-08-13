import tkinter as tk
from tkinter import ttk

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


    def results_entry(self):
        patient_form = tk.Toplevel(self)
        patient_form.title("Results Entry")
        patient_form.geometry("800x600")
        #style = ttk.Style()
        #style.configure("My.Style", background="lightblue", borderwidth=2, relief="solid")
        top_frame = ttk.Frame(patient_form)
        top_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        ttk.Label(top_frame, text="Patient Name:").grid(row=0, column=0, padx=5, pady=5)    
        patient_name = ttk.Entry(top_frame)
        patient_name.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(top_frame, text="Patient ID:").grid(row=0, column=2, padx=5, pady=5)
        patient_id = ttk.Entry(top_frame)
        patient_id.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(top_frame, text="Age:").grid(row=0, column=4, padx=5, pady=5)
        age = ttk.Entry(top_frame)
        age.grid(row=0, column=5, padx=5, pady=5)
        
        ttk.Label(top_frame, text="Sex:").grid(row=1, column=0, padx=5, pady=5)
        sex = ttk.Combobox(top_frame, values=["Male", "Female", "Other"])
        sex.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(top_frame, text="Date:").grid(row=1, column=2, padx=5, pady=5)
        date = ttk.Entry(top_frame)
        date.grid(row=1, column=3, padx=5, pady=5)


        middle_frame = ttk.Frame(patient_form)
        middle_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        ttk.Label(middle_frame, text="Total Bilirubin").grid(row=0, column=0, padx=5, pady=5)
        t_bil = ttk.Entry(middle_frame)
        t_bil.grid(row=0, column=1, padx=50, pady=5)

if __name__ == '__main__':
    app = App()
    app.mainloop()