class Solution: # week15-1.py LeetCode 3158 �n��X�{2��
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        table= {} # �j�A��: table[num] ����������
        for num in nums: #�C�ӼƦr���@��
            if num in table: #�X�{�L����
                table[num] += 1 # ����+1
            else:
                table[num] = 1 #��1���X�{
        #print(table)   # �����٨S��X��
        ans = 0
        for num in table: # ��table�̥������Ʀr���@��
            if table[num]==2: # �p�G�Ʀr��n�X�{2��
                ans = ans ^ num # �⵪��, ���D�حn�D XOR �V�_��
        return ans