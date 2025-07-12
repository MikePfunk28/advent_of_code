from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        if c != None:
            print([c])

        self.graph = defaultdict(list)
        for u, v in connections:
            self.graph[u].append(v)
            self.graph[v].append(u)

        # Process queries and return results
        results = []
        for u, v in queries:  # Changed from 'graph.items()' to 'queries'
            results.append(self.bfs(u, v))
        return results

    def bfs(self, start: int, end: int) -> int:
        visited = set()
        queue = [(start, 0)]
        while queue:
            node, dist = queue.pop(0)
            if node == end:
                return dist
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, dist + 1))
        return -1


if __name__ == '__main__':  # Fixed the string comparison
    my_solution = Solution()
    c = 5
    connections = [[1, 2], [2, 3], [3, 4], [4, 5]]
    queries = [[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]
    result = my_solution.processQueries(c, connections, queries)
    print(result)
