#Differential Leveling Computation
#Caroline Bull, Christine Lacanilao, Daniel Noakes

#Import math and csv module
import math
import csv

#write helper files first
#anything that will read or write

def instHeightCalculation(instHeight, elevation, backSight):
        instHeight = float(instHeight)
        instHeight = float(elevation) + float(bckSight)
        round(instHeight, 3)
        return instHeight
       
def elvCalculation(foreSight, instHeight, elevation):
        elevation = float(elevation)
        elvation = float(instHeight) - float(foreSight)
        round(elevation, 3)
        return elevation


def main():
    # Display program purpose
    print "Welcome to Differential Leveling Computation Tool"
    print

    # Create a while loop with exception handlers that will run until user does not want to input anymore values or CSV files
    try:
        while true:
            print "Differential Leveling Computation"

            manualOrCSV = raw_input("Type of computation: manualInput or importCSV ") #checks to see if user want to input manually or import a CSV
            
            ######################## This Section will compute manual input and print a CSV file with the results ################################

           







            ###################### This section will compute an imported CSV file and print a new CSV with the results #################################



            else:
                importCSV = open("DiffLeveling.csv")

                input_instHeight= []        # create empty list for intrument height
                input_elevation = []        # create empty list for elevation
                input_backSight = []        # create empty list for back sight
                input_foreSight = []         # create empty list for fore sight





            ############################### This Section will include include our outputs #################################################################




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