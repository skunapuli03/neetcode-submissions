class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #the goal is to see if i is greater than i+1
        res = [0] *len(temperatures)

        stack = [] 

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append((t,i))
        
        return res