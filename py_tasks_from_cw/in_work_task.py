# CW link: https://www.codewars.com/kata/5739174624fc28e188000465

def test(funk_rez, right_answer):
	if funk_rez is right_answer:
		return True
	return False 

# starting code

class PokerHand(object):

    RESULT = ["Loss", "Tie", "Win"]
    card_rate = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    def __init__(self, hand):
        self.hand = hand
        
    def sorted_hand(self, e) -> list:
        return self.card_rate[e[0]]

    def is_flush(self, hand, id = 1) -> bool:
        back = ""
        for i in hand:
            if back != "" and i[id] != back: 
                return False
            back = i[id]
        return True 

    def is_straight(self, hand) -> bool:
        back_num = 0
        for i in hand:
            if back_num and self.card_rate[i[0]] != back_num + 1:
                return False
            back_num = self.card_rate[i[0]]
        return True

    def e(self, hand) -> float:
        b = ""
        score = 0
        points = 0
        for i in hand:
            if i[0] == b:
                points += 1
                score += points + (self.card_rate[i[0]] / 100)
            else:
                points = 0
            b = i[0]
        if int(score) == 4 or int(score) == 6: score += 2
        return score

    def all_card_score(self, hand) -> int:
        all_card_score = 0
        for i in hand:
            all_card_score += self.card_rate[i[0]]
        return all_card_score / 100

    def scoring(self, hand) -> int:
        flush: bool = self.is_flush(hand=hand)
        straight: bool = self.is_straight(hand=hand)
        if flush or straight:
            # return (flush * 5) + (straight * 4) + self.card_rate[hand[4][0]] / 100
            return (flush * 5) + (straight * 4) + self.all_card_score(hand) / 100
        score = self.e(hand) + self.all_card_score(hand) / 100
        return score

    def compare_with(self, other):
        my_hand, other_hand = self.hand.split(" "), other.hand.split(" ")
        my_hand.sort(key = self.sorted_hand)
        other_hand.sort(key = self.sorted_hand)
        my_s = self.scoring(my_hand)
        other_s = self.scoring(other_hand)
        print(f"my hand {my_hand}\nother {other_hand} ")
        print(f"{my_s} VS {other_s}")
        if my_s < other_s:
            return self.RESULT[0]
        if my_s == other_s:
            return self.RESULT[1]
        return self.RESULT[2]

def scoring_test(msg, test_values):
    print(msg, PokerHand("2S AH 2H AS AC").scoring(test_values))

# scoring_test("test Pair", ['5H', '6H', '7S', 'AH', 'AC'])
# scoring_test("test two Pair", ['2S', '2H', '4H', '4C', '5S'])
# scoring_test("test Three of a kind", ['5H', '6H', 'AH', 'AC', 'AS'])
# scoring_test("test Straight", ['2S', '3H', '4H', '5S', '6C'])
# scoring_test("test Flush", ['2H', '3H', '5H', '6H', '7H'])
# scoring_test("test Full house", ['2S', '2H', 'AH', 'AS', 'AC'])
# scoring_test("test Four of a kind", ['JS', 'JD', 'JC', 'JH', 'AD'])
# scoring_test("test Straight flush", ['2H', '3H', '4H', '5H', '6H'])


def runTest(msg, expected, hand, other):
    player, opponent = PokerHand(hand), PokerHand(other)
    print(player.compare_with(opponent) == expected)

runTest("", "Loss", "JH 8S TH AH QH", "KD 6S 9D TH AD")

# runTest("", "Win", "4C 5C 9C 8C KC", "3S 8S 9S 5S KS")
# runTest("", "Win", "KC 4H KS 2H 8D", "QH 8H KD JH 8S")
# runTest("Full house wins of flush",           "Win",  "2S AH 2H AS AC", "2H 3H 5H 6H 7H")
# runTest("3 Of a kind wins of two pair",       "Loss", "2S 2H 4H 5S 4C", "AH AC 5H 6H AS")
# runTest("4 Of a kind wins of full house",     "Loss", "2S AH 2H AS AC", "JS JD JC JH AD")
# runTest("Straight wins of three of a kind",   "Win",  "2S 3H 4H 5S 6C", "AH AC 5H 6H AS")
# runTest("Pair wins of nothing",               "Loss", "2S AH 4H 5S KC", "AH AC 5H 6H 7S")
# runTest("Highest pair wins",                  "Loss", "6S AD 7H 4S AS", "AH AC 5H 6H 7S")
# runTest("Highest card wins",                  "Win",  "4S 5H 6H TS AC", "3S 5H 6H TS AC")
# runTest("Equal cards is tie",		          "Tie",  "2S AH 4H 5S 6C", "AD 4C 5H 6H 2C")
# runTest("Flush wins of straight",             "Win",  "2H 3H 5H 6H 7H", "2S 3H 4H 5S 6C")
# runTest("Highest flush wins",                 "Win",  "AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H")
# runTest("Highest card loses",                 "Loss", "2S 3H 6H 7S 9C", "7H 3C TH 6H 9S")
# runTest("Straight flush wins of 4 of a kind", "Win",  "2H 3H 4H 5H 6H", "AS AD AC AH JD")
# runTest("Highest straight flush wins",        "Loss", "2H 3H 4H 5H 6H", "KS AS TS QS JS")
# runTest("2 Pair wins of pair",                "Win",  "2S 2H 4H 5S 4C", "AH AC 5H 6H 7S")
# runTest("Highest 4 of a kind wins",           "Win",  "AS AH 2H AD AC", "JS JD JC JH 3D")
# runTest("Equal straight is tie", 	  	      "Tie",  "2S 3H 4H 5S 6C", "3D 4C 5H 6H 2S")