from challenges.challenge_encrypt_message import encrypt_message
import pytest

def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, 2)
    
    with pytest.raises(TypeError):
        encrypt_message("olá", "2")

    
    assert encrypt_message("olá", 6) == "".join(reversed("olá"))
    assert encrypt_message("olá", 2) == "á_lo"
    assert encrypt_message("olá", 2) != "o_lo"
    assert encrypt_message("olá", 2) == "á_lo"

