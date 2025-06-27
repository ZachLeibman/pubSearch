from pdf2image import convert_from_path
import pytesseract

class nonProfit:

    orgName = None
    orgRev = None
    bldgName = None
    street = None
    city = None
    state = None
    zip = None
    indivName = None
    indivTitle = None
    webAdd = None
    phoneNum = None
   

    def __init__(self, pdfName):
        self.pdfTitle = pdfName
    
    
    def extractText(self):
        images = convert_from_path(self.pdfTitle)
        for i, img in enumerate(images[:1]):
            text = pytesseract.image_to_string(img)
            for line in text:
                if line.contains("Name of organization"):
                    self.orgName = line+1
                elif line.contains("Net assets or fund balances."):
                    self.orgRev = line[66:71]
                elif line.contains("Amended return Number and street"):
                    self.bldgName = line+1
                elif line.contains("ZIP or foreign postal code"):
                    self.city = (line+1).split(" ")[0]
                    self.state = (line+1).split(" ")[1]
                    self.zip = (line+1).split(" ")[2]
                elif line.contains("Is this a group return for"):
                    self.indivName = line+1
                elif line.contains("E Telephone number"):
                    self.indivTitle = (line+1).split(" ")[2]
                elif line.contains("Website"):
                    self.webAdd = line[13:]
                elif line.contains("Telephone number"):
                    self.phoneNum = line+1
        

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
    
    def toCsvType(self):
        return [
            self.orgName, 
            self.orgRev,
            self.bldgName,
            self.street,
            self.city,
            self.state,
            self.zip,
            self.indivName,
            self.indivTitle,
            self.webAdd,
            self.phoneNum,
        ]

    def main():
        nonProfit.toCsvType()
    
    if __name__ == "__main__":
        main()

    
    