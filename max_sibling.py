import itertools as it

num = 0

class Solution:

    def __init__(self, num = 0):
        self.num = num

    def get_max_comb(self):
        global num
        num = [int(n) for n in str(num)]
        comb = []

        for i in it.permutations(num):
            comb.append(int("".join(map(str, i))))

        print(max(comb))


num = 579909

n = Solution().get_max_comb()








