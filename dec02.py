with open('input_dec02.txt') as file:
    #parse the file
    line = [lines.split(": ") for lines in file]
    
    valid_count1 = 0
    valid_count2 = 0

    for policy, pwd in line:
	#parse each line and parts of it
	num_range, letter = policy.split(" ")
	begin, end = num_range.split("-")
	begin, end = int(begin), int(end)

	if pwd.count(letter) >= begin and pwd.count(letter) <= end: 
	  valid_count1 += 1

	if ((pwd[begin-1] == letter or pwd[end-1] == letter) and (pwd[begin-1] != pwd[end-1])): 
	  valid_count2 += 1
	
    print(valid_count1)
    print(valid_count2)
