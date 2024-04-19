class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        M,N = len(grid), len(grid[0])
        for i in range(M):
            if grid[i][0]==1: ans+=1 #最左邊的邊界
            if grid[i][N-1]==1: ans+=1 #最右邊的邊界
        for j in range(N):
            if grid[0][j]==1: ans+=1 #最上面的邊界
            if grid[M-1][j]==1: ans+=1 #最下面的邊界

        for i in range(M): # 左手i 對每一個格子
            for j in range(N): #右手j
                #如果可再看到下面鄰居、右邊鄰居 就看是否0變1 或1變0
                if i+1<M and grid[i][j]+grid[i+1][j]==1: ans+=1
                if j+1<N and grid[i][j]+grid[i][j+1]==1: ans+=1
        return ans
