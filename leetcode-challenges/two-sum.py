from complexity import BigO

@BigO
def twoSum(nums: list[int], target: int) -> list[int]:
    num_dict = {}
    for i, num in enumerate(nums):
        if target - num in num_dict:
            return [num_dict[target - num], i]
        num_dict[num] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    twoSum(nums, target)