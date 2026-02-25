import pyodbc
import time
import random

# setup connection
# '.' means 'This Computer'. 'Trusted_Connection=yes' uses your windows login 

conn_str = (
    r'Driver={SQL Server};'
    r'Server=.\SQLEXPRESS;'
    r'Database=RobotKinematics;'
    r'Trusted_Connection=yes;'
)

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Sucessfully connected to SQL Server !")
    
    # Simulate live data (10 movements)
    for i in range(10):
        # Generate 'fake' robot sensor data
        j1 = round(random.uniform(0, 180), 2) # joint 1 angle
        j2 = round(random.uniform(0, 180), 2) # joint 2 angle
        x = round(random.uniform(100, 500), 1) # x position mm
        y = round(random.uniform(100, 500), 1) # y position mm
        
        # send to sql 
        sql_query = "INSERT INTO ArmMovementLog (Joint1_Angle, Joint2_Angle, X_Pos_mm, Y_Pos_mm) VALUES (?, ?, ?, ?)"
        cursor.execute(sql_query, (j1, j2, x, y))
        conn.commit() # saves the data
        
        print(f"Movement {i+1} Logged: J1={j1}, X={x}")
        time.sleep(1) # wait 1 second between movements 
    print("Mission Complete All data sent to SQL.")
    conn.close()
except Exception as e:
    print(f"Error: {e}")
