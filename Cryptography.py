import random
import io
import os
import time

def encryptNewFile(name, secureKey):
    with open(name,'rb') as reader:
        reader.seek(4)
        stri = reader.readline()
        lenf = len(stri)
        stra =[]
        for i in range (lenf):
            stra.append((stri[i]) + 4)    
        strk = []
        for i in range (lenf):
            strk.append(stra[i].to_bytes(1, byteorder="big", signed="True"))

    with open(name,'rb+') as writer:
        writer.seek(4)
        for i in range(lenf):
            writer.write(strk[i])

        
def descrypt():
    name = input("Qual eh o nome do arquivo? ")
    tentativas = 3
    while tentativas > 0:
        givenkey = int(input("Qual eh a sua secureKey? "))
        lenf = 0
        with open(name, 'rb') as file:
            securkey = file.read(4)
            securekey = int.from_bytes(securkey, byteorder="big", signed="True")
            print(securekey)
            print(givenkey)
            if securekey == givenkey:
                tentativas = 0
                file.seek(4)
                stri = file.readline()
                lenf = len(stri)
                stra =[]
                for i in range (lenf):
                    stra.append((stri[i]) - 4)    
                file.seek(0)
                strk = []
                for i in range (lenf):
                    strk.append(stra[i].to_bytes(1, byteorder="big", signed="True"))  
            else:
                tentativas = tentativas - 1
                print("Key errada")  
                time.sleep(1)

        with open(name,'wb') as writer:
            for i in range(lenf):
                writer.write(strk[i])


def writeFile():
    try:
        name = input("Qual eh o nome do arquivo? ")
        arq = open(name,'wb')
    except FileExistsError:
        print("Arquivo ja existe")
    write = input("Digite o que deseja escrever no arquivo:\n")
    secureKey = random.randrange(900000)
    print("Sua chave de criptografia eh: ",secureKey)
    arq.seek(0)
    secureKey = secureKey.to_bytes(4,byteorder='big', signed=True)
    arq.write(secureKey)
    write = str.encode(write)
    arq.seek(4)
    arq.write(write)
    arq.close()
    encryptNewFile(name,secureKey)


def menu():
    sair = False
    while(sair == False):
        sair = True
        print("\n------------* MENU *------------\n" + 
                "0 - Escrever em um arquivo e criptografar\n" +
                "1 - Criptografar um arquivo\n" +
                "2 - Descriptografar um arquivo\n" +
                "3 - Sair do programa\n")

        option = input("Qual a opcao desejada? ")
        if option == "0":
            print("\t**Escrever um novo arquivo**")
            writeFile()
            sair = False
        elif option == "1":
            print("\t**Criptografar um arquivo**")
            sair = False
        elif option == "2":
            print("\t**Descriptografar arquivo**")
            descrypt()
            sair = False
        elif option == "3":
            print("\t**Fechar programa**")
            sair = True
        else:
            print("\nOpcao invalida!!!")
            time.sleep(1)
            sair = False
        
menu()


