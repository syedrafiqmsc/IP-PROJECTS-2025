# imports--------------------- 

import mysql.connector as c
import csv

# OUT OF SYLABUSS (～￣▽￣)～

import smtplib, ssl
import os
import time

# Functions--------------------

def main():                                                                 # This is the main function and is where the program
    print ("Choose Category".upper())                                       # starts from.
    print("---------------")                                                # The main categories
    print("1. FOOD")
    print("2. CUSTOMER")
    print("3. EXIT")
    choice = enter_correct("Enter The Option: ",1)
    if choice==1:
        food()
    elif choice==2:
        customer()
    elif choice==3:
        print("Are You sure to exit?")
        dump=enter_correct("Enter Y : ")
        if (dump.upper()).strip()=='Y':
            del choice
            exit("Succesfully exited program")
            

# Food -----------------------------

def food():                                                                  # Function deals with all functions that alter the
    while True:                                                              # table food and its contents
        print("\n")
        print("FOOD")
        print("---------")
        print("Options:")
        print("1. Add Food Details ")
        print("2. Delete Food Details ")
        print("3. Update Food Details ")
        print("4. Display Food items ")
        print("5. Search Food Details ")
        print("6. Back")
        choice = enter_correct("Choose the option: ",1)
        if choice == 1:
            add()
        elif choice == 2:
            x=enter_correct("Fno: ",1)
            delete(x)
        elif choice == 3:
            update(enter_correct("Enter Food ID: ",1)  )
        elif choice ==4:
            display()
        elif choice == 5:
            search(enter_correct("Enter Food No or Food Name: ",1))
        elif choice == 6:
            main()
        else:
            del choice
            print("\n--------------\nInvalid Option\n--------------")

#---------------------------------

# Customer -----------------------

def customer():                                                               # Function deals with all things related to the customer
    while True:                                                               # and the billing of his order.
        print("\n")
        print("CUSTOMER")
        print("---------")
        print("1. Add Customer Details And Bill Details")
        print("2. View Details")
        print("3. Back")
        ch = enter_correct("Enter Option: ",1)
        if ch==1:
            customs(enter_correct("Enter the name of the customer: "))
        elif ch==2:
            customs_read()
        elif ch==3:
            main()
        else:
            del ch
            print("\n--------------\nInvalid Option\n--------------")

#----------------------------

# Patent Pending ヾ(≧▽≦*)o-------------------


def enter_correct(var_msg,var=0):                                             # This function prevents the program from crashing
    val = input(var_msg)                                                      # with any errors that occur in the program it solves
    if var==1:                                                                # them, or returns to the main program.
        try:                                                                  # This is also a failsafe to abort the current action
            if (val.lower()).strip() == 'quit':                               # and return to the main program.
                print("\n------------------------")
                print("Aborting Current Process")
                time.sleep(1)
                print("Returning To Main Program")
                print("------------------------\n")
                time.sleep(1)
                main()
            val = int(val)
        except ValueError:
            print("\n--------------\nInvalid Option\n--------------\n")
        return val
        del val
    else:
        if (val.lower()).strip() == 'quit':
            print("\n------------------------")
            print("Aborting Current Process")
            time.sleep(1)
            print("Returning To Main Program")
            print("------------------------\n")
            time.sleep(1)
            main()
        return val
        del val

#-------------------------------

# Add------------------------------

def add():                                                                    # This function helps us add a new food item to the
    x = enter_correct("Enter Food ID: ",1)                                    # table, it checks the wether a simmilar entry exists or
    if x=="":
        time.sleep(1)
        food()
    cur.execute("select fno from food;")                                      # not,and if not gives us an option to add it to the
    l = cur.fetchall()
    lastno = l[-1][0]+1
    for i in l:                                                  # food menu.
        if x == i[-1]:
            print("\nThis ID Already Exists\n")
            time.sleep(1)
            print(f"Try {lastno}")
            time.sleep(2)
            food()
                    
    y = enter_correct("Enter Food Name: ")
    z = enter_correct("Enter Food Type: ")
    w = enter_correct("Enter Price: ",1)
    cur.execute("insert into food values({},'{}','{}',{});".format(x, y, z,w))
    con.commit()
    del (x,y,z,w)
    print("Success")
    time.sleep(2)

