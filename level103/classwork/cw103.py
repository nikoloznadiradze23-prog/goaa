import sqlite3

def read_blob(name, output_path):
    try:
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        sql_query = "select data"
        cursor.execute(sql_query, (name,))
        blob_data = cursor.fetchone()[0]

        with open(output_path, 'wb') as file:
            file.write(blob_data)

        print("success")

    except sqlite3.Error as error:
        print("error", error)
    finally:
        if conn:
            conn.close()