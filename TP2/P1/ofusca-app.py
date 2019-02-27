import sys
from eVotUM.Cripto import eccblind

def printUsage():
    print("Usage: python ofusca-app.py -msg <mensagem a assinar> -RDash <pRDashComponents>")

def parseArgs():
    if (len(sys.argv) != 5):
        printUsage()
    else:
        main(sys.argv[2],sys.argv[4])

def showResults(errorCode, result):
    print("Output")
    if (errorCode is None):
        blindComponents, pRComponents, blindM = result
        print("Blind message: %s" % blindM)
        print("Ficheiro ReqComp criado - Blind components & pRComponents")
        with open ("ReqComp.txt","w") as file:
            file.write(blindComponents)
            file.write("\n")
            file.write(pRComponents)
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")

def main(data,pRDashComponents):
    errorCode, result = eccblind.blindData(pRDashComponents, data)
    showResults(errorCode, result)

if __name__ == "__main__":
    parseArgs()
