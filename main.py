fullname = input("Welcome, please enter your full name: ")
email = input("And your email as well: ")
user = open('details.txt', 'w')
user.write("Full-names: " + fullname)
user.write("\nemail: " + email)
user.close()

input = input("Do you want to see the contents: ")
if input == "yes":
    users = open('details.txt', 'r')
    details = users.read()
    print(details)
    users.close()
else:
    print("Tough luck to you, chump")