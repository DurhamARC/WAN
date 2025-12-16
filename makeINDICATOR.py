# When making comparison (using compareWANS.py) between the WAN for one suspect text and the WANs for multiple
# candidate authors, the fact that some candidates' samples of writing (sole-authored well-attributed) are
# bound to be smaller than other candidates' samples of writing means that the writer will smaller canons
# will have WANs with more zeroes in then, since more of the 100-to-100 transitions we are looking for
# will simply be absent in the works of writers with small samples than are absent in the samples of
# writers with big canons.
# In order that his not disadvantage candidates with small samples, we should in such a multi-candidate
# comparison use only those 100-to-100 transitions that occur in all the candidates' writings. We
# achieve this by the present script looking at a set of WANs and producing an 'indicator' WAN that
# is the same size and shape as the WANs being compared and that has a 1 in each cell where ALL the
# candidates' WANs have a non-zero value (meaning all the candidates use the transition represented by
# that cell at least once) and that has a 0 in each cell where ANY of the candidates' WANs has a
# zero value (meaning that these candidates did not use the transition represented by that cell).
#
# The 'indicator' WAN is then used in the compareWANs.py script during the calculation of relative
# entropy. For each cell in WAN1 and WAN2 being compared, the the calculation only takes place if
# the cell in WAN1 and the cell in WAN2 and the cell in the 'indicator' WAN all have non-zero values.
# 



def showMatrix(anyMatrix):		# This prints our square matrix in two dimensions so it's easier to read
	if anyMatrix == []:
		print("Empty")
		return
	else:
		for i in range (0,len(anyMatrix[0])):
			print(str(anyMatrix[i]))


def loadWAN(anyFileName):

	with open(anyFileName, 'r') as handle:
		inStream = handle.read()							# this reads the whole file in as one string

	asRows=inStream.split("\n")								# create a list of rows breaking the string Instream at \n
	width=len(asRows[0].split(","))							# calculate width matrix by breaking first row at its commas

	WAN=[]													# Create the WAN with 0 in each cell
	for row in range(0, width):								# the number of rows is same as width
		WAN.append([0] * width)							# because WAN is square 

	for row in range(0, width):						# iterate thru all rows except last (because width is one less)
		thisRow=asRows[row].split(",")				# break present row at commas to make a list of cell values
		for column in range(0,width):				# iterate through columns
			WAN[row][column] = float(thisRow[column])	# assign cell to the current element in the list thisRow

	textcounts=[0] * width						# recover raw word counts from final row of matrix
	lastRow=asRows[width].split(",")			# turn final row string {which is asRows[width]) into list split on commas
	for column in range(0,width):				# iterate through that list and stuff each item
		textcounts[column]=int(lastRow[column])#   in that list into the empty list text1counts as integers

	return (WAN, textcounts)

##########################################

listOfWANs = [
'Chapman.WAN',
'Fletcher.WAN',
'Greene.WAN',
'Jonson.WAN',
'Marlowe.WAN',
'Middleton.WAN',
'Peele.WAN',
'Shakespeare.WAN',
]
outputFile='8-authors-2k-0.5k-top-100-words.IND'


indicator=[]									# make an empty list to hold the indicator matrix
(WAN, throwaway) = loadWAN(listOfWANs[0])		# load the first WAN from disk to grab the size
size = len(WAN[0])								# get the size (depth = width) from the first row of the first WAN
for row in range(0, size):						# iterate thru number of rows needed
	indicator.append([0] * size)				# appending a new row of zeroes each time
print(indicator)

for nameOfWAN in listOfWANs:					# iterate thru the list of WANs to process
	(WAN, throwaway) = loadWAN(nameOfWAN)		# load the WAN from disk into the variable matrix WAN
	print(nameOfWAN)							# 
	for row in range(0, size):					# iterate thru rows
		for column in range(0, size):			# iterate thru columns
			if WAN[row][column] != 0:			# if the present row,column is non-zero then ...
				indicator[row][column] = indicator[row][column]+1	# we can add one to this cell in the indicator
	print("That makes indicator be:")
	showMatrix(indicator)

numberOfWANs=len(listOfWANs)					# Now we check the totals in each cell in 'indicator'. If it is
for row in range(0, size):						# smaller than the number of WANs then at least one WAN did not add
	for column in range(0, size):				# a 1 to that cell because that WAN had zero at that place in it.
		if indicator[row][column] < numberOfWANs:	# If this cell didn't reach the total number of WANS
			indicator[row][column] = 0				# then set it to zero
		else:										# and if it did
			indicator[row][column] = 1				# then set it to one. Now 'indicator' is full of 0s and 1s
print("That makes indicator be:")					# indicating yes/no to whether ALL the WANS had a value for
showMatrix(indicator)								# that transition

indicator.append([-9] * size)						# Because the loadWAN function in compareWANS expects the matrix
													# to be one row deeper than it is wide (because the final row
													# is the raw-word counts for the WAN), we need to add a dummy
													# row at the bottom of the 'indicator' matrix

with open(outputFile, 'w') as handle:				# open disk-write channel, handle is my choice of variable name
	for row in range(0, size+1):					# iterate thru rows (notice "+1" because matrix no longer square)
		for column in range(0, size-1):				# iterate thru columns except final one (because not comma'd)
			handle.write(str(indicator[row][column])+",")	# write current cell to disk and then comma
		handle.write(str(indicator[row][column+1]))			# do last cell in row without a comma
		handle.write("\n")									# terminate row with newline
