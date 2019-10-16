# only allow data type of dictionary and list
# data cannot contain "|" and "," which we use to split
# ---------------------------------------------------------------------
import json
# define new functions  -----------------------------------------------

# json load
def loadData(fname):
    fh = open(fname)
    data = json.load(fh)
    fh.close()
    return data

# read from file
def readFile(fname) :
    fh = open(fname)
    s = fh.read()
    fh.close()
    return s

# write to file
def writeToFile(fname, s) :
    fh = open(fname, 'w')
    fh.write(s)
    fh.close()


def serialize(data) :
    res = ''

    if type(data) == type([]) :
        res = '[]'
        for i in data :
            if isinstance(i, str) :
                # use '' to braket string as a notation (differentiate between 1 and '1')
                res = res + '\'' + i + '\'' + '|'
            else :
                res = res + str(i) + '|'
        res = res.rstrip('|')
        
    elif type(data) == type({}) :
        res = '{}'
        for key in data :
            if isinstance(data[key], str) :
                # use '' to braket string as a notation (differentiate between 1 and '1')
                res = res + key + ',' + '\'' + data[key] + '\'' + '|'
            else :
                res = res + key + ',' + str(data[key]) + '|'
        res = res.rstrip('|')

    return res


# transform string to int/float/string type
def str_intFloatStr(s) :
    try :
        newS = int(s)
    except:
        try :
            newS = float(s)
        except:
            # newS = s.strip('\'')  #<-  use this if content doesn't contain \'
            newS = s[1:len(s)-1]
    return newS


def deserialize(s) :
    res = ''
    # deserialize list
    if s.startswith('[]') :
        # s = s.lstrip('[]')  #<-  use this if content doesn't contain '[]'
        s = s[2:]
        res = list()
        if s != '' :
            lst_of_str = s.split('|')
            for strs in lst_of_str :
                res.append(str_intFloatStr(strs))

    # deserialize dictionary                
    elif s.startswith('{}') :
        # s = s.lstrip('{}')  #<-  use this if content doesn't contain '{}'
        s = s[2:]
        res = dict()
        if s != '' :
            lst_of_str = s.split('|')
            for string in lst_of_str :
                namCou = string.split(',')
                res[namCou[0]] = str_intFloatStr(namCou[1])
    return res


def my_compare(ds1, ds2) :
    result = False

    if type(ds1) == type(ds2) :

        if type(ds1) == type([]) and ds1 == ds2:
            result = True
            
        elif type(ds1) == type({}) and len(ds1) == len(ds2) :
            result = True
            for key in ds1 :
                if ds1[key] != ds2.get(key,0) :
                    result = False

    return result

# main program  ----------------------------------------------------------------

# direct, load and return to the path
filePath = input('Please input the path to the json file (e.g. C:\\...\\05): ')
fileName = input('Please input the name of the file (e.g. H1-1.json): ')
data = loadData(filePath.strip() + '\\' + fileName.strip())


# serialize, write, read and deserialized
serialized = serialize(data)

nameNew = input('Please input a file name for storage: ')
writeToFile(nameNew, serialized)

data2 = readFile(nameNew)

deserialized = deserialize(data2)


# compare the original and deserialized data
if my_compare(data, deserialized) :
    print('Success!')