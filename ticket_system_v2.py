import sqlite3

def get_valid_name():
    while True:
        name = input("What is your name? ").strip()
        if name == "":
            print("Name cannot be empty! ")
            continue
        elif not all(ch.isalpha() or ch.isspace() for ch in name):
            print("Name must contain letters or spaces! ")
            continue
        else:
            return name

def get_valid_age():
    while True:
        age = input("Could you enter your age? ").strip()
        if age == "":
            print("Age cannot be empty! ")
            continue
        elif not age.isdigit():
            print("Age must contain numbers! ")
            continue
        else:
            age = int(age)
            if age > 120:
                print("Age cannot be more than 120 ")
                continue
            else:
                return age

def get_student_info():
    while True:
        student_info = input("Are you a student? (y/n) ").strip().lower()
        if student_info == "":
            print("Student information cannot be empty! ")
        elif student_info == "y" or student_info == "n":
            return student_info
        else:
            print("Student information has to be 'y' or 'n' ")
            continue

def calculate_price(student_info, age):
    basic_price = 20
    student_price = 10

    if student_info == "n":
        return basic_price

    if age <=12:
        return student_price * 0.5
    elif age <=15:
        return student_price * 0.7
    else:
        return student_price

def init_db():
    conn = sqlite3.connect("tickets.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            is_student TEXT,
            price REAL
        );
    """)
    conn.commit()
    return conn

def save_ticket(conn, name, age, student_info, price):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tickets (name, age, is_student, price) VALUES (?, ?, ?, ?);",
        (name, age, student_info, price)
    )
    conn.commit()


def main():
    conn = init_db()

    name = get_valid_name()
    age = get_valid_age()
    student_info = get_student_info()

    price = calculate_price(student_info, age)

    save_ticket(conn, name, age, student_info, price)

    print("\n--- Ticket Summary ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Ticket Price: ${price:.2f}")
    conn.close()

if __name__ == "__main__":
    main()