# ------------------------------

# Delete -----------------------------

def delete(fno):                                                              # This function deals with the deletion of a food record
    try:
	    cur.execute(f"select * from food where fno = {fno};")                     # from the menu.
    except:
	    food()
    name=cur.fetchall()
    waste = enter_correct(f"Are you sure you want to delete \n{name[0]}\n Press to confirm press y: ".title())
    if waste.upper() == "y":
        cur.execute("delete from food where fno = {};".format(fno))
        con.commit()
    del (waste,name)
    print("Success")
    time.sleep(2)

#-----------------------------

# Display ------------------------------

def display():                                                                # Displays the entire menu of restaurant.
    print("\n")
    dash = 0
    cur.execute("select * from food")
    na = cur.fetchall()
    if len(na) == 0:
        print("""
                        _____________________
                      /                 `   |
                      |  .-----------.  |   |-----.
                      |  |           |  |   |-=---|
                      |  | No one    |  |   |-----|
                      |  | Found  !  |  |   |-----|
                      |  |           |  |   |-----|
                      |  `-----------'  |   |-----'/|
                       \________________/___'     /  |
                          /                      / / /
                         / //               //  / / /
                        /                      / / /
                       / _/_/_/_/_/_/_/_/_/_/ /   /
                      / _/_/_/_/_/_/_/_/_/_/ /   /
                     / _/_/_/_______/_/_/_/ / __/
                    /______________________/ /    
                    \______________________\/
                    """)
        food()

    print("The following details will be printed out in the following maner:\n")
    print("FOOD ID \t FOOD NAME \t Type \t Price".upper())
    print("---------------------------------------")
    for i in na:
        print("\n", end="")
        for j in i:
            print(j, end="     |     ")
            dash += len(i)
        print("\n")
        print("---------------------------------------------------------------------------")
    else:
        print("That's folks!")
    del (dash,na)
    print("Success")
    time.sleep(2)

#------------------------------

# Search ---------------------------

def search(f_info):
    try:
	    cur.execute("select * from food where fno like '%{}%' or fname like '%{}%';".format(f_info,f_info))
    except:
	    food()
    if len(cur.fetchall())==0:                                                   # This function helps to search for a specific food
        print("\n")                                                              # item and if it doesn't exist,
        print("Invalid Search Query Or List Is Empty.")                          # it informs the user and returns to the previous menu.
        print("If Not, Try Checking The Spelling Or The Food Number")
        time.sleep(1)
        print("returning to previous menu\n".title())
        time.sleep(1)

    else:
        cur.execute("select * from food where fno like '%{}%' or fname like '%{}%';".format(f_info,f_info))
        print("\n")
        for i in cur.fetchall():
            for j in i:
                print(j, end=" ")
            print("\n")
    con.commit()
    print("Success")
    time.sleep(2)

#------------------------------

# Update------------------------------

def update(fno):                                                                 # Update function helps with the updation of a food item
    x=0                                                                          # in the menu.
    try:
        cur.execute(f"select * from food where fno like {fno};")
        x = cur.fetchall()
    except:
        food()
    if len(x) == 0:
        print("\n")
        print("Invalid Search Query Or List Is Empty.")
        print("If Not, Try Checking The Food Number")
        time.sleep(2.5)
        print("returning to previous menu\n".title())
        time.sleep(1)
        food()
    for i in x:
        print("\n\nSure you want to update this entry: ")
        print(i)
    ch = enter_correct("Enter y to continue: ")
    if ch.lower() == 'y':
        pass
    else:
        print("\n\nReturning Back")
        food()
    fname = enter_correct("Enter Food Name: ")
    ftype = enter_correct("Enter Food Type: ")
    price = enter_correct("Enter Price: ",1)
    cur.execute(f"update food set fname='{fname}',type='{ftype}',price={price} where fno={fno};")
    con.commit()
    del (x,ch,fname,ftype,price)
    print("Success")
    time.sleep(2)

