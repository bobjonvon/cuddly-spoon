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

#######################################################################
#                              MakeList                               #
#######################################################################
def makeList():
    lengthOfList = randrange(1500000)
    listOfRandoms = []
    for x in range(lengthOfList):
        listOfRandoms.append(randrange(1000000))

    return listOfRandoms

#######################################################################
#                          Gather List Data/nn inputs                 #
#######################################################################
#gathered data should enclude
#length
#number of repeating variables
#unless i can just input the full list





#######################################################################
#                                Main                                 #
#######################################################################
def main():
    listOfRandoms = makeList()
    return

main()