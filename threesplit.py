#!/usr/bin/env python3

"""

https://app.codesignal.com/arcade/code-arcade/well-of-integration/QmK8kHTyKqh8xDoZk

You have a long strip of paper with integers written on it in
a single line from left to right. You wish to cut the paper into
exactly three pieces such that each piece contains at least one
integer and the sum of the integers in each piece is the same.
You cannot cut through a number, i.e. each initial number will
unambiguously belong to one of the pieces after cutting. How many ways
can you do it?

It is guaranteed that the sum of all elements in the array is divisible by 3.

Example

For a = [0, -1, 0, -1, 0, -1], the output should be
threeSplit(a) = 4.

Here are all possible ways:

[0, -1] [0, -1] [0, -1]
[0, -1] [0, -1, 0] [-1]
[0, -1, 0] [-1, 0] [-1]
[0, -1, 0] [-1] [0, -1]


"""


def threeSplit(a):

    def countN(wanted, a):

        """ generator to generate the wanted sum """
        count = 0
        for ind, item in enumerate(a):
            count += item
            if count == wanted:
                yield ind + 1


    myl = list()
    wanted = sum(a) // 3
    count = 0

    for ind1 in countN(wanted, a):
        if ind1 < len(a):
            for ind2 in countN(wanted, a[ind1:]):
                if (ind1 + ind2) < len(a):
                    for ind3 in countN(wanted, a[ind1 + ind2:]):
                        if (ind1 + ind2 + ind3) == len(a):
                            count += 1

    return count


if __name__ == "__main__":

    a1 = [0, -1, 0, -1, 0, -1]
    exp1 = 4

    a2 = [-1, 0, -1, 0, -1, 0]
    exp2 = 4

    a3 = [-1, 1, -1, 1, -1, 1, -1, 1]
    exp3 = 3

    a4 = [184138, -37745, 82759, 14851, 79647, -91351, -9413,
          84612, -101031, -181203, -162841, -14357, -122060, -56837,
          -59344, 95670, 19230, -197053, -151794, -12451, 1512, 108952,
          -155189, -8121, 43054, -25951, 125440, 28768, -42373, 188365,
          150867, -38140, 61777, 186009, 93565, -76218, -133893, -103795,
          -187274, -175627, -170204, -30250, 151764, 92036, 9080, 41271,
          -34582, 75906, -176277, 179547, 152773, 27776, -70639, -186460,
          134040, 135416, 196278, 15198, -167083, 190726, 175444, -25970,
          -37584, 130247, 163481, -78746, 123875, -127859, 63643, 131400,
          177022, -51120, -33714, -64067, -153262, -152369, -51938, 173432,
          -101008, 124992, -151945, -170175, 182191, 144348, -43276, -29398,
          143683, 4763, 164814, 195818, 28225, 180864, -127334, 37600, 184790,
          4152, 199588, 133654, -18816, -121196, -67769, 112234, 57594, 90858,
          199031, 184334, 112916, 130951, -181948, -61114, 74154, -44010, 164849,
          163083, -165563, 34566, -103124, 185075, 28700, -196978, -192354,
          -17883, -142522, -83792, 43765, -183610, 44134, -22779, 192282, 115221,
          12296, 20731, 98280, -89394, 72800, -110352, -6289, 54054, 151191,
          53169, 12397, -77496, 76249, 40497, 8377, -134898, 1345, -49669, 72688,
          181648, 113789, -91593, -85917, 85401, 76632, -71710, 106722, -128521,
          -119048, 37976, -72773, 34432, 40118, -153781, 163824, 149927, -83901,
          58599, 114268, -195468, 101292, 37934, 163551, -51514, 93980, -178182,
          -152702, -76796, -114697, 31344, -51611, -4632, -85532, -188408, 163967,
          83255, 34003, -175284, -60057, 15142, 175259, 194554, -115806, 47879,
          6083, -181421, 31385, -154069, -280, 187971]
    exp4 = 0


    tests = [(a1, exp1), (a2, exp2),
             (a3, exp3), (a4, exp4),
            ]

    for a, exp in tests:
        print("a = {}".format(a))
        rc = threeSplit(a)
        print("exp = {}".format(exp))
        print("rc  = {}".format(rc))
        print("{}".format(exp == rc))

