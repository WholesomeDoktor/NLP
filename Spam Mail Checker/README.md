# SPAM MAIL CHECKER


Firstly in order to call the directories os library was used together with some regular expressions and logic to remove numerical digits and alphanumeric. Once with cleaning, IDF Document Frequency was used instead of Count vectorizer and DF transformer as the former has both the capabilities builtin. The DF scores for legitimate and spam classes were calculated separately.  Initially pandas library was attempted due to enormous errors, a simple method to separately creating training set and label set was implemented. Sklearn library was used for Multi nominal Naive Bayes classifier, setting alpha at 0 resulted in no Laplace smoothing and at 1 with Laplace smoothing. 


## HOW TO RUN

### UNIX

Make sure all the files are present in the same code folder. The code doesn't work on Windows (change paths accordingly)
