from nonProfit import *
from pathlib import Path

class nonProfitSort():  
    Directory = Path("/Users/EpicManZ/Downloads/download990pdf_01_2024_prefixes_04-06")
    fileList = [] #dictonary to hold file names in directory as a string
    nonProfits = [] #dictionary to hold after being converted into a nonProfit object
    outputFile = None #csv file pointer


    def __init__(self, outputfile):
        self.outputFile = outputfile
        self.fileList =  [f.name for f in self.Directory.glob("*.pdf")]
        self.nonProfits = []
       

    def createList(self):
        for fileName in self.fileList:
            if "_990_" in fileName or "_990EZ_" in fileName:
                full_path = self.Directory / fileName
                np_obj = nonProfit(str(full_path))
                np_obj.extractText()  # Don't forget to populate it!
                self.nonProfits.append(np_obj)
                

    def sortByName(self):
        sorted_list = sorted(self.nonProfits, key=lambda np: np.getName() or "", reverse=False)
        return sorted_list
    
    def sortByRevenue(self):
        sorted_list = sorted(self.nonProfits, key=lambda np: np.getRevenue() or "", reverse=False)
        return sorted_list

    def sortByLocation(self):
        sorted_list = sorted(self.nonProfits, key=lambda np: np.getZipCode() or "", reverse=False)
        return sorted_list
    
    def export_to_csv(self, sorted_list):
        with open(self.outputFile, "a") as f:

            header = ["Organization Name", "Revenue", "Building Name", 
            "City", "State", "ZIP", "Signer Name", "Signer Title", 
            "Website", "Phone Number"]

            f.write(",".join(header) + "\n")

            for item in sorted_list:
                row = item.toCsvType()
                if len(row) == 10:  # Or whatever your expected length is
                    f.write(",".join(map(str, row)) + "\n")
                else:
                    print("Skipping malformed row:", row)


        

def main():
    sorter = nonProfitSort("output.csv")
    sorter.createList()
    sortedNames = sorter.sortByName()
    # sortedRevs = sorter.sortByRevenue()
    # sortedLocations = sorter.sortByLocation()
    sorter.export_to_csv(sortedNames)
    # sorter.export_to_csv(sortedRevs)
    # sorter.export_to_csv(sortedLocations)


        
if __name__ == "__main__":
    main()