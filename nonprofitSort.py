from nonProfit import *
from pathlib import Path

class nonProfitSort():
    fileList = []
    nonProfits = []
    outputFile = None
    def __init__(self, pdfFolderName, outputfile):
        self.outputFile = outputfile
        self.fileList =  [f.name for f in pdfFolderName.glob("*.pdf")]
       

    def createList(self):
        for fileName in self.fileList:
            self.nonProfits.append(nonProfit(fileName))

    def sortByName(self):
        sorted_list = sorted(self.nonProfits, key=lambda np: np.getName(), reverse=False)
        return sorted_list
    
    def sortByRevenue(self):
        sorted_list = sorted(self.nonProfits, key=lambda np: np.getRevenue(), reverse=False)
        return sorted_list

    def sortByLocation(self):
        sorted_list = sorted(self.nonProfits, key=lambda np: np.getZipCode(), reverse=False)
        return sorted_list
    
    def main():
        sortByName()
        sortByRevenue()
        sortByLocation()
        
    if __name__ == "__main__":
        main()