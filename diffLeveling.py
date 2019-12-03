#Differential Leveling Computation
#Caroline Bull, Christine Lacanilao, Daniel Noakes

#Import math and csv module
import math
import csv

#################### User defined functions ####################

# Define the funtions to be used to compute differential leveling(Dan)

def instHeightCalculation(elevation, backSight):
        instHeight = float(elevation) + float(backSight)
        round(instHeight, 3)
        return instHeight
       
def elvCalculation(instHeight, foresight):
        elevation = float(instHeight) - float(foresight)
        round(elevation, 3)
        return elevation

# This function should should calculate elevation change between the initial elevation and the final calculated elevation from the list
def elevationChange(elevation):                                                             
        elevationChange = float(elevation[0]) - float(elevation[-1])              #I think this is how we can calculate elevationChange
        elevationChange = round(elevationChange, 3)
        return elevationChange

#Caroline's Section

def manualInput():
    input_backSight = []        # create empty list for back sight
    input_foresight = []        # create empty list for foresight
    input_elevation = []        # creates an empty list for elevation

    elevation = float(input("Benchmark:")) 
    input_elevation.append(elevation)
    
    while True:
        backSight = float(input("Backsight reading:")) 
        input_backSight.append(backSight) 		        # add

        foresight = float(input("Foresight reading:")) 
        input_foresight.append(foresight) 		        # add

        print
        # determine whether user wants to enter another set of input values
        end = raw_input("Do you want to stop entering values (Y/N)? ")
        end = end.rstrip("\r")
        print
        if  end.upper() == 'Y':
            break

    # Calculations 
    calc_instHeight= []        # create empty list for intrument height

    for index in range(0, len(input_backSight)-1):   	    # index will be 0, 1, 2, ...

        backSight = input_backSight[index]       	    # retrieve backsight in index position from input_backsight list
        foresight = input_foresight[index+1]          
        elevation = input_elevation[index]               

        instHeight = instHeightCalculation(elevation, backSight)
        calc_instHeight.append(instHeight)                    # add 

        elevation = elvCalculation(instHeight, foresight)
        input_elevation.append(elevation)                     # add 
    for index in range(0,len(input_elevation)):         # index will be 0, 1, 2, ...
        print "Backsight\t Instrument Height\tForesight\tElevation"
        print input_backSight[index], calc_instHeight[index], input_foresight[index], input_elevation[index]
        print elevationChange 

def importCSV():
    #Dan's section here 

def main():
    # Display program purpose
    print "Welcome to Differential Leveling Calculation Tool"
    print "This program uses the benchmark, foresight and backsight measurements"
    print "to calculate the instrument height and change in elevation."
    print

    # #################### Start of input ####################

    # # Create a while loop with exception handlers that will run until user does not want to input anymore values or CSV files
    try:
        while True:
            print "Differential Leveling Calculator"
            print ("Type of input: manualInput or importCSV ")
            print "******************************************"
            print "A. Enter measurements manually"
            print "B. Import a .csv file"
            print "C. Exit"
            print "******************************************"
            print 
            manualOrCSV = raw_input("Please choose one of the options above to get started (A, B, C): ") #checks to see if user want to input manually or import a CSV
            manualOrCSV= manualOrCSV.rstrip("\r")
            print
            if manualOrCSV.upper() == "A":
                manualInput()
                print ("Done.")
            elif manualOrCSV.upper() == "B":
                importCSV()
            else:
                print "Exiting"
                break
    except:
        print ("an exception occurred.") 
main()
