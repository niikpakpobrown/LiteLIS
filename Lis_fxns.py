# Import the required libraries for GUI elements and database interaction
import tkinter as tk
from tkinter import ttk

# Custom class for displaying and handling test elements in the UI
class TestElement:
    def __init__(self, parent_frame, row, test_name, r_range, unit):
        self.parent_frame = parent_frame
        self.row = row
        self.test_name = test_name
        self.r_range = r_range
        self.unit = unit

        self.entry_widget = None

        self.create_widgets()

    # Create and arrange widgets for displaying a test element
    def create_widgets(self):
        ttk.Label(self.parent_frame, text=self.test_name, font=("Helvetica", 12, "bold")).grid(row=self.row, column=0, padx=5, pady=5, columnspan=4)
        entry = ttk.Entry(self.parent_frame, font=("Helvetica", 12, "bold"))
        entry.grid(row=self.row, column=4, padx=50, pady=5, columnspan=4)
        self.entry_widget = entry
        ttk.Label(self.parent_frame, text=self.unit, font=("Helvetica", 12, "bold")).grid(row=self.row, column=8, padx=20, pady=5)
        ttk.Label(self.parent_frame, text=self.r_range, font=("Helvetica", 12, "bold")).grid(row=self.row, column=10, padx=10, pady=5, columnspan=2)

    # Get the value entered in the test element's entry widget
    def get_value(self):
        return self.entry_widget.get()
    
# Custom class for inserting test results into the database      
class InsertResult:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    # Insert test result data into the database
    def insert_data(self, patient_id, patient_name, age, sex, test_date, t_bil, d_bil, alt, ast, alp, ggt, tp, alb):
        cursor= self.db_connector.cursor()
        cursor.execute("USE local_lis")

        # SQL INSERT query
        insert_query = """
        INSERT INTO LabTestResults (patient_id, patient_name, age, sex, test_date, t_bil_result, d_bil_result, alt_result, ast_result, alp_result, ggt_result, tp_result, alb_result)
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

# custom class for printing results
class LisDatabase:
    def __init__(self, db_connector):
         self.db_connector = db_connector

    def search_results_by_patient_id(self, patient_id):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM your_table_name WHERE patient_id = %s"
            cursor.execute(query, (patient_id,))
            results = cursor.fetchall()
            return results
        except Exception as e:
            print("Error searching database:", str(e))
        finally:
            cursor.close()