#--------------------------------

# Customer Relations --------------------


def customs(customer_name):                                                   # This function deals with creating a log of
    with open('customer.csv', newline='', mode='r') as file2:                 # customer details, order info, the time
        row_count = len(list(csv.reader(file2, delimiter=","))) + 1           # and date of the transaction. This log
        file2.close()                                                         # is kept as a simplified copy of the bill,
    with open('customer.csv',newline='',mode='a+') as file:                   # usualy for the restraunt owner. This log
        writer = csv.writer(file)                                             # file is a csv file, that can be easily
        t = time.localtime()                                                  # indexed and analysed by restraunt owner.
        current_time = time.strftime("%I:%M:%S %p , %d/%m/%Y", t)                           # recording the time
        the_bill={}                                                                         # initialising the bill
        num=enter_correct("Enter The Phone Number Of The Customer: ",1)
        if enter_correct(f"Proceed Billing Of {customer_name}: ").lower()!='y':
            customer()
        else:
            while True:
                fno = enter_correct("Enter Food Number: ", 1)
                if fno == 0:
                    break
                if fno=='':
                    pass
                else:
                    try:
                        cur.execute(f"select * from food where fno like {fno};")
                        res = cur.fetchall()
                    except c.errors:
                        pass
                    if len(res) != 0:
                        print('\n', res[0], '\n')
                        qun = enter_correct("Enter quantity: ", 1)
                        the_bill[res[0][0]] = [qun,res[0][1],res[0][2],res[0][3]]
                    else:
                        print("\n")
                        print("Invalid Search Query Or List Is Empty.")
                        print("If Not, Try Checking The Food Number")
                        time.sleep(2.5)
        if enter_correct("Is This Order A Parcel?: ").lower()=='y':
            parcel=True
        else:
            parcel=False
        billprint(the_bill,customer_name,num,parcel)
        writer.writerow([row_count,current_time,customer_name,num,the_bill])
        del (row_count,current_time,customer_name,num,the_bill,qun,fno,res)
        print("Success")
        time.sleep(2)

#-----------------------------

# Printing Of The Bill ----------------------------

def billprint(bill,name,num,parcel):                                                          # This function is used to print the bill according to
    global names                                                              # the above done entries in a structural manner
    cur.execute("select fname from food;")
    try:
        names=cur.fetchall()
    except c.errors:
        print("nothing")
        customer()
    x = 0
    for i in names:
        for j in i:
            if len(j) > x:
                x = len(j)

    Body=str('-' * (x + 40))+'\n'
    Body+=str('|' + "LA KOCHI".center(x + 38) + '|')+'\n'
    Body+=str('-' * (x + 40))+'\n'
    Body += ("| Customer Name" + " " * (x + 22-len(name)) + f"{name}  |") + '\n'
    Body += ("| Customer Number" + " " * (x + 20 - len(str(num))) + f"{num}  |") + '\n'
    Body += str('-' * (x + 40)) + '\n'
    Body+=str("| Slno    Food name" + " " * (x - 7) + "Qty    Unit Price    Price |")+'\n'
    Body += str('-' * (x + 40)) + '\n'
    l = []

    for i in bill.keys():
        cur.execute(f"select price from food where fname=\"{bill[i][1]}\";")
        Food_Name = str(bill[i][1]) + " " * (x + 1 - len(bill[i][1]))
        Unit_Price = cur.fetchall()[0][0]
        Final_Price = Unit_Price * (bill[i][0])
        l.append(Final_Price)
        Unit_Price = str(Unit_Price) + " " * (13 - len(str(Unit_Price)))
        Final_Price = str(Final_Price) + " " * (6 - len(str(Final_Price)))
        Quantity = str(bill[i][0]) + " " * (6 - len(str(bill[i][0])))
        Body+= f"| {i}{' ' * (7 - len(str(i)))} {Food_Name} {Quantity} {Unit_Price} {Final_Price}|\n"

    total = 0

    for j in l:
        total += j

    Body+=('-' * (x + 40))+'\n'
    Body+=("| total" + " " * (x + 30 - len(str(total))) + f"{total}  |")+'\n'
    Body += ("| CGST" + " " * (x + 28) + f"8 %  |") + '\n'
    Body += ("| SGST" + " " * (x + 28) + f"8 %  |") + '\n'
    total += 2 * (total * (8 / 100))
    if parcel:
        total+=50
        Body += ("| PARCEL" + " " * (x + 26) + f"50   |") + '\n'
    Body +=('-' * (x + 40))+'\n'
    Body += ("| GRAND total" + " " * (x + 17 - len(str(round(total, 2)))) + f"{round(total, 2)} Rupees  |") + '\n'
    Body += ('-' * (x + 40)) + '\n'
    Body += ('-' * (x + 40)) + '\n'
    Body+=("| HOPE YOU HAVE A WONDERFUL DAY AHEAD (*^v^*)" + " " * (x - 6) + '|')+'\n'
    Body+=('-' * (x + 40))+'\n'

    print(Body)

    # Mail -----------------------------------------

    ask=enter_correct("\nDo you Want the bill to be mailed to you?: ")

    if (ask.upper()).strip()=='Y':
        mailid=enter_correct("Please Enter Your Email ID: ")
        mail(mailid,Body)
    del (bill,name,num,parcel,Body,ask,total,mailid,Food_Name,Quantity,Unit_Price,Final_Price)
    time.sleep(2)

