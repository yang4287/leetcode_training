# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        檢查每個字的數量
        racecar {r:2, a:2, c:2, e:1}
        carrace {c:2, a:2, r:2, e:1}
        核心：兩邊字母數量一樣就是true
        - 解法1 time:O(n) space:O(1)只用一個hashmap做計算，針對s可以用加，t可以個用減，若數量一樣，算完的值會為0
        - 解法2  time:O(n) space:O(1) 用兩個hashmap，計算數量，兩個hashmap相等
        hashmap最多 26 個字母的計數，因此空間複雜度是 𝑂(1)
        edgeCase 長度不一樣 false
        """
        s_length = len(s)
        # 解法1
        if s_length != len(t):
            return False
        count_map = {}
        for i in range(s_length):
            count_map[s[i]] = 1 + count_map.get(s[i], 0)
            count_map[t[i]] = -1 + count_map.get(t[i], 0)
        for v in count_map.values():
            if v != 0:
                return False
        return True

        # 解法2
        # if (len(s) != len(t)):
        #     return False
        # s_count_map = {}
        # t_count_map = {}
        # for i in range(len(s)):
        #     s_count_map[s[i]] = s_count_map.get(s[i], 0) + 1
        #     t_count_map[t[i]] = t_count_map.get(t[i], 0) + 1

        # return s_count_map == t_count_map
