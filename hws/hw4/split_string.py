def split_string(source,splitlist):
	output = []
	atsplit = True	# really important initialization - consider the first word!
	for char in source:
		if char in splitlist:
			atsplit = True
		else:
			if atsplit:
				atsplit = False
				output.append(char)
			else:
				output[-1] = output[-1] + char
	return output
