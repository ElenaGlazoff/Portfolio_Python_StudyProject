import socket 
#Socket used for connecting two nodes on a network to communicate with each

nameList=[]
##list used for storing elements of different types (integer, float, string, etc.)

Name= "Progect" #value
Count = 0 #values that stores the number of lines in the nameList, how many user int data
while Name != '':
         
         Name=input("Please enter a hostname, press ENTER to quit: ")

         if Name == '' and len (nameList) == 0: #list has nothing
           
                  print("You haven't entered any host names")
                  print("Goodbye")
         
         elif Name != '':
                  nameList.append(Name)
                  Count += 1
#- the append() method appends an element to the end of the list.
#In Python, lists are ordered and each item in a list is associated with a number. The number is known as a list index.
#- the index of the first element is 0, second element is 1 and so on
#- the list index always starts with 0. Hence, the first element of a list is present at index 0, not 1.

if len(nameList) > 0:
        
         hostName ="Project"
         validSelection = True
         while validSelection and hostName != '':
                  for index in range(Count):#An iterator is an object that contains a countable number of values.
                           print(str(index) + " " + nameList[index])
                  hostName = input("Please enter the number of the desired host name, or press ENTER to quit: ")
                  if hostName == '':
                           print("Goodbye")
                  elif "." in hostName:
                           print ("Your number is float")
                           print ("Goodbye")
                           break
                  elif int(hostName) in list(range(Count)):
                           try:
                                    ipadd = socket.gethostbyname(nameList[int(hostName)])
                                    print("IPv4 address for host" " " + nameList[int(hostName)] + " " "is" " " + ipadd)#'int' use for converting data to a 'str', becouse hostName has a number type
                           except:
                                    print("Host name "+ nameList[int(hostName)] +" wasn't valid")
                                    print("Goodbye")
                                    validSelection = False
                  else:
                           print("Invalid selection")
                           print("Goodbye")
                           validSelection = False