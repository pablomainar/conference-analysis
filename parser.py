import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import insti
import os
import numpy as np
from operator import add
#############################################################
#
# To-Do:
#   - Institution analysis: maybe get pdf format until the word abstract appears and try to get the institution name from there
#   - Hot words: get the words that appear most
#   - Framework: tensorflow, pytorch, caffe, etc
#
#
#############################################################


#write a for-loop to open many files -- leave a comment if you'd #like to learn how
#filename = 'papers/cvpr18/Acuna_Efficient_Interactive_Annotation_CVPR_2018_paper.pdf'
filenames = os.listdir('papers/cvpr18')
nb_files = len(filenames)




'''
fp = open(filename, 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)
meta = doc.info[0]
authors = meta.get('Author')
authors = authors.split(', ')
nb_authors = len(authors)

'''
institutions = insti.get_institutions_list()
nb_institutions = len(institutions)
institution_counter = [0] * nb_institutions

for n,f in enumerate(filenames):
    print(str(n)+'/'+str(nb_files)+': '+str(f))
    filename = os.path.join('papers/cvpr18',f)
    try:
        text = textract.process(filename,encoding='ascii')
    except UnicodeDecodeError:
        print('UnicodeDecodeError: Omitting file')
        continue
    except TypeError:
        print('TypeError: Omitting file')
        continue

    tokens = word_tokenize(text)

    institution_counter = list(map(add,institution_counter,insti.get_institutions(tokens)))
    #institutions_counter += insti.get_institutions(tokens) #this is concatenating, not adding!
    print(institution_counter)
print(institution_counter)

institution_counter = np.asarray(institution_counter)
np.save('institution_counter.npy',institution_counter)


exit()






print(len(tokens))
index_abstract = tokens.index('Abstract')
first_words = tokens[:index_abstract]
print(first_words)

previous_index = []
for w in first_words:
    if w in institutions:
        index = institutions.index(w)
        if index not in previous_index:
            institutions_counter[index] += 1
            previous_index += [index]

print(institutions)
print(institutions_counter)


exit()

nb_at = first_words.count('@')
print(nb_at)


if nb_at == 0:
    last_author = authors[-1].split(' ')[-1]
    print(last_author)
    index_last_author = first_words.index(last_author)
    print(index_last_author)
    first_words = first_words[index_last_author+1:]
    institution = ' '.join(first_words)
    institution_list = []
    if institution.find(',') == -1:
        institution_list += [institution]
    while institution.find(',') != -1:
        institution_list += [insitution[:institution.find(',')]]
        institution = institution[institution.find(','):]
    print(institution_list)



elif nb_at == nb_authors:
    pass
else:       
    pass



exit()
#we'll create a new list which contains punctuation we wish to clean
punctuations = ['(',')',';',':','[',']',',','.']
numbers = ['0','1','2','3','4','5','6','7','8','9']
#We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords
stop_words = stopwords.words('english')
#We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
keywords = [word.upper() for word in tokens if not word in stop_words and not word in punctuations and not word in numbers]


#print(keywords)

print(len(keywords))
print(type(keywords))


count = Counter(keywords)
print(count.most_common(10))
exit()
words = ['GOOGLE']
for w in words:
    print(w+': '+str(count[w]))