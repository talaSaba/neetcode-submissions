class Solution:
    def carFleet(
        self,
        target: int,
        position: List[int],
        speed: List[int]
    ) -> int:
        array = []

        for i in range(len(position)):
            array.append((position[i], speed[i]))

        # Farthest car to closest car
        array.sort(key=lambda x: x[0])

        stack = []

        for i in range(len(array)):
            pos, speed = array[i]
            current_time = (target - pos) / speed

            # Fleets behind that reach the target earlier
            # will catch this car/fleet.
            while len(stack) > 0:
                pos1, speed1 = stack[-1]
                previous_time = (target - pos1) / speed1

                if previous_time <= current_time:
                    stack.pop()
                else:
                    break

            stack.append((pos, speed))

        return len(stack)