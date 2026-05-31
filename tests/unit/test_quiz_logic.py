import random

from vocabulary_quiz_app.quiz_logic import Word, check_answer, draw_word


def test_check_answer_normalized() -> None:
    word = Word(term="apple", meaning="사과")
    assert check_answer(word, "사과")
    assert check_answer(word, "  사과 ")
    assert not check_answer(word, "apple")


def test_draw_word_uses_rng_choice() -> None:
    words = [Word(term="a", meaning="A"), Word(term="b", meaning="B")]

    class FixedRng:
        def choice(self, seq):
            return seq[0]

    assert draw_word(words, FixedRng()) == words[0]


def test_draw_word_empty_list_raises() -> None:
    try:
        draw_word([], random.Random())
    except ValueError as exc:
        assert "empty" in str(exc)
    else:
        raise AssertionError("Expected ValueError for empty word list")
