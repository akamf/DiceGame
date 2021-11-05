"""
This class is under construction and is not implemented in this version of the game
"""

import pickle


class HighScoreBoard:
    def __init__(self):
        self.board = []

    def load_high_score(self):
        with open('high_scores.taf', 'rb') as score_file:
            loaded_data = pickle.load(score_file)

        for line in loaded_data:
            self.board.append(line)

    def save_high_score(self):
        with open('high_scores.taf', 'wb') as score_file:
            pickle.dump(self.board, score_file)

    def update_high_score(self, player_name: str, player_score: int):
        score = {player_name: player_score}
        for i in self.board:
            if player_score > i[1]:
                self.board.append(score)
                self.board = sorted(self.board, key=int)
                self.board.pop(-1)
                break
