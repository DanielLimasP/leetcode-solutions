#https://leetcode.com/problems/divide-two-integers/discuss/837822/Python-clean-solution


def divideWithExtraSteps(dividend, divisor):
    sign = +1 if (dividend ^ divisor) >= 0 else -1
    dividend, divisor = abs(dividend), abs(divisor)
    ans = 0

    for power in range(31, -1, -1):
        if (divisor << power) <= dividend:
            ans += (1 << power)
            dividend -= (divisor << power)

    ans = 0 - ans if sign == -1 else ans

    if not (-2**31 < ans <= 2**31 - 1):
        return 2**31 - 1
    else:
        return ans


if __name__ == '__main__':
    print(divideWithExtraSteps(10, 3))