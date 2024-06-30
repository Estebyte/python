nums_set = {1,6,45}

print(len(nums_set))
print(45 in nums_set)

# add.()

nums_set.add(8)
print (nums_set)

# update.()

nums_set.update({2,3,4,6})
print(nums_set)

# remove.()

nums_set.remove(3)
print(nums_set)

# discard.()  No presenta error si el elemento no existe

nums_set.discard(9)
print(nums_set)

# clear.()

nums_set.clear()
print(nums_set)