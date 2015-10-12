from collections import defaultdict


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        

        mod = t

        if t == 0:
            mod = 1

        buckets = defaultdict(list)

        n = len(nums)

        for i in range(n):
            buckets[nums[i]//mod].append(i)

        for b in buckets:
            if b-1 in buckets:
                prev = buckets[b-1]
            else:
                prev = []
            if b+1 in buckets:
                next = buckets[b+1]
            else:
                next = []
            curr = buckets[b]

            for i in curr:
                for j in curr:
                    if i != j and abs(j-i) <= k and abs(nums[i] - nums[j]) <= t:
                        return True

                for p in prev:
                    if abs(p-i) <= k and abs(nums[i] - nums[p]) <= t:
                        return True
                for n in next:
                    if abs(n-i) <= k and abs(nums[i] - nums[n]) <= t:
                        return True

        return False


if __name__ == '__main__':
    s = Solution()
    s.containsNearbyAlmostDuplicate([-3,3], 2, 4)

