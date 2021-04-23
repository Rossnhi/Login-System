def move_zeros(nums):
	flag = 0
	for _ in range(len(nums)):
		if nums[_] == 0:
			i = _
			flag = 1
			break
	if flag == 1:
		for j in range(_, len(nums)):
			if nums[j] != 0:
				temp = nums[i] 
				nums[i] = nums[j]
				nums[j] = temp
				i += 1
	return(nums)

print(move_zeros([0,1,0]))

