from otree.api import Bot, expect
from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Intro
        yield Game
        # yield Results

        expect(len(PuzzleRecord.filter(player=self.player, is_correct=True)), 3)
        expect(len(PuzzleRecord.filter(player=self.player, is_correct=False, is_skipped=False)), 5)
        expect(len(PuzzleRecord.filter(player=self.player, is_correct=False, is_skipped=True)), 7)


def call_live_method(method, **kwargs):
    # expecting predictable captchas like NNN
    method(1, {'start': True})
    # 3 correct answers
    for i in range(0, 3):
        method(1, {'answer': f"{i:03}"})
    # 5 incorrect answers
    for i in range(0, 5):
        method(1, {'answer': "999"})
    # 7 skipped
    for i in range(0, 7):
        method(1, {'answer': ""})
