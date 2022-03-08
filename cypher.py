""" imports """
from queue import Empty
import random
import sys
from time import sleep

""" globals """
user = input('\nEnter your identity: ')
err = '\nERROR! ENTER VALID INPUT ...'
gen = '\nERROR! GENERATE A KEY FIRST USING (N)EW KEY'
confirm = '\nConfirm identity to proceed: '
mismatch = '\nERROR! IDENTITY MISMATCH'
redirect = '\nRedirecting back to Menu ...'
exit = f'\nThank you for using cypher.py! We had a great time working with you {user.upper()}!\n'


start = 32
end = 126

shuff1 = []
shuff2 = []
enc = []
dataList = []
cypherList = []
ref_list = []
key_list = []

""" methods """
def run():
    welcome()


def writer(text):
    for char in text:
        sleep(0.10)
        sys.stdout.write(char)
        sys.stdout.flush()


def welcome():
    initialize = '\nInitializing cypher.py ...'
    welcome = f'\nWelcome {user.upper()}! 🦄'

    writer(initialize)
    writer(welcome)

    choice = '\n\n(A)lready have a Ref./Key? or (N)ew?\n\n** Press (V)iew to check content & -1 to terminate cypher.py  at any time in the Menu **'
    writer(choice)
    ch = input('\nEnter: ')
    match ch.upper():
        case 'A':
            cypher_ref_key()
        case 'N' | 'V':
            prompt = '\nLets get started with the process\nWhat do you wanna start with ...\n\n1) (N)ew Key\n2) (G)et Key\n3) (E)ncrypt\n4) (D)ecrypt'
            writer(prompt)      
            menu()   
        case '-1':
            writer(exit)
            sys.exit()
        case _:
            writer(err)
            writer(redirect)
            menu()

def cypher_ref_key():
    n = 2
    start = '\nLets get started with the process ...'
    writer(start)
    
    ref = '\n\nEnter the Reference: \n'
    writer(ref)
    ref_data = input()
    ref_list[:] = ref_data

    key = '\nEnter the Key: \n'
    writer(key)
    key_data = input()
    key_list = [key_data[i:i+n] for i in range(0, len(key_data), n)]

    cy = '\n\nEnter the cyphered data: \n'
    writer(cy)
    cyphered_data = input()
    
    dec_data = ""
    cypherList = [cyphered_data[i:i+n] for i in range(0, len(cyphered_data), n)]
    for item1 in cypherList:
        for item2 in key_list:
            if item1 == item2:
                idx = key_list.index(item2)
                val = str(ref_list[idx])
                dec_data = dec_data + val
                break
    
    writer(confirm)
    identity = input()
    if identity == user:
        success = f'\nCongratulations {user.upper()}! Your data has been decyphered successfully ...\n\n'
        writer(success)
        print(dec_data)
    else:
        writer(mismatch)
    
    cypherList.clear()
    writer(redirect)
    menu()
    

    
def menu():
    choice = input('\n\nEnter: ')
    match choice.upper():
        case 'N':
            newkey()
        case 'G':
            getkey()
        case 'E':
            encrypt()
        case 'D':
            decrypt()
        case 'V':
            opts = '\n\n1) (N)ew Key\n2) (G)et Key\n3) (E)ncrypt\n4) (D)ecrypt'
            writer(opts)
            menu()
        case '-1':
            writer(exit)
            sys.exit()
        case _:
            writer(err)
            writer(redirect)
            menu()
            

def newkey():
    key = f'\nWait while we generate a Key for you ... ... ... ... ... ...'
    writer(key)

    shuff1.clear()
    enc.clear()

    counter = start
    while(counter <= end):
        shuff1.append(chr(counter))
        counter += 1

    random.shuffle(shuff1)
    shuff2 = list(shuff1)
    shuff2.reverse()
    random.shuffle(shuff2)

    i, limit = 0, len(shuff1)
    while i < limit:
        enc.append(shuff1[i]+shuff2[i])
        i +=1
    enc.reverse()
    random.shuffle(enc)

    success = '\nYour Key has been generated successfully! Press (G)et Key to retrieve ...'
    writer(success)
    menu()

def getkey():
    if enc == Empty or shuff1 == Empty:
        writer(gen)
        menu()
    else:
        writer(confirm)
        identity = input()
        
        if identity == user:
            writer('\nReference:\n')
            print("".join(shuff1))          # reference
            # print(shuff1)                   # reference
            writer('\n\nKey:\n')
            print("".join(enc))             # key
            # print(enc)                      # key
            key = '\n\nYour Ref. & Key has been generated above\nPress (E)ncrypt to start cyphering ...'
            writer(key)
        else:
            writer(mismatch)
            writer(redirect)
        
        menu()


def encrypt():
    if enc == Empty or shuff1 == Empty:
        writer(gen)
        menu()
    else:
        enter = '\nEnter your data below to start encryption ...\n'
        writer(enter)
        data = input()

        wait = '\nWait while we encrypt your data ... ... ... ... ... ...\n'
        writer(wait)

        enc_data = ""
        dataList[:] = data
        for item1 in dataList:
            for item2 in shuff1:
                if item1 == item2:
                    idx = shuff1.index(item2)
                    val = str(enc[idx])
                    enc_data = enc_data + val
                    break

        writer(confirm)
        identity = input()
        if identity == user:
            success = f'\nCongratulations {user.upper()}! Your data has been encrypted successfully ...\n\n'
            writer(success)
            print(enc_data)

            choice = "\n\nPress (D)ecrypt to start decrypting or -1 to terminate cypher.py"
            writer(choice)
        else:
            writer(mismatch)
            writer(redirect)
        
        menu()
        

def decrypt():
    if enc == Empty or shuff1 == Empty:
        writer(gen)
        menu()
    else:
        enter = '\nEnter your data below to start decrypting ...\n'
        writer(enter)
        cypher_data = input()

        wait = '\nWait while we dencrypt your data ... ... ... ... ... ...\n'
        writer(wait)


        n = 2
        dec_data = ""
        cypherList = [cypher_data[i:i+n] for i in range(0, len(cypher_data), n)]
        for item1 in cypherList:
            for item2 in enc:
                if item1 == item2:
                    idx = enc.index(item2)
                    val = str(shuff1[idx])
                    dec_data = dec_data + val
                    break

        writer(confirm)
        identity = input()
        if identity == user:
            success = f'\nCongratulations {user.upper()}! Your data has been dencrypted successfully ...\n\n'
            writer(success)
            print(dec_data)
        else:
            writer(mismatch)
        
        cypherList.clear()
        writer(redirect)
        menu()


""" testing """
run()