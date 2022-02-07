#stake holders: staff, customers, manager

#consistent screens, screens have to look neat and appealing
#treeviews that reflect what stakeholders you have
#multiple treewiew widgets i.e spinboxes
#extras - hover texts, keybind events
#help button on every screen
#make sure it is easy to navigate
#clear validation
#store relevant info about the three stakeholders
#must include a primary key
#dont searh primary key or unique id 

####################################################################################
#registration frame:
#firstname
#surname
#email
#gym location
#email address
#address
#phone number
#type of membership
#gym pin number

#customer login frame:
#customer pin number
#record time in gym
#customer logout

#main frame for customer:
#gym progress:
#input weights for exercise e.g dealift, squat, bench press, running.
#input weight in kg
#book a personal trainer(staff) on a particular date(create a calender)

#view gym progress(line graphs)
#aveage time in the gym
#gym programs
#####################################################################################
#manager login:
#username and password
#manager logout

#managers mainframe:

#manager can look treeview of staff
#####################################################################################
#staff login:
#username and password
#staff logout

#staff mainframe 
#staff can look at what dates they have a session.

import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import askstring
import tkinter.simpledialog as simpledialog
from tkinter import messagebox
import tkinter as tk
import datetime
import sys 
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import config
from time import *
'''from email_validator import validate_email'''

def timememberscreen():
	def timemember():
		string = strftime('Members Menu\n'+'%H:%M:%S %p')
		adminMemberClockLabel.config(text = string)
		adminMemberClockLabel.after(1000, timemember)

	timemember()

def timestaffscreen():
	def timestaff():
		string = strftime('Staff Menu\n'+'%H:%M:%S %p')
		adminStaffClockLabel.config(text = string)
		adminStaffClockLabel.after(1000, timestaff)

	timestaff()

def timeclassscreen():
	def timeclass():
		string = strftime('Class Menu\n'+'%H:%M:%S %p')
		adminClassClockLabel.config(text = string)
		adminClassClockLabel.after(1000, timeclass)

	timeclass()





def back_to_login():
	raise_frame(loginframe)
	

def create_account():
	raise_frame(create_account_frame)
	root.geometry('450x550')

conn = sqlite3.connect('gymmembers.db')
c = conn.cursor()

'''def create_login_table():
	conn = sqlite3.connect('gymmembers.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE login (
			username_ text,
			password_ text,
			memebership_ text,
			membership_type_ text,
			age_ integer,
			gender_ text,
			address_ text,
			phonenumber_ integer
		)""")
	print('Table created')
	conn.commit()
	conn.close()

def create_manager_login_table():
	conn = sqlite3.connect('gymmembers.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE managerlogin (
			manager_username_ text,
			manager_password_ text
		)""")
	print('Manager Table created')
	conn.commit()
	conn.close()


def create_staff_table():
	conn = sqlite3.connect('gymmembers.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE staff (
			staff_email text,
			firstname_ text,
			lastname_ text,
			phonenumber_ text,
			gender_ integer,
			speciality_ text
		)""")
	print('Table created')
	conn.commit()
	conn.close()

def create_classes_table():
	conn = sqlite3.connect('gymmembers.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE classes (
			classID integer,
			GymID integer,
			class_name text,
			Day text,
			time_ integer,
			amount_of_ppl text,
			InstructorID integer
		)""")
	print('Table created')
	conn.commit()
	conn.close()

def create_gyms_table():
	conn = sqlite3.connect('gymmembers.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE gyms (
			GymID integer,
			gym_name text,
			gym_address text,
			gym_phonenumber integer
		)""")
	print('Table created')
	conn.commit()
	conn.close()'''



def raise_frame(frame_name):
	frame_name.tkraise()

def login():
	global username
	username_login = username.get()
	username1 = username_login
	password_login = password.get()


	if username_login == '' or password_login == '':
		messagebox.showinfo('Invalid data','Please enter your username and password correctly')

	conn = sqlite3.connect('gymmembers.db')
	c = conn.cursor()
	c.execute("SELECT rowid, * from login WHERE username_ = (?)", (username_login,))
	reader = c.fetchall()
	print(reader)

	for row in reader:
		if row[1] != username_login:
			messagebox.showinfo('Member Account', 'Member account not found')

		elif row[2] != password_login:
			messagebox.showinfo('Member Account', 'Member account not found')


		elif row[4] == 'Unactive':
			messagebox.showinfo('Account blocked','Your account has been banned from using your gym membership or it has not been actived yet.')

		#elif username_login == row[1]:
			#messagebox.showinfo('Email Error','This email is invalid as some one else is using it')

		else:
			raise_frame(MemberClassesFrame)
			root.geometry('950x620')
			username.set('')
			password.set('')


	conn = sqlite3.connect('gymmembers.db')
	c = conn.cursor()
	c.execute("SELECT rowid, * from managerlogin WHERE manager_username_ = (?)", (username_login,))
	managerreader = c.fetchall()
	print(managerreader)

	for row in managerreader:
		if row[1] == username_login:
			raise_frame(managermenuframe)
			root.geometry('950x620')
			username.set('')
			password.set('')
			
		else:
			messagebox.showinfo('Manger Account', 'Manager account not found')
	





        
    
	'''if login != username and password:
		messagebox.showinfo('User Information','There is no such account that exists try again', icon = 'info')
		username_entry.delete(0, END),
		password_entry.delete(0, END)

	else:
		print('Login Successful')'''


	conn.commit()
	conn.close()


def timeworkoutplanscreen():
	def timeworkplan():
		string = strftime('%H:%M:%S %p')
		adminMemberClockLabel.config(text = string)
		adminMemberClockLabel.after(1000, timeworkplan)

	timeworkplan()

	#conn.connect('gymmembers.db')

def ResetPassword():
	FinialOTPcode = OTPcode.get()
	FinialNewPassword = NewPassword.get()
	FinialNewPassword2 = NewPassword2.get()

	print(number, FinialOTPcode)
	if len(FinialNewPassword) < 8:
		print('Invalid password')
	else:
		if str(FinialOTPcode) == str(number) and FinialNewPassword2 == FinialNewPassword:
			value = (FinialNewPassword, email)
			conn = sqlite3.connect('gymmembers.db')
			c = conn.cursor()

			c.execute("""UPDATE login SET password_ = ?
			WHERE username_ = ?

			""", value)

			conn.commit()
			conn.close()
			raise_frame(loginframe)
			messagebox.showinfo('Password Reset', 'Your password has been reset Successfully. Login with your new password')

		elif str(FinialOTPcode) != str(number) and FinialNewPassword2 == FinialNewPassword:
			messagebox.showinfo('Code','Reset password code does match the one sent in the email')

		elif str(FinialOTPcode) == str(number) and FinialNewPassword2 != FinialNewPassword:
			messagebox.showinfo('Invalid password Error','New password must match confirm password')

		else:
			messagebox.showinfo('Invalid Error', 'Error password does not match confrm password try again')
			FinialOTPcode.set('')
			FinialNewPassword.set('')
			FinialNewPassword2.set('')



def cancel_reset():
	raise_frame(loginframe)

def raise_manager_frame():
	pass
	

def forgot_password():
	global number
	number = random.randint(1111, 9999)
	print('OTP:', number)
	global email
	email = simpledialog.askstring("Information", "Enter email:")
	#global forget_email
	#forget_email = email
	subject = 'Reset Password'
	msg = MIMEMultipart()
	msg['From'] = config.emailAddress
	msg['To'] = email
	msg['Subject'] = subject
	body = 'Hello, your reset code is: ' + str(number)
	msg.attach(MIMEText(body, 'plain'))

	part = MIMEBase('application', 'octet-stream')
	text = msg.as_string()

	conn = sqlite3.connect('gymmembers.db')
	c = conn.cursor()
	c.execute("SELECT rowid, * from login WHERE username_ = (?)", (email,))
	reader = c.fetchall()
	print(reader)

	for row in reader:
		if email != row[1]:
			messagebox.showinfo('Email Error','This account does not exist')

		else:
			try:
				server = smtplib.SMTP('smtp.gmail.com:587')
				server.ehlo()
				server.starttls()
				server.login(config.emailAddress, config.password)
				server.sendmail(config.emailAddress, email, text)
				server.quit()
				print('email sent')
				messagebox.showinfo('Email sent','Open up the email to redeem the code to reset your password')
				raise_frame(resetpasswordframe)
				resetpasswordframe.geometry('500x500')


			except:
				print('Email not sent')

	conn.commit()
	conn.close()



