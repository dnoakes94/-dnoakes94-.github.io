#Differential Leveling Computation
#Caroline Bull, Christine Lacanilao, Daniel Noakes

#Import math and csv module
import math
import csv
import itertools

def instHeightCalculation(elevation, backSight):
        instHeight = float(elevation[0]) + float(backSight[0])
        round(instHeight, 3)
        return instHeight
        
      
def elevCalculation(foresight, instHeight):
        elevation = float(instHeight[0]) - float(foresight[1])
        round(elevation, 3)
        return elevation


## should equal to 0
# def errorOfClosure(foresight, backSight):
#         check = sum(input_foresight) - sum(input_backSight)
#         return check

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

  
    # if input_instHeight < 1:
    #     elevCalculation = True

    #else:
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

############################### End of input, start of CSV file calculations #############################################################

    # creates an empty list for the calcualted elevation, intrument height, error of closure and generates a unique ID
    calc_instHeight = []
    calc_elevation = []
    #calc_errOfClosure = []
    #elevationChange = []


    # retrieves the variable in a specific index from the input list
    for index in range(0, len(input_elevation)):
        instHeight = float(input_instHeight[0])
        elevation = float(input_elevation[0])
        foresight = float(input_foresight[1])
        backSight = float(input_backSight[0])
        benchMark = float(input_benchMark[index])
        
        intrumentHeight = instHeightCalculation(elevation, backSight)
        calc_instHeight.append(intrumentHeight)

        groundElevation = elevCalculation(foresight,instHeight)
        calc_elevation.append(groundElevation)

        if index = index + 1:
            break


############################### This Section will include include our outputs #################################################################

    importCSV_write = open('CSVOutputs.csv', 'w')
    importCSV_write.write = ('UniqueID, BenchMark, BackSight, InstrumentHeight, ForeSight, Elevation\n')

    # output loop
    for index in range(0, len(input_elevation)):
        importCSV_write.write = (str(benchMark[index]) + "," + str(input_backSight[index]) \
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