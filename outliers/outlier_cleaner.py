#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    print 'ages: ', ages

    ### your code goes here
    import numpy as np
    k = len(predictions)
    errors = np.empty((1, k))
   #print 'The errors: ', errors
    #print 'np.sqrt(np.square(net_worths - predictions[i]))', np.sqrt(np.square(net_worths - predictions[1]))
    #errors = []
    for i in range(k) :
        
        errors[0][i] = np.sqrt(np.square(net_worths[i] - predictions[i]))
    print 'errors: ', errors
    sortedIndex = errors.argsort()
    #print 'sortedIndex: ', sortedIndex[0][3]
    #print ' ages[sortedIndex[i]][0]: ', ages[sortedIndex[1]][1][0]
    for i in range(int(0.9 * k)):
        cleaned_data.append((ages[sortedIndex[0][i]][0], net_worths[sortedIndex[0][i]][0], errors[0][sortedIndex[0][i]]))
    #print 'cleaned_data: ', cleaned_data
    return cleaned_data

