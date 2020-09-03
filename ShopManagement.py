import pymysql

def Display():
    try:
        ##Display all Order List
        connection = pymysql.connect(host="localhost", user="root", password="", database="mydb")
        cursor = connection.cursor()
        select1 = "SELECT * FROM ITEM;"
        cursor.execute(select1)
        rows = cursor.fetchall()
        for row in rows:
          print(row)

        connection.commit()
        connection.close()
    except:
        print("Please make Connection with XAMPP!")


def AmountUpdate():
    try:
        ##Display the Order List Which has AMOUNT=0
        connection = pymysql.connect(host="localhost", user="root", password="", database="mydb")
        cursor = connection.cursor()


        mark='y'
        while(mark=='y'):
            select1 = "SELECT * FROM ITEM WHERE AMOUNT=0;"
            cursor.execute(select1)
            rows = cursor.fetchall()
            check=[]
            if(rows!=()):     
                for row in rows:
                  print(row)
                  check.append(row[0])

                
                try:
                    #Asking the User that which Order You want to Update
                    OrderNo=int(input("Mention the Order Number You want to Update: "))
                    UpdatedAmount=int(input("Please enter Final Amount: "))
                except:
                    print("WRONG DATA TYPE!")

                if OrderNo in check:      #to check either the OrderNo is present or not which is in check variable   
                    # Updating the Amount
                    Update1="UPDATE ITEM SET AMOUNT = %s WHERE ID = %s;"
                    Update2 = (UpdatedAmount, OrderNo)
                    cursor.execute(Update1,Update2)
                else:
                    print("INVALID Order Number!")
                mark=input("Press y to CONTINUE and any key to EXIT: ")
            else:
                print("No Oreders to Display!")
                mark='n'
            
       
        connection.commit()
        connection.close()
        print("AMOUNT UPDATED SUCCESSFULLY")
    except:
        print("Please make Connection with XAMPP!")


def DeliveryUpdate():
    ##Display the Order List Which has DELIVERY STATUS='NO'

    mark='y'
    while(mark=='y'):
        try:
            ##Display the Order List Which has DELIVERY STATUS='NO'
            connection = pymysql.connect(host="localhost", user="root", password="", database="mydb")
            cursor = connection.cursor()
            select1 = "SELECT * FROM ITEM WHERE DELIVERY='No' AND NOT AMOUNT=0;"
            cursor.execute(select1)
            rows = cursor.fetchall()
            check=[]
            if rows!=():
                for row in rows:
                  print(row)
                  check.append(row[0])
                try:
                    #Asking the User that which Order You want to Update
                    OrderNo=int(input("Mention the Order Number You want to Update: "))
                except:
                    print("Incorrect DATA TYPE!")


                if OrderNo in check:
                    DeliveryStatus=input("Press 1 to Confirm: ")
                    if(DeliveryStatus=='1'):
                        # Updating the Delivery
                        Update1="UPDATE ITEM SET  DELIVERY='Yes' WHERE ID = %s;"
                        Update2 =(OrderNo)
                        cursor.execute(Update1,Update2)          ##Database work as what to do then where to do so in execution line first we put query of doing then which query to do
                    else:
                        print("Confirmation not Provided!")
                    
                else:
                    print("Order not found!")
                mark=input("Press y to CONTINUE and any key to EXIT: ")
                        
            else:
                print("No Order to Display!")
                mark='n'
            connection.commit()
            connection.close()
            print("DELIVERY UPDATED SUCCESSFULLY")  ##Giving message of update status
        except:
            print("Please make Connection with XAMPP!")
    


##Work of Businesman Starts from this Function
def Business():
    Entry=input("Press 1 to Display Order\nPress 2 for Amount Update\nPress 3 for Update Delivery: ")
    if(Entry=='1'):
        Display()    ##Display all Order List
    elif(Entry=='2'):
        AmountUpdate()    ##Display Only those Order which has AMOUNT=0
    elif(Entry=='3'):
        DeliveryUpdate()   ##Display Only those Order Which has DELIVERY STATUS='NO'
    else:
        print("INVALID INPUT")
        
    
    

##If Choice=1 then this function will help the Costomer in Ordering with her/his Detailed record
def PlaceOrder():
    #Asking Customer Detail
    Name=input("Please enter your Name: ")
    Mob=input("Please enter your Mobile number: ")
    Address=input("Please enter your Address: ")
    OrderList=input("Please enter your Order List: ")
    #Default Value
    Amount=0
    Delivery='No'   
    #Database work
    try:
        connection = pymysql.connect(host="localhost", user="root", password="", database="mydb")         ##Making Connection with Database
        cursor = connection.cursor()
        #Insert Query
        insert1 = "INSERT INTO ITEM (NAME, PHONE, ADDRESS, ITEMS, AMOUNT, DELIVERY) VALUES (%s,%s,%s,%s,%s,%s);"
        insert2= (Name, Mob, Address, OrderList, Amount, Delivery)
        cursor.execute(insert1,insert2)                                                                    ##Executing the Query
        connection.commit()
        connection.close()                                                                                 ##Closing Database work
        print("Oreder Successfully Placed!")##Giving Confirmation message Of Order Placed
    except:                                  ##For Error detection
        print("Please Connect with XAMPP!")

#If Choice=2 then for Businessman
def Login():
    Password=input("Please enter your Password: ")
    if(Password=="Rakesh123"):
        print("WELCOME")
        ##This function for Businessman work
        Business()
    else:
        print("UNAUTHORIZED")


##Program Body

#Name of Program         
print("-"*20,"SHOP MANAGEMENT","-"*20)
#Giving Choice to User
Choice=input("Press 1 if you are Customer\nPress 2 if you are a Businessman: ")

if(Choice=="1"):
    PlaceOrder()


elif(Choice=="2"):
    Login()


else:
    print("INVALID INPUT")
