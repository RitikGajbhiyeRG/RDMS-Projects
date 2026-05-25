import mysql.connector as a

# Database connection
condb = a.connect(
    host="localhost",
    user="root",
    password="12345",
    database="student_db"
)

# Create table if not exists
def create_table():
    cursor = condb.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        age INT,
        course VARCHAR(50),
        marks FLOAT
    )
    """)
    condb.commit()


# ================= FUNCTIONS =================

def add():
    cursor = condb.cursor()

    name = input("Enter name: ").strip()
    if not name:
        print("❌ Name cannot be empty")
        return

    try:
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))
    except:
        print("❌ Invalid age or marks")
        return

    course = input("Enter course: ")

    query = "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, age, course, marks))
    condb.commit()

    print("✅ Details Added Successfully")


def view():
    cursor = condb.cursor()

    print("""
1. View all records
2. View recent 5 records
""")

    ch = input("Enter choice: ")

    if ch == "1":
        cursor.execute("SELECT * FROM students")
    elif ch == "2":
        cursor.execute("SELECT * FROM students ORDER BY id DESC LIMIT 5")
    else:
        print("❌ Invalid choice")
        return

    data = cursor.fetchall()
    if data:
        for row in data:
            print(row)
    else:
        print("❌ No records found")


def update():
    cursor = condb.cursor()

    print("""
What do you want to update?
1. Age
2. Course
3. Marks
""")

    ch = input("Enter choice: ")

    try:
        sid = int(input("Enter student ID: "))
    except:
        print("❌ Invalid ID")
        return

    if ch == "1":
        new_val = int(input("Enter new age: "))
        query = "UPDATE students SET age=%s WHERE id=%s"

    elif ch == "2":
        new_val = input("Enter new course: ")
        query = "UPDATE students SET course=%s WHERE id=%s"

    elif ch == "3":
        new_val = float(input("Enter new marks: "))
        query = "UPDATE students SET marks=%s WHERE id=%s"

    else:
        print("❌ Invalid choice")
        return

    cursor.execute(query, (new_val, sid))
    condb.commit()

    if cursor.rowcount:
        print("✅ Updated successfully")
    else:
        print("❌ No record found")


def delete():
    cursor = condb.cursor()

    try:
        sid = int(input("Enter student ID to delete: "))
    except:
        print("❌ Invalid ID")
        return

    cursor.execute("SELECT * FROM students WHERE id=%s", (sid,))
    record = cursor.fetchone()

    if record:
        print("Record:", record)
        confirm = input("Are you sure? (y/n): ").lower()

        if confirm == 'y':
            cursor.execute("DELETE FROM students WHERE id=%s", (sid,))
            condb.commit()
            print("✅ Deleted successfully")
    else:
        print("❌ Record not found")


def search():
    cursor = condb.cursor()

    name = input("Enter name to search: ")
    cursor.execute("SELECT * FROM students WHERE name LIKE %s", (f"%{name}%",))
    data = cursor.fetchall()

    if data:
        for row in data:
            print(row)
    else:
        print("❌ No results found")


# ================= MAIN LOOP =================

def main():
    create_table()

    while True:
        print("""
======== Student Management System ========
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Search Student
6. Exit
""")

        ch = input("Enter choice: ")

        if ch == "1":
            add()
        elif ch == "2":
            view()
        elif ch == "3":
            update()
        elif ch == "4":
            delete()
        elif ch == "5":
            search()
        elif ch == "6":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")


# Run program
if __name__ == "__main__":
    main()