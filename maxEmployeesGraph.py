from collections import defaultdict
from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        adj = defaultdict(list)
        transpose = defaultdict(list)
        
        # Step 1: Build the graph and its transpose
        for i in range(len(favorite)):
            adj[i].append(favorite[i])
            transpose[favorite[i]].append(i)
        
        stack = []
        visited = [False] * len(favorite)
        
        # Step 2: Kosaraju's algorithm - DFS to fill stack
        def dfs(node):
            visited[node] = True
            for n in adj[node]:
                if not visited[n]:
                    dfs(n)
            stack.append(node)
        
        # Perform DFS to fill the stack
        for i in range(len(favorite)):
            if not visited[i]:
                dfs(i)
        
        # Step 3: Perform DFS on the transpose graph to find SCCs
        sccs = []  # list of sets of each SCC
        visited = [False] * len(favorite)
        
        def traverseForScc(node):
            visited[node] = True
            scc.add(node)
            for n in transpose[node]:
                if not visited[n]:
                    traverseForScc(n)
        
        # Traverse the nodes in the order defined by the stack
        while stack:
            top = stack.pop()
            if not visited[top]:
                scc = set()
                traverseForScc(top)
                sccs.append(scc)
        
        # Step 4: Maximize the number of invitations
        ans = max([len(scc) if len(scc) != 2 else -1 for scc in sccs])

        # Function to find the longest arm for two-node SCCs
        def findLongestArm(a, b):
            max_len = 0
            for node in transpose[a]:
                if node != b:
                    max_len = max(max_len, 1 + findLongestArm(node, b))
            return max_len
        
        # Handle SCCs with exactly two nodes
        twoNodeSccs = 0
        for scc in [scc for scc in sccs if len(scc) == 2]:
            n1, n2 = list(scc)
            twoNodeSccs += 2 + findLongestArm(n1, n2) + findLongestArm(n2, n1)
        
        # Return the maximum of the two conditions
        return max(ans, twoNodeSccs)

# Test function
def test_maximum_employees():
    solution = Solution()
    test_cases = [
        ([3, 0, 1, 4, 1], 4),
        ([1, 2, 0], 3),
        ([2, 2, 1, 2], 3),
    ]

    for i, (favorite, expected) in enumerate(test_cases):
        result = solution.maximumInvitations(favorite)
        assert result == expected, f"Test case {i + 1} failed: got {result}, expected {expected}"

    print("All test cases passed!")

# Run the tests
test_maximum_employees()
