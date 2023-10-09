def numOfArrays(n, m, k):
    memo = {}
    MOD = (10 ** 9) + 7

    def aux(index, currentMax=-1, currentK=0):
        key = (index, currentMax, currentK)
        if key in memo:
            return memo[key]
        if currentK > k:
            return 0
        if index >= n:
            if currentK == k:
                return 1
            return 0

        max_val = m if currentK == k else currentMax
        count = 0
        for i in range(1, max_val + 1):
            if i > currentMax:
                count += aux(index + 1, i, currentK + 1)
            else:
                count += aux(index + 1, currentMax, currentK)
        
        memo[key] = count % MOD
        return memo[key]

    return aux(0)

# Example usage:
n1, m1, k1 = 2, 3, 1
print(numOfArrays(n1, m1, k1))  # Output: 6

n2, m2, k2 = 5, 2, 3
print(numOfArrays(n2, m2, k2))  # Output: 0

n3, m3, k3 = 9, 1, 1
print(numOfArrays(n3, m3, k3))  # Output: 1
