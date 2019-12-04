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
try:
    def instHeightCalculation(elevation, backSight):
            instHeight = float(elevation) + float(backSight)
            instHeight = round(instHeight, 3)
            return instHeight
            
        
    def elevCalculation(foresight, instHeight):
            elevation = float(instHeight) - float(foresight)
            elevation = round(elevation, 3)
            return elevation

    # Define the function used to calculate elevation change (Owner: Christine)
    def elevationChange(input_elevation):
            elevationChange = float(input_elevation[0]) - float(input_elevation[-1])
            round(elevationChange, 3)
            return elevationChange

    # try:
        # Main body function  
    def main():
            #Start of inputs #
            # Instantiate all input variables #
            input_benchMark = []        # creates an empty list for the benchmark
            input_backSight = []        # create empty list for back sight
            input_instHeight= []        # create empty list for intrument height
            input_foresight = []        # create empty list for foresight
            input_elevation = []        # create empty list for elevation

            # Display program purpose
            print "Welcome to Differential Leveling Computation Tool"
            print "This program uses the benchmark, foresight and backsight measurements"
            print "to calculate the instrument height and change in elevation."
            print

            # Check if person wants to import CSV ir input manually
            print
            print "Welcome to Differential Leveling Computation Tool"
            print
            print "This program uses the benchmark, foresight and backsight measurements"
            print "to calculate the instrument height and change in elevation."
            print
            print "**************************************"
            print "A. Enter measurements manually"
            print "B. Import a .csv file"
            print "**************************************"
            print

            manualOrCSV = raw_input("Please choose one of the options above to get started (A, B): ") #checks to see if user want to input manually or import a CSV
            if manualOrCSV == "A" or manualOrCSV == "a":
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
                    if  end.upper() == 'N':
                        pass

                    # Calculations 
                    calc_instHeight= []        # create empty list for intrument height

                    for index in range(0, len(input_backSight)):   	    # index will be 0, 1, 2, ...

                        backSight = input_backSight[index]       	    # retrieve backsight in index position from input_backsight list
                        foresight = input_foresight[index]          
                        elevation = input_elevation[index]               

                        instHeight = instHeightCalculation(elevation, backSight)
                        calc_instHeight.append(instHeight)                    # add 

                        elevation = elevCalculation(instHeight, foresight)
                        input_elevation.append(elevation)  
                    print "Backsight\t Instrument Height\tForesight\tElevation"
                    print 0, 0, 0, input_elevation[index]
                        
                    for index in range(1,len(input_elevation)):         # index will be 0, 1, 2, ...
                        print input_backSight[index-1], calc_instHeight[index-1], input_foresight[index-1], input_elevation[index]
                        print "Elevation Change", elevationChange(input_elevation)
                    break

            else:
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
                        # retrieves the variable in a specific index from the input list
                for index in range(0, len(input_elevation) -1 ):
                    elevation = float(input_elevation[index])
                    foresight = float(input_foresight[index + 1])
                    backSight = float(input_backSight[index])
                    benchMark = float(input_benchMark[index])
                    
                    intrumentHeight = instHeightCalculation(elevation, backSight)
                    input_instHeight[index] = intrumentHeight

                    groundElevation = elevCalculation(foresight, intrumentHeight)
                    input_elevation[index + 1 ] = groundElevation

                    importCSV_write = open('CSVOutputs.csv', 'w')
                importCSV_write.write('BenchMark, BackSight, InstrumentHeight, Foresight, Elevation\n')

                # output loop
                for index in range(0, len(input_elevation)):
                    importCSV_write.write( str(input_benchMark[index]) + "," + str(input_backSight[index]) \
                        + "," + str(input_instHeight[index]) + "," + str(input_foresight[index]) + "," + str(input_elevation[index]) + '\n' )
                
                    end = raw_input("Would you like to import another CSV file?(Y/N): ")
                    end = end.upper()
                    end = end.rstrip("\r")
                
                    if end == "Y":
                        pass
                    else: 
                        print "Thanks for using the program. Your CSV(s) has been printed to a file. "
                        break
        

    if __name__ == "__main__":
        main()

# except Exception, message:
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