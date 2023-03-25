class movie:
    def __init__(self,rows,columns):
        self.rows=rows
        self.columns=columns
        self.store_data={}
    def show_seats(self):
        print("\n*******Showing seats avilable*******")
        print("avilable seat: S\nBooked seats: B")
        k=0
        for i in range(self.rows+1):
            for j in range(self.columns+1):
                if i==0 or j==0:
                    print(" ",end=" ")
                else:
                    k+=1
                    if k in self.store_data.keys():
                        print("B",end=" ")
                    else:
                        print("S",end=" ")
            print()

    def buy_ticket(self):
        print("\n*******Buy tickets*******")
        seat_number=int(input("enter seat number:"))
        if seat_number>self.rows*self.columns or seat_number==0:
            print("\ninvalid seat number try again..!")
            obj.buy_ticket()
        elif seat_number in self.store_data.keys():
            print("\nseat already booked try another seat..!")
            obj.buy_ticket()
        else:
            print("\nenter follwing details for booking:")
            name=input("name:")
            gender=input("gender:")
            age=input("age:")
            phone=input("phone number:")
            ch=input("confirm booking(y/n):")
            if ch=="y":
                self.store_data[seat_number]=[name,gender,age,phone]
                print("\nseat number",seat_number,"booked succesfully..")
                #print(self.store_data)
            else:
                print("\nBooking cancelled..!")

    def statistics(self):
        print("\n*******Statistics*******")
        total_seats=self.rows*self.columns
        total_booked=len(self.store_data.keys())
        print("total number of seats:",total_seats)
        print("total number of seat booked:",total_booked)
        print("percentage of ticket booked:",(total_seats*total_booked)/100)
        if total_seats>60:
            total_income=((total_seats/2)*10)+((total_seats/2)*8)
            first_half_booked=0
            second_half_booked=0
            for i in self.store_data.keys():
                if i>total_seats/2:
                    second_half_booked+=1
                else:
                    first_half_booked+=1
            current_income=(first_half_booked*10)+(second_half_booked*8)
        else:
            total_income=total_seats*10
            current_income=total_booked*10
        print("current income:",current_income)
        print("total income:",total_income)
    
    def show_user_info(self):
        print("\n*******User information*******")
        check_seat=int(input("enter seat number:"))
        if check_seat not in self.store_data.keys():
            print("\nseat number",check_seat,"is not booked..")
        else:
            print("seat number:",check_seat)
            info=self.store_data[check_seat]
            print("name:",info[0])
            print("gender:",info[1])
            print("age:",info[2])
            print("phone number:",info[3])
        

rows=int(input("enter the number of rows:"))
columns=int(input("enter the number of seats in each row:"))
obj=movie(rows,columns)
while 1:
    print("\nMENU\n1. Show the seats\n2. Buy a ticket\n3. Statistics\n4. Show booked ticket User Info\n0. Exit")
    choice=int(input("enter your choice:"))
    match choice:
        case 0:
            print("\nThank you...\n")
            exit(0)
        case 1:
            obj.show_seats()
        case 2:
            obj.buy_ticket()
        case 3:
            obj.statistics()
        case 4:
            obj.show_user_info()
        case _:
            print("\ninvalid input..!")
    
