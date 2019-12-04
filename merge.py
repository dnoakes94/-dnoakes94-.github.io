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
       
def elevCalculation(instHeight, foresight):
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

    elevation = float(input("Benchmark:___")) 
    input_elevation.append(elevation)
    
    while True:
        backSight = float(input("Backsight reading:___")) 
        input_backSight.append(backSight) 		        # add

        foresight = float(input("Foresight reading:___")) 
        input_foresight.append(foresight) 		        # add

        print
        # determine whether user wants to enter another set of input values
        end = raw_input("Do you want to stop entering values (Y/N)?___ ")
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

        elevation = elevCalculation(instHeight, foresight)
        input_elevation.append(elevation)                     # add 
   
    for index in range(0,len(input_elevation)):         # index will be 0, 1, 2, ...
        print "Backsight\t Instrument Height\tForesight\tElevation"
        print input_backSight[index], calc_instHeight[index], input_foresight[index], input_elevation[index]
        print elevationChange 


def importCSV():
    # Lists to hold file input from the CSV
    input_benchMark = []        # creates an empty list for the benchmark
    input_backSight = []        # create empty list for back sight
    input_instHeight= []        # create empty list for intrument height
    input_foresight = []        # create empty list for foresight
    input_elevation = []        # create empty list for elevation

    importCSV = open("TextDoc.csv", "r")

    firstline = True
    for strRead in importCSV:
        if firstline:
            firstline = False
            continue
        
        strLst = strRead.split(",")

        benchMark = strLst[0]
        input_benchMark.append(benchMark)           # add benchMark to input_benchMark list

        backSight = strLst[1]
        input_backSight.append(backSight) 	        # add backSight to input_backSight list
        
        instHeight = strLst[2]
        input_instHeight.append(instHeight) 	    # add instHeight to input_instHeight list
        
        foresight = strLst[3]
        input_foresight.append(foresight) 		    # add foresight to input_foresight list

        elevation = strLst[4]                       # add elevation to input_elevation list
        elevation = elevation.rstrip('\n')
        input_elevation.append(elevation)

    importCSV.close()

        
        ################## This section will read an imported CSV file and print a new CSV with the results (Dans Section) ########################

        # retrieves the variable in a specific index from the input list
    for index in range(0, len(input_elevation) -1 ):
        instHeight = float(input_instHeight[index])
        elevation = float(input_elevation[index])
        foresight = float(input_foresight[index + 1])
        backSight = float(input_backSight[index])
        benchMark = float(input_benchMark[index])
        
        instHeight = instHeightCalculation(elevation, backSight)
        input_instHeight[index] = instHeight

        elevation = elevCalculation(instHeight, foresight)
        input_elevation[index] = elevation

    
    ########################## This Section will include include our CSV import outputs (Dan's Section) #####################################################

    importCSV_write = open('CSVOutputs.csv', 'w')
    importCSV_write.write('BenchMark, BackSight, InstrumentHeight, Foresight, Elevation\n')

    # output loop
    for index in range(0, len(input_elevation)):
        importCSV_write.write( str(input_benchMark[index]) + "," + str(input_backSight[index]) \
            + "," + str(input_instHeight[index]) + "," + str(input_foresight[index]) + "," + str(input_elevation[index]) + '\n' )
            
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
            manualOrCSV = raw_input("Please choose one of the options above to get started (A, B, C): ___") #checks to see if user want to input manually or import a CSV
            manualOrCSV= manualOrCSV.rstrip("\r")
            print
            if manualOrCSV.upper() == "A":
                manualInput()
                print ("Done.")
            elif manualOrCSV.upper() == "B":
                importCSV()
                print ("Done.")
            else:
                print "Exiting"
                break
    except:
        print ("an exception occurred.") 
main()