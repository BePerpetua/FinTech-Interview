
def test_number(x, y, z):
   if x == y or x == z or y == z:
       return True
   else:
       return False
 

def prime_checker(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True       


def remove_duplicates(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list



def getPairsCount(arr, n, sum):
    count = 0  
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
 
    return count
 
     


def isPalindrome(string):
	left = 0
	right = len(string) - 1
	
	while right >= left:
		if not string[left] == string[right]:
			return False
		left += 1
		right -= 1
	return True



def test_duplicate(array_nums):
    nums_set = set(array_nums)    
    return len(array_nums) != len(nums_set)     
