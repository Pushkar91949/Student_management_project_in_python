print("                                           WELCOME ")
print()
print("                           ******STUDENT MANAGEMENT SYSTEM******")
print()
import matplotlib.pyplot as pl  #importing required modules
import mysql.connector
#A database named psj_students has already been created.
#tables named table_students and fee_details has been created in the above database.
#That's why the below lines are commented out.
#While running the code for the first time in your system, uncomment the below 14 lines and run the program once.
#then comment these 14 lines again before use.
###############################################
##mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
##cursor=mydb.cursor()
##cursor.execute("create database psj_students")
##cursor.close()
##mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")
##cursor=mydb.cursor()
##cursor.execute("""create table table_students(name varchar(20),Contact_number bigint,UniqueSID int,
##Math_Marks float,Physics_Marks float,Chemistry_marks float, CS_Marks float,English_Marks float)""")
##cursor.close()
##mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")
##cursor=mydb.cursor()
##cursor.execute("create table fee_details(Name varchar(20),UniqueSID int, fee_status varchar(13))")
##mydb.commit()
##cursor.close()
nmlst=[]
opt=0
print("""                  SELECT THE DESIRED OPTION:

1)  ADD NEW STUDENT
2)  VIEW ALL STUDENTS
3)  VIEW ONE PARTICULAR STUDENT WITH MARKS GRAPH
4)  REMOVE STUDENT
5)  VIEW NAMES OF STUDENTS ADDED RIGHT NOW
6)  COMPARE MARKS OF ALL STUDENTS
7)  COMPARE MARKS OF ANY TWO STUDENTS
8)  CLEAR ALL DATA
9)  UPDATE DETAILS OF A STUDENT
10) VIEW FEE STATUS OF ALL STUDENTS
11) VIEW STUDENTS WHO HAVE NOT PAID THE FEES
12) QUIT
""") #PRINT MAIN MENU
while opt!=12:
    opt=int(input("Enter your Option:"))
    while opt==1: #IF OPTION SELECTED IS 1, A NEW STUDENT IS ADDED
        fl=[]
        l=[]
        name=input("Enter the Name:")
        l.append(name)
        fl.append(name)
        nmlst.append(name)
        Contact_number=int(input("Enter the Contact Number:"))
        l.append(Contact_number)
        UniqueSID=int(input("Enter the UNIQUE STUDENT ID (USID) of the Student:"))
        l.append(UniqueSID)
        Math_Marks=float(input("Enter the Marks Scored by the student in Maths:"))
        l.append(Math_Marks)
        Physics_Marks=float(input("Enter the Marks Scored by the student in Physics:"))
        l.append(Physics_Marks)
        Chemistry_Marks=float(input("Enter the Marks Scored by the student in Chemistry:"))
        l.append(Chemistry_Marks)
        CS_Marks=float(input("Enter the Marks Scored by the student in Computer science:"))
        l.append(CS_Marks)
        English_Marks=float(input("Enter the Marks Scored by the student in English:"))
        l.append(English_Marks)
        fl.append(UniqueSID)
        print("------------------------------------")
        print("Write 'Paid' or 'Unpaid' for Fees.")
        print("------------------------------------")
        Fees=input("Has the student paid the fees?")
        fl.append(Fees)
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")
        cursor=mydb.cursor()
        stud=(l)
        query="insert into table_students values(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,stud)
        mydb.commit()
        cursor.close()
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")
        cursor=mydb.cursor()
        query="insert into fee_details values(%s,%s,%s)"
        cursor.execute(query,fl)
        mydb.commit()
        cursor.close()
        print("--------------------------------")
        print("|","STUDENT ADDED SUCCESSFULLY!!","|")
        print("--------------------------------")
        break
    while opt==2:  #IF OPTION SELECTED IS 2, ALL THE STUDENTS DETAILS SAVED IN THE SYSTEM WIL BE SHOWN ONE BY ONE
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")   #MAKING DATABASE CONNECTION
        cursor=mydb.cursor()
        cursor.execute("select* from table_students")
        S=cursor.fetchall()
        if len(S)==0:
            print("-------------------------------------")
            print("|","No students in the system right now","|")
            print("-------------------------------------")
        else:
            for row in S:
                print("-"*(20+len(row[0])))
                print("Name:-             ",row[0])
                print("Contact Number:-   ",row[1])
                print("Unique Student ID:-",row[2])
                print("Math Marks:-       ",row[3])
                print("Physics Marks:-    ",row[4])
                print("Chemistry Marks:-  ",row[5])
                print("CS Marks:-         ",row[6])
                print("English Marks:-    ",row[7])
                print("-"*(20+len(row[0])))
        cursor.close()
        break
    while opt==3:  #IF OPTION 3 IS SELECTED, USER IS ASKED TO ENTER USID AND THAT STUDENT'S DETAILS ARE SHOWN 
        s=int(input("Enter UniqueSID Of the desired student:"))
        l1=[]
        l1.append(s)
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")
        cursor=mydb.cursor()
        stu=l1
        q="select* from table_students where UniqueSID=%s"
        cursor.execute(q,stu)
        c=cursor.fetchall()
        if len(c)==0:
            print("---------------------")
            print("| Student not found.|")
            print("---------------------")
        else:
            for row in c:
                print("-"*(20+len(row[0])))
                print("Name:-             ",row[0])
                print("Contact Number:-   ",row[1])
                print("Unique Student ID:-",row[2])
                print("Math Marks:-       ",row[3])
                print("Physics Marks:-    ",row[4])
                print("Chemistry Marks:-  ",row[5])
                print("CS Marks:-         ",row[6])
                print("English Marks:-    ",row[7])
                print("-"*22)
                pl.plot(['Maths','Physics','Chemistry','CS','English'],list(c[0][3::]))
                pl.title(c[0][0])
                pl.xlabel("Subjects")
                pl.ylabel("Marks")
                pl.show()
        cursor.close()
        break
    while opt==4:  #4TH OPTION REMOVES A STUDENT
        s=int(input("Enter UniqueSID Of the student to be removed:"))
        l1=[]
        l1.append(s)
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")
        cursor=mydb.cursor()
        stu=l1
        q="delete from table_students where UniqueSID='%s'"
        cursor.execute(q,stu)
        mydb.commit()
        cursor.close()
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")
        cursor=mydb.cursor()
        q="delete from fee_details where UniqueSID='%s'"
        cursor.execute(q,stu)
        mydb.commit()
        cursor.close()
        print()
        print("STUDENT REMOVED SUCCESSFULLY")
        print("----------------------------")
        print()
        break
    while opt==5:   # 5TH OPTION SHOWS THE STUDENTS NAMES WHO WERE ADDED JUST THEN.
        if len(nmlst)==0:
            print("--------------------------------------")
            print("|","No students were added RIGHT NOW.","|")
            print("--------------------------------------")
        else:
            for i in range(0,len(nmlst)):
                print()
                print(nmlst[i])
            print("-"*len(nmlst[len(nmlst)-1]))
        break
    while opt==6:    #6TH OPTION GRAPHICALLY COMPARES MARKS OF ALL STUDENTS
        print("-------------------------------------------------")
        legendlist=[]
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")
        cursor=mydb.cursor()
        cursor.execute("select* from table_students")
        f=cursor.fetchall()
        if len(f)==0:
            print("No students in the system right now.")
        else:
            for i in range(0,len(f)):
                legendlist.append(f[i][0])
                print(list(f[i]))
                x=["Maths","Physics","Chemistry","CS","English"]
            for j in range(0,len(f)):
                pl.plot(x,f[j][3::])
            pl.legend(legendlist,loc="best",fontsize="x-small")
            pl.xlabel("Subjects")
            pl.ylabel("Marks")
            pl.title("Marks Comparison")
            pl.show()
        print("-------------------------------------------------")
        cursor.close()
        break
    while opt==7:  #COMPARE MARKS OF ANY 2 STUDENTS Graphically
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")
        cursor=mydb.cursor()
        s1=input("Enter the UniquSID of the first student:")
        l1=[]
        l1.append(s1)
        p=l1
        q="select* from table_students where UniqueSID=%s"
        cursor.execute(q,p)
        m1=cursor.fetchall()
        cursor.close()
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")
        cursor=mydb.cursor()
        s2=input("Enter the UniquSID of the second student:")
        l2=[]
        l2.append(s2)
        q=l2
        qu="select* from table_students where UniqueSID=%s"
        cursor.execute(qu,q)
        m2=cursor.fetchall()
        cursor.close()
        if len(m1)==0 or len(m2)==0:
            print("-------------------------------")
            print("One or more students not found.")
            print("-------------------------------")
        else:
            g1=list(m1[0])
            gm1=g1[3::]
            g2=list(m2[0])
            gm2=g2[3::]
            x=["Maths","Physics","Chemistry","CS","English"]
            pl.plot(x,gm1)
            pl.plot(x,gm2)
            pl.legend([g1[0],g2[0]],loc="upper right")
            pl.xlabel("Subjects")
            pl.ylabel("Marks")
            pl.title("Subject-wise Marks comparison")
            pl.show()
            print("-------------------------------------------------")
            print(g1)
            print(g2)
            print("-------------------------------------------------")
        break
    while opt==8:   #CLEARS ALL THE EXISTING DATA FROM THE SYSTEM
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")
        cursor=mydb.cursor()
        cursor.execute("delete from table_students")
        mydb.commit()
        cursor.close()
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")
        cursor=mydb.cursor()
        cursor.execute("delete from fee_details")
        mydb.commit()
        cursor.close()
        print()
        print("DATA CLEARED SUCCESSFULLY")
        print("-------------------------")
        break
    while opt==9:   #9th OPTION HELPS IN CHANGING ANY DETAILS EXCEPT USID
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")
        cursor=mydb.cursor()
        q=[]
        s=int(input('Enter the UniqueSID of the student whose info is to be updated:')) #ASKING USER WHICH STUDENT'S INFO IS TO BE UPDATED
        print("""SELECT WHAT YOU WANT TO EDIT\n1)Name\n2)Contact Number\n3)Math marks
4)Physics Marks\n5)Chemistry marks\n6)CS marks\n7)English marks\n8)Fee Status\n9)Cancel""")
        choice=int(input("Enter your choice:"))
        if choice==1:
            namenew=input("Enter the new name:")  #CHANGE NAME
            q.append(namenew)
            q.append(s)
            qu="update table_students set name=%s where UniqueSID=%s"
            cursor.execute(qu,q)
            mydb.commit()
            cursor.close()
            print("Name Changed Successfully!!!")
            print("----------------------------")
            q.pop()
            q.pop()
        elif choice==2:  #CHANGE CONTACT NUMBER
            cnnew=int(input("Enter the new contact number:"))
            q.append(cnnew)
            q.append(s)
            qu="update table_students set Contact_number=%s where UniqueSID=%s"
            cursor.execute(qu,q)
            mydb.commit()
            cursor.close()
            print("Contact Number changed successfully!!!")
            print("--------------------------------------")
            q.pop()
            q.pop()
        elif choice==3:               #CHANGE MATH MARKS
            mmnew=int(input("Enter the new Math marks:"))
            q.append(mmnew)
            q.append(s)
            qu="update table_students set Math_Marks=%s where UniqueSID=%s"
            cursor.execute(qu,q)
            mydb.commit()
            cursor.close()
            print("Math marks changed successfully!!!")
            print("----------------------------------")
            q.pop()
            q.pop()
        elif choice==4: #CHANGE PHYSICS MARKS
            pmnew=int(input("Enter the new Physics Marks:"))
            q.append(pmnew)
            q.append(s)
            qu="update table_students set Physics_Marks=%s where UniqueSID=%s"
            cursor.execute(qu,q)
            mydb.commit()
            cursor.close()
            print("Physics Marks changed successfully!!!")
            print("-------------------------------------")
            q.pop()
            q.pop()
        elif choice==5: #CHANGE CHEMISTRY MARKS
            cmnew=int(input("Enter the new Chemistry Marks:"))
            q.append(cmnew)
            q.append(s)
            qu="update table_students set Chemistry_Marks=%s where UniqueSID=%s"
            cursor.execute(qu,q)
            mydb.commit()
            cursor.close()
            print("Chemistry Marks changed successfully!!!")
            print("---------------------------------------")
            q.pop()
            q.pop()
        elif choice==6:  #CHANGE CS MARKS
            csmnew=int(input("Enter the new CS Marks:"))
            q.append(csmnew)
            q.append(s)
            qu="update table_students set CS_Marks=%s where UniqueSID=%s"
            cursor.execute(qu,q)
            mydb.commit()
            cursor.close()
            print("CS Marks changed successfully!!!")
            print("--------------------------------")
            q.pop()
            q.pop() 
        elif choice==7: #CHANGE ENGLISH MARKS
            emnew=int(input("Enter the new English Marks:"))
            q.append(emnew)
            q.append(s)
            qu="update table_students set English_Marks=%s where UniqueSID=%s"
            cursor.execute(qu,q)
            mydb.commit()
            cursor.close()
            print("English Marks changed successfully!!!")
            print("-------------------------------------")
            q.pop()
            q.pop()
        elif choice>9 or choice<=0:  #ERROR FOR INVALID OPTION
            print("INVALID CHOICE!!!!  TRY AGAIN")
        elif choice==8:   #CHANGE FEE STATUS
            fsnew=input("Enter the updated fee status('paid' or 'Unpaid'):")
            q.append(fsnew)
            q.append(s)
            qu='update fee_details set fee_status=%s where UniqueSID=%s'
            cursor.execute(qu,q)
            mydb.commit()
            cursor.close()
            print("")
            print("FEE STATUS CHANGED SUCCESSFULLY")
            print("-------------------------------")
            q.pop()
            q.pop()
        else:
            print("-------------------------------")
            print("You Cancelled Changing Details.")
            print("-------------------------------")
            pass #BACK TO WHILE LOOP 
        break
    while opt==10:   #OPTION 10 SHOWS FEE STATUS OF ALL STUDENTS
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")
        cursor=mydb.cursor()
        cursor.execute("select* from fee_details ")
        c1=cursor.fetchall()
        if len(c1)==0:
            print("-----------------------------------")
            print("No students in the system right now")
            print("-----------------------------------")
        else:
            for i in c1:
                print("-"*(11+len(i[0])))
                print("Name      :",i[0])
                print("Fee Status:",i[2])
                print("-"*(11+len(i[0])))
        cursor.close()
        break
    while opt==11: #OPTION 11 SHOWS NAMES OF STUDENTS WHO HAVE NOT PAID THE FEES
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="psj_students")
        cursor=mydb.cursor()
        cursor.execute("select* from fee_details where fee_status='Unpaid'")
        c2=cursor.fetchall()
        if len(c2)==0:
            print("------------------")
            print("No students found.")
            print("------------------")
        else:
            print("--------------------------------")
            for i in c2:
                print(i[0])
            print("--------------------------------")
            print("The above student(s) have not paid the fees.")
            print("------------------------------------------")
        cursor.close()
        break
    while opt>12 or opt<=0:  #IF INVALID OPTION IS SELECTED, ERROR IS SHOWN.
        print("-----------------------------------")
        print("|","PLEASE SELECT A VALID OPTION !!","|")
        print("-----------------------------------") 
        break
    else:  #OPTION 12 QUITS THE PROGRAM
        exit