#Differential Leveling Computation
#Caroline Bull, Christine Lacanilao, Daniel Noakes

#Import math and csv module
import math
import csv

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

#try: 

def main():
    # Display program purpose
    print "Welcome to Differential Leveling Computation Tool"
    print

    # Lists to hold file input from the CSV
    input_instHeight= []        # create empty list for intrument height
    input_elevation = []        # create empty list for elevation
    input_backSight = []        # create empty list for back sight
    input_foresight = []        # create empty list for foresight
    input_benchMark = []        # creates an empty list for the benchmark

    importCSV = open("test.csv", "r")


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

    calc_instHeight = []                # empty list for calculated intrument height
    calc_elevation = []                 # empty list for calculated elevation
    #calc_errOfClosure = []              # empty list for error of closure
    objectID = []                       # empty list for unique object ID's
    uniqueID = 0

    for index in range(0, len(input_elevation)):   	        # index will be 0, 1, 2, ...
        elevation = input_elevation[index]       	        # retrieve elevation in index position from input_elevation list
        instHeight = input_instHeight[index]                # retrieve instHeight in index position from input_instHeight list
        foresight = input_foresight[index]                  # retrieve foresight  in index position from input_foresight  list
        backSight = input_backSight[index]                  # retrieve backsight in index position from input_foresight list
        benchMark = input_benchMark[index]                  # retrieve benchMark in index position from input_benchmark list

    groundElevation = elvCalculation(foresight, instHeight, elevation)
    calc_elevation.append(groundElevation)

    intrumentHeight = instHeightCalculation(instHeight, elevation, backSight)
    calc_instHeight.append(intrumentHeight)

    # Give the new CSV rows a unique ID
    uniqueID += 1
    objectID.append(uniqueID)
    

############################### This Section will include include our outputs #################################################################

    importCSV_write = open('CSVOuputs', 'w')
    importCSV_write.write = ('UniqueID, BenchMark, BackSight, InstrumentHeight, ForeSight, Elevation\n')

    #output loop
    for index in range(0, len(input_elevation)):
        importCSV_write.write = (str(objectID[index]) + "," + str(benchMark[index]) + "," + str(input_backSight[index]) \
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