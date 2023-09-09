def addpatient():
      import mysql.connector
      myconn=mysql.connector.connect(host="localhost",user="root",passwd="TANUJBHATIA",database='HospitalManagement')
      cur=myconn.cursor()
      patient_ID= int(input("Enter patient ID : "))
      Name=input("Enter Patient name : ")
      Age=int(input("Enter patient age : "))
      Gender=input("Enter patient gender : ")
      Phoneno=int(input("Enter patient phone number : "))
      Department=input("Enter patient department : ")
      DoctorName=input("Enter name of doctor following the case : ")
      query="insert into  patientdatabase(Patient_id,Name,Age,Gender,Phone_Number,Department,Doctorname) values('%d','%s','%d','%s','%d','%s','%s')"%(patient_ID,Name,Age,Gender,Phoneno,Department,DoctorName)
      cur.execute(query)
      myconn.commit()
      cur.close()
      print("----------------------Patient added successfully----------------------")
      
def displaypatient():
            import mysql.connector
            myconn=mysql.connector.connect(host="localhost",user="root",passwd="TANUJBHATIA",database='HospitalManagement')
            cur=myconn.cursor()
            patientID = int(input("Enter patient ID : "))
            cur.execute("select * from patientdatabase where Patient_id='%d'" %patientID)
            rec=cur.fetchall()
            if cur.rowcount==1:
              for r in rec:  
                print(" patient name                  : ",r[1])
                print(" patient age                   : ",r[2])
                print(" patient gender                : ",r[3])
                print(" patient phone number          : ",r[4])
                print(" patient's department          : ",r[5])
                print(" patient is followed by doctor : ",r[6])
            else:
               print("Patient ID not found")
            cur.close()
           
def deletepatient():
            import mysql.connector
            myconn=mysql.connector.connect(host="localhost",user="root",passwd="TANUJBHATIA",database='HospitalManagement')
            cur=myconn.cursor()            
            patientid=int(input("enter patient id to delete"))
            ch=input('Are you sure you want to delete the record( y/n) ?')
            if ch=='y':
              a="delete from patientdatabase where Patient_id ='%d'"%(patientid)
              cur.execute(a)
              if cur.rowcount>=1:
                myconn.commit()
                print("total records deleted ", cur.rowcount)
                print("----------------------Patient data deleted successfully----------------------")
              else:
                print("Invalid Patient ID")
              cur.close()

def editpatient():
               import mysql.connector
               myconn=mysql.connector.connect(host="localhost",user="root",passwd="TANUJBHATIA",database='HospitalManagement')
               cur=myconn.cursor()                
               patient_ID=int(input("Enter patient ID : "))
               a="select * from patientdatabase where Patient_ID='%d'"%(patient_ID)
               cur.execute(a)
               rec=cur.fetchone()
               if cur.rowcount==1:
                      print(rec)
                      while True :
                             print("------------------------------------------")
                             print("|To Edit pateint Department Enter 1 :    |")
                             print("|To Edit Doctor following case Enter 2 : |")
                             print("|To Edit pateint Name Enter 3 :          |")
                             print("|To Edit pateint Age Enter 4 :           |")
                             print("|To Edit pateint Gender Enter 5 :        |")
                             print("|To Edit pateint Phone number Enter 6 :  |")
                             print("|To be Back Enter B                      |")
                             print("-----------------------------------------")
                             admin_choice = input("Enter your choice : ")
                             if admin_choice == "1" :
                                      department=input("Enter new department: ")
                                      a="update patientdatabase set Department='%s' where Patient_id='%d'"%(department,patient_ID)
                                      cur.execute(a)
                                      myconn.commit()
                                      print("----------------------Patient Department edited successfully----------------------")
                             elif admin_choice == "2" :
                                      doctor=input("Enter new doctor name: ")
                                      a="update patientdatabase set Doctorname='%s' where Patient_id='%d'"%(doctor,patient_ID)
                                      cur.execute(a)
                                      myconn.commit()
                                      print("----------------------Doctor following case edited successfully----------------------")
                             elif admin_choice == "3" :
                                      name=input("Enter new patient name: ")
                                      a="update patientdatabase set Name='%s' where Patient_id='%d'"%(name,patient_ID)
                                      cur.execute(a)
                                      myconn.commit()
                                      print("----------------------Patient name edited successfully----------------------")
                             elif admin_choice == "4" :
                                      age=int(input("Enter new patient age: "))
                                      a="update patientdatabase set Age='%d' where Patient_id='%d'"%(age,patient_ID)
                                      cur.execute(a)
                                      myconn.commit()
                                      print("----------------------Patient age edited successfully----------------------")
                             elif admin_choice == "5" :
                                      gender=input("Enter new patient gender: ")
                                      a="update patientdatabase set Gender='%s' where Patient_id='%d'"%(gender,patient_ID)
                                      cur.execute(a)
                                      myconn.commit()
                                      print("----------------------Patient gender edited successfully----------------------")
                             elif admin_choice == "6" :
                                      phoneno=int(input("Enter new patient phone number: "))
                                      a="update patientdatabase set Phone_Number='%d' where Patient_id='%d'"%(phoneno,patient_ID)
                                      cur.execute(a)
                                      myconn.commit()
                                      print("----------------------Patient phone number edited successfully----------------------") 
                             elif admin_choice == "B" :
                                  break
                             else :
                                   print("Please Enter a correct choice")
               else:
                   print("Patient ID not found")
               cur.close()    
