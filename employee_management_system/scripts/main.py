import streamlit as st
import mysql.connector
import pandas as pd
import datetime
from PIL import Image
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-\[A-Z|a-z]{2,}\b'
Pattern = re.compile("(91)?[7-9][0-9]{9}")
st.set_page_config(page_title='Employee Management System',page_icon="https://www.shutterstock.com/image-vector/hr-employee-retention-staff-icon-260nw-2117845013.jpg")
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20200821/pngtree-pure-white-minimalist-background-wallpaper-image_396581.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
add_bg_from_url()
def add_sidebg_from_url():
    st.markdown("""
    <style>
    .css-6qob1r {
               background-image: url("https://st2.depositphotos.com/1071909/9791/i/950/depositphotos_97918754-stock-photo-data-management-and-privacy.jpg");
               background-size: 100% 100%
    }
    </style>
        """, unsafe_allow_html=True)    
add_sidebg_from_url()    
choice=st.sidebar.selectbox("MY MENU",("HOME","EMPLOYEE LOGIN","MANAGEMENT LOGIN"))
if(choice=="HOME"):
    image=Image.open('welcome_clipart.jpg')
    new_image = image.resize((1100, 900))
    st.image(new_image) 
    image=Image.open('Home_clipart.jpg')
    new_image = image.resize((1200, 900))
    st.image(new_image) 
    text = '<p style="font-family:Papyrus; color:Black; font-size: 60px;text-align:center">One place for All employees and Management</p>'
    st.markdown(text, unsafe_allow_html=True)
    text = '<p style="font-family:Papyrus; color:Black; font-size: 20px;">Employees</p>'
    st.markdown(text, unsafe_allow_html=True)
    e_img = [
    'https://icons.iconarchive.com/icons/icons8/windows-8/512/Data-View-Details-icon.png',
    'https://cdn-icons-png.flaticon.com/512/2807/2807708.png',
    'https://icon-library.com/images/login-icon/login-icon-27.jpg',
    'https://cdn-icons-png.flaticon.com/512/4993/4993541.png',
    'https://cdn-icons-png.flaticon.com/512/5115/5115801.png',
    'https://cdn-icons-png.flaticon.com/512/6117/6117000.png'
    ]
    st.image(e_img, width=100,caption=['View details','Update details','Sign in','Report Absence','Apply for resignation','Reset password'])
    text = '<p style="font-family:Papyrus; color:Black; font-size: 20px;">Management</p>'
    st.markdown(text, unsafe_allow_html=True)
    m_img = [
    'https://cdn.iconscout.com/icon/premium/png-256-thumb/add-employee-2945111-2432088.png',
    'https://static.thenounproject.com/png/2590601-200.png',
    'https://www.shutterstock.com/image-vector/businessman-case-walk-stairs-icon-260nw-1074807740.jpg',
    'https://cdn.iconscout.com/icon/premium/png-256-thumb/resignation-letter-6298069-5244237.png',
    'https://static.thenounproject.com/png/1782336-200.png',
    'https://static.vecteezy.com/system/resources/previews/000/642/323/original/search-job-icon-vector.jpg',
    'https://cdn-icons-png.flaticon.com/512/6117/6117000.png'
    ]
    st.image(m_img, width=100,caption=['Add employee','Display employee details','Promote employee','View resignations','Remove employee record','Search employee record','Reset password'])
