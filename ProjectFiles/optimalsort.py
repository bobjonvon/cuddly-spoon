#######################################################################
# Program Name: OptimalSort - Try to decide an optimal sort algorithm #
# Author:       Jonathan Vaughan                                      # 
# Installation: Legacy Outoust - 14445 3C                             #
#  Date Written: May 5, 2020                                          #
#######################################################################

# bring in a list
    #for now a randomly generated list of numbers
# gather info on said list
# put info into an nn and from there decide the estimated best
# time all the options and find out whats best
# put this info into the training set


from random import randrange
from tensorflow.keras.models import load_model
from tensorflow.keras.models import save_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

#######################################################################
#                              Constants                              #
#######################################################################
MAX_LIST_LENGTH           = 1500000 # The maximum length of any list fed 
                                    # through the neural network. 
LARGEST_POSSIBLE_ELEMENT  = 1000000 # The largest number possible in the 
                                    # list 


#######################################################################
#                              MakeList                               #
#######################################################################
def makeList():
    lengthOfList = randrange(MAX_LIST_LENGTH)
    listOfRandoms = []
    for x in range(lengthOfList):
        listOfRandoms.append(randrange(LARGEST_POSSIBLE_ELEMENT))

    return listOfRandoms

#######################################################################
#                          Clean Inputs for NN                        #
#######################################################################
def cleanList(listOfRandoms):
    for x in range(len(listOfRandoms)):
        listOfRandoms[x] = listOfRandoms[x]/LARGEST_POSSIBLE_ELEMENT
    while(len(listOfRandoms) < MAX_LIST_LENGTH):
        listOfRandoms.append(0)
    print(listOfRandoms)
    print(len(listOfRandoms))






#######################################################################
#                                Main                                 #
#######################################################################
def main():
    listOfRandoms = makeList()
    cleanList(listOfRandoms)
    return

main()