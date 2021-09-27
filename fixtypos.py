from textblob import TextBlob

import sys

with open(sys.argv[1], "r") as f: # Opening the test file with the intention to read
    text = f.read() # Reading the file
    textBlb = TextBlob(text) # Making our first textblob
    textCorrected = textBlb.correct() # Correcting the text
    if textBlb != textCorrected:
      print(textCorrected)