def submit_account():
	data_check = 0
	global username_create_account
	username_create_account = account_email.get()
	password_ = password1.get()
	password_confirm = confirm_password.get()
	memebership_ = memebership.get()
	membership_type_ = 'Unactive'
	age_ = age_spinbox.get()
	gender_ = gender.get()
	address_ = address.get()
	phonenumber_ = phonenumber.get()
	print('hello ' + username_create_account)
	set_login_black()


	conn = sqlite3.connect('gymmembers.db')
	c = conn.cursor()
	c.execute("SELECT rowid, * from login WHERE username_ = (?)", (username_create_account,))
	reader = c.fetchall()
	print(reader)

	email = "my+address@mydomain.tld"
	valid = validate_email(email)
	
	'''if username_create_account != valid.email:
		email_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Error please enter email', icon = 'warning')
		account_email.set('')
		data_check = 1'''

	for row in reader:
		if username_create_account == row[1]:
			messagebox.showinfo('Email Error','This email is invalid as some one else is using it')
			account_email.set('')
		else:
			pass




	if username_create_account == '':
		email_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Error please enter email', icon = 'warning')
		account_email.set('')
		data_check = 1

	elif username_create_account.isnumeric() == True:
		email_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Error please enter email', icon = 'warning')
		account_email.set('')
		data_check = 1


	if password_ == '':
		password_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Error please enter password', icon = 'warning')
		password1.set('')
		data_check = 1


	elif password_.isnumeric() == True:
		password_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Error please enter password', icon = 'warning')
		password1.set('')
		data_check = 1

	elif password_ != password_confirm:
		Cpassword_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Password does not match confirm password', icon = 'warning')
		confirm_password.set('')
		data_check = 1

	elif len(password_) < 8:
		messagebox.showinfo('User Information','Error your password must be longer than 8 characters', icon = 'warning')
		password1.set('')
		data_check = 1


	if phonenumber_ == '':
		phone_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Error please enter your phonenumber', icon = 'warning')
		phonenumber.set('')

	elif phonenumber_.isnumeric() == False:
		phone_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Your phone number should only include numbers', icon = 'warning')
		phonenumber.set('')
		data_check = 1

	elif len(phonenumber_) != 11:
		messagebox.showinfo('User Information','Your phonenumber must be 11 numbers', icon = 'warning')
		phonenumber.set('')
		data_check = 1

	#print(data_check)
	elif data_check == 0:
		print('added')
		conn = sqlite3.connect('gymmembers.db')
		c = conn.cursor()
		c.execute("INSERT INTO login VALUES (:account_email, :password1, :memebership, :membership_type, :age, :gender, :address, :phonenumber)", 
					{
						'account_email': account_email.get(),
						'password1': password1.get(),
						'memebership': memebership.get(),
						'membership_type': membership_type_,
						'age': age_spinbox.get(),
						'gender': gender.get(),
						'address': address.get(),
						'phonenumber': phonenumber.get()

					})

		recipientemail = account_email.get()
		emailAddress = 'marco.donaghy@gmail.com'
		email_password = password1.get()
		part = MIMEBase('application', 'octet-stream')
		global msg
		subject = "Welcome to the your Gym Membership!"
		msg = MIMEMultipart()
		msg['From'] = emailAddress
		msg['To'] = recipientemail
		msg['Subject'] = subject
		text = msg.as_string()
		body = ("Hi" + recipientemail, "\nThanks for joining the gym and fitness centre – we’re excited to have you on board! You’ve taken the first step towards achieving your fitness goals and objectives. Get started by joining up to your first session on our new app you have signed up to. During this session we’ll prepare a workout program to help you achieve your goals and show you how to use all of the equipment. You’ll find our opening times, class timetable on our app. If you have any questions, then please don’t hesitate to get in touch. Simply call us on 07328494568 or reply to this email and we’ll respond asap.\nKind regards Marco Donaghy")
		msg.attach(MIMEText(body,'plain'))
		msg.attach(part)
		text = msg.as_string()
		messagebox.showinfo('Gym members','Data added Successfully')
		raise_frame(loginframe)
		show_all_members()
		root.geometry('900x500')
			
			
			

		try:
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.ehlo()
			server.starttls()
			server.login(config.emailAddress,config.password)
			server.sendmail(emailAddress,recipientemail,text)
			server.quit()
			print('Email sent')
		except:
			print('Email not sent')

		conn.commit()
		conn.close()
		email_entry.delete(0 , END),
		password_entry.delete(0 , END),
		Cpassword_entry.delete(0 , END),
		address.set(''),
		phone_entry.delete(0 , END)
		show_all_members()

	elif data_check == 1:
		messagebox.showinfo('Invalid','Check the data you inputted')


		#send_email(subject, msg, config.recipientemail)
		
		#send_email(subject,msg,recipientemail)
		
		#messagebox.showinfo('Gym members','Data added Successfully')
	


def set_login_black():
	email_label.config(fg ='black')
	password_label.config(fg ='black')
	Cpassword_label.config(fg ='black')
	phone_label.config(fg ='black')



'''def send_email(subject,msg,recipientemail):
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.emailAddress, config.password)
		server.sendmail(config.emailAddress,recipientemail,text)
		server.quit()
		print('Email sent')
	except:
		print('Email not sent')


	send_email(subject, msg, config.recipientemail)

	subject = "Gym Membership confirmation"
	msg = MIMEMultipart()
	msg['From'] = config.emailAddress
	msg['To'] = config.recipientemail
	msg['Subject'] = subject
	body = ("Welcome to the your Libray Membership")
	msg.attach(MIMEText(body,'plain'))
	msg.attach(part)
	text = msg.as_string()
#send_email(subject, msg, config.recipientemail)'''

def show_all_members():
    MemberDetails = []
    conn = sqlite3.connect('gymmembers.db')
    c = conn.cursor()
    c.execute("SELECT * FROM login")
    reader = c.fetchall()
    for row in reader:
        if not row:
            pass
        else:
            MemberDetails.append(row)

    records = memberTV.get_children()

    for elements in records:
        memberTV.delete(elements)

    for row in MemberDetails:
    	if row[3] == 'Active':
    		memberTV.tag_configure('Active', background = '#00ff4c')
    		memberTV.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]), tag = 'Active')
    	#row = booking_details[x-1]
    	#if row[3] == 'Active':
    	elif row[3] == 'Unactive':
    		memberTV.tag_configure('Unactive', background = '#ff0000')
    		memberTV.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]), tag = 'Unactive')
    
    conn.commit()
    conn.close()

def show_all_staff():
    StaffDetails = []
    conn = sqlite3.connect('gymmembers.db')
    c = conn.cursor()
    c.execute("SELECT * FROM staff")
    reader = c.fetchall()
    for row in reader:
        if not row:
            pass
        else:
            StaffDetails.append(row)

    records = staffTV.get_children()

    for elements in records:
        staffTV.delete(elements)

    for row in StaffDetails:
        staffTV.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))

    conn.commit()
    conn.close()

