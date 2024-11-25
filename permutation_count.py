import sys
import threading

def count_permutations_with_inversions(n, k):

    f = [ [0]*(k+1) for _ in range(n+1) ]
    f[0][0] = 1  # Caso base


    for i in range(1, n+1):
        for s in range(k+1):
            f[i][s] = 0
            max_c = min(i-1, s)
            for c in range(0, max_c+1):
                f[i][s] += f[i-1][s - c]

   
    total_permutations = sum(f[n][s] for s in range(k+1))
    return total_permutations


def count_permutations_with_entropy(n, k):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(pos, used, total_displacement):
        if total_displacement > k:
            return 0  
        if pos == n:
            return 1  

        total = 0
        for e in range(n):
            if not (used & (1 << e)):
                displacement = abs(pos - e)
                new_total = total_displacement + displacement
                if new_total <= k:
                    total += dp(pos + 1, used | (1 << e), new_total)
        return total

    total_permutations = dp(0, 0, 0)
    return total_permutations


def count_lambda_permutations(n, k):
    from functools import lru_cache
    allowed_positions = []
    for i in range(n):
        start = max(0, i - (k - 1))
        end = min(n - 1, i + (k - 1))
        allowed_positions.append(set(range(start, end + 1)))

    @lru_cache(maxsize=None)
    def dp(pos, used):
        if pos == n:
            return 1
        total = 0
        for p in allowed_positions[pos]:
            if not (used & (1 << p)):
                total += dp(pos + 1, used | (1 << p))
        return total

    total_permutations = dp(0, 0)
    return total_permutations





def main():
    n = 5
    k = 12

    result = count_permutations_with_inversions(n, k)
    print(f"Número de permutações com inversões ≤ {k}: {result}")
    result = count_lambda_permutations(n,k)
    print(f"Número de lambda-permutações com lambda = {k}: {result}")
    result = count_permutations_with_entropy(n, k)
    print(f"Número de permutações com entropia ≤ {k}: {result}")

if __name__ == "__main__":
    threading.Thread(target=main).start()





