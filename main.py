import sys
import json
import os




#class for a basic Customer with a account
class Customer:
    
    def __init__(self, First, Last, email = 'haider@gmail.com', Contact = 'xxx-xxx-xxxx', Transaction = "None", Transaction_type = "None", password ='1234' ):
        self.First_name = First
        self.Last_name = Last
        self.email = email
        self.Contact = Contact
        #transaction is the ammount
        self.Transaction = Transaction
        #type is the deposit or withdrawal for now
        self.Transaction_type = Transaction_type
        self.password = password
        #can i use oracle data base to store this information

    #i need to process the information
        """
        the code will start of by checking the account_info.text
        if there is a line with the person entered then it will take the balance that was initially
        on the person such as the balance check if the password is okay then change the balance in the 
        text file according to how much transaction the person want
        the person cannot withdraw more that what he/she has

        """

        """
        IF Not person found the code will make a new line with the persons information as a account
        and later the person can add or withdraw

        if the person is new he/she cannot withdraw
        """




def check():
     # Will check Ammounts in clients account
     print('NICE')
     return 0
            


def new_Clients():
     #will start account for a customer by taking 
     #FirstName, LastName, email, phone, Initial Deposit
     print('OKAT=Y')
     return 0

def Widthdraw():
     #will help withdraw if previous account exists
     print("NOOOO")
     return 0
     
def Deposit():
     #will help add ammount if account exist if not help create new account
     print("GOOD")
     return 0



# this is where the code starts
def main():
    # command line
        scriptName= sys.argv
        task = scriptName[1]
        
        
        print(task)
        task_types = {
        'Check': check,
        'New_client': new_Clients,
        'WithDraw': Widthdraw,
        'Deposit': Deposit
    }   
        
        if task in task_types:
             task_types[task]()
        else:
             print("Sorry Only", "Check", "New_client", "Withdraw", "Deposit", "available", end=" ")
        
     
         
if __name__ == "__main__":
     main()

    
        


        #  data_inside_file = file.read()
            #seperates the input as file will have, First name, lastname, email, phone no, ammount of initial deposit
        #   print(data_inside_file)
        #  parts = tuple(data_inside_file.split(","))
        #
        #  New_Client = Customer(*parts)

        # print(New_Client.balace)
            
            
