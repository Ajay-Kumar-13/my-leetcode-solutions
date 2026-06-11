class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        frequency = {}
        total = 0

        def total_combinations(n, r):
            if r > n:
                return 0

            numerator = 1
            denominator = 1

            for i in range(r):
                numerator *= (n - i)
                denominator *= (i + 1)

            return numerator // denominator


        for x in arr:
            frequency[x] = frequency.get(x, 0) + 1

        arr = sorted(set(arr))

        for i in range(len(arr)):
            for j in range(i, len(arr)):
                k = target - arr[i] - arr[j]

                if k not in frequency:
                    continue

                if k < arr[j]:
                    continue

                if arr[i] == arr[j] == k:
                    total += total_combinations(frequency[arr[i]], 3)

                elif arr[i] == arr[j]:
                    total += (
                        total_combinations(frequency[arr[i]], 2)
                        * frequency[k]
                    )

                elif arr[j] == k:
                    total += (
                        frequency[arr[i]]
                        * total_combinations(frequency[arr[j]], 2)
                    )

                else:
                    total += (
                        frequency[arr[i]]
                        * frequency[arr[j]]
                        * frequency[k]
                    )

        return total % (10**9 + 7)