#-----------------------------

# Customer Info Logging -------------------------

def customs_read():                                                           # Function helps to read the bill log on the hard disk
    with open('customer.csv',newline='',mode='r') as file:                    # of the computer. (customer.csv)
        reader = csv.reader(file)
        if os.stat('customer.csv').st_size > 0:
            pass
        else:
            print("\n\nempty file".title())
            customer()
        for i in reader:
            print(i[1])
            print(i[2])
            print(i[3])
    del reader
    print("Success")
    time.sleep(2)

                                                               #nice
#-----------------------------

# Connector ------------------------------

con = c.connect(host="localhost", user="root", passwd="tiger", database="ZLI3GiQekn")
cur = con.cursor()

#-----------------------------

# Mailing Of Bills -----------------------

def mail(email_id,bill):                                                      # This function will sent the bill to the intended
    port = 465  # For SSL                                                     # recipient's email id, if requested
    smtp_server = "smtp.gmail.com"
    sender_email = "thelakochi@gmail.com"  # Enter your address
    receiver_email = str(email_id)  # Enter receiver address
    password = "thelakochi"
    message = f"""\
    Bill Recipt From The La Kochi Hotel ^_^

    {bill}"""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    del (port,smtp_server,sender_email,email_id,bill,receiver_email,context)

#-----------------------------

# This is the introduction part of the program
# All below include the part of the design

print("""

    █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀
    █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░
    
    █░░ ▄▀█   ▄▄   █▄▀ █▀█ █▀▀ █░█ █
    █▄▄ █▀█   ░░   █░█ █▄█ █▄▄ █▀█ █
""")
print("""
       __                        @@;,                {_}
      (  ;          ?           :  );                |(|
     _| |_  |  |   ||  |  |     _| |_                |=|
    |  \  \  \/    ||   \/ ___ /  /  |              /   |
  __|   |\ __||____||___||______/|   |              |.--|
  |||   | |_______    _________| |   |||            ||  |
  |||   |____     |   |      ____|   |||            ||  |    .    ' .    
  \ \______  )    |   |     /  ______/ /            |'--|  '     \~~~/
   ||    | | |    |   |    /___|     ||             '-=-' \~~~/   \_/  
   ||    | | |_  /| | |\   _| ||     ||                    \_/     Y
   ||    | \__, / | | |  \<__/ |     ||                     Y     _|_
                                                           _|_       
""")
# This is very important---
while True:
    print("""\n------------------------------------------------------------------------------------------------------\n""")
    main()
