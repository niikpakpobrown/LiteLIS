import tkinter as tk
from tkinter import ttk

class TestElement:
    def __init__(self, parent_frame, row, test_name, r_range, unit):
        self.parent_frame = parent_frame
        self.row = row
        self.test_name = test_name
        self.r_range = r_range
        self.unit = unit

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.parent_frame, text=self.test_name, font=("Helvetica", 12, "bold")).grid(row=self.row, column=0, padx=5, pady=5, columnspan=4)
        ttk.Entry(self.parent_frame, font=("Helvetica", 12, "bold")).grid(row=self.row, column=4, padx=50, pady=5, columnspan=4)
        ttk.Label(self.parent_frame, text=self.unit, font=("Helvetica", 12, "bold")).grid(row=self.row, column=8, padx=20, pady=5)
        ttk.Label(self.parent_frame, text=self.r_range, font=("Helvetica", 12, "bold")).grid(row=self.row, column=10, padx=10, pady=5, columnspan=2)
       
class InsertResult:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def insert_data(self, patient_id, patient_name, age, sex, test_date, t_bil, d_bil, alt, ast, alp, ggt, tp, alb):
        # SQL INSERT query
        insert_query = """
        INSERT INTO LabTestResults (patient_id, patient_name, age, sex, test_date, t_bil, d_bil, alt, ast, alp, ggt, tp, alb)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Data to be inserted
        data = (
            patient_id, patient_name, age, sex, test_date, t_bil, d_bil, alt, ast, alp, ggt, tp, alb
        )

        # Execute the INSERT query
        cursor = self.db_connector.cursor()
        cursor.execute(insert_query, data)

        # Commit the changes
        self.db_connector.commit()
        cursor.close()
        print("Data inserted successfully.")



