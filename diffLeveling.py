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
       
def elvCalculation(forSight, instHeight, elevation):
        elevation = float(elevation)
        elvation = float(instHeight) - float(forSight)
        round(elevation, 3)
        return elevation


def main():
    # Display program purpose
    print "Welcome to Differential Leveling Computation Tool"
    print


    try:
        while true:
            print "Differential Leveling Computation"

            manualOrCSV = raw_input("Type of computation: manual or csv ") 
            
            # if manualOrCSV = "manual"

            #     if
            #      if
            #
        

            else:









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