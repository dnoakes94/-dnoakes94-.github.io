#Differential Leveling Computation
#Caroline Bull, Christine Lacanilao, Daniel Noakes

#Import math and csv module
import math
import csv

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

#def elevationChange()
# im confused with how we will do this

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

           #Caroline's Section







            ###################### This section will compute an imported CSV file and print a new CSV with the results #################################

            # Dan's Section






            ############################### End of input, start of CSV file calculations #############################################################

            # Dan's Section









            ############################### This Section will include include our outputs #################################################################

            # Christine's Section




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