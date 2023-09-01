class Solution:
    def __getPossibleResultsList (self, num1, num2):
        possible_results = [num1 + num2, num1 - num2, num2 - num1, num1 * num2]
        if (num1): possible_results.append(num2 / num1)
        if (num2): possible_results.append(num1 / num2)
        return possible_results

    def judgePoint24 (self, cards: List[int]) -> bool:
        if (len(cards) == 1):
            return (abs(cards[0] - 24.0) <= 0.1)
        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                next_cards = [cards[k] for k in range(len(cards)) if ((k != i) and (k != j))]
                for possible_result in self.__getPossibleResultsList(cards[i], cards[j]):
                    next_cards.append(possible_result)
                    if (self.judgePoint24(next_cards)): return True
                    next_cards.pop()
        return False
