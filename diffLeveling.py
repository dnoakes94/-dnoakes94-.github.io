# diffLeveling.py

# Differential Leveling Computation

# Caroline Bull, Christine Lacanilao, Daniel Noakes

# Calculate elevation given a starting elevation point, and entered backsight and foresight values
# The user is given the option to do a manual entry or to import a csv
# The program returns a report in the form of a text file for the user.

# Import math and csv module
import math
import csv
import itertools

############################## User Created Functions ##############################

# Define the funtions to be used to compute differential leveling CSV Import (Owner: Dan)

def instHeightCalculation(elevation, backSight):
        instHeight = float(elevation) + float(backSight)
        instHeight = round(instHeight, 3)
        return instHeight
        
      
def elevCalculation(foresight, instHeight):
        elevation = float(instHeight) - float(foresight)
        elevation = round(elevation, 3)
        return elevation

# Define the functions to be used to compute differential leveling manually (Owner: Caroline)
def manualInput():
        input_backSight = []        # create empty list for back sight
        input_foresight = []        # create empty list for foresight
        input_elevation = []        # creates an empty list for elevation

        elevation = float(input("Benchmark:")) 
        input_elevation.append(elevation)

# Define the function used to calculate elevation change (Owner: Christine)
def elevationChange(elevation):
        elevationChange = float(elevation[0]) - float(elevation[-1])
        round(elevationChange, 3)
        return elevationChange

# Main body function

def main():
        # Display program purpose
        print "Welcome to Differential Leveling Computation Tool"
        print "This program uses the benchmark, foresight and backsight measurements"
        print "to calculate the instrument height and change in elevation."
        print

        while True:
            print "Differential Leveling Calculator"
            print
            print "******************************************"
            print "A. Enter measurements manually"
            print "B. Import a .csv file"
            print "C. Exit"
            print "******************************************"
        ("Type of input: manualInput or importCSV ")
        
        manualOrCSV = raw_input("Please choose one of the options above to get started (A, B, C): ") #checks to see if user want to input manually or import a CSV
        if manualOrCSV == "A" or manualOrCSV == "a":
            manualInput()
        elif manualOrCSV == "B" or choice == "b":
            importCSV()
        else:
            print ("Exiting")




############################## Start of inputs ##############################

    # #----- Import CSV Input -----#
    # # Lists to hold file input from the CSV
    #     input_benchMark = []        # creates an empty list for the benchmark
    #     input_backSight = []        # create empty list for back sight
    #     input_instHeight= []        # create empty list for intrument height
    #     input_foresight = []        # create empty list for foresight
    #     input_elevation = []        # create empty list for elevation
    
    #     importCSV = open("TextDoc.csv", "r")

    
    #     firstline = True
    #     for strRead in importCSV:
    #         if firstline:
    #             firstline = False
    #             continue
            
    #         strLst = strRead.split(",")
        
    #         benchMark = strLst[0]
    #         input_benchMark.append(benchMark)           # add benchMark to input_benchMark list

    #         backSight = strLst[1]
    #         input_backSight.append(backSight) 	        # add backSight to input_backSight list
            
    #         instHeight = strLst[2]
    #         input_instHeight.append(instHeight) 	    # add instHeight to input_instHeight list
            
    #         foresight = strLst[3]
    #         input_foresight.append(foresight) 		    # add foresight to input_foresight list

    #         elevation = strLst[4]                       # add elevation to input_elevation list
    #         elevation = elevation.rstrip('\n')
    #         input_elevation.append(elevation)

    #     importCSV.close()

    #----- Manual Entry Input -----#
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


