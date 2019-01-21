# Business Card OCR 

This product allows our users to use their mobile device to take a picture of a business card and have the name, email, and phone number be converted to text on their device.

## Build Instructions

Use either command line, a python shell, or bash to run the file BusinessCardOCR.py

## Test Instructions

Once done you will see the output of the three test cases provided. If new test cases would like to be entered, please enter the text after the promt, hitting enter when finished.

## Notes

The application succeeds in some areas and does not in others. I was not able to think of a way to determine the difference between a name and a company name so I set it to take the first two non-numeric 'words' and print them. One possible solution to this I thought of is to  research how to implement a library of names into the program and query those names with the document string. On a match I would extract the match from the document string.

However this application succeeds fully in finding emails, so long as they have the @ symbol, and succeeds in returning a phone number instead of a fax number. This was done by singling out the fax number and returning the phone number. However if there is more than one phone number present, it will take the first number presented.

## Contributions

Any modifications and/or comments are welcome. The only way I can get better as a developer is through developer feedback. Thank you for your time and consideration.
