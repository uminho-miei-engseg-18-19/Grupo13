from eVotUM.Cripto import utils
import sys
from eVotUM.Cripto import eccblind

def printUsage():
    print("Usage: python blindSignature-app.py -key <chave privada> -bmsg <Blind message>")

def parseArgs():
    if (len(sys.argv) != 5):
        printUsage()
    else:
        main(sys.argv[2],sys.argv[4])

def showResults(errorCode, blindSignature):
    print("Output")
    if (errorCode is None):
        print("Blind signature: %s" % blindSignature)
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the private key")
    elif (errorCode == 2):
        print("Error: init components are invalid")
    elif (errorCode == 3):
        print("Error: invalid blind message format")

def main(eccPrivateKeyPath,blindM):
    pemKey = utils.readFile(eccPrivateKeyPath)
    print("Input")
    passphrase = raw_input("Passphrase: ")
    with open("AssComp.txt",'r') as file:
        lines = file.readlines()
        initComponents = lines[0]
    errorCode, blindSignature = eccblind.generateBlindSignature(pemKey, passphrase, blindM, initComponents)
    showResults(errorCode, blindSignature)

if __name__ == "__main__":
    parseArgs()
