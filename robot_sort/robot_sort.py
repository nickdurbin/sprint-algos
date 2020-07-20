class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        # At first glance I was thinking a bubble sort
        # Or an iterative sort or selection sort
        # based on we are evalutaing
        # Values and comparing to pick up or leave
        # We also have the ability to move left and right only
        # So, thinking of a long line of cards
        # we grab one and compare as we move down the list
        # Only picking up what is larger and moving right
        
        # Our robot should start at 0 in l 
        # Currently not holding a card 
        # So, we need to pick it up
        # Then, compare our item with the item to our right
        # Essentially swapping each item till we reach
        # the final destination or no longer can move
        # right. Which should mena our list is sorted.

        # pick up the first item
        self.swap_item()
        # While we have the ability to move right
        while True:
            while self.move_right():
                # compare the current item with the item on its right
                # if the held item's value is larger or greater than 0
                # Let's swap items
                if self.compare_item() > 0:
                    # the robot is now holding the smaller item in hand
                    self.swap_item()
                    print(self._list)
            # if the robot has made its way all the way to the end of the list
            # meaning we can no longer move right AND we have nothing to compare
            # which results in None, then let's swap items to complete the sorted list
            if self.can_move_right() == False and self.compare_item() == None:
                # If the above is true, then we simply swap item
                # aka put down our card if we have not already
                self.swap_item()
                print(self._list)
                # our list should now be sorted and we no longer
                # need to be in the loop
                # so we break it
                False
                break
            # Now we need to move through the list after we have reached the end
            # Meaning, go back towards the beginning of the list.
            else:
                while self.move_left():
                    # if either item is none
                    if self.compare_item() == None:
                        # we need to swap the item
                        self.swap_item()
                        print(self._list)
                        # continue to move right
                        self.move_right()
                        # swap again and then break out of the loop
                        self.swap_item()
                        print(self._list)
                        break

b = [2, 5, 4, 1, 3, 9, 6, 8, 7]

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(b)

    robot.sort()
    print(robot._list)