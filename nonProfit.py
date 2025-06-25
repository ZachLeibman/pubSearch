from pypdf import pdfReader

class nonProfit:

    orgName = None
    orgRev = None
    zip = None
    indivName = None
    indivTitle = None
    webAdd = None

    def __init__(self, pdfName):
        self.pdfTitle = pdfName
    
    
    def extractText(self):
        reader = pdfReader(pdfTitle)
        i=1
        while i >= 6:
            for line in reader.pages[i]:
                if line.contains(""):
                    orgName = line
                elif line.contains(""):
                    orgRev = line
                elif line.contains(""):
                    zip = line
                elif line.contains(""):
                    indivName = line
                elif line.contains(""):
                    indivTitle = line
                elif line.contains(""):
                    webAdd = line
        

    def getName(self):
        return self.orgName
    
    def getRevenue(self):
        return self.orgRev
    
    def getZipCode(self):
        return self.zip
    
    def getSignerName(self):
        return self.indivName
    
    def getSignerTitle(self):
        return self.indivTitle
    
    def getSignerNum(self):
        return self.indivNum
    
    def getWebsite(self):
        return self.webAdd
    
    def main():
        return True
    
    if __name__ == "__main__":
        main()

    
    