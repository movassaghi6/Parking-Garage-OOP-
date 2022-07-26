class parkingGarage:

    def __init__(self, tickets , parkingSpaces, currentTicket):
        self.tickets = tickets #list
        self.parkingSpaces = parkingSpaces #list
        self.currentTicket = currentTicket #dictionary {space# : paid/unpaid}


    #method1
    def taketicket(self):
        if len(self.tickets) == 0:
            print("we're full get lost!")
        else:
            open_stall = self.tickets.pop(0)


            print(f"Go to your spot now: Stall #{open_stall}. Lock your doors! We are not liable for losses/damages.")
            if self.currentTicket == {}:
                print(" You've got the VIP spot.")
            else:
                print(self.currentTicket)


            self.parkingSpaces.append(open_stall)
            self.currentTicket[open_stall] = "unpaid"
            
    #Method2
    def payforParking(self):

        open_stall = int(input("what number space are you in? "))
        if len(self.parkingSpaces) == 0 :
            print("Uhhh..try parking first.")
            return

        if open_stall not in self.parkingSpaces:
            print(" Gimme your space number foo. ")
            return

        if self.currentTicket[open_stall] == "paid":
            print('You paid already. what are you a wise guy?')
        else:
            print("You've got to pay to play.")
            pay = input("Please type 'Y' to pay")



            if pay.lower() == 'y':
                self.currentTicket[open_stall] = "paid"
                print(f'Guy, your ticket has been {self.currentTicket[open_stall]}. Leave in 15 minutes or that ride is OURS. ')



    #Method3
    def leaveGarage(self):

        paid_space = int(input("Enter the parking space number of your ticket: "))
        if len(self.parkingSpaces) == 0:
            print("You need to park first!!")
            return

        elif paid_space not in self.parkingSpaces:
            print("What's your space number? We don't got all day...")

        elif self.currentTicket[paid_space] == 'paid':
            self.parkingSpaces.remove(paid_space)
            self.tickets.append(paid_space)
            self.tickets.sort()
            del self.currentTicket[paid_space]
            print("Thank you, safe travels :) now GET OUTTA HERE.\n")

        else:
            command = input("I see you tryna dip out of here without paying. Pay uo: yes/no ")
            if command.lower() == "no":
                print("You trying to live here?\n")

            elif command.lower() == "yes":
                self.payforParking()


# ([tickets],[parking_spaces],{current tickets: {parking ticket number : paid/unpaid}})
parking_stalls = [1,2,3,4,5,6,7,8,9,10]
kourteous = parkingGarage(parking_stalls , [] , {})



def run():

    while True:
        do = input("Welcome to the one and only KOURTEOUS Parking Garage. What do you want?! park/Pay/Leave/Quit ")
        if do.lower() == 'quit':
            print("DEUCES!")
            break
        elif do.lower() == 'park':
            kourteous.taketicket()
        elif do.lower() == 'pay':
            kourteous.payforParking()
        elif do.lower() == 'leave':
            kourteous.leaveGarage()
        else:
            print("???")


run()
        
            
