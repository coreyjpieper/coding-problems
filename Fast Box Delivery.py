"""
# Fast Box Delivery

The top floor of your office has recently been vacated. Currently, your team is scattered and you would like to relocate your group there. Boxes of equipment and supplies will need to be moved to the top
floor.

- The building contains *n*+1 floors, indexed 0 to *n*
- You start at the top (*n*th) floor. You can take the elevator down to some floor *i* and back up, which takes a total of *n-i* minutes.
- Along the way, you can load a maximum of one box from *each* floor and deposit it back at the top. The operations of loading and unloading a box take 1 minute total for both operations.

Given an initial number of boxes on each floor, what is the minimum time required to get all of them to floor *n*?

### Example
*n* = 3
*boxes* = [1, 2, 3]

There are *n*+1 = 4 floors with boxes on floors 0, 1, and 2. The top floor is floor 3. You can minimize the time as follows:
1. Start at floor 3, ride down to floor 2 (1 minute), load a box from there and unload it back at the top (1 minute) - 2 minutes needed
2. Ride down to floor 1 (2 minutes), picking up boxes from floors 2 and 1, and unload them (2 minutes) - 4 minutes
3. Ride down to floor 0 (3 minutes), picking up boxes from floors 1, 2, and 3 and unloading them (3 minutes) - 6 minutes
This requires a total of 2 + 4 + 6 = 12 minutes

### Function Description
Complete the function *minTime* in the editor below. The function must return a long integer.

*minTime* has the following parameters:
    *boxes* an array of integers , so that *boxes[i]* denotes the number of boxes on the floor *i*

### Constraints
- 1 <= n <= 5 * 10^5
- 1 <= *num[i]* <= 10^9
"""

# start at the nth floors and there are n floors with boxes below
# [3, 4, 5, 6, 7] -> 3*5 + 1*4 + 1*3 + 1*2 + 1*1 + 25 = 50  num trips * len trips + total packages = total time
# [3, 3, 3, 3] -> 3*4 + 12 = 24
# [5, 5] -> 5*2 + 10 = 20
# [4, 0, 7] -> 4*3 + 3*1 + 11 = 26
# [0] -> 0
# [0, 0, 2, 0, 0] -> 2*3 + 2 = 8
# [0, 0, 0, 10] -> 10*1 + 10 = 20

from typing import *

def minTime(boxes: List[int]) -> int:
    if not boxes:
        return 0

    top_floor = len(boxes)  # time for trip = topfloor - i
    max_so_far = time = 0
    for floor, n_boxes in enumerate(boxes):
        # print(floor, n_boxes)
        if n_boxes > max_so_far:
            time += (n_boxes - max_so_far) * (top_floor - floor)
            max_so_far = n_boxes
    return time + sum(boxes)

print(minTime([1, 2, 3]))
assert minTime([1, 2, 3]) == 12
assert minTime([3, 4, 5, 6, 7]) == 50
assert minTime([3, 3, 3, 3]) == 24
assert minTime([5, 5]) == 20
assert minTime([4, 0, 7]) == 26
assert minTime([0]) == 0
assert minTime([0, 0, 2, 0, 0]) == 8
assert minTime([0, 0, 0, 10]) == 20