elif(choice=="EMPLOYEE LOGIN"):
    def add_bg_from_url():
        st.markdown(
             f"""
             <style>
             .stApp {{
                 background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20200821/pngtree-pure-white-minimalist-background-wallpaper-image_396581.jpg");
                 background-attachment: fixed;
                 background-size: cover
             }}
            </style>
             """,
             unsafe_allow_html=True
         )
    add_bg_from_url()
    image=Image.open('employee_clipart.jpg')
    st.image(image)
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False
    sub_title = '<p style="font-family:Garamond; color:Blue; font-size: 30px;">HELLO EMPLOYEE</p>'
    st.markdown(sub_title, unsafe_allow_html=True)
    if 'login' not in st.session_state:
        st.session_state['login']=False
    if st.session_state['login']==False:    
        st.session_state['eid']=st.text_input("",label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder="Enter employee ID",)
        pwd=st.text_input("",label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,placeholder="Enter employee Password",type="password")	
        btn=st.button("LOGIN")
        btn2=st.button("LOGOUT")
        if btn2:
            st.session_state['login']=False
        if btn:
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
            c=mydb.cursor()
            c.execute("select * from employee")
            for row in c:
                if(row[0]==st.session_state['eid'] and row[1]==pwd):
                    st.session_state['login']=True
                    break
            if(st.session_state['login']==False):
                st.header("Incorrect ID or Password")
    if st.session_state['login']:
        message = '<p style="font-family:Garamond; color:Blue; font-size: 30px;">Login Successfull</p>'
        st.markdown(message, unsafe_allow_html=True)
        choice2=st.selectbox("Features",("None","View my details","Update my details","Sign in","Report Absence","Apply for resignation","Reset password"))
        btnl1=st.button("LOGOUT NOW")
        if btnl1:
           st.session_state['login']=False
           st.experimental_rerun()
        if choice2=="View my details":
            emplid=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your employee ID",)
            empwd=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your employee password",type="password")
            btn1=st.button("Show details")
            if(btn1):
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                c=mydb.cursor()
                c.execute("select * from employee")
                for row in c:
                    if (row[0]==emplid and row[1]==empwd):
                        mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                        c1=mydb1.cursor()
                        c1.execute("select * from empldata where empid=%s",(emplid,))
                        for row in c1:                        
                            l=[]
                            st.write("EMPLOYEE ID:",row[0])
                            st.write("EMPLOYEE NAME:",row[1])
                            st.write("EMPLOYEE EMAIL:",row[2])
                            st.write("EMPLOYEE CONTACT NO:",row[3])
                            st.write("EMPLOYEE ADDRESS:",row[4])
                            st.write("EMPLOYEE POST:",row[5])
                            st.write("EMPLOYEE SALARY:",row[6])
        elif choice2=="Update my details":
            emplid=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your employee ID",)
            empwd=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your employee password",type="password")
            choice3=st.selectbox("Select the one you want to update",("None","Update my Email id","Update my Phone number","Update my Address"))
            if choice3=="Update my Email id":
                emilid=st.text_input("",label_visibility=st.session_state.visibility,
                disabled=st.session_state.disabled,placeholder="Enter Your new email ID",)
                if(re.fullmatch(regex,emilid)):
                    message = '<p style="font-family:Garamond; color:Blue; font-size: 10px;">Valid Email ID</p>'
                    st.markdown(message, unsafe_allow_html=True)
                else:
                    message = '<p style="font-family:Garamond; color:Blue; font-size: 10px;">Invalid Email ID</p>'
                    st.markdown(message, unsafe_allow_html=True)
                btnd1=st.button("Update details")
                if(btnd1):
                    if((re.fullmatch(regex,emilid)) and len(emilid)>0):
                        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                        c=mydb.cursor()
                        c.execute("select * from employee")
                        for row in c:
                            if (row[0]==emplid and row[1]==empwd):
                                mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                                c1=mydb1.cursor()
                                c1.execute("update empldata set emailid=%s where empid=%s",(emilid,emplid,))    
                                mydb1.commit()
                                message = '<p style="font-family:Garamond; color:Blue; font-size: 30px;">Updated successfull</p>'
                                st.markdown(message, unsafe_allow_html=True) 
                    else:
                        message = '<p style="font-family:Garamond; color:Blue; font-size: 30px;">Invalid values given correct it and retry</p>'
                        st.markdown(message, unsafe_allow_html=True)    
            if choice3=="Update my Phone number":        
                phno=st.text_input("",label_visibility=st.session_state.visibility,
                disabled=st.session_state.disabled,placeholder="Enter Your new phone number",)
                if(Pattern.match(phno)):
                    message = '<p style="font-family:Garamond; color:Blue; font-size: 10px;">Valid phone number</p>'
                    st.markdown(message, unsafe_allow_html=True)
                else:
                    message = '<p style="font-family:Garamond; color:Blue; font-size: 10px;">Invalid phone number</p>'
                    st.markdown(message, unsafe_allow_html=True)
                btnd2=st.button("Update details")
                if(btnd2):
                    if(Pattern.match(phno) and len(phno)>0):
                        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                        c=mydb.cursor()
                        c.execute("select * from employee")
                        for row in c:
                            if (row[0]==emplid and row[1]==empwd):
                                mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                                c1=mydb1.cursor()
                                c1.execute("update empldata set phoneno=%s where empid=%s",(phno,emplid,))    
                                mydb1.commit()
                                message = '<p style="font-family:Garamond; color:Blue; font-size: 30px;">Updated successfull</p>'
                                st.markdown(message, unsafe_allow_html=True) 
                    else:
                        message = '<p style="font-family:Garamond; color:Blue; font-size: 30px;">Invalid values given correct it and retry</p>'
                        st.markdown(message, unsafe_allow_html=True)        
            if choice3=="Update my Address":                    
                addr=st.text_input("",label_visibility=st.session_state.visibility,
                disabled=st.session_state.disabled,placeholder="Enter Your new address",)
                btnd3=st.button("Update details")
                if(btnd3):
                    if(len(addr)>0):
                        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                        c=mydb.cursor()
                        c.execute("select * from employee")
                        for row in c:
                            if (row[0]==emplid and row[1]==empwd):
                                mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                                c1=mydb1.cursor()
                                c1.execute("update empldata set address=%s where empid=%s",(addr,emplid,))    
                                mydb1.commit()
                                message = '<p style="font-family:Garamond; color:Blue; font-size: 30px;">Updated successfull</p>'
                                st.markdown(message, unsafe_allow_html=True) 
                    else:
                        message = '<p style="font-family:Garamond; color:Blue; font-size: 30px;">Invalid values given correct it and retry</p>'
                        st.markdown(message, unsafe_allow_html=True)                   
        elif choice2=="Sign in":
            emplid=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your employee ID",)
            empwd=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your employee password",type="password")
            btn3=st.button("Sign in")
            if(btn3):
                sindt=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                c=mydb.cursor()
                c.execute("select * from employee")
                for row in c:
                    if (row[0]==emplid and row[1]==empwd):
                        mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                        c1=mydb1.cursor()
                        c1.execute("insert into emplin values (%s,%s)",(emplid,sindt))    
                        mydb1.commit()
                        message = '<p style="font-family:Garamond; color:Blue; font-size: 30px;">Sign-in successfull</p>'
                        st.markdown(message, unsafe_allow_html=True)
        elif choice2=="Report Absence":        
            emplid=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your employee ID",)
            empwd=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your employee password",type="password")
            abdt=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your Absence date in YYYY-MM-DD",)
            btn4=st.button("Report")
            if(btn4): 
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                c=mydb.cursor()
                c.execute("select * from employee")
                for row in c:
                    if (row[0]==emplid and row[1]==empwd):
                        mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                        c1=mydb1.cursor()
                        c1.execute("insert into Abreport values (%s,%s)",(emplid,abdt))    
                        mydb1.commit()
                        message = '<p style="font-family:Garamond; color:Blue; font-size: 30px;">Absence Reported successfull</p>'
                        st.markdown(message, unsafe_allow_html=True)
        elif choice2=="Apply for resignation":    
            emplid=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your employee ID",)
            empwd=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your employee password",type="password")
            btn5=st.button("Resign")
            if(btn5):
                resdt=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                c=mydb.cursor()
                c.execute("select * from employee")
                for row in c:
                    if (row[0]==emplid and row[1]==empwd):
                        mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                        c1=mydb1.cursor()
                        c1.execute("insert into resignempdata values (%s,%s)",(emplid,resdt))    
                        mydb1.commit()
                        message = '<p style="font-family:Garamond; color:Blue; font-size: 30px;">Resigned successfull Thankyou for working with us!</p>'
                        st.markdown(message, unsafe_allow_html=True)
            btn6=st.button("Undo Resign")
            if(btn6):  
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                c=mydb.cursor()
                c.execute("select * from employee")
                for row in c:
                    if (row[0]==emplid and row[1]==empwd):
                        mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                        c1=mydb1.cursor()
                        c1.execute("Delete from resignempdata where empid=%s",(emplid,))    
                        mydb1.commit()
                        message = '<p style="font-family:Garamond; color:Blue; font-size: 30px;"> Undo Resign successfull Thanku for continuing with us!</p>'
                        st.markdown(message, unsafe_allow_html=True)
        elif choice2=="Reset password":    
            emplid=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your employee ID",)
            empwd=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your old employee password",type="password")
            emnpwd=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your new employee password",type="password")
            btn7=st.button("Reset password")
            if(btn7):
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                c=mydb.cursor()
                c.execute("select * from employee")
                for row in c:
                    if (row[0]==emplid and row[1]==empwd):
                        mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                        c1=mydb1.cursor()
                        c1.execute("update employee set epassword=%s where empid=%s",(emnpwd,emplid))    
                        mydb1.commit()
                        message = '<p style="font-family:Garamond; color:Blue; font-size: 30px;">Reset password successfully!</p>'
                        st.markdown(message, unsafe_allow_html=True)
                    else:
                        message = '<p style="font-family:Garamond; color:Green; font-size: 30px;">Wrong ID or PWD</p>'
                        st.markdown(message, unsafe_allow_html=True)    
