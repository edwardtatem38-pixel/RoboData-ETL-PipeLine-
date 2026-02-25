# RoboData-ETL-PipeLine-
A Python and SQL Server Extract, Transform and Load that simulates real-time robotic arm kinematics. This project extracts joints angles and coordinate data, transforms timestamps for readability, and loads the results into relational database for industrial logging. 

# Robot-Kinematics-ETL-Pipeline

An end-to-end data pipeline that simulates robotic arm movements in Python and logs the telemetry data into a Microsoft SQL Server database.

## 🚀 Project Overview
This project demonstrates a functional ETL (Extract, Transform, Load) workflow:
* **Extract:** Python simulates joint angles ($J_1$) and Cartesian coordinates ($X, Y$).
* **Load:** Data is streamed via `pyodbc` into a local MS SQL Server Express instance.
* **Transform:** SQL queries format raw timestamps into human-readable reporting formats.

## 🛠️ Technical Stack
* **Language:** Python 3.10
* **Database:** Microsoft SQL Server (SSMS)
* **Libraries:** `pyodbc` for database connectivity.

## 📈 Database Schema
The project utilizes a `RobotKinematics` database with an `ArmMovementLog` table containing:
* `Entry`: Primary Key (Identity)
* `Joint1_Angle`: Floating point sensor data
* `X_Pos_mm` / `Y_Pos_mm`: Coordinate data
* `TimeStamp`: Recording time

## 🔧 Challenges Overcome
* Resolved **Python Environment (venv)** conflicts to ensure correct module mapping in VS Code.
* Debugged **SQL Connection strings** and handled object name mismatch errors.

