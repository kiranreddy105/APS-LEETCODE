class Solution(object):
    def findCircleNum(self, isConnected):
        
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        def dfs(city):
            for neighbor in range(n):
            
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
                    
        for i in range(n):
            if i not in visited:
                
                visited.add(i)
                dfs(i)
                provinces += 1
                
        return provinces
        