import mysql.connector
import time
import os
import csv
mydb=mysql.connector.connect(host="127.0.0.1",user="root",password="XXXXX")
print("---DATABASE CONNECTED---")
sql=mydb.cursor()
def edit(num):
      loop=False
      while not loop:
                        print("What do you want to change:")
                        print("1.Student Name\n2.Gender\n3.Blood group\n4.Guardian Name\n5.phone number\n6.Native District\n7.Back to main menu")
                        op=int(input("enter your choice:"))
                        value=""
                        change=""
                        syn=""
                        if op==1:
                              syn="update  student set student_name = %s,Last_updated=now() where student_id=%s"
                              value=input("enter Student Name:")
                        elif op==2:
                              syn="update  student set gender = %s,Last_updated=now() where student_id=%s"
                              value=input("enter gender:")
                        elif op==3:
                              syn="update  student set blood_group = %s,Last_updated=now() where student_id=%s"
                              value=input("enter Blood Group:")
                        elif op==4:
                              syn="update  student set Guardian_name = %s,Last_updated=now() where student_id=%s"
                              value=input("Enter guardian name:")
                        elif op==5:
                              syn="update  student set phone_number = %s,Last_updated=now() where student_id=%s"
                              value=input("enter phone number:")
                        elif op==6:
                              syn="update  student set address = %s,Last_updated=now() where student_id=%s"
                              value=input("enter Native district:")
                        else:
                              break
            
                        val=[value,num]
                        sql.execute(syn,val)
                        print("---Data Updated---")
                        time.sleep(2)
                        os.system("cls")
                        syn="select * from student where student_id = %s"
                        val=[num]
                        sql.execute(syn,val)
                        for i in sql:
                              print("ID=",i[0],"\nStudent name=",i[1],"\ngender=",i[2],"\nblood group=",i[3],"\nGuardian=",i[4],"\nphone",i[5],"\nNative=",i[6])
                        print("--------------------")
def Admission_form():
      while True:
            print("----STUDENT ADMISSION FORM----")
            print("1.New Admission\n2.Student list\n3.Edit stduent detail\n4.Export data in excel sheet\n5.quit")
            ch=int(input("enter your choice:"))
            if ch==1:
                  os.system("cls")
                  print("---ADMISSION FORM---")
                  stu_name=input("Student Name:")
                  gender=input("Gender:")
                  blood=input("blood group:")
                  guardian=input("Gaurdian Name:")
                  phone=input("Phone Number:")
                  address=input("Native district:")
                  val=[stu_name,gender,blood,guardian,phone,address]
                  syn="insert into student(student_name,gender,blood_group,Guardian_name,phone_number,address)  values(%s,%s,%s,%s,%s,%s)"
                  sql.execute(syn,val)
                  mydb.commit()
                  print("--Student details added--")
                  time.sleep(1)
                  os.system("cls")
            elif ch==2:
                  sql.execute("select * from student")
                  os.system("cls")
                  print("ID      NAME")
                  print("---------------------------")
                  for i in sql:
                        print(i[0],"    ",i[1])
                  back=input("press enter to go back")
                  os.system("cls")
                  Admission_form()
            elif ch==3:
                  os.system("cls")
                  print("--------EDIT STUDENT DETAIL--------")
                  num=int(input("enter student ID number:"))
                  syn="select * from student where student_id = %s"
                  val=[num]
                  sql.execute(syn,val)
                  for i in sql:
                        print("ID= ",i[0],"\nStudent name = ",i[1],"\ngender = ",i[2],"\nblood group = ",i[3],"\nGuardian = ",i[4],"\nphone = ",i[5],"\nNative = ",i[6])
                  print("--------------------")
                  ch=input("Do you want to edit details?(Y/N):")
                  if ch=="Y" or ch=='y':
                        edit(num)
                  ret=input("press enter to return:")
                  os.system("cls")               
            elif ch==4:
                  file=open("admission form.csv",'w')
                  c=csv.writer(file)
                  sql.execute("select * from student")
                  data=sql.fetchall()
                  head=["ID","STUDENT NAME","GENDER","BLOOD GROPU","GUARDIAN","PHONE","NATIVE DISTRICT","ADMITTED DATE","Last updated date"]
                  c.writerow(head)
                  for row in data:
                        c.writerow(row )
                  print("--file saved succefully--")
                  time.sleep(2)
                  file.close()
                  os.system("cls")
            else:
                  exit()
try:
      sql.execute("create database school")
      print("Database created")
      sql.execute("use school")
      print("select admission database")
      sql.execute("create table student(student_id int primary key auto_increment,student_name varchar(30),gender varchar(10),blood_group varchar(5),Guardian_name varchar(30),phone_number varchar(15),address varchar(100),admission_date date default (now()),Last_updated date default null)")
      print("Table created")
      time.sleep(6)
      os.system("cls")
      Admission_form()
except:
      try:
            sql.execute("use school")
            sql.execute("create table student(student_id int primary key auto_increment,student_name varchar(30),gender varchar(10),blood_group varchar(5),Guardian_name varchar(30),phone_number varchar(15),address varchar(100),admission_date date default (now()),Last_updated date default null)")
            os.system("cls")
            Admission_form()
      except:
            sql.execute("use school")
            os.system("cls")
            Admission_form()
      

