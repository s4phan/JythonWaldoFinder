from time import clock #Imported a clock so it would be easier to keep track of how long program takes
tinyscene = makePicture(r'D:\\Desktop\\CPS109\\assignment 2\\tinyscene.jpg')
tinywaldo = makePicture(r'D:\\Desktop\\CPS109\\assignment 2\\tinywaldo.jpg')
scene = makePicture(r'D:\\Desktop\\CPS109\\assignment 2\\scene.jpg')
waldo = makePicture(r'D:\\Desktop\\CPS109\\assignment 2\\waldo.jpg')
#Question 1:
def compareOne(template,searchImage,x1,y1):
  #grayscale(template)   
  #grayscale(searchImage) 
  sum=0 #sum for the absolute differences
  i=0
  j=0  #i and j are the counters for the template
  for y in range(y1,y1+getHeight(template),1):
    for x in range(x1,x1+getWidth(template),1): 
      pixelimage = getPixel(searchImage,x,y) #the searchimage starts at the given x and y
      pixeltemplate = getPixel(template,i,j) #template has to start at 0,0 because it has to start comparing from the first pixel in the template.
      sum+=abs(getRed(pixelimage)-getRed(pixeltemplate)) #gets the abs difference and adds it to a continuance sum 
      i+=1 #increments for the template so it can go through the entire template.
    j+=1
    i=0
  return sum #returns total sum
  
#Question 2:
def compareAll(template,searchImage):
  grayscale(template)
  grayscale(searchImage)
  W = getWidth(searchImage)
  H = getHeight(searchImage)
  matrix = [[300000 for i in range(W)] for j in range(H)] #500,000 is just the random number i chose for the default value of the matrix.
  for y in range(0,H-getHeight(template)):  #i decided to subtract the template height and width from the matrix because if the range of the compareAll loop stops at the last pixel
    for x in range(0,W-getWidth(template)): #before the template goes over the edge to avoid the undefined region error, i should apply the same concept to the matrix to avoid creating a unnecessary larger matrix which would slow the program down.
      L = compareOne(template,searchImage,x,y) #assigns a variable to the compareOne function
      matrix[y][x] = L #L is the returned value from CompareOne and is added to the matrix.
  return matrix
    
#Question 3:
def find2Dmin(matrix):
  list = [] #creates a list to store the minimum of every matrix
  for i in range(0,len(matrix),1):  #i was playing around with how the min() function works with matrixes and realized that it only returns the minimum of the first matrix   
    minimum = min(matrix[i]) # knowing that i created a loop to go through every matrix and return the minimum
    list.append(minimum) #appended each matrix minimum to a list.
  trueminimum = min(list) #knowing that the list contained every minimum of each matrix, if i find the minimum in the list, it would return the TRUE minimum throughout all matrix
  mincol = list.index(trueminimum) #Now that i have the true minimum, since the list is each matrix, it is essentially each column, so if i find the index where the true minimum is, that is the column
  minrow = matrix[mincol].index(trueminimum)#now that i have the column i can just find the row by searching the position where the true minimum exists in the matrix[column]
  return minrow,mincol 
   
#Question 4:
def displayMatch(searchImage,x1,y1,w1,h1,color): #Since the assignment asked for a 3 pixel width rectangle, the addRect only 1 width so i did it 3 times
  addRect(searchImage,x1,y1,w1+1,h1+1,color) #creates the first rectangle                  i had to change the xy positions so it does not overlap
  addRect(searchImage,x1-1,y1-1,w1+3,h1+3,color) #creates the second rectangle 
  addRect(searchImage,x1-2,y1-2,w1+5,h1+5,color) # creates third rectange
  
#Question 5: 
def grayscale(picture): #simple grayscale function
  for y in range(0,getHeight(picture),1):
    for x in range(0,getWidth(picture),1):
      pixelf = getPixel(picture,x,y)
      valuer = getRed(pixelf)
      valueg = getGreen(pixelf)
      valueb = getBlue(pixelf)
      lum = (valuer+valueg+valueb)/3
      setColor(pixelf,makeColor(lum,lum,lum))
        
#Question 6:
def findWaldo(targetJPG,searchJPG):
  duplicate = duplicatePicture(searchJPG) #i decided to duplicate the searchJPG so i can output a final image which is not grayscale b/c once compareAll() function runs, the searchJPG becomes grayscaled
  start = clock() #Starts a clock
  matrix = compareAll(targetJPG,searchJPG)
  x,y = find2Dmin(matrix) #returns the x,y that best matches the template
  displayMatch(duplicate,x,y,getWidth(targetJPG),getHeight(targetJPG),blue) #creates the border
  explore(duplicate) #explore :D
  print 'time: ',clock()-start #prints the time it took for function to run
  
