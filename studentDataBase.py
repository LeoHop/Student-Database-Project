import sqlite3

db_name = "students.db"

connection = sqlite3.connect(db_name)

cursor = connection.cursor()

# this is so you don't recreate the school db if it already exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
 student_id integer PRIMARY KEY,
 first_name text NOT NULL,
 last_name text NOT NULL,
 email text NOT NULL UNIQUE,
 grade integer DEFAULT 9);
 """) # note: the primary key will be uniquely generated

# in case the database is new, put some students in it to get started
if len(cursor.execute("""SELECT * FROM students""").fetchall()) == 0:
    # note, no need to input the student_id
    cursor.execute("""
        INSERT INTO students 
        (first_name, last_name, email, grade)
        VALUES ("Alice", "Apples", "aapples@lsoc.org", 11)
        """)

    cursor.execute("""
        INSERT INTO students
        (first_name, last_name, email) 
        VALUES ("Bob", "Bananas", "bbananas@lsoc.org")
        """)

# loop to input many students
num = int(input("How many students do you want to input? "))
for i in range(num):
    print("Student {}: ".format(i+1))
    # get info from the user
    fname = input("First name? ")
    lname = input("Last name? ")
    email = input("Email? ")
    grade = int(input("Grade? "))

    # insert the information you got from the user
    cursor.execute("""
        INSERT INTO students 
        (first_name, last_name, email, grade) 
        VALUES ("{}", "{}", "{}", {})
        """.format(fname, lname, email, grade))



    
        DELETE 
        FROM
        students                #i do not know how to delete something if it is the same as something else
        WHERE 
        fname = fname or lname = lname


# get the student list
cursor.execute("""
    SELECT first_name, last_name
    FROM students
    """);

result = cursor.fetchall() 

print("The students:")
for r in result: 
    for c in r:
        print(c, end = ' ')
    print()

question = input("would you like me to update a students information? yes/no")

whichStudent = input("which student would you like to update?")

columChange = input("which colum would you like to change?")

newValue = input("what would you like the new value to be?")


if question = "yes"
    print(whichStudent)
    print(columChange)
    print(newValue)
    update students
    set columChange = newValue

else

# commit your results!
connection.commit()
connection.close()























sql_command = """INSERT INTO Activities(Activity_id, Activity_name, start_time, end_time, day_of_the_week)
VALUES 
 ("2", "Swimming", "3:30", "6:30 PM", "Tuesday"); """

crsr.execute(sql_command)












