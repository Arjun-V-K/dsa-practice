from typing import List

"""
Fibonacci:
    Recurse function : F(n) = F(n-1) + F(n-2)
    Base Case: F(1) = F(2) = 1
"""


def fibonacci(n: int) -> int:
    memo = {}

    def fibonacci_helper(n: int) -> int:
        if n in memo:
            return memo[n]
        memo[n] = fibonacci_helper(n-1) + fibonacci_helper(n-2)
        return memo[n]
    
    # Setting base case
    memo[1] = 1
    memo[2] = 1
    return fibonacci_helper(n)


"""
You have a list of integers representing points associated with bowling pins. You have three options for each position in the list:

    Option a: Hit a single pin and get points equal to its value.
    Option b: Hit two adjacent pins at once and get points equal to the product of their values.
    Option c: Decide not to hit the pins at all.

The goal is to maximize the total points obtained by choosing the optimal sequence of actions.


Subproblem: Solve for the suffix A[i:], where F(i) = max points that can be achieved for pins from i to n-1
Recurse relation: F(i) = max(
                            A[i] + F(i+1), # hit the pin
                            A[i]*A[i+1] + F(i+2), # hit two adj pins
                            F(i+1) # dont hit the pin
                        )
Base Case: F(n) = 0 # No pins -> no points
Original problem: F(0)

"""

def maximize_bowling_points(points):
    n = len(points)

    def helper(i):
        if i >= n:
            return 0
        return max(
            points[i] + helper(i+1),
            points[i] * points[i+1] + helper(i+2) if i+1 < n else 0,
            helper(i+1) 
        )
    
    return helper(0)


"""
300. Longest Increasing Subsequence

"""

class Solution:
    counter = 0
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def lengthOfLISRec(i):
            self.counter += 1
            if i == n-1:
                return 1
            if i in memo:
                return memo[i]
            max_length = 1  # At least the current element itself
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    max_length = max(max_length, 1 + lengthOfLISRec(j))
            
            memo[i] = max_length
            return memo[i]
        return lengthOfLISRec(0)
    

def main():
    solution = Solution()
    test_cases = [
        [7,7,7,7,7,7,7],
        [4,10,4,3,8,9],
        [4,10,4,10,4,10]

    ]

    for test_case in test_cases:
        print(f"Input: {test_case}")
        print(f"Output: {solution.lengthOfLIS(test_case)}")
        print(f"Iterations: {Solution.counter}")
        print()

if __name__ == "__main__":
    main()