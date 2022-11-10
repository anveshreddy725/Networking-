<<<<<<< HEAD
from cryptoHash import sha256

def readData_fromFile(nameOftheFile):
    myReadblefile = open("data.txt", "r")


    dataList = myReadblefile.readlines()

#closing the file
    myReadblefile.close()
#itterate through list
    for line in dataList:
    #printing 
        print(line)



def writeData_toFile(ouputFileName, dataList):
    myWritableFile = open('output.txt', 'w')

#ittrearting through the list
    for line in dataList:
    #writing a string to a file
        myWritableFile.write(line)

#writing multiple strings at atime
    myWritableFile.writelines("Additional Data")



#close
    myWritableFile.close()




dataList= readData_fromFile("data.txt")

outList = []
for data in dataList:
    hash = sha256(data)
    print(hash)

    length = len(hash)
    print(length)

    outList.append(hash)

=======
from cryptoHash import sha256

def readData_fromFile(nameOftheFile):
    myReadblefile = open("data.txt", "r")


    dataList = myReadblefile.readlines()

#closing the file
    myReadblefile.close()
#itterate through list
    for line in dataList:
    #printing 
        print(line)



def writeData_toFile(ouputFileName, dataList):
    myWritableFile = open('output.txt', 'w')

#ittrearting through the list
    for line in dataList:
    #writing a string to a file
        myWritableFile.write(line)

#writing multiple strings at atime
    myWritableFile.writelines("Additional Data")



#close
    myWritableFile.close()




dataList= readData_fromFile("data.txt")

outList = []
for data in dataList:
    hash = sha256(data)
    print(hash)

    length = len(hash)
    print(length)

    outList.append(hash)

>>>>>>> b6de8fe534019f087940b43791f09b2c609938c3
writeData_toFile("ouput.txt", outList)