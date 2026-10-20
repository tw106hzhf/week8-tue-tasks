# Credit: The Database SQL code is from this YouTube Video: https://www.youtube.com/watch?v=_vxobA36UN4
# The original file was in SQL. Gemini converted the SQL file into a Python file to generate the database.

import sqlite3
import os

DATABASE_FILE = 'school_database.db'

# The complete SQL script for creating tables and inserting data.
# Note: Data types (VARCHAR, DECIMAL, DATE) have been mapped to
# SQLite equivalents (TEXT, REAL, TEXT). Foreign Key added for safety.
STUDENT_GRADES_SQL = """
PRAGMA foreign_keys = ON; -- Enforce foreign key constraints

-- Delete tables if they exist to ensure a clean run
DROP TABLE IF EXISTS student_grades;
DROP TABLE IF EXISTS students;

-- Table structure for table `students`
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    student_name TEXT,
    grade_level INTEGER,
    gpa REAL, -- Maps DECIMAL(2, 1)
    school_lunch TEXT,
    birthday TEXT, -- Maps DATE
    email TEXT
);

-- Table structure for table `student_grades`
CREATE TABLE student_grades (
    semester_id TEXT,
    class_id INTEGER,
    department TEXT,
    class_name TEXT,
    student_id INTEGER,
    final_grade INTEGER,
    PRIMARY KEY (semester_id, class_id, student_id),
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Insert data into table `students`
INSERT INTO students (id, student_name,  grade_level, gpa, school_lunch, birthday, email) VALUES
(1, 'Abby Johnson', 10, 3.1, 'Yes', '2008-05-14', 'abby.johnson@mavenhighschool.com'),
(2, 'Bob Smith', 11, 3.1, 'No', '2007-09-30', 'bob.smith@mavenhighschool.com'),
(3, 'Catherine Davis', 12, 3.6, 'Yes', '2006-11-21', 'catherine.davis@mavenhighschool.com'),
(4, 'Daniel Brown', 9, 3.5, 'Yes', '2009-03-10', 'daniel.brown@mavenhighschool.com'),
(5, 'Eva Martinez', 10, 2.7, 'No', '2008-02-05', 'eva.martinez@mavenhighschool.com'),
(6, 'Frank Wilson', 11, 3.2, 'No', '2007-07-17', 'frank.wilson@mavenhighschool.com'),
(7, 'Grace Lee', 12, 3.0, 'Yes', '2006-12-02', 'grace.lee@mavenhighschool.com'),
(8, 'Henry Taylor', 9, 3.0, 'Yes', '2009-06-08', 'henry.taylor@mavenhighschool.com'),
(9, 'Isabella Moore', 10, 2.8, 'Yes', '2008-01-19', 'isabella.moore@mavenhighschool.com'),
(10, 'Jack Thompson', 11, 2.9, 'Yes', '2007-04-25', 'jack.thompson@mavenhighschool.com'),
(11, 'Karen White', 9, 3.4, 'No', '2009-09-10', 'karen.white@mavenhighschool.com'),
(12, 'Liam Green', 10, 4.0, 'Yes', '2008-08-03', 'liam.green@mavenhighschool.com'),
(13, 'Mia Harris', 11, 3.0, 'No', '2007-02-28', 'mia.harris@mavenhighschool.com'),
(14, 'Noah Scott', 12, NULL, 'No', '2006-10-15', 'noah.scott@mavenparkdistrict.com'),
(15, 'Olivia Adams', 9, 3.7, 'Yes', '2009-12-11', 'olivia.adams@mavenhighschool.com'),
(16, 'Peter Park', 12, 2.9, 'Yes', '2006-02-11', 'peter.park@mavenhighschool.com');

-- Insert data into table `student_grades`
INSERT INTO student_grades (semester_id, class_id, department, class_name, student_id, final_grade) VALUES
('SPR_2024', 101, 'Math', 'Algebra', 4, 85),
('SPR_2024', 101, 'Math', 'Algebra', 8, 76),
('SPR_2024', 101, 'Math', 'Algebra', 11, 90),
('SPR_2024', 101, 'Math', 'Algebra', 15, 97),
('SPR_2024', 102, 'Math', 'Geometry', 1, 93),
('SPR_2024', 102, 'Math', 'Geometry', 5, 80),
('SPR_2024', 102, 'Math', 'Geometry', 9, 72),
('SPR_2024', 103, 'Math', 'Statistics', 2, 88),
('SPR_2024', 103, 'Math', 'Statistics', 6, 90),
('SPR_2024', 103, 'Math', 'Statistics', 10, 82),
('SPR_2024', 103, 'Math', 'Statistics', 12, 99),
('SPR_2024', 103, 'Math', 'Statistics', 13, 85),
('SPR_2024', 104, 'Math', 'Calculus', 3, 98),
('SPR_2024', 104, 'Math', 'Calculus', 7, 86),
('SPR_2024', 104, 'Math', 'Calculus', 16, 71),
('SPR_2024', 201, 'Science', 'Biology', 4, 82),
('SPR_2024', 201, 'Science', 'Biology', 8, 72),
('SPR_2024', 201, 'Science', 'Biology', 11, 87),
('SPR_2024', 201, 'Science', 'Biology', 15, 96),
('SPR_2024', 202, 'Science', 'Chemistry', 1, 94),
('SPR_2024', 202, 'Science', 'Chemistry', 2, 87),
('SPR_2024', 202, 'Science', 'Chemistry', 5, 74),
('SPR_2024', 202, 'Science', 'Chemistry', 6, 98),
('SPR_2024', 202, 'Science', 'Chemistry', 9, 76),
('SPR_2024', 203, 'Science', 'Physics', 3, 95),
('SPR_2024', 203, 'Science', 'Physics', 7, 82),
('SPR_2024', 203, 'Science', 'Physics', 10, 77),
('SPR_2024', 203, 'Science', 'Physics', 12, 96),
('SPR_2024', 203, 'Science', 'Physics', 13, 86),
('SPR_2024', 203, 'Science', 'Physics', 16, 74),
('SPR_2024', 301, 'Humanities', 'English', 1, 82),
('SPR_2024', 301, 'Humanities', 'English', 4, 75),
('SPR_2024', 301, 'Humanities', 'English', 5, 87),
('SPR_2024', 301, 'Humanities', 'English', 8, 80),
('SPR_2024', 301, 'Humanities', 'English', 9, 84),
('SPR_2024', 301, 'Humanities', 'English', 11, 98),
('SPR_2024', 301, 'Humanities', 'English', 15, 99),
('SPR_2024', 302, 'Humanities', 'World History', 2, 75),
('SPR_2024', 302, 'Humanities', 'World History', 3, 92),
('SPR_2024', 302, 'Humanities', 'World History', 6, 95),
('SPR_2024', 302, 'Humanities', 'World History', 7, 94),
('SPR_2024', 302, 'Humanities', 'World History', 10, 84),
('SPR_2024', 302, 'Humanities', 'World History', 12, 98),
('SPR_2024', 302, 'Humanities', 'World History', 13, 82),
('SPR_2024', 302, 'Humanities', 'World History', 16, 86),
('SPR_2024', 401, 'General', 'Physical Education', 1, 85),
('SPR_2024', 401, 'General', 'Physical Education', 2, 80),
('SPR_2024', 401, 'General', 'Physical Education', 4, 95),
('SPR_2024', 401, 'General', 'Physical Education', 5, 85),
('SPR_2024', 401, 'General', 'Physical Education', 6, 95),
('SPR_2024', 401, 'General', 'Physical Education', 8, 90),
('SPR_2024', 401, 'General', 'Physical Education', 9, 90),
('SPR_2024', 401, 'General', 'Physical Education', 10, 85),
('SPR_2024', 401, 'General', 'Physical Education', 11, 95),
('SPR_2024', 401, 'General', 'Physical Education', 12, 95),
('SPR_2024', 401, 'General', 'Physical Education', 13, 90),
('SPR_2024', 401, 'General', 'Physical Education', 15, 95),
('SPR_2024', 404, 'General', 'Senior Seminar', 3, 100),
('SPR_2024', 404, 'General', 'Senior Seminar', 7, 98),
('SPR_2024', 404, 'General', 'Senior Seminar', 16, 95);
-- Note: Two rows referencing non-existent student IDs (17, 18) were removed to avoid a Foreign Key violation.
"""

