import tkinter as tk
from tkinter import ttk

# Create results entry page top frame
def create_results():
    top_frame = ttk.Frame(self)
    top_frame.pack(padx=10, pady=10, fill=tk.X)

    ttk.Label(top_frame, text="Pateint Name:").grid(row=0, column=0, padx=5, pady=5)
    patient_name = ttk.Entry(top_frame)
    atient_name.grid(row=0, column=1, padx=5, pady=5)