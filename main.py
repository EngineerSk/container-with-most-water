# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List


class Solution:
    def container_with_most_water(self, array: List[int]) -> int:
        max_area = 0
        array_size = len(array)
        if array_size < 2:
            return max_area
        left = 0
        right = array_size - 1
        while left < right:
            height = min(array[left], array[right])
            width = right - left
            max_area = max(height * width, max_area)
            if array[left] < array[right]:
                left += 1
            else:
                right -= 1
        return max_area


print(Solution().container_with_most_water([1, 8, 9, 4, 5, 7]))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
