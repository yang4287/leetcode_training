class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        解法1：耗空間，利用正則畫，先去符號跟轉小寫，解法2：掃描時非字母(.isalnum())就跳過，比對時再轉換小寫比對
        用two pointer 判斷回文，一個指向最左邊，一個指向最右邊，直到中間為止，若是回文兩邊值都要一樣
        abba  => a=a     abba  => b=b    true
        |  |              ||

        """
        # 解法1:
        # s = re.sub('[^a-z0-9]', '', s.lower())

        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer <= right_pointer:
            # 解法2:非字母數字跳過
            if not s[left_pointer].isalnum():
                left_pointer += 1
                continue
            if not s[right_pointer].isalnum():
                right_pointer -= 1
                continue

            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            left_pointer += 1
            right_pointer -= 1
        return True
