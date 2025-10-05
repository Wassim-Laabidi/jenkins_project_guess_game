from app import game


def test_play_round_success_first_try():
    secret = 42
    guesses = iter([str(secret)])

    def provider():
        return next(guesses)

    res = game.play_round(secret=secret, guess_provider=provider)
    assert res["success"] is True
    assert res["attempts"] == 1


def test_play_round_failure_on_invalid_input():
    secret = 10
    # provider raises ValueError when converting, simulate invalid input
    def provider():
        raise ValueError("bad input")

    res = game.play_round(secret=secret, guess_provider=provider)
    assert res["success"] is False
    assert res["attempts"] == 1
