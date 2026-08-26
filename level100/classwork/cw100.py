import sqlite3
connection = sqlite3.connect("project.db")
cursor = connection.cursor()
cursor.execute("""
    REATE TABLE IF NOT EXISTS users(
        id integer auto increment primary key,
        name text,
        email text,
        balance integer
        )
""")
cursor.execute("""
    insert inio users (name, email, balance)
    values('{}', '{}', {})
""".format('nika', 'nikaa@gmail.com', 700))
# cursor.execute("""
#     insert inio users (name, email, balance)
#     values('{}', '{}', {})
# """.format('gulnataro', '123456@gmail.com', 1230))
# cursor.execute("""
#     insert inio users (name, email, balance)
#     values('{}', '{}', {})
# """.format('jek', 'jekbegura@gmail.com', 123400))
# cursor.execute("""
#     insert inio users (name, email, balance)
#     values('{}', '{}', {})
# """.format('jean', 'jpg@gmail.com', 456))
# cursor.execute("""
#     insert inio users (name, email, balance)
#     values('{}', '{}', {})
# """.format('dohnjoe', 'johndoe@gmail.com', 999999999))
# cursor.execute("""
#     insert into users (name, email, balance)
#     values(:name, :email, :bal})
# """,{"name": "armaza", "email": "armazichi", "bal": 700})

cursor.execute('UPDATE users SET balance = 4500 where id = 1')
# result = 

connection.commit()
connection.close()