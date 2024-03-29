#Differential Leveling Computation
#Caroline Bull, Christine Lacanilao, Daniel Noakes

#Import math and csv module 
import math
import csv
import itertools


def instHeightCalculation(elevation, backSight):
        instHeight = float(elevation) + float(backSight)
        instHeight = round(instHeight, 3)
        return instHeight
        
      
def elevCalculation(foresight, instHeight):
        elevation = float(instHeight) - float(foresight)
        elevation = round(elevation, 3)
        return elevation


## should equal to 0
# def errorOfClosure(foresight, backSight):
#         check = sum(input_foresight) - sum(input_backSight)
#         return check

# Get user to enter reference elevation and have the calulation subtract the final elevation
# have the first elevation reverence elevation (bm1) ask user what the final elevation was 
# def elevationChange(): 
#         elevationChange = float(elevation[0]) - float(elevation[-1])
#         round(elevationChange, 3)
#         return elevationChange

#try:

def main():
    # Display program purpose
    print "Welcome to Differential Leveling Computation Tool"
    print

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

############################### End of input, start of CSV file calculations (Completed By Dan) #############################################################

    # creates an empty list for the calcualted elevation, intrument height, error of closure and generates a unique ID
    #calc_instHeight = []
    #calc_elevation = []
    #calc_errOfClosure = []
    #elevationChange = []


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


############################### This Section will include include our outputs (Completed by Dan) #################################################################

    importCSV_write = open('CSVOutputs.csv', 'w')
    importCSV_write.write('BenchMark, BackSight, InstrumentHeight, Foresight, Elevation\n')

    # output loop
    for index in range(0, len(input_elevation)):
        importCSV_write.write( str(input_benchMark[index]) + "," + str(input_backSight[index]) \
            + "," + str(input_instHeight[index]) + "," + str(input_foresight[index]) + "," + str(input_elevation[index]) + '\n' )

if __name__ == "__main__":
    main()
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