elif(choice=="MANAGEMENT LOGIN"):
    def add_bg_from_url():
        st.markdown(
             f"""
             <style>
             .stApp {{
                 background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20200821/pngtree-pure-white-minimalist-background-wallpaper-image_396581.jpg");
                 background-attachment: fixed;
                 background-size: cover
             }}
            </style>
             """,
             unsafe_allow_html=True
         )
    add_bg_from_url()
    image=Image.open('management_clipart.jpg')
    st.image(image)
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False
    sub_title = '<p style="font-family:Garamond; color:Green; font-size: 30px;">HELLO MANAGMENT</p>'
    st.markdown(sub_title, unsafe_allow_html=True)
    if 'llogin' not in st.session_state:
        st.session_state['llogin']=False
    if st.session_state['llogin']==False:
        mid=st.text_input("",label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,placeholder="Enter Management ID",)
        pwd=st.text_input("",label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,placeholder="Enter Management Password",type="password")
        btn=st.button("LOGIN")
        btn2=st.button("LOGOUT")
        if btn2:
            st.session_state['llogin']=False 
        if btn:
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
            c=mydb.cursor()
            c.execute("select * from management")
            for row in c:
                if(row[0]==mid and row[1]==pwd):
                    st.session_state['llogin']=True
                    break
            if(st.session_state['llogin']==False):
                st.header("Incorrect ID or Password")
    if st.session_state['llogin']:
        message = '<p style="font-family:Garamond; color:Green; font-size: 30px;">Login Successful</p>'
        st.markdown(message, unsafe_allow_html=True)
        choice2=st.selectbox("Features",("None","Add employee","Display employee details","Promote employee","View resignations","Remove employee record","Search employee record","Reset password"))
        btnl1=st.button("LOGOUT NOW")
        if btnl1:
           st.session_state['llogin']=False
           st.experimental_rerun() 
        if choice2=="Add employee":
            eid=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Employee ID",)	
            ename=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Employee Name",)	
            emid=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Employee Email ID",)
            if(re.fullmatch(regex,emid)):
                message = '<p style="font-family:Garamond; color:Green; font-size: 10px;">Valid Email ID</p>'
                st.markdown(message, unsafe_allow_html=True)
            else:
                message = '<p style="font-family:Garamond; color:Green; font-size: 10px;">Invalid Email ID</p>'
                st.markdown(message, unsafe_allow_html=True)
            pno=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Employee contact no",)
            if(Pattern.match(pno)):
                message = '<p style="font-family:Garamond; color:Green; font-size: 10px;">Valid phone number</p>'
                st.markdown(message, unsafe_allow_html=True)
            else:
                message = '<p style="font-family:Garamond; color:Green; font-size: 10px;">Invalid phone number</p>'
                st.markdown(message, unsafe_allow_html=True)   
            adr=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Employee Address",)
            pst=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Employee Designation",)
            sal=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Employee current Salary",)
            btn1=st.button("Add employee")
            if btn1:
                if(re.fullmatch(regex,emid) and Pattern.match(pno) and len(eid)>0 and len(ename)>0 and len(emid)>0 and len(pno)>0 and len(adr)>0 and len(pst)>0 and len(sal)>0):
                    mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                    c=mydb.cursor()
                    c.execute("insert into empldata values(%s,%s,%s,%s,%s,%s,%s)",(eid,ename,emid,pno,adr,pst,sal))
                    mydb.commit()
                    message = '<p style="font-family:Garamond; color:Green; font-size: 30px;">Employee Added Successfully</p>'
                    st.markdown(message, unsafe_allow_html=True)
                else:
                        message = '<p style="font-family:Garamond; color:Blue; font-size: 30px;">Invalid values given correct it and retry</p>'
                        st.markdown(message, unsafe_allow_html=True)    
        elif choice2=="Display employee details":   
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
            c=mydb.cursor()
            c.execute("select * from empldata")
            l=[]
            for row in c:
                l.append(row)
            df=pd.DataFrame(data=l,columns=['Employee ID','Employee Name','Email ID','Phone No','Address','Designation','Salary'])
            st.dataframe(df)    
        elif choice2=="Promote employee":
            eid=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Employee ID who will be promoted",)	
            sal=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Employee's New Salary",)
            btn2=st.button("Promote")
            if btn2:
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                c=mydb.cursor()
                c.execute("Update empldata set salary=%s where empid=%s",(sal,eid))  
                mydb.commit()
                message = '<p style="font-family:Garamond; color:Green; font-size: 30px;">Employee Promoted Successfully</p>'
                st.markdown(message, unsafe_allow_html=True)
        elif choice2=="View resignations":   
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
            c=mydb.cursor()
            c.execute("select * from resignempdata")
            l=[]
            for row in c:
                l.append(row)
            df=pd.DataFrame(data=l,columns=['Employee ID','Resigned On'])
            st.dataframe(df)            
        elif choice2=="Remove employee record":            
            eid=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Employee ID which needs to be deleted",)	
            btn3=st.button("Remove Employee")
            if btn3: 
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                c=mydb.cursor()
                c.execute("Delete from empldata where empid=%s",(eid,))  
                mydb.commit()
                mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                c1=mydb1.cursor()
                c1.execute("Delete from employee where empid=%s",(eid,))  
                mydb1.commit()
                message = '<p style="font-family:Garamond; color:Green; font-size: 30px;">Employee Removed Successfully</p>'
                st.markdown(message, unsafe_allow_html=True)                
        elif choice2=="Search employee record":   
            eid=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Employee ID which needs to be Viewed",)	
            btn4=st.button("View Employee Details")
            if btn4:
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                c=mydb.cursor()
                c.execute("select * from empldata where empid=%s",(eid,))
                msg = c.fetchone()  
                if not msg:
                    message = '<p style="font-family:Garamond; color:Green; font-size: 30px;">Employee details doesnot exists</p>'
                    st.markdown(message, unsafe_allow_html=True)
                else: 
                    mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                    c1=mydb1.cursor()
                    c1.execute("select * from empldata where empid=%s",(eid,))                
                    l=[]
                    for row in c1:
                        l.append(row)
                        df=pd.DataFrame(data=l,columns=['Employee ID','Employee Name','Email ID','Phone No','Address','Designation','Salary'])
                        st.dataframe(df)    
        elif choice2=="Reset password":   
            mgid=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your Managment ID",)
            mgpwd=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your old Managment password",type="password")
            mgnpwd=st.text_input("",label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,placeholder="Enter Your new Managment password",type="password")
            btn5=st.button("Reset password")
            if(btn5):
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                c=mydb.cursor()
                c.execute("select * from management")
                for row in c:
                    if (row[0]==mgid and row[1]==mgpwd):
                        mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="ems")
                        c1=mydb1.cursor()
                        c1.execute("update management set mpassword=%s where mngtid=%s",(mgnpwd,mgid))    
                        mydb1.commit()
                        message = '<p style="font-family:Garamond; color:Green; font-size: 30px;">Reset password successfully!</p>'
                        st.markdown(message, unsafe_allow_html=True)        
                    else:
                        message = '<p style="font-family:Garamond; color:Green; font-size: 30px;">Wrong ID or PWD</p>'
                        st.markdown(message, unsafe_allow_html=True)                    