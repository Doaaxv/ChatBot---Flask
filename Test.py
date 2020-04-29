import nltk
import numpy as np
import io
import string
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from flask import Flask, render_template, request
from flask_mail import Message, Mail
#Chatbase
from chatbase import Message as MsgChat
import os

warnings.filterwarnings('ignore')

nltk.download('punkt')
nltk.download('wordnet')

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER,'info.txt')

f = open(my_file,"r", errors='ignore')
text = f.read()

def chatbot(user_response):

    sent_tokens = nltk.sent_tokenize(text)
    word_tokens = nltk.word_tokenize(text)

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
            return chatbot_response

    flag = True
#    f_out= open("info.txt", 'r', errors='ignore')
#    txtfile = f_out.read()

    #pointless while loop, should be removed
    while(flag):

        user_response = user_response.lower()
        if(user_response!= "bye"):
            bot_response = response(user_response)
            sent_tokens.remove(user_response)
            return(bot_response)
        else:
            flag = False
            return 'bye'

def not_handeled(user_response):
    msg = MsgChat(api_key= "6f6aa25c-e467-49f7-9799-67efb413b829",
            type= "user",
            platform= "web",
            message= user_response,
            version= "1.0",
            user_id= "user-404",
            not_handled= "true")
    resp = msg.send()
    print(resp)

def handeled(user_response):
    msg = MsgChat(api_key= "6f6aa25c-e467-49f7-9799-67efb413b829",
            type= "user",
            platform= "web",
            message= user_response,
            version= "1.0",
            user_id= "user-200"
    )
    resp = msg.send()
    print(resp)


############################################## WEB PAGE #################################################################
app = Flask(__name__)

##### Email Configuraion for Contact page :
mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'thebeezco19@gmail.com'
app.config["MAIL_PASSWORD"] = 'THE@@beez'

mail.init_app(app)



def word_count(string):
    tokens = string.split()
    n_tokens = len(tokens)
    return n_tokens 

@app.route('/')
def index():
    return render_template('firstpage.html')

@app.route('/contact' , methods=['GET','POST'])
def contact():
    if request.method == 'POST':
      msg = Message("New Msg from a Fan!!", sender="thebeezco19@gmail.com", recipients=["thebeezco19@gmail.com"])
      msg.body = request.form['Message'] +"\n \n \nThis msg was sent by: {email}".format(email=request.form['Email']) 
      mail.send(msg)
      return render_template('contact.html', success=True)

    else:    
        return render_template('contact.html')

@app.route('/home')# , methods=['GET'])
def home():
    return render_template('firstpage.html')

@app.route('/get')# methods=['POST'])
def process():
    user_input = request.args.get("user_input")#.form['user_input']
    if word_count(user_input) < 3:
        return ("Sorry, in order to get the best response possible, your query must be at least three words long.")
    output = chatbot(user_input)
    if "Sorry, cannot understand your query" in output:
        not_handeled(user_input)
    else :
        handeled(user_input)
    return output#render_template('index.html', user_input = user_input, bot_response=output)

if __name__ == '__main__':
    app.run(debug=True, port=8081)