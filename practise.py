class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        score_Alex = 0

        def go(index,last,alex):