def setup_database_and_load_data():
    """Connects to SQLite, executes the full SQL script, and verifies the data."""
    conn = None
    try:
        # Remove existing database file for a clean run
        if os.path.exists(DATABASE_FILE):
            os.remove(DATABASE_FILE)
            print(f"Removed existing database file: {DATABASE_FILE}")

        # Connect to SQLite database (creates it if it doesn't exist)
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Execute the full SQL script (DDL and DML) at once
        print(f"\nCreating tables and inserting data into {DATABASE_FILE}...")
        cursor.executescript(STUDENT_GRADES_SQL)

        # Commit changes
        conn.commit()
        print("SQL script execution complete. Database populated.")

        # Verification: Run a query to confirm data loaded correctly (e.g., Abby Johnson's scores)
        print("\n--- Verification Query (Abby Johnson's Scores) ---")
        cursor.execute('''
            SELECT
                s.student_name, g.class_name, g.final_grade
            FROM
                students s
            JOIN
                student_grades g ON s.id = g.student_id
            WHERE
                s.student_name = 'Abby Johnson'
            ORDER BY
                g.class_name
        ''')
        results = cursor.fetchall()

        if results:
            print(f"{'Student':<20}{'Class':<20}{'Grade':<5}")
            print("-" * 45)
            for name, class_name, final_grade in results:
                print(f"{name:<20}{class_name:<20}{final_grade:<5}")
        else:
            print("Verification failed: No data found for Abby Johnson.")

    except sqlite3.Error as e:
        print(f"\nAn SQLite error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print(f"\nDatabase connection closed. Data saved to {DATABASE_FILE}.")

if __name__ == "__main__":
    setup_database_and_load_data()
