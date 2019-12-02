#Differential Leveling Computation
#Caroline Bull, Christine Lacanilao, Daniel Noakes

#Import math and csv module
import math
import csv

#################### User defined functions ####################

# Define the funtions to be used to compute differential leveling(Dan)

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



# Display program purpose
print "Welcome to Differential Leveling Calculation Tool"
print "This program uses the benchmark, foresight and backsight measurements"
print "to calculate the instrument height and change in elevation."
print

    #################### Start of input #################### 

# Create a while loop with exception handlers that will run until user does not want to input anymore values or CSV files
try:
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
    

    def main():
        def manualInput():                                  # This Section will compute manual input and print a CSV file with the results #
            
            input_backSight = []                            # create empty list for back sight
            input_foresight = []                            # create empty list for foresight
            input_elevation = []                            # creates an empty list for elevation

            elevation = float(input("Benchmark:")) 
            input_elevation.append(elevation)
            
            while True:
                backSight = float(input("Backsight reading:")) 
                input_backSight.append(backSight) 		        # add backSsight to input_backSight list

                foresight = float(input("Foresight reading:")) 
                input_foresight.append(foresight) 		        # add foreSsight to input_foreSight list

                print
                end = raw_input("Do you want to stop entering values (Y/N)? ") # determine whether user wants to enter another set of input values
                end = end.rstrip("\r")
                print
                if  end.upper() == 'Y' :
                        break

            # Calculations 
            calc_instHeight= []                                 # create empty list for intrument height

            for index in range(0, len(input_elevation)):   	    # index will be 0, 1, 2, ...

                backSight = input_backSight[index]       	    # retrieve backsight in index position from input_backsight list
                foresight = input_foresight[index]              # retrieve foresight in index position from input_foresight list
                elevation = input_elevation[index]              # retrieve elevation in index position from input_elevation list
                instHeight =  calc_instHeight[index]            # retrieve instHeight in index position from calc_instHeight list      

                instHeight = instHeightCalculation(elevation, backSight, instHeight)
                calc_instHeight.append(instHeight)              # add instHeight to calc_instHeight

                elevation = elvCalculation(foresight, instHeight, elevation)
                input_elevation.append(elevation)               # add elevation to input_elevation list
            
            
        ###################### This section will read an imported CSV file and print a new CSV with the results #################################
        # Dan's Section
        def importCSV():
        





            ############################### End of input, start of CSV file calculations #############################################################

            # Dan's Section








        #################### End of input, start of calculations ####################

        #################### End of calculations, Start of outputs ####################

        ############################### This Section will include include our outputs #################################################################

        # Christine's Section

        # print "---------------------------------------------------------------------------------"
        # print


        #Exception Handlers (Dan)
        except:
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