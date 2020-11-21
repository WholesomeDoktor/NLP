from nltk.tokenize import regexp_tokenize
from pyxdameraulevenshtein import damerau_levenshtein_distance
from collections import Counter
L_corpus=[]
di ={}
wordcorpus=[]

with open('corpus.txt','r') as rf, open('tokens.txt','w') as fout:
    for line in rf:
        for char in '-.,\n_\'1234567890':
            line=line.replace(char,' ')
            line=line.casefold()
            L_corpus=(regexp_tokenize(line, "[\w']+"))
        for word in L_corpus:
            di[word]=di.get(word,0)+1
    for key,value in di.items():
        wordcorpus.append((key))

missword=[]   
with open('test-words-misspelled.txt','r') as rm:
    rm_contents=rm.read()
    missword=rm_contents.splitlines()

rank_y=()      
possible_word=[]
fo = open("predictedlist.txt", "w+")
for mword in missword:
    rank_dict=[]
    for word in wordcorpus:
        if damerau_levenshtein_distance(mword,word) ==1:
            rank_dict.append((di.get(word),word))
        else:
            pass
        rank_dict.sort(reverse=True)
    if rank_dict==[]:
        fo.write('\n')
    else:
        rank_y=rank_dict[0]
        fo.write(rank_y[1]+'\n')
    possible_word.append(rank_y[1])
fo.close()

correct_word=[]   
with open('test-words-correct.txt','r') as rc:
    rc_contents=rc.read()
    correct_word=rc_contents.splitlines()
    Accuracy= sum(1 for x,y in zip(correct_word,possible_word) if x == y) / float(len(correct_word))*100
    print('Accuracy:%', Accuracy)