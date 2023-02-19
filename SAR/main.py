#opening account informaiton
#Asking for input to copy and paste information into the SAR report narrative
date = input("date: ")
name = input("name: ")
address = input("address: ")
account = input("account: ")
branch = input("branch: ")
branchaddress = input("branch address: ")

print("On {}, {}, {}, opened BOTW checking account #{} at, BOTW {}.".format(date, name, address, account, branch, branchaddress))


#check
#taking the elements of the check and generating a sentence to paste into the SAR report narrative
date = input("date: ")
amount = input("amount: ")
check_number = input("check number: ")
drawn_on_bank = input("Drawn on Bank: ")
drawn_on_bank_address = input("Drawn on Bank Address: ")
payable = input("Payee: ")
account_type = input("Account Type: ")
account_number = input("Deposit Account Number: ")
branch_name = input("Branch Name: ")
branch_address = input("Branch Address: ")


print("On {}, check #{} for ${}, drawn on {}, {}, payable to {} was deposited into {}'s BOTW {} account {} at the BOTW {} branch, {}".format(date, check_number, amount, drawnonbank, drawn_on_bank_address, payable, payable, account_type, account_number, branch_name, branch_address))
      
