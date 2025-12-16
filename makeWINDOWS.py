
# This divides each play in a listOfFiles into a series of 2000-word blocks advancing
#   by 500 words each time. The last block created is the first one for which there
#   are fewer than 2000 words left in the input file, so this 'remainder' (of
#   between 1500 and 1999 words) is the final block we make

def makeWindow(anyText, anyStart, anyLength):			# function to return window o string of words
	anyText=anyText.split()								# break string into list on whitespace (default split)
	window=" ".join(anyText[anyStart:anyStart+anyLength])	# make window-sized slice of list and rejoin
	return window											#   the items to return a single string


#####################################

listOfFiles= [
'Chapman-AF.txt',
'Chapman-BBA.txt',
'Chapman-BUS.txt',
'Chapman-BYR.txt',
'Chapman-CAE.txt',
'Chapman-GOO.txt',
'Chapman-GU.txt',
'Chapman-HUM.txt',
'Chapman-MAY.txt',
'Chapman-OLI.txt',
'Chapman-RBD.txt',
'Chapman-WID.txt',
'Fletcher-BON.txt',
'Fletcher-CHA.txt',
'Fletcher-FAI.txt',
'Fletcher-HML.txt',
'Fletcher-ISL.txt',
'Fletcher-LOY.txt',
'Fletcher-MAD.txt',
'Fletcher-MON.txt',
'Fletcher-PIL.txt',
'Fletcher-RUL.txt',
'Fletcher-VAL.txt',
'Fletcher-WFAM.txt',
'Fletcher-WIL.txt',
'Fletcher-WPL.txt',
'Fletcher-WPR.txt',
'Jonson-ALC.txt',
'Jonson-BF.txt',
'Jonson-CAT.txt',
'Jonson-CR.txt',
'Jonson-DIAA.txt',
'Jonson-EMI.txt',
'Jonson-EMO.txt',
'Jonson-EPI.txt',
'Jonson-MAG.txt',
'Jonson-NI.txt',
'Jonson-POE.txt',
'Jonson-SEJ.txt',
'Jonson-SS.txt',
'Jonson-STAP.txt',
'Jonson-TUB.txt',
'Jonson-VOLP.txt',
'Marlowe-1TAM.txt',
'Marlowe-2TAM.txt',
'Marlowe-E2.txt',
'Marlowe-FAU.txt',
'Marlowe-JOM.txt',
'Marlowe-MASS.txt',
'Middleton-2MT.txt',
'Middleton-CHASTE.txt',
'Middleton-GAM.txt',
'Middleton-HENG.txt',
'Middleton-MDBW.txt',
'Middleton-MIC.txt',
'Middleton-MWMM.txt',
'Middleton-NWNH.txt',
'Middleton-PHOE.txt',
'Middleton-PUR.txt',
'Middleton-RT.txt',
'Middleton-TRI.txt',
'Middleton-WBW.txt',
'Middleton-WDO.txt',
'Middleton-WIT.txt',
'Middleton-Y5G.txt',
'Shakespeare-1H4.txt',
'Shakespeare-2H4.txt',
'Shakespeare-ADO.txt',
'Shakespeare-ANT.txt',
'Shakespeare-AWW.txt',
'Shakespeare-AYLI.txt',
'Shakespeare-COR.txt',
'Shakespeare-CYM.txt',
'Shakespeare-ERR.txt',
'Shakespeare-H5.txt',
'Shakespeare-HAM.txt',
'Shakespeare-JC.txt',
'Shakespeare-LLL.txt',
'Shakespeare-LR.txt',
'Shakespeare-MND.txt',
'Shakespeare-MV.txt',
'Shakespeare-OTH.txt',
'Shakespeare-R2.txt',
'Shakespeare-R3.txt',
'Shakespeare-ROM.txt',
'Shakespeare-SHR.txt',
'Shakespeare-TGV.txt',
'Shakespeare-TMP.txt',
'Shakespeare-TN.txt',
'Shakespeare-TRO.txt',
'Shakespeare-WIV.txt',
'Shakespeare-WT.txt'
]

for inputFileName in listOfFiles:

	trimmedInputFileName=inputFileName[0:inputFileName.find(".")]

	with open(inputFileName, "r") as handle:
		text=handle.read()

	width = 2000
	advance = 500
	blockCount=1
	for i in range(0,len(text.split()), advance):			# for i = 0 to wordcount-of-text step 'advance',
		blockCountString=str(blockCount)
		if len(blockCountString) == 1:
			blockCountString = "0"+blockCountString
		OutputFileName = trimmedInputFileName+"-"+blockCountString+".win"
		with open(OutputFileName, 'w') as handle:
			block=(makeWindow(text, i, width))
			handle.write(block)
		blockCount=blockCount+1
		# print(str(len(block.split())))
		if len(block.split())<2000:							# if the block we just created is shorter than
			break											#   2000 words make that the last block we create
