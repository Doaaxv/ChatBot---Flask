from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import re
import nltk
import sys
import os
from nltk import tokenize
from nltk.corpus import stopwords
import string

def word_count(string):
    tokens = string.split()
    n_tokens = len(tokens)
    return n_tokens 

# URl to web scrap from.
page_url = ["https://www.cdc.gov/coronavirus/2019-ncov/symptoms-testing/symptoms.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/symptoms-testing/testing.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/index.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/how-covid-spreads.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/prevention.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/diy-cloth-face-coverings.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/cloth-face-cover.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/cloth-face-cover-faq.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/disinfecting-your-home.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/cleaning-disinfection.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/social-distancing.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/checklist-household-ready.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/get-your-household-ready-for-COVID-19.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/living-in-close-quarters.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/essential-goods-services.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/managing-stress-anxiety.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/reducing-stigma.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/share-facts.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/children.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/talking-with-children.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/visitors.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/animals.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/if-you-are-sick/steps-when-sick.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/if-you-are-sick/care-for-someone.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/people-at-higher-risk.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/older-adults.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/asthma.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/hiv.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/groups-at-higher-risk.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/people-with-disabilities.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/homelessness.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/pregnancy-breastfeeding.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/racial-ethnic-minorities.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/what-you-can-do.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/faq.html#Coronavirus-Disease-2019-Basics",
            "https://www.cdc.gov/coronavirus/2019-ncov/faq.html#How-COVID-19-Spreads",
            "https://www.cdc.gov/coronavirus/2019-ncov/faq.html#In-Case-of-an-Outbreak-in-Your-Community",
            "https://www.cdc.gov/coronavirus/2019-ncov/faq.html#Symptoms-&-Testing",
            "https://www.cdc.gov/coronavirus/2019-ncov/faq.html#How-to-Protect-Yourself",
            "https://www.cdc.gov/coronavirus/2019-ncov/faq.html#Higher-Risk",
            "https://www.cdc.gov/coronavirus/2019-ncov/faq.html#Healthcare-Professionals-and-Health-Departments",
            "https://www.cdc.gov/coronavirus/2019-ncov/faq.html#COVID-19-and-Children",
            "https://www.cdc.gov/coronavirus/2019-ncov/faq.html#COVID-19-and-Animals",
            "https://www.cdc.gov/coronavirus/2019-ncov/faq.html#What-CDC-is-Doing",
            "https://www.cdc.gov/coronavirus/2019-ncov/faq.html#COVID-19-and-Funerals",
            "https://www.cdc.gov/coronavirus/2019-ncov/faq.html#Preparing-Your-Home-and-Family-for-COVID-19",
            "https://www.cdc.gov/coronavirus/2019-ncov/faq.html#Children-and-Youth-with-Special-Healthcare-Needs",
            "https://www.cdc.gov/coronavirus/2019-ncov/faq.html#School-Dismissals-and-Children"]
# opens the connection and downloads html page from url
with open("info.txt", 'w') as f:
    f.write("")

for page in range(len(page_url)):
    uClient = uReq(page_url[page])

    # parses html into a soup data structure to traverse html
    # as if it were a json data type.
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    # finds each product from the store page
    page_soup = page_soup.find("main")
    information1 = page_soup.findAll("p")
    information2 = page_soup.findAll("li")
    information3 = page_soup.findAll("span")
    myList = [information1]#, information2]#, information3]
    text = ''
    for elem in range(len(myList)):
        for info in range(len(myList[elem])):
            if(word_count(str(myList[elem][info])) > 5):
                text = text + str(myList[elem][info]) + ".\n"
    text = re.sub('<[^<]+?>', '', text)
    #text = text.lower()
    text = text.replace('.,','')
    text = text.replace(':,','')
    text = text.replace(' , ','')
    text = text.replace('[','')
    text = text.replace(']','')
    text = text.replace('"', '')
    text = text.replace("’", "")
    text = text.replace('“', "")
    text = text.replace('”', "")
    text =  re.sub(r'\[.*\]', '', text)
    text = re.sub(r'([^.]*?More details[^.]*\.)','',text)
    #text = re.sub(r'([^.]*?How[^.]*\.)','',text)
    #text = re.sub(r'([^.]*? ?[^.]*\.)','',text)
    text = re.sub(r'([^.]*?Additional information[^.]*\.)','',text)
    text = re.sub(r'([^.]*?See also[^.]*\.)','',text)
    #text = text.replace('Additional information on how COVID-19 is spread is available at How COVID-19 Spreads Related: Talking to Children','')
    #text = ' '.join(text.split())
    tokens = nltk.sent_tokenize(text)

    with open("info.txt", 'a', encoding='utf-8') as f_out:
        for token in tokens:
            #token = token.translate(str.maketrans('','',string.punctuation))
            f_out.write(token + '\n')
    # name the output file to write to local disk
    #out_filename = "info.txt"

    # opens file, and writes headers
    #f = open(out_filename, "a")
    #f.write() 

    f_out.close()  # Close the file