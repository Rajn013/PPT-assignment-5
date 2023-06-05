#!/usr/bin/env python
# coding: utf-8

# In[14]:


def convert_to_2d(original, m, n):
    if len(original) != m * n:
        return[]
    
    result =[[0] * n for _ in range(m)]
    
    for i in range(len(original)):
        row = i // n
        col = i % n
        result[row][col] = original[i]
        
    return result


# In[15]:


original = [1,2,3,4]
m = 2
n = 2
print(convert_to_2d(original, m, n))


# In[16]:


#2


def complete_rows(n):
    k = 1
    sum = 1
    
    while sum <= n:
        k += 1
        sum = k *(k + 1) // 2
    return k - 1


# In[17]:


n = 5
print(complete_rows(n))


# In[18]:


#3

def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    
    for i in range (n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
            
    return result


# In[19]:


nums = [-4,-1,0,3,10]
print(sorted_squares(nums))


# #creqate an empty resukt array of the same lenghts S NUMS
# #initializer 2 point left point array (index0) and rught point to the end of the array (index,len(nums)- 1)
# #iterate over the result array from the last index(len(nums)-1)to 0 using a reverse loop:
# - #calculate the squares of nums[left] and nums[right]
# - #compare the squared values. if nums[left] has a higher value, current index of the result array and move the left pointer to the right (increment left by 1)
# - #otherwide if nums[right] has a higher or equal square value, the current index of the result and move the right pointer to the left (decrement right by 1)
# - #return the result array.
# 

# #4
# 
# convert both num 1 and num 2 to set to eliminate duplicate and enav=ble efficient membership testing.
# initialize 2 equal set num 1 only and num 2 only to store the distinct integer that are present in num 1 but not in num2 and vice versa
# lterate through each element num in num1
#  - if num is not present in the set representation og nums 2 add it to the num1 only set
# lterate through each element num in nums2:
# 
# -If num is not present in the set representation of nums1, add it to the nums2_only set.
# -Convert nums1_only and nums2_only back to lists and return them as elements of a list [nums1_only, nums2_only].

# In[20]:


def find_disjoint(nums1, nums2):
    nums1_set = set(nums1)
    nums2_set = set(nums2)
    
    nums1_only = set()
    nums2_only = set()
    
    for num in nums1:
        if num not in nums2_set:
            nums1_only.add(num)
    for num in nums2:
        if num not in nums1_set:
            nums2_only.add(num)
            
    return [list(nums1_only), list(nums2_only)]


# In[21]:


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(find_disjoint(nums1, nums2))


# In[9]:


#5

def find_distance_value(arr1, arr2, d):
    distance = 0
    for num1 in arr1:
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                break
            
        else:
            distance += 1
    return distance


# In[10]:


arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
print(find_distance_value(arr1, arr2, d))


# In[13]:


#6

def findDuplicates(nums):
    duplicate = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            duplicate.append(abs(num))
        else:
            nums[index] = -nums[index]
    return duplicate


# In[14]:


nums = [ 4, 3, 2, 7, 8, 2, 3, 1]
print(findDuplicates(nums))


# In[16]:


#7


def findMin(nums):
    left = 0
    right =len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
    


# In[17]:


nums = [3, 4, 5, 1, 2]
print(findMin(nums))


# In[41]:


#8

def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []

    original = []
    num_count = {}

    for num in changed:
        num_count[num] = num_count.get(num, 0) + 1

    for num in sorted(changed):
        if num_count.get(num, 0) > 0 and num_count.get(num * 2, 0) > 0:
            original.append(num)
            num_count[num] -= 1
            num_count[num * 2] -= 1

    return original if sum(num_count.values()) == 0 else []


changed = [1, 3, 4, 2, 6, 8]
result = findOriginalArray(changed)
print(result)


# In[ ]:





# In[ ]:




