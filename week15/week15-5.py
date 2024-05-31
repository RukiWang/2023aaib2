class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0
        N = len(s)
        j=0 # ����j
        for i in range(N):  # ���� Python ��r�ꪺ�j��g�X��
            maxCost -= abs( ord(s[i]) - ord(t[i]) ) # ����Ϊ��Yi �Y���l
            while maxCost < 0: # �w�⤣��, �ܭt��
                maxCost += abs( ord(s[j]) - ord(t[j]) ) # ����j �j�K�X��
                j += 1 # ����j ���k�Y
            ans = max(ans, i-j+1) # �Yi - ��j +1 �N�O����Ϊ�����
        return ans
