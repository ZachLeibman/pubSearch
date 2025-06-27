from nonProfit import *
from pathlib import Path

class nonProfitSort():  
    Directory = None
    fileList = [] #dictonary to hold file names in directory as a string
    nonProfits = [] #dictionary to hold after being converted into a nonProfit object
    outputFile = None #csv file pointer
    def __init__(self, pdfFolderName, outputfile):
        self.outputFile = outputfile
        self.Directory = pdfFolderName
        self.fileList =  [f.name for f in pdfFolderName.glob("*.pdf")]
       
       
    def createList(self):
        for fileName in self.fileList:
            if fileName.contains("_990_" or "_990EZ_"):
                self.nonProfits.append(nonProfit(fileName))
            else:
                pass

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
        sortedNames = nonProfitSort.sortByName()
        sortedRev = nonProfitSort.sortByRevenue()
        sortedRev = nonProfitSort.sortByLocation()

        
    if __name__ == "__main__":
        main()