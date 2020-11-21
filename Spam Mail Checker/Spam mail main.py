import os
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from scipy.sparse import hstack
from scipy.sparse.construct import vstack
from scipy.sparse.csr import csr_matrix
from sklearn.metrics._classification import classification_report

#Directory of Legit and Spam Files
dir_train_legit="./dataset/training/legitimate"
dir_train_spam="./dataset/training/spam"
dir_test_legit="./dataset/test/legitimate"
dir_test_spam="./dataset/test/spam"

# Function creating a dictionary of all words within Legit and Spam
def build_dictionary(rootdir):
    dictionary=[]
    for directories, subdirs, files in os.walk(rootdir):
        for filename in files:      
            with open(os.path.join(directories, filename), encoding="latin-1") as f:
                for i, line in enumerate(f):
                    if i == 2:              # Body of email is only 3rd line of text file
                        line = re.sub("(^|\W)\d+($|\W)", " ", line) #Removing all digits
                        words = line.split()
                        dictionary += words
    dictionary = list(set(dictionary))

    for index, word in enumerate(dictionary):
        if (word.isalpha() == False) or (len(word) == 1):  #Removing all alphanumerics
            del dictionary[index]
        

    return dictionary

#Creating Labels for the Dictionary
def build_labels(legit,spam):
  label_legit=np.zeros(legit)
  label_spam=np.zeros(spam)
  for index in range(legit):
      label_legit[index]=1
      for index2 in range(spam):
          label_spam[index2]=0
    
  return (np.append(label_legit,label_spam))


#Calling Dictionary functions and Intializing Train and Test files
train_legit=build_dictionary(dir_train_legit)
train_spam=build_dictionary(dir_train_spam)
test_legit=build_dictionary(dir_test_legit)
test_spam=build_dictionary(dir_test_spam)

#Using TFid Document Frequency max 200 features are collected for Legit and Spam classes for both Train and Test files
vectorizer = TfidfVectorizer(ngram_range=(1,2),max_features=200)

train_legit_tfid=vectorizer.fit_transform(train_legit)
#Printing the top 200 best words for Legit Class
print('Printing Legit 200 words:', vectorizer.get_feature_names())

train_spam_tfid=vectorizer.fit_transform(train_spam)
#Printing the top 200 best words for Spam Class
print('Printing Spam 200 words:', vectorizer.get_feature_names())

test_legit_tfid=vectorizer.fit_transform(test_legit)
test_spam_tfid=vectorizer.fit_transform(test_spam)

#Creating Features and Lables for Training
X_train=vstack((train_legit_tfid,train_spam_tfid))
labels_train=build_labels(train_legit_tfid.shape[0],train_spam_tfid.shape[0])
 
#Creating Features and Lables for Testing
X_test=vstack((test_legit_tfid,test_spam_tfid))
labels_test=build_labels(test_legit_tfid.shape[0],test_spam_tfid.shape[0])


#Initializing Naives Classifier with alpha =0 No Laplace Smoothing
classifier = MultinomialNB(alpha=0)
classifier.fit(X_train, labels_train)
print(classifier)

predict_test = classifier.predict(X_test)

accuracy = classifier.score(X_test, labels_test)
print ('Accuracy : ', accuracy)
Report=classification_report(labels_test, predict_test)
print(Report)

#Initializing Naives Classifier with alpha =1 Laplace Smoothing
classifier_L = MultinomialNB(alpha=1)
classifier_L.fit(X_train, labels_train)
print(classifier_L)
predict_test = classifier_L.predict(X_test)

accuracy = classifier_L.score(X_test, labels_test)
print ('Accuracy : ', accuracy)
Report=classification_report(labels_test, predict_test)
print(Report)