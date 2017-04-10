#Global variables
x = 0 #loop controller
key = 0
oddString = 0 #boolean to check if odd or even string




#cipher and key function:
#x is the key
#y is the right
def cipherFunction(x,y):
    x = (x*2)

    for i in range(len(y)):
        y[i] = y[i] + x

    return y

#this does the reverse of th function above
#hence the name....
def revCipherFunction(x,y):
    x=(x*2)

    for i in range(len(y)):
        y[i] = y[i] - x

    return y




while x!=5:
    print "Welcome to Dino Biel's Feistel Cipher Please Make a Selection\n"
    print "1) Encode a Message"
    print "2) Decode a Message"
    print "3) Check Encoded Message"
    print "4) Check Decoded Message"
    print "5) Exit \n"

    x = input("Make your selection:")


    if x==1:       #encode a message
        ifh = []
        ish = []
        scramble = []
        cipheredLeft = []
        cipheredRight = []
        oddString = 0


        #get message and key
        secretMessage = raw_input("What message would you like to encrypt? \n")
        key = input("Enter a key \n")

        print "How many Rounds would you like to Encrypt by?"
        numRounds = input("CAUTION: The more rounds the longer the encryption will take:")

        #split the string into two halves
        firstHalf, secondHalf = secretMessage[:len(secretMessage)/2], secretMessage[len(secretMessage)/2:]

        #turn them into char lists
        charFirstHalf = list(firstHalf)
        charSecondHalf = list(secondHalf)

        #convert to int lists for xor process
        for i in range(len(charFirstHalf)):
            ifh.append(ord(charFirstHalf[i]))

        for i in range(len(charSecondHalf)):
            ish.append(ord(charSecondHalf[i]))

        #if different len lists append 0 to make them the same
        if len(ifh) != len(ish):
            ifh.append(0)
            oddString = 1 #this means we have to delete a buffered char at the end

            for i in range(0, numRounds):
                scramble = []
                # instantiate a scramble list
                for i in range(0, len(ish)):
                    scramble.append(ish[i])

                #run cipher function
                scramble = cipherFunction(key, scramble)

                #xor values together
                #I mod by 96 because 127-32 = 96 and I want my #'s
                #between 32 and 127....hence %96 +32
                for i in range(len(ifh)):
                    ifh[i] = ((ifh[i] ^ scramble[i]) % 96)+32

                #swap for next round
                temp = ifh
                ifh = ish
                ish = temp

            #Now you are done with the cipher
            #remove buffer char

            if oddString == 1:
                #if the buffer char is in left take out
                if numRounds % 2 == 0:
                    del ifh[len(ifh)-1]
                #if the buffer char is in right take out
                else:
                    del ish[len(ish)-1]

            #convert values to ascii
            for i in range(len(ifh)):
                cipheredLeft.append(str(unichr(ifh[i])))

            for i in range(len(ish)):
                cipheredRight.append(str(unichr(ish[i])))

            for i in range(len(cipheredRight)):
                cipheredLeft.append(cipheredRight[i])

            #turn lists to string
            cipheredText = ''.join(cipheredLeft)


    elif x==2:     #decode a message
        #clear values
        key = 0
        ifh = []
        ish = []
        cipheredLeft = []
        cipheredRight = []
        oddString = 0  # boolean to check if odd or even string
        firstHalf = []
        secondHalf = []
        secretMessage = []
        charFirstHalf = []
        charSecondHalf = []


        #get message and key
        secretMessage = raw_input("What message would you like to decrypt? \n")
        key = input("Enter a key \n")

        print "How many Rounds would you like to decrypt by?"
        numRounds = input("CAUTION: The more rounds the longer the decryption will take:")

        #split the string into two halves
        firstHalf, secondHalf = secretMessage[:len(secretMessage)/2], secretMessage[len(secretMessage)/2:]

        #turn them into char lists
        charFirstHalf = list(firstHalf)
        charSecondHalf = list(secondHalf)

        #convert to int lists for xor process
        for i in range(len(charFirstHalf)):
            ifh.append(ord(charFirstHalf[i]))

        for i in range(len(charSecondHalf)):
            ish.append(ord(charSecondHalf[i]))

        #if different len lists append 0 to make them the same
        if len(ifh) != len(ish):
            ifh.append(0)
            oddString = 1 #this means we have to delete a buffered char at the end

        for i in range(0, numRounds):
            # swap for next round
            temp = ifh
            ifh = ish
            ish = temp

            scramble = []
             # instantiate a scramble list
            for i in range(0, len(ish)):
                scramble.append(ish[i])

            #run cipher function
            scramble = revCipherFunction(key, scramble)

            #xor values together
            for i in range(len(ifh)):
                ifh[i] = ((ifh[i] ^ scramble[i]))


        #Now you are done with the cipher
        #remove buffer char

        if oddString == 1:
            #if the buffer char is in left take out
            if numRounds % 2 == 0:
                del ifh[len(ifh)-1]
            #if the buffer char is in right take out
            else:
                del ish[len(ish)-1]

        #convert values to ascii
        for i in range(len(ifh)):
            cipheredLeft.append(str(unichr(ifh[i])))

        for i in range(len(ish)):
            cipheredRight.append(str(unichr(ish[i])))

        for i in range(len(cipheredRight)):
            cipheredLeft.append(cipheredRight[i])

        #turn lists to string
        cipheredText = ''.join(cipheredLeft)


        #space out menu
        for i in range(0, 30):
            print "\n"

        print ifh
        print ish


    elif x==3:     #check encode
        for i in range(0, 30):
            print "\n"

        #display cipheredText
        print "Your Ciphered text is: " + cipheredText

        #display key
        print "Your key is: ", key

        #display number of rounds
        print "Number of rounds: ", numRounds

    elif x==4:     #check decode
        for i in range(0, 30):
            print "\n"

        #display cipheredText
        print "Your Ciphered text is: " + cipheredText

        #display key
        print "Your key is: ", key

        #display number of rounds
        print "Number of rounds: ", numRounds

    elif x==5:     #exit
        print "Thank you for using Dino's Feistel Cipher\n Good Day!"
    else:
        print "invalid entry pick again!\n\n"

