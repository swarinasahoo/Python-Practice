import pg8000

# ---------- CONNECT ----------
def connect_db():
    try:
        conn = pg8000.connect(
            host="localhost",
            database="test_db",
            user="postgres",
            password="1234"
        )
        print("Step 1: Connected to database")
        return conn
    except Exception as e:
        print("Connection Error:", e)
        return None


# ---------- CREATE TABLE ----------
def create_table(conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                age INT,
                course VARCHAR(50)
            );
        """)
        conn.commit()
        cur.close()
        print("Step 2: Table created")
    except Exception as e:
        print("Table Creation Error:", e)


# ---------- INSERT ----------
def insert_data(conn, name, age, course):
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO students (name, age, course)
            VALUES (%s, %s, %s);
        """, (name, age, course))
        conn.commit()
        cur.close()
        print(f"Step 3: Inserted → {name}")
    except Exception as e:
        print("Insert Error:", e)


# ---------- READ ----------
def read_data(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students;")
        rows = cur.fetchall()
        cur.close()

        print("Step 4: Reading Data")
        for row in rows:
            print(row)
    except Exception as e:
        print("Read Error:", e)


# ---------- UPDATE ----------
def update_data(conn, name, new_age):
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE students
            SET age = %s
            WHERE name = %s;
        """, (new_age, name))
        conn.commit()
        cur.close()
        print(f"Step 5: Updated age for {name}")
    except Exception as e:
        print("Update Error:", e)


# ---------- DELETE ----------
def delete_data(conn, name):
    try:
        cur = conn.cursor()
        cur.execute("""
            DELETE FROM students
            WHERE name = %s;
        """, (name,))
        conn.commit()
        cur.close()
        print(f"Step 6: Deleted {name}")
    except Exception as e:
        print("Delete Error:", e)


# ---------- MAIN FLOW ----------
def main():
    conn = connect_db()

    if conn is None:
        return

    create_table(conn)

    insert_data(conn, "Suraj", 22, "Data Science")
    insert_data(conn, "Rahul", 21, "AI")

    read_data(conn)

    update_data(conn, "Suraj", 23)
    read_data(conn)

    delete_data(conn, "Rahul")
    read_data(conn)

    conn.close()
    print("Step 7: Connection closed")


# Run program
if __name__ == "__main__":
    main()