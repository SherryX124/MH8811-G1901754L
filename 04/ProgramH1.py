# define new functions

# open, read and close file
def getFileLines(fname) :
    fhandle = open(fname)
    lines = []
    for line in fhandle :
        line = line.rstrip()
        if line :
            lines.append(line)
    fhandle.close()
    return lines

# find minimum value
def my_min(list):
    smallest_so_far = None
    for the_num in list:
        if smallest_so_far is None :
            smallest_so_far = the_num
        elif the_num < smallest_so_far :
            smallest_so_far = the_num
    return smallest_so_far

# find maximum value
def my_max(list):
    largest_so_far = None
    for the_num in list:
        if largest_so_far is None :
            largest_so_far = the_num
        elif the_num > largest_so_far :
            largest_so_far = the_num
    return largest_so_far

# compute average
def my_average(list):
    average = None
    count = 0

    for the_num in list:
        if average is None :
            average = the_num
        else :
            average = (average*count + the_num) / (count+1)
        count = count + 1

    return average

# find median
def my_median(list):
    if len(list) == 0 :
        median = None
    else :
        list.sort()
        r = int(len(list) / 2)
        remainder = len(list) % 2

        if remainder == 1 :
            median = list[r]
        else :
            median = (list[r-1] + list[r]) / 2

    return median

# compute range
def my_range(list) :
    if my_max(list) is None :
        range_ = None
    else :
        range_ = my_max(list) - my_min(list)
    return range_

# compute sample variance
def my_sampleVariance(list) :
    if len(list) == 0 :
        variance = None
    else :
        average = my_average(list)
        sumS = 0
        for the_num in list :
            square = (the_num - average)**2
            sumS = sumS + square
        variance = sumS / (len(list)-1)
    return variance

#--------------------------------------------------------------------------------------
# main program

list = getFileLines('MH8811-04-Data.csv')

# transfer data to int type
for i in range(0,len(list)) :
    list[i] = int(list[i])

print('List:', list)
print('Minimum:', my_min(list))
print('Maximum:', my_max(list))
print('Average:', my_average(list))
print('Median:', my_median(list))
print('Range:', my_range(list))
print('Sample Variance:', my_sampleVariance(list))