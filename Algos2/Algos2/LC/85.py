class Solution(object):

    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        stack = []

        n = len(height)

        maxArea = 0

        if n == 0:
            return 0

        for i in range(n):
            if len(stack) == 0:
                stack.append(i)
                continue

            top = stack[-1]

            if height[i] <= height[top]:
                while len(stack) and height[top] >= height[i]:
                    top = stack[-1]
                    rightArea = (i - top) * height[top]
                    stack.pop()

                    if len(stack):
                        leftArea = (top - stack[-1]-1) * height[top]
                        top = stack[-1]
                    else:
                        leftArea = (top * height[top])

                    if rightArea  + leftArea > maxArea:
                        maxArea = rightArea + leftArea                        
                stack.append(i)

            else:
                stack.append(i)

        i += 1
        while len(stack):
            top = stack[-1]
            rightArea = (i - top) * height[top]
            stack.pop()

            if len(stack):
                leftArea = (top - stack[-1]-1) * height[top]
            else:
                leftArea = (top * height[top])

            if rightArea  + leftArea > maxArea:
                maxArea = rightArea + leftArea     


        return maxArea

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        
        r = len(matrix)

        if r == 0:
            return 0

        c = len(matrix[0])

        histo = [0] * c

        maxArea = 0

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    histo[j] += 1
                else:
                    histo[j] = 0


            area = self.largestRectangleArea(histo)

            if area > maxArea:
                maxArea = area

        return maxArea

