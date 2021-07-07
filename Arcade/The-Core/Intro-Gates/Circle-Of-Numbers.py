def circleOfNumbers(n, firstNumber):
    nums = [i for i in range(n)]
    t = nums[nums.index(firstNumber):]
    t.extend(nums[:nums.index(firstNumber)])
    print(t)
    return t[(len(t)//2)]
