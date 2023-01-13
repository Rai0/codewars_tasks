
class Solution:
    def threeSumOne(self, nums: list[int]) -> list[list[int]]:
        rez = []
        for i in range(0, len(nums) - 1):
            for s in range(i + 1, len(nums)):
                finding_num = -(nums[i] + nums[s])
                if finding_num in nums and i != s and nums.index(finding_num) != i and nums.index(finding_num) != s:
                    pre_rez = [nums[i], nums[s], finding_num]
                    pre_rez.sort()
                    if not rez.count(pre_rez):
                        rez.append(pre_rez)
        print(f"[INFO] {rez}")
        return rez
    
    def __scorer(self, nums, unic_nums):
        e = {}
        for i in unic_nums:
            e.update({i : nums.count(i)})
        return e

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        unic_nums = list(set(nums))
        if unic_nums == [0]:
            return [[0, 0, 0]] 
        score = self.__scorer(nums=nums, unic_nums=unic_nums)
        rez = []
        for i in range(0, len(unic_nums)):
            for s in range(0, len(unic_nums)):
                finding_num = -(unic_nums[i] + unic_nums[s])
                if finding_num in unic_nums:
                    is_it_pos = True
                    pre_rez = [unic_nums[i], unic_nums[s], finding_num]
                    for f in pre_rez:
                        if not pre_rez.count(f) <= score[f]:
                            print(f"{pre_rez}")
                            is_it_pos = False
                    pre_rez.sort()
                    if not rez.count(pre_rez) and is_it_pos:
                        rez.append(pre_rez)
        print(f"[INFO] {rez}")
        return rez

def testing(correct_answer, test_rez):
    print(test_rez == correct_answer)

# testing([[-1,-1,2],[-1,0,1]], Solution().threeSum([-1,0,1,2,-1,-4]))
testing([[-1,0,1]], Solution().threeSum([-1,0,1]))
# testing([], Solution().threeSum([0,1,1]))
# testing([[0,0,0]], Solution().threeSum([0,0,0]))