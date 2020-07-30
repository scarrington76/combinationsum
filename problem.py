class Problem:
    def combinationSum(self, target, nums):  ##Setup answer list, sort array, avoid 0, begin recursion
        answer = []
        nums.sort()
        if 0 in nums:
            return 'Invalid Entry - List must not contain zero'
        self.get_combos(target, nums, 0, 0, [], answer)
        return answer

    def get_combos(self, target, nums, i, total, combo, answer):
        if total == target:  ##if total equals target num, append combo list to answer list
            answer.append(list(combo))
        for n in range(i, len(nums)): ##traverse list of numbers
            if total + nums[n] > target:
                break;
            combo.append(nums[n]) ##append number to combo list
            self.get_combos(target, nums, i, total + nums[n], combo, answer) #recursive attempt
            combo.pop() ##pop combo from list