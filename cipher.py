symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
maxKeySize = len(symbols)

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt or brute-force a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd', 'brute', 'b']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b"')

def getMessage():
    print('Enter your message')
    return input()

def getKey():
    key = 0
    while True:
        print(f'Enter the key number (1-{maxKeySize})')
        key = int(input())
        if (key >= 1 and key <= maxKeySize):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key

    translated = ''

    for i in message:
        symbolIndex = symbols.find(i)
        if symbolIndex == -1:   #Symbol not found in sumbols
            translated += i     #Add not found symbol as it is
        else:
            #Encrypt or Decrypt
            symbolIndex += key
            if symbolIndex >= len(symbols):
                symbolIndex -= len(symbols)
            elif symbolIndex < 0:
                symbolIndex += len(symbols)
                
            translated += symbols[symbolIndex]

    return translated   

mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()
print('Your translated text is:')
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for i in range(1, maxKeySize + 1):
        print(i, getTranslatedMessage('decrypt', message, i))
    