def adddoctor():
             import mysql.connector
             myconn=mysql.connector.connect(host="localhost",user="root",passwd="TANUJBHATIA",database='HospitalManagement')
             cur=myconn.cursor()                             
             doctor_ID= int(input("Enter doctor ID : "))
             Name=input("Enter doctor name : ")
             Phoneno=int(input("Enter doctor phone number : "))
             Department=input("Enter doctor department : ")
             query="insert into doctordatabase(doctor_id,Name,Phone_Number,Department) values('%d','%s','%d','%s')"%(doctor_ID,Name,Phoneno,Department)
             cur.execute(query)
             myconn.commit()
             print("----------------------Doctor added successfully----------------------")
             cur.close()
def displaydoctor():
            import mysql.connector
            myconn=mysql.connector.connect(host="localhost",user="root",passwd="TANUJBHATIA",database='HospitalManagement')
            cur=myconn.cursor()                                 
            doctorID=int(input("Enter doctor ID : "))
            cur.execute("select * from doctordatabase where doctor_id='%d'" %doctorID)
            rec=cur.fetchall()
            if cur.rowcount==1:
              for r in rec:    
                print(" doctor name               : ",r[1])
                print(" doctor's phone number       : ",r[2])
                print(" doctor's department     : ",r[3])
            else:
               print("Doctor ID not found")
               cur.close()
def deletedoctor():
            import mysql.connector
            myconn=mysql.connector.connect(host="localhost",user="root",passwd="TANUJBHATIA",database='HospitalManagement')
            cur=myconn.cursor()                                 
            doctorid=int(input("enter doctor id to delete"))
            ch=input('Are you sure you want to delete the record( y/n) ?')
            if ch=='y':
              a="delete from doctordatabase where doctor_id ='%d'"%(doctorid)
              cur.execute(a)
              if cur.rowcount>=1:
                myconn.commit()
                print("total records deleted ", cur.rowcount)
                print("----------------------Doctor data deleted successfully----------------------")
              else:
                print("Invalid Doctor ID")
              cur.close()   
def editdoctor():
               import mysql.connector
               myconn=mysql.connector.connect(host="localhost",user="root",passwd="TANUJBHATIA",database='HospitalManagement')
               cur=myconn.cursor()                     
               doctor_ID=int(input("Enter doctor ID : "))
               a="select * from doctordatabase where doctor_ID='%d'"%(doctor_ID)
               cur.execute(a)
               rec=cur.fetchone()
               if cur.rowcount==1:
                      print(rec)
                      while True :
                             print("------------------------------------------")
                             print("|To Edit doctor Name Enter 1 :           |")
                             print("|To Edit doctor Department Enter 2 :     |")
                             print("|To Edit doctor Phone number Enter 3 :  |")
                             print("|To be Back Enter B                      |")
                             print("-----------------------------------------")
                             admin_choice = input("Enter your choice : ")
                             
                             if admin_choice == "1" :
                                      name=input("Enter new doctor name: ")
                                      a="update doctordatabase set Name='%s' where doctor_id='%d'"%(name,doctor_ID)
                                      cur.execute(a)
                                      myconn.commit()
                                      print("----------------------Doctor name edited successfully----------------------")
                             
                             elif admin_choice == "2" :
                                      department=input("Enter new doctor department: ")
                                      a="update doctordatabase set Department='%s' where doctor_id='%d'"%(department,doctor_ID)
                                      cur.execute(a)
                                      myconn.commit()
                                      print("----------------------Doctor department edited successfully----------------------")

                             elif admin_choice == "3" :
                                      phoneno=int(input("Enter new doctor phone number: "))
                                      a="update doctordatabase set Phone_Number='%d' where doctor_id='%d'"%(phoneno,doctor_ID)
                                      cur.execute(a)
                                      myconn.commit()
                                      print("----------------------Doctor phone number edited successfully----------------------") 
                             elif admin_choice == "B" :
                                  break
                             else :
                                   print("Please Enter a correct choice")
               else:
                   print("Doctor ID not found")
               cur.close()    


