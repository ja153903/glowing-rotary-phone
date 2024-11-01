from problem_solving.leetcode.q2684 import Solution

solution = Solution()


def test_problem():
    assert (
        solution.maxMoves([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]])
        == 3
    )

    assert solution.maxMoves([[3, 2, 4], [2, 1, 9], [1, 1, 7]]) == 0
