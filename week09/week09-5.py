class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0]) # �����D����M �k��N���h�j, �~��ΰj��

        def travel(i,j): #�|���W�U���k(�|�Ӥ�V)�Ȧ�, �P�ɻ\��, ��쪺�a�賣���L
            if i<0 or j<0 or i>=M or j>=N: return #�W�L��l�d��, ���}
            if grid[i][j] == '0': return #���ਫ����l, ���}
            # �{�b�٨S���}, �N��o��i�H��
            grid[i][j] = '0'# �Хܲ{�b���F �H�ᤣ�n�A�i�ӤF
            travel(i+1,j) # �A���|�Ӥ�V�Ȧ�
            travel(i-1,j)
            travel(i,j+1)
            travel(i,j-1)

        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]=='1':#���@�ӥi�H���}�����a
                    ans += 1 # ���1�ӵ��פF
                    travel(i,j) # �}�l�Ȧ�
        return ans
