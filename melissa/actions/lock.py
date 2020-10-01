#when i saw your actions, i realised you added some confidential actions like your jarvis can find iphones, so anyone can trace it so your code has to be more secure. so i add tis file . I hope you like it



import getpass





CorrectUsername = "Lucifer"
CorrectPassword = "Lucifer007"

loop = 'true'
while (loop == 'true'):
    username = raw_input("Please enter your username: ")
    if (username == CorrectUsername):
    	password = raw_input("Please enter your password: ")
        if (password == CorrectPassword):
            print( "Logged in successfully as " + username)
            loop = 'false'
        else:
            print( "Password incorrect!")
    else:
        print ("Username incorrect!")
