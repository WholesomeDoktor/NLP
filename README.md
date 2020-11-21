# NLP

The Spelling checking project was built around ntlk library. Using regexp_tokenize to produce a list of words which are separated based on punctutations. 
The program starts with open and close functions followed by removal of character from the lists using replace and case folding. 
A dictionary is created with the frequency of words. The mispelled words are fed into the edit distance function using Damerau levenshtein function. For words with edit distance=1 their frequency was determined and were chosen based on frequency in the corpus text. 
Accuracy of the program was under satisfactory conditons. 


## HOW TO RUN 
### UNIX

Inorder to run the program, make sure these files are present in the same folder

1. test-words-misspelled

2.test-words-misspelled

3.test-words-misspelled

Other files will be created as the program runs. 

Predicted Words is the text file which displays the words predicted by the program. Other files are unnecessary. 

### WINDOWS

Change the directories to windows style directory.
