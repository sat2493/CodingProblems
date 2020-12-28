# BFS Algorithm copied from Wikipedia

'''

 1  procedure BFS(G, root) is
 2      let Q be a queue
 3      label root as discovered
 4      Q.enqueue(root)
 5      while Q is not empty do
 6          v := Q.dequeue()
 7          if v is the goal then
 8              return v
 9          for all edges from v to w in G.adjacentEdges(v) do
10              if w is not labeled as discovered then
11                  label w as discovered
12                  Q.enqueue(w)
'''

class Queue:
    def __init__(self):
        self.q = []
    def push(self, value):
        self.q.append(value)
    def pop(self):
        return self.q.pop(0)
    def isEmpty(self):
        return len(self.q) == 0
    

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        # let Q be a queue
        Q = Queue()
        # label root as discovered
        discovered = set([root])
        # Q.enqueue(root)
        Q.push(root)
        
        # while Q is not empty do
        while not Q.isEmpty():
            # v := Q.dequeue()
            node = Q.pop()
            
            # Edit: Handle a null case
            if node == None:
                continue
            
            # if v is the goal then
            if node.val == val:
                # return v
                return node
            # for all edges from v to w in G.adjacentEdges(v) do
            for child in [node.left, node.right]:
                # if w is not labeled as discovered then
                if child not in discovered:
                    # label w as discovered
                    discovered.add(child)
                    # Q.enqueue(w)
                    Q.push(child)
                    
        return None
