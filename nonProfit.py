from pathlib import Path
from pdf2image import convert_from_path
import pytesseract
import re

class nonProfit:
   

    def __init__(self, pdfName):
        self.pdfTitle = pdfName
        self.orgName = None
        self.orgRev = None
        self.bldgName = None
        self.city = None
        self.state = None
        self.zip = None
        self.indivName = None
        self.indivTitle = None
        self.webAdd = None
        self.phoneNum = None
   
    
    
    def extractText(self):
        images = convert_from_path(self.pdfTitle)
        for i, img in enumerate(images[:1]):
            text = pytesseract.image_to_string(img).splitlines()
            text = [line.strip() for line in text if line.strip()]  # Clean and remove empty line

            for i, line in enumerate(text):
                line_lower = line.lower()

                if self.orgName is None:
                    if ("name of organization" in line_lower or 
                        "employer identification number" in line_lower):
                        if i + 1 < len(text) and text[i + 1].strip():
                            self.orgName = text[i + 1].strip()
                        # If that's empty, try the line after
                        elif i + 2 < len(text) and text[i + 2].strip():
                            self.orgName = text[i + 2].strip()
                        
                elif "gross receipts" in line_lower and self.orgRev is None:
                    match = re.search(r"\$?[\d,]+", line)
                    if match:
                        self.orgRev = match.group().replace("$", "").replace(",", "")


                elif "number and street" in line_lower:
                    self.bldgName = text[i+1] if i + 1 < len(text) else None

                elif "zip or foreign postal code" in line_lower:
                    if i + 1 < len(text):
                        parts = text[i + 1].split()
                        self.city = parts[0] if len(parts) > 0 else None
                        self.state = parts[1] if len(parts) > 1 else None
                        self.zip = parts[2] if len(parts) > 2 else None

                elif "signature of officer" in line_lower or line_lower.startswith("sign here"):
                    for j in range(1, 5):
                        if i + j < len(text):
                            candidate = text[i + j].strip()
                            if re.search(r"[a-zA-Z]{2,}", candidate) and len(candidate.split()) >= 2:
                                self.indivName = candidate
                                parts = candidate.split()
                                self.indivTitle = parts[-1] if len(parts) > 1 else "officer"
                                break

                elif "website" in line_lower:
                    if ":" in line:
                        self.webAdd = line.split(":")[1].strip()
                    elif i+1 < len(text):
                        self.webAdd = text[i+1].strip()

                elif "telephone number" in line_lower:
                    if i + 1 < len(text):
                        phoneLine = text[i+1].strip()
                        # Extract just digits, parentheses, and dashes
                        self.phoneNum = re.sub(r'[^\d()-]', '', phoneLine)
            
            print(f"Extracted orgName: {self.orgName}, revenue: {self.orgRev}")
                
                
        

    def getName(self):
        return self.orgName
    
    def getRevenue(self):
        return self.orgRev
    
    def getZipCode(self):
        return self.zip
    
    @staticmethod
    def cleanText(text):
        if not text:
            return ""
        text = str(text)
        text = text.replace("\n", " ").replace("\r", " ")  # Remove newlines
        text = re.sub(r"[^\x20-\x7E]", "", text)  # Remove non-ASCII junk
        text = re.sub(r"\s+", " ", text).strip()  # Collapse spaces
        return text
    
    def toCsvType(self):
        return [
            self.cleanText(self.orgName), 
            self.cleanText(self.orgRev),
            self.cleanText(self.bldgName),
            self.cleanText(self.city),
            self.cleanText(self.state),
            self.cleanText(self.zip),
            self.cleanText(self.indivName),
            self.cleanText(self.indivTitle),
            self.cleanText(self.webAdd),
            self.cleanText(self.phoneNum),
        ]

def main():
    test_dir = "/Users/EpicManZ/Downloads/download990pdf_01_2024_prefixes_04-06"
    test_file = "/066040747_202301_990_2024011722246609.pdf"
    
    test_path = test_dir + test_file

    obj = nonProfit(test_path)
    obj.extractText()
    csvObj = obj.toCsvType()
    print(csvObj)


if __name__ == "__main__":
    main()

    
    