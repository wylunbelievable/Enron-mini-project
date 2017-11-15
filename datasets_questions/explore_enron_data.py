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

#print "There are %d persons" % len(enron_data)
#print "And there are %d features for everyone" %len(enron_data["SKILLING JEFFREY K"])
#print enron_data['COLWELL WESLEY']


list_of_person = []
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
for key in enron_data:
    list_of_person.append(key)
    if enron_data[key]["poi"] == 1:
        counter_1 += 1
        if enron_data[key]['total_payments'] == 'NaN':
            counter_5 += 1
    if enron_data[key]['salary'] != 'NaN':
        counter_2 += 1
    if enron_data[key]['email_address'] != 'NaN':
        counter_3 += 1
    if enron_data[key]['total_payments'] == 'NaN':
        counter_4 += 1
    
print 'The percent of the persons who have \'NaN\' in their is ', float(counter_4)/list_of_person.__len__()
print 'The percent of the PIOs who have \'Nan\' in their is ', float(counter_5)/float(counter_1)
#print list_of_person
#print '%d have quantified salary' % counter_2 , 'and %d have email address' %counter_3

#print 'There are %d POIs' % counter
#print enron_data['PRENTICE JAMES']
#print 'james Prentice had a total value of stock of %d dollors' % enron_data["PRENTICE JAMES"]["total_stock_value"]    

