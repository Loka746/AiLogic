def rotate(nums,target):

  l = 0
  right = len(nums)-1

  while l <= right:

    mid = (l + right) // 2

    if nums[mid] == target:
      return mid

    if nums[l] <= nums[mid]:
      if nums[l] <= target < nums[mid]:

        right = mid + 1

      else: 
        l = mid + 1

    else:
      if nums[mid] < target <= nums[right]:

        l = mid + 1

      else: 
        right = mid - 1
    return -1

nums = list(map(int,input().split()))

target = int(input())

print(rotate(nums,target))
  