def show_all_classes():
    ClassDetails = []
    conn = sqlite3.connect('gymmembers.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM classes")
    reader = c.fetchall()
    print(reader)
    for row in reader:
        if not row:
            pass
        else:
            ClassDetails.append(row)

    records = clasesTV.get_children()


    for elements in records:
        clasesTV.delete(elements)

    for row in ClassDetails:
    	a=row[6].replace('(','')
    	b=a.replace(')','')
    	c=b.replace("'",'')
    	d = c.replace(',','')

    	e=row[1].replace('(','')
    	f=e.replace(')','')
    	g=f.replace("'",'')
    	h = g.replace(',','')
    	clasesTV.insert('', 'end', text=row[0], values=(h, row[2], row[3], row[4], row[5], d))

        #print(row[6].replace('(',''))

    conn.commit()
    conn.close()







def delete_gym_member_RC():

	curItem = memberTV.focus()
	dictionary = memberTV.item(curItem)
	print(curItem)
	print(dictionary)
	listvalues = list(dictionary.values())
	print(listvalues)
	minilist = listvalues[0]
	print(minilist)
	conn = sqlite3.connect('gymmembers.db')
	are_you_sure = messagebox.askyesno('Are you sure','Are you sure you want to delete '+ str(minilist))
	if are_you_sure == True:
		c = conn.cursor()
		c.execute("DELETE from login WHERE username_ = (?)", (minilist,))
		
		conn.commit()
		conn.close()
		messagebox.showinfo('Data Deleted',str(minilist) +' Has been deleted Successfully')
		show_all_members()
	elif are_you_sure == 'No':
		are_you_sure.destroy()

def DeleteMember():
	delete_gym_member_RC()
	'''curItem = memberTV.focus()
	dictionary = memberTV.item(curItem)
	print(curItem)
	print(dictionary)
	listvalues = list(dictionary.values())
	print(listvalues)
	minilist = listvalues[0]
	print(minilist)
	conn = sqlite3.connect('gymmembers.db')
	c = conn.cursor()
	c.execute("DELETE from login WHERE username_ = (?)", (minilist,))
	
	conn.commit()
	conn.close()
	messagebox.showinfo('Data Deleted','Gym member has been deleted Successfully')
	show_all_members()'''


def confirm_membership_RC():
	curItem = memberTV.focus()
	dictionary = memberTV.item(curItem)
	print('item', curItem)
	print('dictinary', dictionary)
	listvalues = list(dictionary.values())
	print('list: ', listvalues)
	minilist = listvalues[0]
	print('memberhip:', minilist)
	conn = sqlite3.connect('gymmembers.db')
	c = conn.cursor()
	confirm_membership = askstring('Memebership Status', 'Deactivate or Activate: '+ str(minilist))
	c.execute("""UPDATE login SET membership_type_ = :membership_type WHERE username_ = :username""",
		{
		'username':minilist,
		'membership_type':confirm_membership})

	if confirm_membership == '':
		pass


	elif confirm_membership == 'Active':

		recipientemail = "marco.donaghy@gmail.com"
		emailAddress = "marco.donaghy@gmail.com"
		password = "kdcfd142a"
		#email_password = password1.get()
		part = MIMEBase('application', 'octet-stream')
		global msg
		subject = "Gym Membership confirmation Active"
		msg = MIMEMultipart()
		msg['From'] = emailAddress
		msg['To'] = recipientemail
		msg['Subject'] = subject
		text = msg.as_string()
		body = ("Welcome to the your Gym Membership your membership is now active")
		msg.attach(MIMEText(body,'plain'))
		msg.attach(part)
		text = msg.as_string()
			
			
			

		try:
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.ehlo()
			server.starttls()
			server.login(config.emailAddress, config.password)
			server.sendmail(config.emailAddress,recipientemail,text)
			server.quit()
			print('Email sent')
		except:
			print('Email not sent')

	elif confirm_membership == 'Unactive':
		recipientemail = "marco.donaghy@gmail.com"
		emailAddress = "marco.donaghy@gmail.com"
		password = "kdcfd142a"
		#email_password = password1.get()
		part = MIMEBase('application', 'octet-stream')
		#global msg
		subject = "Gym Membership confirmation Deactive"
		msg = MIMEMultipart()
		msg['From'] = emailAddress
		msg['To'] = recipientemail
		msg['Subject'] = subject
		text = msg.as_string()
		body = ("Sorry your gym membership has been deactived")
		msg.attach(MIMEText(body,'plain'))
		msg.attach(part)
		text = msg.as_string()
			
		try:
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.ehlo()
			server.starttls()
			server.login(config.emailAddress, config.password)
			server.sendmail(config.emailAddress,recipientemail,text)
			server.quit()
			print('Email sent')
		except:
			print('Email not sent')

	
	conn.commit()
	conn.close()
	messagebox.showinfo('Data Updated','Gym membership has been Updated Successfully')
	show_all_members()

def ConfirmMember():
	confirm_membership_RC()

def SearchMember():
	search_item = search_entry.get()
	MemberDetails = []
	found = False
	conn = sqlite3.connect('gymmembers.db')
	c = conn.cursor()

	#search_item = search


	c.execute("SELECT * FROM login")

	reader = c.fetchall()
	for row in reader:
		if row == []:
			pass
		else:
			if search_item == row[0]:
				found = True
				MemberDetails.append(row)
				print(row)
			elif search_item == row[1]:
				found = True
				MemberDetails.append(row)
				print(row)
			elif search_item == row[2]:
				found = True
				MemberDetails.append(row)
				print(row)
			elif search_item == row[3]:
				found = True
				MemberDetails.append(row)
				print(row)
			elif search_item == row[4]:
				found = True
				MemberDetails.append(row)
				print(row)
			elif search_item == row[5]:
				found = True
				MemberDetails.append(row)
				print(row)
			elif search_item == row[6]:
				found = True
				MemberDetails.append(row)
				print(row)
			elif search_item == row[7]:
				found = True
				MemberDetails.append(row)
				print(row)
			else:
				print('not found')

	if found == False:
		messagebox.showinfo('Not found','The item you are serching for could not be found')
		search_entry.set('')

	else:
		records = memberTV.get_children()

		for elements in records:
			memberTV.delete(elements)

		for row in MemberDetails:
			memberTV.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
		search_entry.set('')
		conn.commit()
		conn.close()


def delete_gym_staff_RC():

	curItem = staffTV.focus()
	dictionary = staffTV.item(curItem)
	print(curItem)
	print(dictionary)
	listvalues = list(dictionary.values())
	print(listvalues)
	minilist = listvalues[0]
	print(minilist)
	conn = sqlite3.connect('gymmembers.db')
	are_you_sure = messagebox.askyesno('Are you sure','Are you sure you want to delete '+ str(minilist))
	if are_you_sure == True:
		c = conn.cursor()
		c.execute("DELETE from staff WHERE staff_email = (?)", (minilist,))
		
		conn.commit()
		conn.close()
		messagebox.showinfo('Data Deleted',str(minilist) +' Has been deleted Successfully')


		recipientemail = "marco.donaghy@gmail.com"
		emailAddress = "marco.donaghy@gmail.com"
		password = "kdcfd142a"
		email_password = password1.get()
		part = MIMEBase('application', 'octet-stream')
		global msg
		subject = "You have been removed from the gym"
		msg = MIMEMultipart()
		msg['From'] = emailAddress
		msg['To'] = recipientemail
		msg['Subject'] = subject
		text = msg.as_string()
		body = ("We are sorry to inform you that you are no longer one of our staff members")
		msg.attach(MIMEText(body,'plain'))
		msg.attach(part)
		text = msg.as_string()
		show_all_staff()
		clear_staff()
		
			
			
			

		try:
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.ehlo()
			server.starttls()
			server.login(config.emailAddress, config.password)
			server.sendmail(config.emailAddress,recipientemail,text)
			server.quit()
			print('Email sent')
		except:
			print('Email not sent')

		show_all_staff()
	elif are_you_sure == 'No':
		are_you_sure.destroy()

def delete_gym_staff():
	delete_gym_staff_RC()


def set_staff_black():
	staff_email_label.config(fg = 'black')
	staff_firtname_label.config(fg = 'black')
	staff_lastname_label.config(fg = 'black')
	staff_phone_label.config(fg = 'black')
	staff_speciality_label.config(fg = 'black')


def clear_staff():
	staff_email_entry.delete(0 , END),
	staff_firtname_entry.delete(0 , END),
	staff_lastname_entry.delete(0 , END),
	staff_phone_entry.delete(0 , END),
	select_speciality.set('Select Speciality')



def create_staff():
	data_check = 0
	global staff_create_email
	staff_create_email = staff_account_email.get()
	firstname_ = staff_firstname.get()
	lastname_ = staff_lastname.get()
	phonenumber_ = staff_phone.get()
	gender_ = staff_gender.get()
	speciality_ = select_speciality.get()
	print('hello ' + staff_create_email)
	set_staff_black()


	conn = sqlite3.connect('gymmembers.db')
	c = conn.cursor()
	c.execute("SELECT rowid, * from staff WHERE staff_email = (?)", (staff_create_email,))
	reader = c.fetchall()
	print(reader)

	for row in reader:
		if staff_create_email == row[1]:
			messagebox.showinfo('Email Error','This email is invalid as some one else is using it')
			staff_account_email.set('')
		else:
			pass


	if staff_create_email == '':
		staff_email_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Error please enter email', icon = 'warning')
		staff_account_email.set('')
		data_check = 1

	elif staff_create_email.isnumeric() == True:
		staff_email_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Error please enter email', icon = 'warning')
		staff_account_email.set('')
		data_check = 1


	if firstname_ == '':
		staff_firtname_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Error please enter password', icon = 'warning')
		staff_firstname.set('')
		data_check = 1


	elif firstname_.isnumeric() == True:
		staff_firtname_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Error please enter password', icon = 'warning')
		staff_firstname.set('')
		data_check = 1


	if lastname_ == '':
		staff_lastname_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Error please enter your phonenumber', icon = 'warning')
		staff_lastname.set('')
		data_check = 1

	elif lastname_.isnumeric() == True:
		staff_lastname_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Your phone number should only include numbers', icon = 'warning')
		staff_lastname.set('')
		data_check = 1

	if phonenumber_ == '':
		staff_phone_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Error please enter your phonenumber', icon = 'warning')
		staff_phone.set('')
		data_check = 1

	elif phonenumber_.isnumeric() == False:
		staff_phone_label.config(fg = 'red')
		#messagebox.showinfo('User Information','Your phone number should only include numbers', icon = 'warning')
		staff_phone.set('')
		data_check = 1

	elif len(phonenumber_) != 11:
		messagebox.showinfo('User Information','Your phonenumber must be 11 numbers', icon = 'warning')
		staff_phone_label.config(fg = 'red')
		staff_phone.set('')
		data_check = 1






	#print(data_check)
	if data_check == 0:
		print('added')
		conn = sqlite3.connect('gymmembers.db')
		c = conn.cursor()
		c.execute("INSERT INTO staff VALUES (:staff_account_email, :staff_firstname, :staff_lastname, :staff_phone, :staff_gender, :select_speciality)", 
					{
						'staff_account_email': staff_account_email.get(),
						'staff_firstname': staff_firstname.get(),
						'staff_lastname': staff_lastname.get(),
						'staff_phone': staff_phone.get(),
						'staff_gender': staff_gender.get(),
						'select_speciality': select_speciality.get()

					})

		recipientemail = staff_account_email.get()
		emailAddress = "marco.donaghy@gmail.com"
		password = "kdcfd142a"
		email_password = password1.get()
		part = MIMEBase('application', 'octet-stream')
		global msg
		subject = "Congratulations you have been employed to the gym"
		msg = MIMEMultipart()
		msg['From'] = emailAddress
		msg['To'] = recipientemail
		msg['Subject'] = subject
		text = msg.as_string()
		body = ("Congratulations you are now an a staff member within the gym!")
		msg.attach(MIMEText(body,'plain'))
		msg.attach(part)
		text = msg.as_string()
		messagebox.showinfo('Gym staff','Data added Successfully')
		show_all_staff()
		clear_staff()
		
			
			
			

		try:
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.ehlo()
			server.starttls()
			server.login(config.emailAddress, config.password)
			server.sendmail(config.emailAddress,recipientemail,text)
			server.quit()
			print('Email sent')
		except:
			print('Email not sent')

		conn.commit()
		conn.close()
		staff_email_entry.delete(0 , END),
		staff_firtname_entry.delete(0 , END),
		staff_lastname_entry.delete(0 , END),
		staff_phone_entry.delete(0 , END),
		select_speciality.set('Select Speciality')
		show_all_staff()






def MenuManageMember():
	raise_frame(managermenuframe)

def SettingsManageMember():
	raise_frame(managermenuframe)


def from_menu_go_to_settings():
	raise_frame(ManagerSettingsFrame)

def from_settings_to_settings():
	raise_frame(ManagerSettingsFrame)

def from_menu_go_to_staff():
	raise_frame(ManagerStaffFrame)

def from_staff_go_to_members():
	raise_frame(managermenuframe)

def from_settings_to_staff():
	raise_frame(ManagerStaffFrame)

def from_staff_go_to_staff():
	raise_frame(ManagerStaffFrame)

def from_staff_go_to_settings():
	raise_frame(ManagerSettingsFrame)

def from_menu_go_to_classes():
	raise_frame(ManagerClassesFrame)

def from_settings_go_to_classes():
	raise_frame(ManagerClassesFrame)

def from_staff_go_to_classes():
	raise_frame(ManagerClassesFrame)

def from_classes_go_to_members():
	raise_frame(managermenuframe)

def from_classes_go_to_staff():
	raise_frame(ManagerStaffFrame)

def from_classes_go_to_settings():
	raise_frame(ManagerSettingsFrame)

def from_classes_to_classes():
	raise_frame(ManagerClassesFrame)


def ManagerLogout():
	raise_frame(loginframe)
	root.geometry('400x550')


def go_from_classes_to_classes():
	raise_frame(MemberClassesFrame)	
	
def from_classes_to_workout():
	raise_frame(MemberWorkoutFrame)

def go_from_workout_to_classes():
	raise_frame(MemberClassesFrame)

def from_workoutplan_to_workoutplan():
	raise_frame(MemberWorkoutFrame)


root = Tk()
root.geometry('400x550')
root.title('Gym App')
root.configure(background = 'light grey')

username = StringVar()
password = StringVar()

account_email = StringVar()
password1 = StringVar()
confirm_password = StringVar()
memebership = StringVar()
age = StringVar()
gender = StringVar()
address = StringVar()
phonenumber = StringVar()

NewPassword = StringVar()
NewPassword2 = StringVar()
OTPcode = StringVar()

search_entry = StringVar()





loginframe = Frame(root, bg = 'light grey')
create_account_frame = Frame(root, bg = 'light grey')
resetpasswordframe = Frame(root, bg = 'light grey')
managermenuframe = Frame(root, bg = 'light grey')
ManagerSettingsFrame = Frame(root, bg = 'light grey')
ManagerStaffFrame = Frame(root, bg = 'light grey')
ManagerClassesFrame = Frame(root, bg = 'light grey')
MemberClassesFrame = Frame(root, bg = 'light grey')
MemberWorkoutFrame = Frame(root, bg = 'light grey')


for frame in(loginframe, create_account_frame, resetpasswordframe, managermenuframe, ManagerSettingsFrame, ManagerStaffFrame, ManagerClassesFrame, MemberClassesFrame, MemberWorkoutFrame):
	frame.grid(row=0,column=0, sticky = 'news')


login_photo_frame = Frame(loginframe)
login_photo_frame.grid(row = 0, column = 1, columnspan = 2)
login_photo_frame.configure(bg = 'light grey')

photologinscreen = PhotoImage(file = 'Gym_logo.png')
photolabel = Label(login_photo_frame, image = photologinscreen, bg = 'light grey')
photolabel.grid(row = 0, column = 0, sticky = N, padx = 80)

username_label = Label(login_photo_frame,text = 'Username:',bg='light grey',fg='black', padx=10, pady = 20, font = 18)
username_label.grid(row = 1, column = 0)
username_entry = Entry(login_photo_frame, textvariable = username, font = 18)
username_entry.grid(row = 2, column = 0)

password_label = Label(login_photo_frame, text = 'Password:', bg ='light grey', padx= 10,  pady = 20, font = 18)
password_label.grid(row = 3, column = 0)
password_entry = Entry(login_photo_frame, textvariable=password, font = 18)
password_entry.grid(row = 4, column = 0)

login_button = Button(login_photo_frame,text ='Login', command = login, fg = 'white',bg = 'black', font = 18, height = 1, width = 15)
login_button.grid(row = 5, column = 0, pady = 10)

forgot_password_button = Button(login_photo_frame, text= 'Forgot password?', command=forgot_password,fg = 'white', bg = 'black', font =18,  height = 1, width = 15)
forgot_password_button.grid(row = 7, column = 0)

create_account_button = Button(login_photo_frame,text= 'Create account', command=create_account,fg = 'white',bg = 'black',  font = 18, height = 1, width = 15)
create_account_button.grid(row = 8, column = 0, pady =10)


photocreateaccountscreen = PhotoImage(file = 'Gym_logo_small.png')
photolabel1 = Label(create_account_frame, image = photocreateaccountscreen, bg = 'light grey')
photolabel1.grid(row = 0, column = 0, sticky = N, columnspan = 1)

email_label = Label(create_account_frame, text = 'Email', fg = 'black', bg = 'light grey', padx = 10, pady = 10, font = 18)
email_label.grid(row = 1, column = 0)
email_entry = Entry(create_account_frame, textvariable = account_email, font = 18, width = 25)
email_entry.grid(row = 1, column = 1)

password_label = Label(create_account_frame, text = 'Password', fg = 'black', bg = 'light grey', padx = 10, pady = 10, font = 18)
password_label.grid(row = 2, column = 0)
password_entry = Entry(create_account_frame, textvariable = password1, font = 18)
password_entry.grid(row = 2, column = 1)

Cpassword_label = Label(create_account_frame, text = 'Confirm Password', fg = 'black', bg = 'light grey', padx = 10, pady = 10, font = 18)
Cpassword_label.grid(row = 3, column = 0)
Cpassword_entry = Entry(create_account_frame, textvariable = confirm_password, font = 18)
Cpassword_entry.grid(row = 3, column = 1)

membership1 = Radiobutton(create_account_frame, text="£10.00/per month", variable = memebership, value="£10.00/per month", bg ='light grey',fg = 'black', padx = 10, pady = 10, font = 18)
membership1.grid(row = 4, column = 0)
membership2= Radiobutton(create_account_frame, text="£100.00/per year", variable = memebership, value="£100.00/per year", bg ='light grey',fg = 'black', padx = 10, pady = 10, font = 18)
membership2.grid(row = 4, column = 1)

age_label=Label(create_account_frame,text='Age',bg='light grey', fg = 'black', padx = 10, pady = 10, font = 18)
age_label.grid(row = 5, column = 0)
age_spinbox = Spinbox(create_account_frame, from_ = 16, to = 80, fg = 'black', font = 18)
age_spinbox.grid(row = 5, column = 1)

GenderRBM = Radiobutton(create_account_frame, text="Male", variable = gender, value="Male", bg ='light grey', padx = 10, pady = 10, font = 18)
GenderRBM.grid(row = 6, column = 0)
GenderRBF= Radiobutton(create_account_frame, text="Female", variable = gender, value="Female", bg ='light grey', padx = 10, pady = 10, font = 18)
GenderRBF.grid(row = 6, column = 1)

'''address_label = Label(create_account_frame, text = 'Address', bg='white', fg = 'black', padx = 10, pady = 10, font =18)
address_label.grid(row = 7, column = 0)
address_entry= Entry(create_account_frame,textvariable=address , font = 18)
address_entry.grid(row = 7, column = 1)'''

gymchoices = { 'City Center','Boucher Road','Finaghy','Lisburn','Newtownbredda'}
address.set('City Center') # set the default option

popupMenu = OptionMenu(create_account_frame, address, *gymchoices)
Label(create_account_frame, text="Gym location",bg = 'light grey', padx = 10, pady = 1, font = 18).grid(row = 7, column = 0)
popupMenu.grid(row = 7, column =1,pady = 10)

phone_label = Label(create_account_frame, text = 'Phone number', bg='light grey', fg = 'black', padx = 10, pady = 1, font = 18)
phone_label.grid(row = 8, column = 0)
phone_entry= Entry(create_account_frame,textvariable= phonenumber, font = 18)
phone_entry.grid(row = 8, column = 1)

back_button = Button(create_account_frame, command=back_to_login, text ='Cancel',bg='black', fg = 'white',width = 15, height = 1, font = 18)
back_button.grid(row = 9, column = 0, pady = 10)

submit_button = Button(create_account_frame, command = submit_account, text='Create Account', bg='black', fg = 'white',width = 15, height = 1, font = 18)
submit_button.grid(row = 9, column = 1, pady = 10)


photoresetpasswordcreen = PhotoImage(file = 'Gym_logo_small.png')
photolabel3 = Label(resetpasswordframe, image = photoresetpasswordcreen, bg = 'light grey')
photolabel3.grid(row = 0, column = 0, columnspan = 2)

verification_code_label = Label(resetpasswordframe, text = 'Code:', bg='white', fg = 'black', padx = 10, pady = 10, font = 18)
verification_code_label.grid(row = 1, column=0)
verification_code_entry = Entry(resetpasswordframe,textvariable= OTPcode, font = 18)
verification_code_entry.grid(row=1, column =1)

change_password_label = Label(resetpasswordframe, text = 'Password:', bg='white', fg = 'black', padx = 10, pady = 10, font = 18)
change_password_label.grid(row = 2, column=0)
change_password_entry = Entry(resetpasswordframe,textvariable= NewPassword, font = 18)
change_password_entry.grid(row=2, column =1)


change_password2_label = Label(resetpasswordframe, text = 'Confirm Password:', bg='white', fg = 'black', padx = 10, pady = 10, font = 18)
change_password2_label.grid(row = 3, column=0)
change_password2_entry = Entry(resetpasswordframe,textvariable= NewPassword2, font = 18)
change_password2_entry.grid(row=3, column =1)

reset_password_button = Button(resetpasswordframe, command=ResetPassword, text ='Reset password',fg = 'white', bg='black',width = 15, height = 1, font = 18)
reset_password_button.grid(row=4,column=1)

cancel_reset_button = Button(resetpasswordframe, command = cancel_reset, text = 'Cancel', fg ='white', bg = 'black',width = 15, height = 1, font = 18)
cancel_reset_button.grid(row = 4, column = 0)

photomemberclassesscreen = PhotoImage(file = 'Gym_logo_small.png')
photolabel7 = Label(MemberClassesFrame, image = photomemberclassesscreen, bg = 'light grey')
photolabel7.grid(row = 0, column = 0)

ClassesPlanButton = Button(MemberClassesFrame, command= go_from_classes_to_classes, text ='Classes',fg = 'white', bg='black',width = 15, height = 2, font = 18)
ClassesPlanButton.grid(row=0,column = 1)

ClassesWorkouPlanButton = Button(MemberClassesFrame, command=from_classes_to_workout, text ='Workout Plans',fg = 'white', bg='black',width = 15, height = 2, font = 18)
ClassesWorkouPlanButton.grid(row=0,column= 2)

photomemberworkoutplanscreen = PhotoImage(file = 'Gym_logo_small.png')
photolabel8 = Label(MemberWorkoutFrame, image = photomemberworkoutplanscreen, bg = 'light grey')
photolabel8.grid(row = 0, column = 0)

adminMemberClockLabel = Label(MemberWorkoutFrame, bg = 'light grey', font = 'bold')
adminMemberClockLabel.grid(row = 0, column = 3, padx = 10)
timeworkoutplanscreen()

WorkoutPlanClassesButton = Button(MemberWorkoutFrame, command= go_from_workout_to_classes, text ='Classes',fg = 'white', bg='black',width = 15, height = 2, font = 18)
WorkoutPlanClassesButton.grid(row=0,column = 1)

WorkouPlanButton = Button(MemberWorkoutFrame, command=from_workoutplan_to_workoutplan, text ='Workout Plans',fg = 'white', bg='black',width = 15, height = 2, font = 18)
WorkouPlanButton.grid(row=0,column= 2)

Weights_workout_plan_lf = LabelFrame(MemberWorkoutFrame,text = 'Weights', padx = 5, pady = 5)
Weights_workout_plan_lf.grid(row = 1, column = 0, sticky = 'NW', columnspan = 15)
Weights_workout_plan_lf.configure(bg = 'white')

testlabel = Label(Weights_workout_plan_lf, text ='test')
testlabel.grid(row = 0, column =1 )

Cardio_workout_plan_lf = LabelFrame(MemberWorkoutFrame,text = 'Cardio', padx = 5, pady = 5)
Cardio_workout_plan_lf.grid(row = 2, column = 0, sticky = 'NW', columnspan = 15)
Cardio_workout_plan_lf.configure(bg = 'white')


testlabel2 = Label(Cardio_workout_plan_lf, text ='test')
testlabel2.grid(row = 0, column = 1)


photomanagermenuscreen = PhotoImage(file = 'Gym_logo_small.png')
photolabel4 = Label(managermenuframe, image = photomanagermenuscreen, bg = 'light grey')
photolabel4.grid(row = 0, column = 0)

memberTV = ttk.Treeview(managermenuframe, height = 10, columns =('Password','Membership','Membership Status','Age','Gender','Address','Phone number'))
memberTV.grid(row = 2, column = 0, columnspan = 30, pady = 10)

memberTV.heading('#0', text = 'Email')
memberTV.column('#0', minwidth = 0 , width =200, anchor = 'center')
memberTV.heading('#1', text = 'Password')
memberTV.column('#1', minwidth = 0 , width =110, anchor = 'center')
memberTV.heading('#2', text = 'Membership')
memberTV.column('#2', minwidth = 0 , width = 130, anchor = 'center')
memberTV.heading('#3', text = 'Membership Status')
memberTV.column('#3', minwidth = 0 , width = 120, anchor = 'center')
memberTV.heading('#4', text = 'Age')
memberTV.column('#4', minwidth = 0 , width = 70, anchor = 'center')
memberTV.heading('#5', text = 'Gender')
memberTV.column('#5', minwidth = 0 , width = 100, anchor = 'center')
memberTV.heading('#6', text = 'Address')
memberTV.column('#6', minwidth = 0 , width = 110, anchor = 'center')                         
memberTV.heading('#7', text = 'Phone number')
memberTV.column('#7', minwidth = 0 , width = 110, anchor = 'center')

ttk.Style().theme_use('default')




popupmenumember = Menu(managermenuframe, tearoff = 0)
popupmenumember.add_command(label = 'Cancel Membership', command = delete_gym_member_RC)
popupmenumember.add_command(label = 'Confirm memebership', command = confirm_membership_RC)

def do_popup_member(event):
	try:
		popupmenumember.tk_popup(event.x_root, event.y_root)
	finally:
		popupmenumember.grab_release()
memberTV.bind("<Button-3>", do_popup_member)

searh_bar = Entry(managermenuframe,textvariable= search_entry, font = 18)
searh_bar.grid(row=1, column =0, columnspan = 8)
SearchMemberButton = Button(managermenuframe, command=SearchMember, text ='Search',fg = 'white', bg='black',width = 15, height = 2, font = 18)
SearchMemberButton.grid(row=1,column=1, pady = 10, columnspan= 8)


MembersLabelFrame = LabelFrame(managermenuframe, text = 'Edit Members', bg = 'white', fg = 'black', padx = 228, pady = 5)
MembersLabelFrame.grid(row = 3, column = 0, sticky = 'NW', columnspan = 15)


show_all_member = Button(MembersLabelFrame, command= show_all_members, text ='Show all',fg = 'white', bg='black',width = 15, height = 2, font = 18)
show_all_member.grid(row=3,column=0, padx = 10)

DeleteMemberButton = Button(MembersLabelFrame, command=DeleteMember, text ='Cancel Membership',fg = 'white', bg='black',width = 15, height = 2, font = 18)
DeleteMemberButton.grid(row=3,column=1, padx = 10)

ConfirmMemberButton = Button(MembersLabelFrame, command=ConfirmMember, text ='Membership Status',fg = 'white', bg='black',width = 15, height = 2, font = 18)
ConfirmMemberButton.grid(row=3,column=2, padx = 10)

MenuManageMemberButton = Button(managermenuframe, command= MenuManageMember, text ='Members',fg = 'white', bg='black',width = 15, height = 2, font = 18)
MenuManageMemberButton.grid(row=0,column=1, pady = 10)

MenuManagerStaffButton = Button(managermenuframe, command=from_menu_go_to_staff, text ='Staff',fg = 'white', bg='black',width = 15, height = 2, font = 18)
MenuManagerStaffButton.grid(row=0,column=2, pady = 10)

MenuManagerSettingsButton = Button(managermenuframe, command=from_menu_go_to_settings, text ='Settings',fg = 'white', bg='black',width = 15, height = 2, font = 18)
MenuManagerSettingsButton.grid(row=0,column=4, pady = 10)

MenuManagerClassesButton = Button(managermenuframe, command=from_menu_go_to_classes, text ='Classes',fg = 'white', bg='black',width = 15, height = 2, font = 18)
MenuManagerClassesButton.grid(row=0,column=3)

adminMemberClockLabel = Label(managermenuframe, bg = 'light grey', font = 'bold')
adminMemberClockLabel.grid(row = 0, column = 5, padx = 10)
timememberscreen()



adminClassClockLabel = Label(ManagerClassesFrame, bg = 'light grey', font = 'bold')
adminClassClockLabel.grid(row = 0, column = 5, padx = 10)
timeclassscreen()


SettingsManageMemberButton = Button(ManagerSettingsFrame, command= SettingsManageMember, text ='Members',fg = 'white', bg='black',width = 15, height = 2, font = 18)
SettingsManageMemberButton.grid(row=0,column=1)

StaffManagerSettingsButton = Button(ManagerSettingsFrame, command=from_settings_to_staff, text ='Staff',fg = 'white', bg='black',width = 15, height = 2, font = 18)
StaffManagerSettingsButton.grid(row=0,column=2)

ManagerSettingsButton = Button(ManagerSettingsFrame, command=from_settings_to_settings, text ='Settings',fg = 'white', bg='black',width = 15, height = 2, font = 18)
ManagerSettingsButton.grid(row=0,column=4)

SettingsManagerClassesButton = Button(ManagerSettingsFrame, command=from_settings_go_to_classes, text ='Classes',fg = 'white', bg='black',width = 15, height = 2, font = 18)
SettingsManagerClassesButton.grid(row=0,column=3)





photomanagersettingsscreen = PhotoImage(file = 'Gym_logo_small.png')
photolabel6 = Label(ManagerSettingsFrame, image = photomanagersettingsscreen, bg = 'light grey')
photolabel6.grid(row = 0, column = 0)

ManagerLogoutButton = Button(ManagerSettingsFrame, command=ManagerLogout, text ='Logout',fg = 'white', bg='black',width = 15, height = 2, font = 18)
ManagerLogoutButton.grid(row=1,column=0, pady = 10)








staff_treeview_frame = Frame(ManagerStaffFrame)
staff_treeview_frame.grid(row = 1, column = 0)
staff_treeview_frame.configure(bg = 'light grey')

photomanagerstaffscreen = PhotoImage(file = 'Gym_logo_small.png')
photolabel5 = Label(staff_treeview_frame, image = photomanagerstaffscreen, bg = 'light grey')
photolabel5.grid(row = 0, column = 0)

MenuManagerStaffButton = Button(staff_treeview_frame, command=from_staff_go_to_members, text ='Members',fg = 'white', bg='black',width = 15, height = 2, font = 18)
MenuManagerStaffButton.grid(row=0,column=1)

ManagerStaffButton = Button(staff_treeview_frame, command=from_staff_go_to_staff, text ='Staff',fg = 'white', bg='black',width = 15, height = 2, font = 18)
ManagerStaffButton.grid(row=0,column=2)

StaffManagerSettingsButton = Button(staff_treeview_frame, command=from_staff_go_to_settings, text ='Settings',fg = 'white', bg='black',width = 15, height = 2, font = 18)
StaffManagerSettingsButton.grid(row=0,column=4)

StaffManagerClassesButton = Button(staff_treeview_frame, command=from_staff_go_to_classes, text ='Classes',fg = 'white', bg='black',width = 15, height = 2, font = 18)
StaffManagerClassesButton.grid(row=0,column=3)

adminStaffClockLabel = Label(staff_treeview_frame, bg = 'light grey', font = 'bold')
adminStaffClockLabel.grid(row = 0, column = 5, padx = 10)
timestaffscreen()



staffTV = ttk.Treeview(staff_treeview_frame, height = 10, columns =('Firstname','Last name','Phone number','Gender','Speciality'))
staffTV.grid(row = 1, column = 0, columnspan = 8, sticky = 'NW')

staffTV.heading('#0', text = 'Email')
staffTV.column('#0', minwidth = 0 , width =230, anchor = 'center')
staffTV.heading('#1', text = 'Firstname')
staffTV.column('#1', minwidth = 0 , width =150, anchor = 'center')
staffTV.heading('#2', text = 'Last name')
staffTV.column('#2', minwidth = 0 , width = 150, anchor = 'center')
staffTV.heading('#3', text = 'Phone number')
staffTV.column('#3', minwidth = 0 , width = 150, anchor = 'center')
staffTV.heading('#4', text = 'Gender')
staffTV.column('#4', minwidth = 0 , width = 130, anchor = 'center')
staffTV.heading('#5', text = 'Speciality')
staffTV.column('#5', minwidth = 0 , width = 150, anchor = 'center')

ttk.Style().theme_use('default')

popupmenustaff = Menu(staff_treeview_frame, tearoff = 0)
popupmenustaff.add_command(label = 'Remove staff', command = delete_gym_staff_RC)

def do_popup_staff(event):
	try:
		popupmenustaff.tk_popup(event.x_root, event.y_root)
	finally:
		popupmenustaff.grab_release()
staffTV.bind("<Button-3>", do_popup_staff)

DeleteStaffButton = Button(staff_treeview_frame, command= delete_gym_staff, text ='Remove Staff Member',fg = 'white', bg='black',width = 20, height = 2, font = 18)
DeleteStaffButton.grid(row=2,column=0, pady = 10)

staff_account_email = StringVar()
staff_firstname = StringVar()
staff_lastname = StringVar()
staff_phone = StringVar()
staff_gender = StringVar()
select_speciality = StringVar()


add_staff_frame = LabelFrame(ManagerStaffFrame, text = 'Edit Staff', bg = 'white', fg = 'black', padx = 150, pady = 10)
add_staff_frame.grid(row = 2, column = 0, sticky = 'NW')


staff_email_label = Label(add_staff_frame, text = 'Email', fg = 'black', bg = 'white', padx = 10, pady = 10, font = 14)
staff_email_label.grid(row = 0, column = 0)
staff_email_entry = Entry(add_staff_frame, textvariable = staff_account_email, font = 14, width = 25)
staff_email_entry.grid(row = 0, column = 1)

staff_firtname_label = Label(add_staff_frame, text = 'First name', fg = 'black', bg = 'white', padx = 10, pady = 10, font = 14)
staff_firtname_label.grid(row = 0, column = 2)
staff_firtname_entry = Entry(add_staff_frame, textvariable = staff_firstname, font = 14)
staff_firtname_entry.grid(row = 0, column = 3)

staff_lastname_label = Label(add_staff_frame, text = 'Last name', fg = 'black', bg = 'white', padx = 10, pady = 10, font = 14)
staff_lastname_label.grid(row = 1, column = 0)
staff_lastname_entry = Entry(add_staff_frame, textvariable = staff_lastname, font = 14)
staff_lastname_entry.grid(row = 1, column = 1)

staff_phone_label = Label(add_staff_frame, text = 'Phone number', fg = 'black', bg = 'white', padx = 10, pady = 10, font = 14)
staff_phone_label.grid(row = 1, column = 2)
staff_phone_entry = Entry(add_staff_frame, textvariable = staff_phone, font = 14)
staff_phone_entry.grid(row = 1, column = 3)

staff_GenderRBM = Radiobutton(add_staff_frame, text="Male", variable = staff_gender, value="Male", bg ='white', padx = 10, pady = 10, font = 14)
staff_GenderRBM.grid(row = 2, column = 0)
staff_GenderRBF= Radiobutton(add_staff_frame, text="Female", variable = staff_gender, value="Female", bg ='white', padx = 10, pady = 10, font = 14)
staff_GenderRBF.grid(row = 2, column = 1)

speciality_options = {'Weight training','Cardio workout','Strength Endurance','Spin Classes','Yoga'}
select_speciality.set('Select Speciality')

staff_speciality_label = Label(add_staff_frame, text = 'Speciality', fg = 'black', bg = 'white', padx = 10, pady = 5, font = 14)
staff_speciality_label.grid(row = 2, column = 2)
staff_speciality_entry = OptionMenu(add_staff_frame, select_speciality, *speciality_options)
staff_speciality_entry.grid(row = 2, column = 3)



#staff_speciality_choices = { 'City Center','Boucher Road','Finaghy','Lisburn','Newtownbredda'}
#.set('City Center') # set the default option

#popupMenu2 = OptionMenu(add_staff_frame, address, *staff_speciality_choices)
#Label(create_account_frame, text="Gym location",bg = 'white', padx = 10, pady = 1, font = 18).grid(row = 7, column = 0)
#popupMenu2.grid(row = 7, column =1,pady = 10)

add_staff_member = Button(add_staff_frame,text= 'Add staff member', command=create_staff,fg = 'white',bg = 'black',  font = 18, height = 1, width = 15)
add_staff_member.grid(row = 3, column = 1)

clear_staff_member = Button(add_staff_frame,text= 'Clear', command= clear_staff,fg = 'white',bg = 'black',  font = 18, height = 1, width = 15)
clear_staff_member.grid(row = 3, column = 2)



photomanagerclassesscreen = PhotoImage(file = 'Gym_logo_small.png')
photolabel8 = Label(ManagerClassesFrame, image = photomanagerclassesscreen, bg = 'light grey')
photolabel8.grid(row = 0, column = 0)

ClassesManageMemberButton = Button(ManagerClassesFrame, command= from_classes_go_to_members, text ='Members',fg = 'white', bg='black',width = 15, height = 2, font = 18)
ClassesManageMemberButton.grid(row=0,column=1)

ClassesManagerStaffButton = Button(ManagerClassesFrame, command=from_classes_go_to_staff, text ='Staff',fg = 'white', bg='black',width = 15, height = 2, font = 18)
ClassesManagerStaffButton.grid(row=0,column=2)

SettingsManagerClassesButton = Button(ManagerClassesFrame, command=from_classes_go_to_settings, text ='Settings',fg = 'white', bg='black',width = 15, height = 2, font = 18)
SettingsManagerClassesButton.grid(row=0,column=4)

ManagerClassesButton = Button(ManagerClassesFrame, command=from_classes_to_classes, text ='Classes',fg = 'white', bg='black',width = 15, height = 2, font = 18)
ManagerClassesButton.grid(row=0,column=3)

classes_tv_frame = Frame(ManagerClassesFrame)
classes_tv_frame.grid(row = 2, column = 0, sticky = 'NW', columnspan = 6)
classes_tv_frame.configure(bg = 'light grey')

clasesTV = ttk.Treeview(classes_tv_frame, height = 10, columns =('Gym Name','Day','Class name','Time','Number of People', 'Instructor'))
clasesTV.grid(row = 1, column = 0, columnspan = 30, pady = 10)

clasesTV.heading('#0', text = 'ClassID')
clasesTV.column('#0', minwidth = 0 , width =125, anchor = 'center')
clasesTV.heading('#1', text = 'Gym Name')
clasesTV.column('#1', minwidth = 0 , width =145, anchor = 'center')
clasesTV.heading('#2', text = 'Day')
clasesTV.column('#2', minwidth = 0 , width = 145, anchor = 'center')
clasesTV.heading('#3', text = 'Class name')
clasesTV.column('#3', minwidth = 0 , width = 145, anchor = 'center')
clasesTV.heading('#4', text = 'Time')
clasesTV.column('#4', minwidth = 0 , width = 105, anchor = 'center')
clasesTV.heading('#5', text = 'Number of People')
clasesTV.column('#5', minwidth = 0 , width = 145, anchor = 'center')
clasesTV.heading('#6', text = 'Instructor')
clasesTV.column('#6', minwidth = 0 , width = 145, anchor = 'center')


treeviewStyle = ttk.Style()
treeviewStyle.theme_use('clam')
treeviewStyle.configure('Treeview.Heading', background = 'light grey', foreground = 'black', rowheight = 50)




gym_name = StringVar()
class_day = StringVar()
class_name = StringVar()
time = StringVar()
select_amount_of_ppl = StringVar()
select_instructor = StringVar()

def set_classes_black():
	gym_popup_label.config(fg ='black')
	day_popup_label.config(fg ='black')
	classname_popup_label.config(fg ='black')
	time_popup_label.config(fg ='black')
	number_of_ppl_label.config(fg ='black')
	instructor_popup_label.config(fg = 'black')




def add_class():
	set_classes_black()
	add_gympopup = gym_name.get()
	add_classday_popup = class_day.get()
	add_classname_popup = class_name.get()
	add_time_popup = time.get()
	add_select_amount_ppl_popup = select_amount_of_ppl.get()
	add_select_instuctor_popup = select_instructor.get()

	if add_gympopup == 'Select Gym':
		gym_popup_label.config(fg = 'red')

	elif add_classday_popup == 'Select Day':
		day_popup_label.config(fg = 'red')

	elif add_classname_popup == 'Select Class':
		classname_popup_label.config(fg = 'red')

	elif add_time_popup == 'Select Time':
		time_popup_label.config(fg = 'red')

	elif add_select_amount_ppl_popup == 'Select amount of People':
		number_of_ppl_label.config(fg = 'red')

	elif add_select_instuctor_popup == 'Select Instructor':
		instructor_popup_label.config(fg = 'red')


	else:
		conn = sqlite3.connect('gymmembers.db')
		c = conn.cursor()
		c.execute("INSERT INTO classes VALUES (:gym_name, :class_day, :class_name, :time, :select_amount_of_ppl, :select_instructor)", 
					{
						'gym_name': gym_name.get(),
						'class_day': class_day.get(),
						'class_name': class_name.get(),
						'time': time.get(),
						'select_amount_of_ppl': select_amount_of_ppl.get(),
						'select_instructor': select_instructor.get()

					})
		gym_name.set('Select Gym')
		class_day.set('Select Day')
		class_name.set('Select Class')
		time.set('Select Time')
		select_amount_of_ppl.set('Select amount of People')
		select_instructor.set('Select Instructor')

		conn.commit()
		conn.close()
		show_all_classes()


def clear_class():
	gym_name.set('Select Gym')
	class_day.set('Select Day')
	class_name.set('Select Class')
	time.set('Select Time')
	select_amount_of_ppl.set('Select amount of People')
	select_instructor.set('Select Instructor')





def delete_gym_class_RC():

	curItem = clasesTV.focus()
	dictionary = clasesTV.item(curItem)
	print(curItem)
	print(dictionary)
	listvalues = list(dictionary.values())
	print(listvalues)
	minilist = listvalues[0]
	print(minilist)
	conn = sqlite3.connect('gymmembers.db')
	are_you_sure = messagebox.askyesno('Are you sure','Are you sure you want to delete '+ str(minilist))
	if are_you_sure == True:
		c = conn.cursor()
		c.execute("DELETE from classes WHERE rowid = (?)", (minilist,))
		
		conn.commit()
		conn.close()
		messagebox.showinfo('Data Deleted',str(minilist) +' Has been deleted Successfully')
		show_all_classes()
	elif are_you_sure == 'No':
		are_you_sure.destroy()

def delete_gym_class():
	search_item = search_class.get()
	found = False
	conn = sqlite3.connect('gymmembers.db')
	are_you_sure = messagebox.askyesno('Are you sure','Are you sure you want to delete '+ str(search_item))
	if are_you_sure == True:
		c = conn.cursor()
		c.execute("DELETE from classes WHERE rowid = (?)", (search_item,))
		
		conn.commit()
		conn.close()
		messagebox.showinfo('Data Deleted',str(search_item) +' Has been deleted Successfully')
		show_all_classes()
	elif are_you_sure == 'No':
		are_you_sure.destroy()
	#delete_gym_class_RC()
	


popupmenusclasses = Menu(classes_tv_frame, tearoff = 0)
popupmenusclasses.add_command(label = 'Delete Class', command = delete_gym_class_RC)

def do_popup_class(event):
	try:
		popupmenusclasses.tk_popup(event.x_root, event.y_root)
	finally:
		popupmenusclasses.grab_release()
clasesTV.bind("<Button-3>", do_popup_class)


def search_gym_class():
	search_item = search_class.get()
	ClassDetails = []
	found = False
	conn = sqlite3.connect('gymmembers.db')
	c = conn.cursor()

	#search_item = search


	c.execute("SELECT rowid, * FROM classes")

	reader = c.fetchall()
	for row in reader:
		if row == []:
			pass
		else:
			if search_item == row[0]:
				found = True
				ClassDetails.append(row)
				print(row)
			elif search_item == row[1]:
				found = True
				ClassDetails.append(row)
				print(row)
			elif search_item == row[2]:
				found = True
				ClassDetails.append(row)
				print(row)
			elif search_item == row[3]:
				found = True
				ClassDetails.append(row)
				print(row)
			elif search_item == row[4]:
				found = True
				ClassDetails.append(row)
				print(row)
			elif search_item == row[5]:
				found = True
				ClassDetails.append(row)
				print(row)
			elif search_item == row[6]:
				ClassDetails.append(row)
				print(row)

			else:
				print('not found')
			
			

	if found == False:
		messagebox.showinfo('Not found','The item you are serching for could not be found')
		search_class.set('')

	else:
		records = clasesTV.get_children()

		for elements in records:
			clasesTV.delete(elements)

		for row in ClassDetails:
			clasesTV.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6]))
		search_class.set('')
		conn.commit()
		conn.close()

