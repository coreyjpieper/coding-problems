"""
# Oscillating String

Sam and Alex are competitive coders working together on strings. They like to create challenges for each other as practice. In one challenge, Sam asks Alex to create a function to sort a string. The terms
smaller and larger refer to the alphabetically lower or higher character. For example 'a' is smaller than 'b' and 'b' is larger than 'a'. To make the challenge more complex, the following string formation rules
are stated:

1. The sorted string, ss, begins with the smallest character in the original string, s.
2. Choose the smallest character from the remaining string that is larger than the previous letter, and append it to ss.
3. Repeat step 2 until it is no longer possible
4. Choose the largest character from the remaining string that is smaller than the previous one, and append it to ss.
5. Repeat step 4 until is is no longer possible.
6. If no character was chosen in steps 2 through 5 because all characters are equal, choose any of the characters and append it to ss.
7. Repeat steps 2 through 6 until the entire string has been processed.

### Example
s = *ababyz*

The following table shows the method
s | choose | ss
-----------------

The final sorted string is *abyzba*

### Function Description
Complete the function *formString* in the editor below. The function must return a string which is formed per the rules.

formString has the following parameter:
    *string s:* a string of characters

### Constraints
- 0 < |s| <= 10^5
- All letters in s \in *ascii[a-z]
"""

# corey -> ceory
# cabbage -> abcegba
# xyyyyzz -> xyzyzyyy
# illinois -> ilnosli

from typing import *

def formString(s: str) -> str:
    sortedst = sorted(s)  # list
    print("sorting finished")
    if not sortedst:
        return ""

    ss = lastchar = sortedst.pop(0)
    while sortedst:
        origlen = len(sortedst)
        for i in sortedst.copy():
            # print(i)
            if i > lastchar:
                lastchar = i
                ss = ss + i
                sortedst.remove(i)
                # print("added", i)
        for i in reversed(sortedst):
            if i < lastchar:
                lastchar = i
                ss = ss + i
                sortedst.remove(i)
        if origlen == len(sortedst):  # no characters were chosen because all are equal
            print("no char were chosen")
            ss = ss + ''.join(sortedst)
            sortedst.clear()
    return ss






# split string
# list('blue')
#
# [c for c in 'blue']


print(formString("aaaabbbbb"))
# print(formString("az" * 10**5))
# assert formString("corey") == "ceory"
# assert formString("cabbage") == "abcegba"
# assert formString("xyyyyzz") == "xyzyzyy"
# assert formString("illinois") == "ilnosli"

from collections import Counter
x = dict(Counter(c for c in "Mississippi"))
print(x)

d = {}
for i in "Mississippi":
    d[i] = d.get(i, 0) + 1

print(d)


def formString(s: str) -> str:
    if not s:
        return ""
    d = dict(Counter(c for c in s))
    
    ss = "0"  # place holder, removed at the return statement

    while d:
        for k in sorted(d.keys()):
            if k > ss[-1]:
                ss += k
                if d[k] == 1:
                    del d[k]
                else:
                    d[k] = d[k] - 1
        for k in reversed(sorted(d.keys())):
            if k < ss[-1]:
                ss += k
                if d[k] == 1:
                    del d[k]
                else:
                    d[k] = d[k] - 1
        if len(d) == 1:
            letter, num_times = d.popitem()
            ss += letter * num_times
    return ss[1:]


print(formString("ababyz"))
print(formString("aaaabbbbb"))
print(formString("az" * 10**6))
