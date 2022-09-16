import getpass
import sqlite3 as lite
import email, smtplib


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
conn = lite.connect("student.db")
c=conn.cursor()
def create_table():
    c.execute("create table students(rollno number, name varchar(250), email varchar(250), phone number)")
    c.execute("create table marks(rollno number, telugu number, hindi number, english number, maths number, science number, social number)")
    conn.commit()
    # c.execute("insert into students values (123456,'sai','sai@gmail.com',9888888888)")
    # c.execute("insert into marks values (123456,90,90,90,90,90,90)")
    print("table created successfully")
def add_student():
    isValid=True
    while(isValid):
        rollNo=input("enter student roll no: ")
        c.execute("select * from students where rollno ="+rollNo)
        results=c.fetchall()
        if(len(results)>0):
            print("students rollNo already exists please try with new ID")
        else:
            isValid=False
            studentName=input("please enter student name: ")
            emailId=input("please enter parent's email Id: ")
            phoneNumber=input("please enter parent's phone number: ")
            c.execute("insert into students values ("+rollNo+",'"+studentName+"','" +emailId+ "',"+phoneNumber+")")
            conn.commit()
            print("student details saved successfully\n")
            mark=(input("press 1 to add marks to student "+studentName+ "roll no "+rollNo+"and press other key to update later "))
            if(mark=='1'):
                print("print AB if the student is absent for exam\n")
                telugu=input("enter marks for telugu: ")
                hindi=input("enter marks for hindi: ")
                english=input("enter marks for english: ")
                maths=input("enter marks for maths: ")
                science=input("enter marks for science: ")
                social=input("enter marks for social: ")
                c.execute("insert into marks values ("+rollNo+",'"+telugu+"', '"+hindi+"', '"+english+"','"+maths+"','"+science+"','"+social+"')")
                conn.commit()
                print("marks added successfully")
            else:
                #c.execute("insert into marks(rollno) values("+rollNo+")")
                telugu='0'
                hindi='0'
                english='0'
                maths='0'
                science='0'
                social='0'
                c.execute("insert into marks values ("+rollNo+",'"+telugu+"', '"+hindi+"', '"+english+"','"+maths+"','"+science+"','"+social+"')")
                conn.commit()
                print("student record inserted successfully in marks with values 0")
                print("please update marks later")
def update_student_marks():
    rollNo=input("enter student rollno: ")
    c.execute("select * from students where rollno ="+rollNo)
    results=c.fetchall()
    if(len(results)<=0):
        print("students rollNo not found in database")
    else:
        c.execute("select * from marks where rollno ="+rollNo)
        marks=c.fetchall()
        print('enter the telugu marks : '+"existing marks: "+str(marks[0][1]))
        telugu=input()
        print('enter the hindi marks : '+"existing marks: "+str(marks[0][2]))
        hindi=input()
        print('enter the english marks : '+"existing marks: "+str(marks[0][3]))
        english=input()
        print('enter the maths marks : '+"existing marks: "+str(marks[0][4]))
        maths=input()
        print('enter the science marks : '+"existing marks: "+str(marks[0][5]))
        science=input()
        print('enter the social marks : '+"existing marks: "+str(marks[0][6]))
        social=input()
        c.execute("update marks set telugu ="+telugu+", hindi ="+hindi+", english ="+english+", maths ="+maths+", science ="+science+", social ="+social+" where rollno ="+rollNo)
        conn.commit()
        print("marks updated successfully")
def student_personal_details():
    rollNo = input("enter student rollno: ")
    c.execute("select * from students where rollno =" + rollNo)
    results = c.fetchall()
    if (len(results) <= 0):
        print("student details not found in database")
    else:
        c.execute("select * from students where rollno =" + rollNo)
        details=c.fetchall()
        print("enter student name: "+"existing",details[0][1])
        studentName=input()
        print("enter student email: "+"existing",details[0][2])
        emailId=input()
        print("enter student phone number: "+"existing",details[0][3])
        phoneNumber=input()
        c.execute("update students set name ='"+studentName+"', email ='"+emailId+"', phone ="+phoneNumber+" where rollno ="+rollNo)
        conn.commit()
        print("student details updated successfully")
def delete_student():
    rollNo=input("enter student rollno: ")
    c.execute("select * from students where rollno ="+rollNo)
    results=c.fetchall()
    if(len(results)<=0):
        print("student details not found in database")
    else:
        c.execute("delete from students where rollno ="+rollNo)
        c.execute("delete from marks where rollno ="+rollNo)
        conn.commit()
        print("student details deleted successfully")