ClassesLabelFrame = LabelFrame(ManagerClassesFrame, text = 'Edit Classes', bg = 'white', fg = 'black', padx = 102)
ClassesLabelFrame.grid(row = 3, column = 0, sticky = 'NW', columnspan = 15)

DeleteClassButton = Button(ClassesLabelFrame, command= delete_gym_class, text ='Delete Class ',fg = 'white', bg='black',width = 20, height = 1, font = 18)
DeleteClassButton.grid(row=0,column=0, pady = 10)

search_class = StringVar()
search_class_entry = Entry(ClassesLabelFrame, textvariable = search_class, font = 14, width = 20)
search_class_entry.grid(row = 0, column = 1, padx =10)

SearchClassButton = Button(ClassesLabelFrame, command= search_gym_class, text ='Search Class ',fg = 'white', bg='black',width = 20, height = 1, font = 18)
SearchClassButton.grid(row=0,column=2, pady = 10)

show_class_button = Button(ClassesLabelFrame, command = show_all_classes, text = 'Show all', bg = 'black', fg = 'white', font = 18, height = 1, width = 15)
show_class_button.grid(row = 0, column = 3, padx= 10)




add_classes_frame = LabelFrame(ManagerClassesFrame, text = 'Create Class', padx = 55, pady = 5)
add_classes_frame.grid(row = 1, column = 0, sticky = 'NW', columnspan = 15)
add_classes_frame.configure(bg = 'white')