print("****************************************************************************")
print("*                 Welcome to Hospital Management System                    *")
print("****************************************************************************")
attempt=0
while True:
     if attempt==3:
         break
     print("-------------------------")
     print("|Enter 1 for Admin mode |\n|Enter 2 for user mode  |\n|Enter B to exit")
     print("-------------------------")
     Admin_user_mode=input("Enter your mode : ")
     if Admin_user_mode=="1" : #Admin mode
          print("*********************************\n|     Welcome to admin mode     |\n*********************************")
          Password=input("Please enter your password : ")
          while True :
             if attempt==3:
               break
             elif Password=="1234" :
                  print("-----------------------------")
                  print("|To manage patients Enter 1 |\n|To manage doctors Enter 2  |\n|To be back Enter B         |")
                  print("-----------------------------")
                  AdminOptions=input("Enter your choice : ")
                  if AdminOptions=="1" : #Admin mode ; Pateints Management
                    while True:
                     print("---------------------------------")
                     print("|To add new patient Enter 1     |")
                     print("|To display patient Enter 2     |")
                     print("|To delete patient data Enter 3 |")
                     print("|To edit patient data Enter 4   |")
                     print("|To Back enter B                |")
                     print("---------------------------------")
                     Admin_choice=input("Enter your choice : ")       
                     if Admin_choice == "1" : #Admin mode ; Pateints Management ; Enter new patient data
                          addpatient()
                     elif Admin_choice == "2" : #Admin mode; Pateints Management ; Display patient data
                          displaypatient()
                     elif Admin_choice == "3" : #Admin mode; Pateints Management ; Delete patient data
                          deletepatient() 
                     elif Admin_choice == "4" : #Admin mode; Pateints Management ; Edit patient data
                          editpatient()                   
                     elif Admin_choice=='B':
                          break         
                     else:
                          print("Please enter correct choice")
  
                  elif AdminOptions == "2" : #Admin mode ; Doctors Management
                      while True:
                          print("-----------------------------------------")
                          print("|To add new doctor Enter 1              |")
                          print("|To display doctor Enter 2              |")
                          print("|To delete doctor data Enter 3          |")
                          print("|To edit doctor data Enter 4            |")
                          print("|To be back enter B                     |")
                          print("-----------------------------------------")
                          Admin_choice = input ("Enter your choice : ")
                          if Admin_choice == "1" : #Admin mode ; Doctors Management ; Enter new doctor data
                              adddoctor()             
                          elif Admin_choice == "2" : #Admin mode; Doctor Management ; Display doctor data
                              displaydoctor()           
                          elif Admin_choice == "3" : #Admin mode; Dcotors Management ; Delete doctor data
                              deletedoctor()                
                          elif Admin_choice == "4" : #Admin mode; Doctors Management ; Edit doctor data
                              editdoctor()           
                          elif Admin_choice=='B':
                              break
                          else:
                              print("Please enter correct choice")
                  elif AdminOptions=='B':
                      break
                  else:
                      print('Enter correct choice')

             elif Password!='1234':
                   attempt+=1
                   print("Incorrect password")
                   if attempt==3:
                       print('No more tries')
                       break
                   else:
                       Password=input('Enter password')

     elif Admin_user_mode == "2" : #User mode
         print("*********************\n|      Welcome to user mode     |\n********************")
         while True :
            print("\n-----------------------------------------")
            print("|To view hospital's departments Enter 1 |")
            print("|To view hospital's docotrs Enter 2     |")
            print("|To view patient's details Enter 3      |")
            print("|To be Back Enter B                     |")
            print("-----------------------------------------")
            UserOptions = input("Enter your choice : ")
            if UserOptions == "1" : #User mode; view hospital's departments
                      print("Hospital's departments: ")
                      import mysql.connector
                      myconn=mysql.connector.connect(host="localhost",user="root",passwd="TANUJBHATIA",database="HospitalManagement")
                      cur=myconn.cursor()
                      cur.execute("select distinct Department from doctordatabase")
                      for i in cur:
                          print(i)
                      cur.close()    
            elif UserOptions == "2" : #User mode ; view hospital's Doctors
                      print("Hospital's doctors :")
                      import mysql.connector
                      myconn=mysql.connector.connect(host="localhost",user="root",passwd="TANUJBHATIA",database="HospitalManagement")
                      cur=myconn.cursor()
                      cur.execute("select Name,Department from doctordatabase")
                      for i in cur:
                          print(i[0],'\t',i[1])
                      cur.close()    
            elif UserOptions == "3" : #User mode ; view patients' details
                          displaypatient()
            elif UserOptions == "B" : #Back
                          break
            else :
                     print("Please Enter a correct choice")
     elif Admin_user_mode=='B':
           choice=input('Are you sure you want to exit(y/n) ? ')
           if choice=='y':
                 print("************   Program closed    ************")
                 print("                Thank you                    ")
                 break
     else :
          print("Please choice just 1 or 2")
    