def delete_allstudent():
    conn.commit()
    c.execute("delete TABLE students")
def get_record_by_rollno():
    rollNo=input("enter student rollno: ")
    c.execute("select * from students where rollno ="+rollNo)
    results=c.fetchall()
    if(len(results)<=0):
        print("student details not found in database")
    else:
        c.execute("select * from students where rollno ="+rollNo)
        details=c.fetchall()
        print("student details are: ")
        print(details)
        c.execute("select * from marks where rollno ="+rollNo)
        marks=c.fetchall()
        print("student marks are: ")
        print(marks)
def get_all_records():
    c.execute("select * from students")
    students=c.fetchall()
    c.execute("select * from marks")
    marks=c.fetchall()
    print("student details are: ")
    print(students)
    print("student marks are: ")
    print(marks)
def delete_all_records():
    if(input("please type OK to confirm: ").lower()=='ok'):
        c.execute("delete from students")
        c.execute("delete from marks")
        conn.commit()
        print("all records deleted")
def send_email():
    rollNo=input("enter student rollno: ")
    c.execute("select * from students where rollno ="+rollNo)
    results=c.fetchall()
    if(len(results)<=0):
        print("student details not found in database")
    else:
        c.execute("select * from students where rollno ="+rollNo)
        details=c.fetchall()

        studentName=details[0][1]
        
        emailId=details[0][2]
        
        phoneNumber=details[0][3]
        c.execute("select * from marks where rollno ="+rollNo)
        marks=c.fetchall()
        
        telugu=str(marks[0][1])
        
        hindi=str(marks[0][2])
        
        english=str(marks[0][3])
        
        maths=str(marks[0][4])
        
        science=str(marks[0][5])
        
        social=str(marks[0][6])
        

    msg = MIMEMultipart()
    msg['From'] = "saitejasvi.01@gmail.com"
    msg['To'] = emailId
    msg['Subject'] = "marks of your child"
    body = "student name: "+studentName+"\n"+"student phone number: "+str(phoneNumber)+"\n"+"student marks: \n"+"telugu: "+telugu+"\n"+"hindi: "+hindi+"\n"+"english: "+english+"\n"+"maths: "+maths+"\n"+"science: "+science+"\n"+"social: "+social
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("saitejasvi.01@gmail.com", getpass.getpass('Enter your password:'))
    text = msg.as_string()
    server.sendmail("sender email id", emailId, text)
    server.quit()
    print("email sent successfully")
try:
    
    create_table()
    while(True):
        print("1. add student details")
        print("2. update student marks")
        print("3. update student details")
        print("4. delete student details")
        print("5. get student details by rollno")
        print("6. get all student details")
        print("7. send email")
        print("8. delete all student details")
        print("9. exit")
        choice=input("enter your choice: ")
        if(choice=='1'):
            add_student()
        elif(choice=='2'):
            update_student_marks()
        elif(choice=='3'):
            student_personal_details()
        elif(choice=='4'):
            delete_student()
        elif(choice=='5'):
            get_record_by_rollno()
        elif(choice=='6'):
            get_all_records()
        elif(choice=='7'):
            send_email()
        elif(choice=='8'):
            delete_all_records()
        elif(choice=='9'):
            exit()
        else:
            print("invalid choice")


except:
    # print("table already exists")
    # c.execute("select * from students s inner join marks m on s.rollno = m.rollno")
    # results=c.fetchall()
    # print(results)
    while(True):
        print("1. add student details")
        print("2. update student marks")
        print("3. update student details")
        print("4. delete student details")
        print("5. get student details by rollno")
        print("6. get all student details")
        print("7. send email")
        print("8. delete all student details")
        print("9. exit")
        choice=input("enter your choice: ")
        if(choice=='1'):
            add_student()
        elif(choice=='2'):
            update_student_marks()
        elif(choice=='3'):
            student_personal_details()
        elif(choice=='4'):
            delete_student()
        elif(choice=='5'):
            get_record_by_rollno()
        elif(choice=='6'):
            get_all_records()
        elif(choice=='7'):
            send_email()
        elif(choice=='8'):
            delete_all_records()
        elif(choice=='9'):
            exit()
        else:
            print("invalid choice")


