class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        res = [0] * n

        stack = []  # (day, temp)

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((i, temp))
                continue

            while stack and stack[-1][1] < temp:
                day, t = stack.pop()
                res[day] = i - day


            # print("Stack: ", stack)
            stack.append((i, temp))

        return res

            