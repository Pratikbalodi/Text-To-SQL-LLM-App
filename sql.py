import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()  #cursor is use to execute sql command

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Pratik','Data Science','C',90)''')
cursor.execute('''Insert Into STUDENT values('Abhishek','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Aakash','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Anuj','DEVOPS','C',50)''')
cursor.execute('''Insert Into STUDENT values('Harshit','DEVOPS','A',35)''')
cursor.execute('''Insert Into STUDENT values('Abhi','Cloud','C',20)''')


## Disspaly ALl the records

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()