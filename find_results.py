
def func(file):
	with open(file) as file_in:
		lines_ = open(file).read().split('\n')

		lines = {}
		for line in lines_:  
			if line == '':
				continue
			lines[line] = 1  
	return lines 

def find_differences():
	def differences(a,b):
		count = 0	
		for c in a:
			if c not in b:
				print(c)
				count += 1
		print("Total: ", count)

	following = func("following.txt")
	followers = func("followers.txt")

	print("People that don't follow you")
	differences(following, followers)

	print("\nPeople that you don't follow back")
	differences(followers, following)

# find_differences()
