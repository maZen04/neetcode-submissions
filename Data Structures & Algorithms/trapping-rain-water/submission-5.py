class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxL, maxR = height[0], height[len(height)-1]
        water = 0
        while l <= r:
            if height[l] <= height[r]:
                if height[l] >= maxL:
                    maxL = height[l]
                else:
                    water += maxL - height[l]

                l += 1

            else:
                if height[r] >= maxR:
                    maxR = height[r]
                else:
                    water += maxR - height[r]

                r -= 1

        return water