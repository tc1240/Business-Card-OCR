## Business Card OCR

import re

## Class for ContactInfo object
class ContactInfo:

    ## Makes document passed to ContactInfo avaliable to all child methods
    def __init__(self, document):
        self.document = document

    ## Searches document for the first two non-numeric character sequences
    ##      This function is not complete as currently the only way I can determine a name
    ##      from a company is the first letters being capital, and even that is not entirely fool proof
    ##      What I would do here had I more time, I would research how to query a library of existing names
    ##      and when I find a match I would extract that name.
    def getName(self):
        name = re.findall('^[a-zA-Z ]+', self.document)
        firstAndLastName = name[0].split(" ")
        return firstAndLastName[0] + " " + firstAndLastName[1]

    ## Searches document for a phone number, returning the number found. This method also discriminates between a
    ##    fax number and phone number based on the appearance of the word 'fax'.
    ##    NOTE: If there are 2 non-fax numbers present then this method will choose the first number present 
    def getPhoneNumber(self):
        ## If there is an phone number present...
        if "(" or "-" in self.document:
            ## Get all phone numbers from document
            phoneNumbers = re.findall(r"\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b", self.document)
            ## Search document for the word fax, as this word alone indicates a fax number not a phone number,
            ##    and return the phone number not the fax number.
            if "fax" in self.document:
                ## Split document on the first phone number found
                splitDoc = self.document.split(phoneNumbers[0])
                for i in range (len(splitDoc)):
                    ## If there is fax in the current splitDoc...
                    if "fax" in splitDoc[i]:
                        ## and there is a phone number in that split doc...
                        if phoneNumbers[1] in splitDoc[i]:
                            ## then the number that was split out of the string is the phone number
                            phone = phoneNumbers[0]
                        ## and there is no phone number in the split doc
                        else:
                            ## then the fax number was taken out and the remaining number is the phone number
                            phone = phoneNumbers[1]
                    
            ## No fax? return the phone number
            else:
                phone = phoneNumbers[0]
                    
            ## Format number before returning
            unwantedChars = "-() "
            for c in unwantedChars:
                if c in phone:
                    phone = phone.replace(c, "")
            return phone
        ## Else return an empty string
        else:
            phone = ""
            return phone

    ## Searches document for an email, returning the email found
    def getEmailAddress(self):
        ## If there is an email present...
        if "@" in self.document:
            ## Break the document into pieces based on spaces
            splitDoc = self.document.split( )
            ## Search split document for the Email and return it when done
            for i in range (len(splitDoc)):
                if "@" in splitDoc[i]:
                    email = splitDoc[i]
                    

            return email
        ## Else return an empty string
        else:
            email = ""
            return email

## Class for the BusinessCardParser object
class BusinessCardParser:
    ## Receives the Name, Phone number, and Email found within a document
    def getContactInfo(self, document):
        ci = ContactInfo(document)
        
        ci.name = ci.getName()
        ci.email = ci.getEmailAddress()
        ci.phone = ci.getPhoneNumber()
        print("Name: " + ci.name + "\nPhone: " + ci.phone + "\nEmail: " + ci.email)


def main():
    BCP = BusinessCardParser()
    BCP.getContactInfo("ASYMMETRIK LTD Mike Smith Senior Software Engineer (410)555-1234 msmith@asymmetrik.com")
    print("----")
    BCP.getContactInfo("Foobar Technologies Analytic Developer Lisa Haung 1234 Sentry Road Columbia, MD 12345 Phone: 410-555-1234 Fax: 410-555-4321 lisa.haung@foobartech.com")
    print("----")
    BCP.getContactInfo("Arthur Wilson Software Engineer Decision & Security Technologies ABC Technologies 123 North 11th Street Suite 229 Arlington, VA 22209 Tel: +1 (703) 555-1259 Fax: +1 (703) 555-1200 awilson@abctech.com")
    
main()
close = input("Press enter to close")