gym_names = c.execute("SELECT gym_name FROM gyms")
gym_name.set('Select Gym')

gympopup = OptionMenu(add_classes_frame,gym_name, *gym_names)
gym_popup_label = Label(add_classes_frame, text="Gym name",bg = 'white', padx = 10, pady = 1, font = 18)
gym_popup_label.grid(row =0, column = 0)
gympopup.grid(row = 0, column =1, pady = 5)

class_days = { 'Monday','Tuesday','Wedensday','Thursday','Friday'}
class_day.set('Select Day')

daypopup = OptionMenu(add_classes_frame,class_day, *class_days)
day_popup_label = Label(add_classes_frame, text="Day",bg = 'white', padx = 10, pady = 1, font = 18)
day_popup_label.grid(row =1, column = 0)
daypopup.grid(row = 1, column =1, pady = 5)

class_names = {'Weight training','Cardio Session','Spin class','Stength Endurance','Yoga'}
class_name.set('Select Class')

class_name_popup = OptionMenu(add_classes_frame,class_name, *class_names)
classname_popup_label = Label(add_classes_frame, text="Class",bg = 'white', padx = 10, pady = 1, font = 18)
classname_popup_label.grid(row = 0, column = 2)
class_name_popup.grid(row = 0, column =3, pady = 5)

