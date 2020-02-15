#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print(len(enron_data.keys()))#counting the number of data points
print(len(enron_data["SKILLING JEFFREY K"]))#counting the number of features

#counting the number of poi
c=0
for k,v in enron_data.items():
    if enron_data[k]["poi"]==1:
        c=c+1
print(c)

#number of poi
f = open("C:/Users/Pushkal Dwivedi/Desktop/SourceCodeML/ud120-projects/final_project/poi_names.txt","r")
x=f.read().splitlines()
print(len(x)-2)

#stock value prentice james
print(enron_data["PRENTICE JAMES"]["total_stock_value"])

#messages to poi
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

#excercised stock options jeff skilling
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

#largest total_payments
list1 = ["LAY KENNETH L","SKILLING JEFFREY K","FASTOW ANDREW S"]
list2 = [enron_data["LAY KENNETH L"]["total_payments"],enron_data["SKILLING JEFFREY K"]["total_payments"],enron_data["FASTOW ANDREW S"]["total_payments"]]
max_pay = max(list2)
print(max_pay)
for i in range(3):
    if list2[i]==max_pay:
        print(list1[i])

#quantified salary
folks_salary=0
known_email=0
for k,v in enron_data.items():
    if enron_data[k]["salary"]!='NaN':
        folks_salary+=1
    if enron_data[k]["email_address"]!='NaN':
        known_email+=1
print(folks_salary,known_email)

#Nan in total payments
total_payments=0
print(enron_data.items())
print(enron_data["METTS MARK"]["salary"])
for k,v in enron_data.items():
    if enron_data[k]["total_payments"]=='NaN':
        total_payments+=1
print(total_payments)
print(len(enron_data.keys()))
x1 = float(total_payments)/len(enron_data.keys())
print(x1)

        
    

