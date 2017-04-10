#######
p = 17
q = 11
r = (p-1)*(q-1)
n = p * q
e = 7
d = 23
messageInt = []
cmessageInt = []
changed =[]
cText =""

x = 0

while x != 3:
    print "============================="
    print "Welcome to Dino's RSA Cipher!"
    print "============================="
    print "Please Choose from the following:"
    print "1) Encrypt a Message"
    print "2) Decrypt a Message"
    print "3) Exit"

    x = input("Enter your selection: ")


    #Encrypt
    if x == 1:
        message = raw_input("Enter your message to Encrypt: ")

        #convert to array
        message = list(message)

        #convert message to int
        for i in range(len(message)):
            messageInt.append(ord(message[i]))
            changed.append(0)


        #Encrypt message block
        for i in range(len(message)):
            messageInt[i] = (messageInt[i]**e) % n

        #error handling (make it convert to a char not gibberish)
        for i in range(len(messageInt)):
                if messageInt[i]%2==1:
                    messageInt[i]+=1
                    changed[i]=1

                messageInt[i] += 32
                messageInt[i]/=2

        #convert to chr
        for i in range(len(message)):
            messageInt[i] = chr(messageInt[i])


        #make string
        cText = ''.join(messageInt)

        #print output
        print "Your Ciphered Text is: ", cText
        print "Lock#1: ", e, "Lock #2: ", n

    #Decrypt
    if x == 2:

        #Take input from user:
        cmessage = raw_input("Enter your message to Decrypt: ")

        #check lock
        l1 = input("Enter lock 1: ")
        l2 = input("Enter lock 2: ")

        while (((l1*d)%r)!=1):
            print "Wrong lock try again!"
            #check lock
            l1 = input("Enter lock 1: ")
            l2 = input("Enter lock 2: ")

        #convert to array
        cmessage = list(cmessage)

        #convert message to int
        for i in range(len(cmessage)):
            cmessageInt.append(ord(cmessage[i]))

        # error handling (make it convert to a char not gibberish)
        for i in range(len(cmessageInt)):
            cmessageInt[i] *=2
            cmessageInt[i] -= 32
            if changed[i] == 1:
                cmessageInt[i] -= 1


        #Decypher block
        for i in range(len(cmessage)):
            cmessageInt[i] = (cmessageInt[i]**d) % l2

        #=strip L
        for i in range(len(cmessage)):
            cmessageInt[i] = str(cmessageInt[i])
            cmessageInt[i] = int(cmessageInt[i])

        # convert to chr
        for i in range(len(cmessage)):
            cmessageInt[i] = chr(cmessageInt[i])

        # make string
        cText = ''.join(cmessageInt)

        # print output
        print "Your deciphered Text is: ", cText

    #Exit
    if x == 3:
        print "Thank you for using my cipher"
        print "See you next time!"