times = {'9am','10am','11am','12am','1pm','2pm','3pm','4pm','5pm','6pm','7pm'}
time.set('Select Time')

timepopup = OptionMenu(add_classes_frame,time, *times)
time_popup_label = Label(add_classes_frame, text="Time",bg = 'white', padx = 10, pady = 1, font = 18)
time_popup_label.grid(row = 1, column = 2)
timepopup.grid(row = 1, column =3, pady = 5)

number_of_ppl = {'5','10','15','20','25','30','35','40'}
select_amount_of_ppl.set('Select amount of People')

number_of_ppl_popup = OptionMenu(add_classes_frame,select_amount_of_ppl, *number_of_ppl)
number_of_ppl_label=Label(add_classes_frame, text="Number of People",bg = 'white', padx = 10, pady = 1, font = 18)
number_of_ppl_label.grid(row = 0, column = 4)
number_of_ppl_popup.grid(row = 0, column =5, pady = 5)




conn = sqlite3.connect('gymmembers.db')
c = conn.cursor()

instructor_name = c.execute("SELECT firstname_ FROM staff")
#WHERE firstname_ = (?)",(minilist,))
select_instructor.set('Select Instructor')

instructor_popup = OptionMenu(add_classes_frame, select_instructor, *instructor_name)
instructor_popup_label = Label(add_classes_frame, text="Instructor",bg = 'white', padx = 10, pady = 1, font = 18)
instructor_popup_label.grid(row = 1, column = 4)
instructor_popup.grid(row = 1, column =5, pady = 5)

