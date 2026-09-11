class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
            input   :   asteriods[List]
            output  :   asteroids after collision [List]

            positive -> right
            negative -> left

            given asteroid x and y, where x > 0 and y < 0

            if x > -y:
                y is destroyed

            if x < -y:
                x is destroyed

            if x == -y:
                both x and y are destroyed

            given [3, 5, -6, 2, -1, 4]
                # keep a result array
                # add 3 [3]
                # add 5 [3. 5]

            *** asteroids moving in the same direction should not collide

                # since the next is -6, we check to out left    : we can use a stack implementation for this to check the top of the stack (checking to our left)
                while stack and curr < 0 and abs(curr (-6)) > stack[-1]:
                    stack.pop() --> 2 iterations of this should run to remove [3, 5] => []

                if curr < 0 and abs(curr) == stack[-1]:
                    stack.pop()
                    continue

                stack.append(curr)            
        """
        # [3, 5, -6, -10, 4] -> [-6, -10, 4]
        res = []

        for asteroid in asteroids:
            while res and asteroid < 0 and abs(asteroid) > res[-1] and res[-1] > 0:
                res.pop()
            
            if res and asteroid < 0 and abs(asteroid) == res[-1] and res[-1] > 0:
                res.pop()
                continue
            
            if res and asteroid < 0 and abs(asteroid) < res[-1]:
                continue

            res.append(asteroid)

        return res