import sys
from eVotUM.Cripto import eccblind

def printUsage():
    print("Usage: python init-app.py || python init-app.py -init")

def parseArgs():
    if (len(sys.argv) > 2):
        printUsage()
    else:
        main()

def main():
    initComponents, pRDashComponents = eccblind.initSigner()
    #devolve o pRDashComponents
    if(len(sys.argv) == 1):
        print("Output")
        print("pRDashComponents: %s" % pRDashComponents)
    #inicializa InitComponents e pRDashComponents e guarda-as em AssComp.txt
    else:
        print("Ficheiro AssComp.txt criado - InitComponents & pRDashComponents")
        with open ("AssComp.txt","w") as file:
            file.write(initComponents)
            file.write("\n")
            file.write(pRDashComponents)

if __name__ == "__main__":
    parseArgs()
