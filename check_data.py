import sqlite3

try:
    conn = sqlite3.connect("exams_questions.db")
    cursor = conn.cursor()

    # Query the table
    cursor.execute("SELECT * FROM exam_questions LIMIT 5;")
    rows = cursor.fetchall()

    if not rows:
        print("[!] The database table is still empty.")
    else:
        print(f"[✓] Found {len(rows)} records. Displaying sample rows:\n")
        for row in rows:
            print(f"ID: {row[0]}")
            print(f"Subject: {row[1]}")
            print(f"Q: {row[2]}")
            print(f"A) {row[3]}  B) {row[4]}  C) {row[5]}  D) {row[6]}")
            print(f"Correct Answer: {row[7]}")
            print("-" * 50)

except Exception as e:
    print(f"[!] Error reading database: {e}")
finally:
    if "conn" in locals():
        conn.close()