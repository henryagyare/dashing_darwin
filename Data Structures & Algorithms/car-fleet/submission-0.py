class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # def calc_time(pos, speed_val):
        #     return (target - pos)/speed_val

        # n = len(position)
        # cars = [(0, 0, 0)] * n
        cars = zip(position, speed, map(lambda pos, s : (target - pos)/s, position, speed))

        # creating cars array : cars[(position, speed, time)]
        # for i in range(n):

        sorted_cars = sorted(cars, key=lambda x : x[0], reverse=True)
        # cars.sort(key=lambda x : x[0])

        curr_pos, _, curr_time = sorted_cars[0]
        fleets = 0
        # print(sorted_cars)
        for i, (_, _, time) in enumerate(sorted_cars):
            if i == 0:
                continue
            if time > curr_time:
                fleets += 1
                curr_time = time
            
        return fleets + 1

