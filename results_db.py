import mysql.connector

try:
    # connect to server
    conn = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "timothy69"    
)

    cursor = conn.cursor()
    
    # Check if the database exists
    cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in cursor]

    if "local_lis" in databases:
        print("local_lis database already exists.")
    else:
        # Create the local_lis database
        cursor.execute("CREATE DATABASE local_lis")
        print("local_lis database created successfully.")

    # use local_lis DB
    cursor.execute("USE local_lis")


    # Check if the LabTestResults table exists
    cursor.execute("SHOW TABLES LIKE 'LabTestResults'")
    table_exists = cursor.fetchone()

    if table_exists:
        print("LabTestResults table already exists.")
    else:
        # Create the LabTestResults table
        createTable = """
        CREATE TABLE LabTestResults (
            patient_id VARCHAR(20) NOT NULL PRIMARY KEY,
            patient_name VARCHAR(100) NOT NULL,
            age INT,
            sex ENUM('Male', 'Female', 'Other'),
            test_date DATE NOT NULL,
            t_bil_result FLOAT,
            d_bil_result FLOAT,
            alt_result FLOAT,
            ast_result FLOAT,
            alp_result FLOAT,
            ggt_result FLOAT,
            tp_result FLOAT,
            alb_result FLOAT
        );"""
        cursor.execute(createTable)
        print("LabTestResults table created successfully.")

except mysql.connector.Error as err:
    print("Error:", err)
