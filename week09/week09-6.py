class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        M,N = len(grid), len(grid[0])
        for i in range(M):
            if grid[i][0]==1: ans+=1 #�̥��䪺���
            if grid[i][N-1]==1: ans+=1 #�̥k�䪺���
        for j in range(N):
            if grid[0][j]==1: ans+=1 #�̤W�������
            if grid[M-1][j]==1: ans+=1 #�̤U�������

        for i in range(M): # ����i ��C�@�Ӯ�l
            for j in range(N): #�k��j
                #�p�G�i�A�ݨ�U���F�~�B�k��F�~ �N�ݬO�_0��1 ��1��0
                if i+1<M and grid[i][j]+grid[i+1][j]==1: ans+=1
                if j+1<N and grid[i][j]+grid[i][j+1]==1: ans+=1
        return ans
