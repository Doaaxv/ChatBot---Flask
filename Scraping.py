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
            "https://www.cdc.gov/coronavirus/2019-ncov/faq.html#School-Dismissals-and-Children",
            "https://www.cdc.gov/coronavirus/2019-ncov/travelers/travel-in-the-us.html",
            "https://emergency.cdc.gov/han/2020/han00430.asp",
            "https://emergency.cdc.gov/han/2020/han00431.asp",
            "https://emergency.cdc.gov/han/2020/HAN00429.asp",
            "https://emergency.cdc.gov/han/2020/HAN00428.asp",
            "https://emergency.cdc.gov/han/HAN00427.asp",
            "https://emergency.cdc.gov/han/HAN00426.asp",
            "https://emergency.cdc.gov/han/HAN00425.asp",
            "https://emergency.cdc.gov/han/HAN00424.asp",
            "https://www.cdc.gov/coronavirus/2019-ncov/travelers/cruise-ship/what-cdc-is-doing.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/covid-data/investigations-discovery/assessing-risk-factors.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/critical-workers/implementing-safety-practices.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/disinfecting-building-facility.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/cleaning-disinfection.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/disinfecting-transport-vehicles.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/schools-childcare/guidance-for-schools.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/schools-childcare/schools-faq.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/schools-childcare/checklist.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/schools-childcare/guidance-for-childcare.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/student-foreign-travel.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/colleges-universities/faq.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/conserving-respirator-supply.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/guidance-business-response.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/guidance-small-business.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/general-business-faq.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/airline-catering-kitchen-workers.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/airline-catering-truck-drivers.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/airport-customer-factsheet.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/airport-baggage-cargo-handlers.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/airport-custodial-staff.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/airport-passenger-assistance-workers.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/aircraft-maintenance-workers.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/airport-retail-factsheet.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/bus-transit-operator.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/grocery-food-retail-workers.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/rail-transit-operator.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/transit-maintenance-worker.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/transit-station-workers.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/mail-parcel-drivers.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/rideshare-drivers-for-hire.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/food-grocery-drivers.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/large-events/mass-gatherings-ready-for-covid-19.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/election-polling-locations.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/large-events/event-planners-and-attendees-faq.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/guidance-law-enforcement.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/firefighter-EMS.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/guidance-community-faith-organizations.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/community-faith-based/faq.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/organizations/checklist.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/parks-rec/park-administrators.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/homeless-shelters/unsheltered-homelessness.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/homeless-shelters/unsheltered-homelessness.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/homeless-shelters/plan-prepare-respond.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/homeless-shelters/screening-clients-respiratory-infection-symptoms.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/homeless-shelters/faqs.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/retirement/guidance-retirement-response.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/retirement/checklist.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/retirement/faq.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/correction-detention/guidance-correctional-detention.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/correction-detention/faq.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/tribal/faq-burial-practice.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/tribal/social-distancing.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/community/veterinarians.html",
            "https://www.cdc.gov/coronavirus/2019-nCoV/hcp/clinical-criteria.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/clinical-guidance-management-patients.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/therapeutic-options.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/underlying-conditions.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/disposition-in-home-patients.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/guidance-home-care.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/disposition-hospitalized-patients.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/pediatric-hcp.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/inpatient-obstetric-healthcare-guidance.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/infection-control-recommendations.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/infection-control-faq.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/using-ppe.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/hand-hygiene.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/hand-hygiene-faq.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/alternative-care-sites.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/ambulatory-care-settings.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/assisted-living.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/blood-and-plasma-collection.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/dental-settings.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/dialysis.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/long-term-care.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/pharmacies.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/guidance-postmortem-specimens.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/ppe-strategy/burn-calculator.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/ppe-strategy/eye-protection.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/ppe-strategy/isolation-gowns.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/ppe-strategy/face-masks.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/respirators-strategy/index.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/ppe-strategy/powered-air-purifying-respirators-strategy.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/elastomeric-respirators-strategy/index.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/ppe-strategy/ventilators.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/respirator-use-faq.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/guidance-risk-assesment-hcp.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/non-covid-19-client-interaction.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/return-to-work.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/guidance-for-ems.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/hcp-personnel-checklist.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/steps-to-prepare.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/guidance-hcf.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/covidsurge.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/hcp-hospital-checklist.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/long-term-care-checklist.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/clinic-preparedness.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/mitigating-staff-shortages.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/preparedness-resources.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/non-us-settings/ipc-healthcare-facilities-non-us.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/non-us-settings/sop-triage-prevent-transmission.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/non-us-settings/guidance-identify-hcw-patients.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/non-us-settings/hcf-visitors.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/non-us-settings/public-health-management-hcw-exposed.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/hcp/faq.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/open-america/infection-control.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/open-america/surveillance-data-analytics.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/open-america/laboratory.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/open-america/contact-tracing.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/principles-contact-tracing.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/open-america/community-mitigation.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/open-america/staffing.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/open-america/financial-resources.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/open-america/communications.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/open-america/response-corps.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/public-health-communicators-get-your-community-ready.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/investigating-cases-homeless-shelters.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/guidance-evaluating-pui.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/reporting-pui.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/risk-assessment.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/public-health-recommendations.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/pandemic-preparedness-resources.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/interim-guidance-managing-people-in-home-care-and-isolation-who-have-pets.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/animal-testing.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/cooling-center.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/building-water-system.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/water.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/lab/testing-laboratories.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/testing.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/lab/serology-testing.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/php/grows-virus-cell-culture.html",
            "https://www.cdc.gov/coronavirus/2019-nCoV/lab/guidelines-clinical-specimens.html",
            "https://www.cdc.gov/coronavirus/2019-nCoV/lab/lab-biosafety-guidelines.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/lab/biosafety-faqs.html",
            "https://www.cdc.gov/coronavirus/2019-ncov/lab/tool-virus-requests.html"]
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
                text = text + str(myList[elem][info]) + "\n"

    ######### TEXT PREPROCESSING #############################################################
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
    text = re.sub(r'([^.]*?Additional information[^.]*\.)','',text)
    text = re.sub(r'([^.]*?See also[^.]*\.)','',text)
    tokens = nltk.sent_tokenize(text)

    ######### TEXT PREPROCESSING #############################################################

    #Wirting output in file 
    with open("info.txt", 'a', encoding='utf-8') as f_out:
        for token in tokens:
            f_out.write(token + '\n')

    f_out.close()  # Close the file