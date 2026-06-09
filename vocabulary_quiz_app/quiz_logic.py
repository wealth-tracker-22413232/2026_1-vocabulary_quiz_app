from __future__ import annotations

import random

import time

from dataclasses import dataclass


@dataclass(frozen=True)
class Word:
    term: str
    meaning: str


def normalize_answer(text: str) -> str:
    return " ".join(text.strip().lower().split())


def check_answer(word: Word, user_input: str) -> bool:
    is_correct = normalize_answer(user_input) == normalize_answer(word.meaning)
    return is_correct

def draw_word(words: list[Word], rng: random.Random | None = None) -> Word:
    if not words:
        raise ValueError("Word list is empty")
    chooser = rng if rng is not None else random
    return chooser.choice(words)

class QuizSession:
    def __init__(self):
        self.start_time = 0
        self.total_time = 0
        self.wrong_words = []

    def start(self):
        self.start_time = time.time()
        self.wrong_words = []

    def record_wrong(self, word: Word):
        self.wrong_words.append(word)

    def end(self):
        if self.start_time != 0:
            self.total_time = round(time.time() - self.start_time, 2)
            self.start_time = 0