######################## End of input, Start of calculations ##########################
    
    #-------------------- Calculation for CSV Input (Owner: Dan) --------------------#
    
    # creates an empty list for the calcualted elevation, intrument height, error of closure and generates a unique ID
    #calc_instHeight = []
    #calc_elevation = []
    #calc_errOfClosure = []
    #elevationChange = []

    # # retrieves the variable in a specific index from the input list
    #     for index in range(0, len(input_elevation) -1 ):
    #         elevation = float(input_elevation[index])
    #         foresight = float(input_foresight[index + 1])
    #         backSight = float(input_backSight[index])
    #         benchMark = float(input_benchMark[index])
            
    #         intrumentHeight = instHeightCalculation(elevation, backSight)
    #         input_instHeight[index] = intrumentHeight

    #         groundElevation = elevCalculation(foresight, intrumentHeight)
    #         input_elevation[index + 1 ] = groundElevation


    #-------------------- Calculations for Manual Input (Owner: Caroline) --------------------#
    

        calc_instHeight= []        # create empty list for intrument height

        for index in range(0, len(input_elevation)):   	    # index will be 0, 1, 2, ...

                backSight = input_backSight[index]       	    # retrieve backsight in index position from input_backsight list
                foresight = input_foresight[index]          
                elevation = input_elevation[index] 
                instHeight =  calc_instHeight[index]                 

                instHeight = instHeightCalculation(elevation, backSight)
                calc_instHeight.append(instHeight)                    # add 

                elevation = elvCalculation(instHeight, foresight)
                input_elevation.append(elevation)                     # add    
                print calc_instHeight


    # Create a while loop with exception handlers that will run until user does not want to input anymore values or CSV files
        while True:
            print "Differential Leveling Calculator"
            print
            print "******************************************"
            print "A. Enter measurements manually"
            print "B. Import a .csv file"
            print "C. Exit"
            print "******************************************"
        ("Type of input: manualInput or importCSV ")
        
        manualOrCSV = raw_input("Please choose one of the options above to get started (A, B, C): ") #checks to see if user want to input manually or import a CSV
        if manualOrCSV == "A" or manualOrCSV == "a":
            manualInput()
        elif manualOrCSV == "B" or choice == "b":
            importCSV()
        else:
            print ("Exiting")
    

    ######################## End of input, Start of calculations ##########################
    
    # # list to hold calculated results
    #     calc_elevationChange = []                           #create empty list for elevation change

    #     elevation_Change = elevation_Change(elevation)
    #     calc_elevationChange.append(elevation_Change)       #add elevation change to calc_elevationChange list


    #     importCSV = open("TextDoc.csv", "r")

    #     firstline = True
    #     for strRead in importCSV:
    #         if firstline:
    #             firstline = False
    #             continue
            
    #         strLst = strRead.split(",")

    #         benchMark = strLst[0]
    #         input_benchMark.append(benchMark)           # add benchMark to input_benchMark list

    #         backSight = strLst[1]
    #         input_backSight.append(backSight) 	        # add backSight to input_backSight list
            
    #         instHeight = strLst[2]
    #         input_instHeight.append(instHeight) 	    # add instHeight to input_instHeight list
            
    #         foresight = strLst[3]
    #         input_foresight.append(foresight) 		    # add foresight to input_foresight list

    #         elevation = strLst[4]                       # add elevation to input_elevation list
    #         elevation = elevation.rstrip('\n')
    #         input_elevation.append(elevation)

    #     importCSV.close()

    ######################## End of calculations, Start of outputs ###########################

    ############################### This Section will include include our outputs #################################################################

    #-------------------- CSV Import Outputs --------------------#

        # importCSV_write = open('CSVOutputs.csv', 'w')
        # importCSV_write.write('BenchMark, BackSight, InstrumentHeight, Foresight, Elevation\n')

        # # output loop
        # for index in range(0, len(input_elevation)):
        #     importCSV_write.write( str(input_benchMark[index]) + "," + str(input_backSight[index]) \
        #         + "," + str(input_instHeight[index]) + "," + str(input_foresight[index]) + "," + str(input_elevation[index]) + '\n' )
        
        # end = raw_input("Would you like to import another CSV file or input caculations manually?(Y/N): ")
        # end = end.upper()
        # end = end.rstrip("\r")
        
        # if end == "N":
        #     print "Thanks for using the program!"
        #     break
    
    #-------------------- Manual Entry Outputs --------------------#

        print "---------------------------------------------------------------------------------"
        print
    
    # This should display all the gathered inputs and calculations in a table format
    # Display column header line
        print "Benchmark\tBackSight\tInstrument Height\t ForeSight\tElevation"

    # Display benchmark, backsight, instrument height, foresight, and elevation lists in table format
        for index in range(0, len(input_benchmark)):        # index will be 0, 1, 2, ...
        # print benchmark, backsight, instrument height, foresight, and elevation from lists
        # formated to three decimals with decimals aligned
            print input_benchmark[index], "\t", "\t", input_backSight[index], "\t", "\t", input_instHeight[index], "\t", "\t", input_foreSight[index], "\t", "\t", input_elevation[index]


        print "---------------------------------------------------------------------------------"
        print

    # Display elevation change
    # print elevation change from list
    # formatted to three decimal places
        print "The elevation change for your inputs is: ", calc_elevationChange[index]

    # Based on the generated inputs and calculations from the above table, generate a text file with it
    # Output for csv 
        fo1 = open('ManualOutput.txt', 'w')
        fo1.write("Benchmark"+"\t\t"+"Backsight"+"\t\t"+"Instrument Height"+"\t\t"+"Foresight"+"\t\t"+"Elevation"+"\t\n")
        for index in range(0, len(input_benchmark)):
            # Create new list for each item, convert to strings
            newLst = str(input_benchmark[index]) + "\t\t\t\t" + str(input_backSight[index]) + "\t\t\t\t" + str(listinput_instHeight[index]) + "\t\t\t\t" + str(input_foreSight[index]) + "\t\t" + str(listinput_foreSight[index]) + "\t\n"
            fo1.write(newLst)                                  #Write each item to a new list
        fo1.close()

        print
        print "Done"


######################## End of outputs ###########################


# Exception handlers (Dan)
# Exeption handlers for errors
# except Exception, message:
#     print "An error occured. Please try again."
#     print message

# except NameError:
#     print "Variable is not found in local space. Please try again."

# except IndexError:
#     print "Index of a sequence is out of range. Please try again."

# except TypeError:
#     print "You cant add strings and integers. Please try again."

# except ValueError:
#     print "Value must be a number. Please try again."

# except ZeroDivisionError:
#     print "You can't divide by zero. Please try again."

if __name__ == "__main__":
    main()