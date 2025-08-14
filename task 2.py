class VotingSystem:
    def __init__(self):
        self.__candidates = {}  # private dict

    def add_candidate(self, name):
        if name not in self.__candidates:
            self.__candidates[name] = 0

    def remove_candidate(self, name):
        if name in self.__candidates:
            del self.__candidates[name]

    def vote_to_candidate(self, name):
        if name in self.__candidates:
            self.__candidates[name] += 1

    def display_winner(self):
        if self.__candidates:
            winner = max(self.__candidates, key=self.__candidates.get)
            print(f"Winner: {winner} with {self.__candidates[winner]} votes")

# example
vote = VotingSystem()
vote.add_candidate("Ali")
vote.add_candidate("Sara")
vote.vote_to_candidate("Sara")
vote.vote_to_candidate("Sara")
vote.vote_to_candidate("Ali")
vote.display_winner()