import nltk
import numpy as np
import io
import string
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

warnings.filterwarnings('ignore')

#nltk.download('punkt')
#nltk.download('wordnet')

f = open("info.txt","r", errors='ignore')
text = f.read()
#text = text.lower()
#text = text.strip('\n\t[]<>/</br>See COVID-19')
#text = text.replace('.,','')
#text = text.replace('Additional information on how COVID-19 is spread is available at How COVID-19 Spreads Related: Talking to Children','')
#text = text.replace(':,','')
#text = text.replace(' , ','')
#text = text.replace('[','')
#text = text.replace(']','')
#text = re.sub('<[^<]+?>', '', text)

sent_tokens = nltk.sent_tokenize(text)
word_tokens = nltk.word_tokenize(text)

#print(str(word_tokens) +' -----'+ str(sent_tokens))

lemmer = nltk.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(txt):
    return LemTokens(nltk.word_tokenize(txt.lower().translate(remove_punct_dict)))

def response(user_response):
    chatbot_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1],tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req = flat[-2]
    if(req==0):
        chatbot_response = chatbot_response + 'Sorry, cannot understand your query'
        return chatbot_response
    else:
        chatbot_response = chatbot_response+sent_tokens[idx]
        #print(sent_tokens)
        return chatbot_response

flag = True
important_words = ['vaccine', 'old people', 'cat', 'pet', 'animal', 'zoo', 'sun', 'weather', 'surface'
                 'cloth', 'sneeze', 'sneezing','coughing','cough', 'distance', 'sick'
                ,'illness', 'ill', 'clean','protect', 'symptoms', 'spread',]
while(flag):
    user_response = input()
    user_response = user_response.lower()
    #user_response = user_response.replace('virus' , '')
    #user_response = user_response.replace('covid-19' , '')
    for word in range(len(important_words)):
        #print('----------------'+important_words[word]+''+str(user_response.find(important_words[word])))
        if  1==0:#important_words[word] in user_response:
            user_response = important_words[word]
            break
    #user_response = user_response.lower()

    if(user_response!= "bye"):
        print('chatbot: ', end='' )
        print(response(user_response))
        sent_tokens.remove(user_response)
    else:
        flag = False
        print('bye')