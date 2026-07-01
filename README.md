# Face Recognition Attendance System

A desktop application built in Python to automate attendance tracking using face recognition. The project uses a Tkinter GUI frontend to register students, take photo samples, train the recognition model, and run live detection linked with a local MySQL database backend to automatically log daily attendance.

## How It Works
1. **Student Registration:** Add new student profiles via the GUI dashboard. The details are saved directly into a local MySQL database.
2. **Dataset Generation:** The app opens the webcam to take 100 quick photo samples of the student's face and saves them into a local directory.
3. **Training:** The trainer script reads the saved photos and uses OpenCV's LBPH algorithm to generate facial features, saving them into `classifier.xml`.
4. **Face Detection & Attendance Logging:** The live tracking screen uses Haar Cascades to find faces in the camera feed and matches them against the trained XML file. Once a face is recognized, it fetches the student's details from the database and automatically records their Name, Roll Number, and Time into the attendance log.

## Tech Stack
* **Language:** Python
* **Libraries:** OpenCV, Tkinter, Pillow (PIL), MySQL Connector
* **Database:** MySQL

## Core Modules
* `main.py` - The main dashboard menu containing routing buttons for all screens.
* `student.py` - The registration interface handling database CRUD operations (Save, Update, Delete).
* `train.py` - The training script that compiles the image dataset into the XML classifier.
* `face_recognition.py` - The camera tracking window that identifies faces, displays database details, and logs attendance records in real-time.