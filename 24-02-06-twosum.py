nums = [4, 9, 7, 5, 1, 10, 15, 56, 3, 8, 2]
k = 5
target = 36

def twosum():
    n = len(nums)
    for i in range(n):
        # 4
        for j in range(i + 1, n):
            # 9
            for k in range(j + 1, n):
                # 7
                for l in range(k+1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        return i, j, k, l


#print(twosum())


def twosum_re(nums, k, target):
    n = len(nums)
    start = 0
    result = []

    # 재귀함수
    def recur(start):
        if len(result) == k:
            sum_target = 0
            for i in range(k):
                sum_target += nums[result[i]]
            if sum_target == target:
                print("result: ", result)
            return False

        for i in range(start, n):
            result.append(i)
            recur(i + 1)
            result.pop()

    return recur(start)


twosum_re(nums, k, target)
