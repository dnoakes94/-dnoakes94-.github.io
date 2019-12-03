# diffLeveling.py
#Differential Leveling Computation
#Caroline Bull, Christine Lacanilao, Daniel Noakes
#Calculated the elevation 

#Import math and csv module
import math
import csv

#write helper files first
#anything that will read or write

############################## User Created Functions ##############################

def instHeightCalculation(instHeight, elevation, backSight):
        instHeight = float(instHeight)
        instHeight = float(elevation) + float(backSight)
        round(instHeight, 3)
        return instHeight
       
def elvCalculation(foresight, instHeight, elevation):
        elevation = float(elevation)
        elevation = float(instHeight) - float(foresight)
        round(elevation, 3)
        return elevation

#     #should equal to 0
# def errorOfClosure(foresight, backSight):
#         check = sum(input_foresight) - sum(input_backSight)
#         return check

#This function should should calculate elevation change between the initial elevation and the final calculated elevation from the list
def elevationChange(elevation):                                                             
        elevationChange = float(elevation[0]) - float(elevation[-1])              #I think this is how we can calculate elevationChange
        round(elevationChange, 3)
        return elevationChange

def main():
    # Display program purpose
    print "Welcome to Differential Leveling Computation Tool"
    print

    ############################## Start of inputs ##################################

    # lists to hold file input
    input_benchmark = []                    #create empty iist for benchmark
    input_instHeight = []                   # create empty list for intrument height
    input_elevation = []                    # create empty list for elevation
    input_backSight = []                    # create empty list for back sight
    input_foreSight = []                    # create empty list for foresight

    # obtain inputs from user

    # Create a while loop with exception handlers that will run until user does not want to input anymore values or CSV files
    try:
        while True:
            print "Differential Leveling Computation"

            manualOrCSV = raw_input("Type of computation: manualInput or importCSV ") #checks to see if user want to input manually or import a CSV
            
            ######################## This Section will compute manual input and print a CSV file with the results ################################

           #Caroline's Section







            ###################### This section will compute an imported CSV file and print a new CSV with the results #################################

            # Dan's Section


    



            ############################### End of input, start of CSV file calculations #############################################################

            # Dan's Section


    ######################## End of input, Start of calculations ##########################
    
    # list to hold calculated results



    ######################## End of calculations, Start of outputs ###########################

    ############################### This Section will include include our outputs #################################################################

    # Christine!

    print "---------------------------------------------------------------------------------"
    print

    # This should display all the gathered inputs and calculations in a table format
    # Display column header line
    print "Station Number\tBackSight\tInstrument Height\t ForeSight\tElevation"

    # Display station number, backsight, instrument height, foresight, and elevation lists in table format
    for index in range(0, len(input_benchmark)):        # index will be 0, 1, 2, ...
    # print station number, backsight, instrument height, foresight, and elevation from lists
    # formated to three decimals with decimals aligned
        print 

    # Based on the generated inputs and calculations from the above table, generate a text file with it
    #Output for csv 
    fo1 = open('Output.txt', 'w')
    fo1.write("Station Number"+"\t\t"+"Backsight"+"\t\t"+"Instrument Height"+"\t\t"+"Foresight"+"\t\t"+"Elevation"+"\t\n")
    for index in range(0, len(input_centralpress)):
        #Create new list for each item, convert to strings
        newLst = str(list) + "\t\t\t\t" + str(list) + "\t\t\t\t" + str(list) + "\t\t\t\t" + str(list) + "\t\t" + str(list) + "\t\n"
        fo1.write(newLst)                                  #Write each item to a new list
    fo1.close()

    ######################## End of outputs ###########################

    #Exception Handlers (Dan)

    #exeption handlers for errors
    except Exception, message:
        print "An error occured. Please try again."
        print message

    except NameError:
        print "Variable is not found in local space. Please try again."

    except IndexError:
        print "Index of a sequence is out of range. Please try again."

    except TypeError:
        print "You cant add strings and integers. Please try again."

    except ValueError:
        print "Value must be a number. Please try again."

    except ZeroDivisionError:
        print "You can't divide by zero. Please try again."

if __name__ == "__main__":
    main()