add_class_button = Button(add_classes_frame,text= 'Add Class', command=add_class,fg = 'white',bg = 'black',  font = 18, height = 1, width = 15)
add_class_button.grid(row = 1, column = 6)

clear_class_button = Button(add_classes_frame, command = clear_class, text = 'Clear', bg = 'black', fg = 'white', font = 18, height = 1, width = 15)
clear_class_button.grid(row = 0, column = 6)

#CALENDER CODE
'''style = ttk.Style(addMatchFrame)
style.theme_use('clam')

cal = Calendar(addMatchFrame, selectmode="day", year=2021, month=6, background="light green",
disabledbackground="green", bordercolor="black",
headersbackground="white", normalbackground="white", foreground='black',
normalforeground='black', headersforeground='black', mindate=datetime.today())
cal.place(x=160, y=40)

cal.config(background="light green")'''


'''many_members = [
					('marco.donaghy@gmail','marco123','£10.00','17','Male','5 cricklewood','0712345678'),
					('dan@parker.com','dan123','£10.00','18','Male','4 will road','0787654321'),
					('stephan@frier.com','stephan123','£100.00','Female','21','3 twin brooke','0772484542'),
					]

conn = sqlite3.connect('gymmembers.db')
c = conn.cursor()
c.executemany("INSERT INTO login VALUES (?,?,?,?,?,?,?)", many_members)

conn.commit()
conn.close()'''



#create_login_table()
#create_staff_table()
#create_classes_table()
#create_gyms_table()
show_all_members()
show_all_staff()
show_all_classes()
raise_frame(loginframe)
root.mainloop()