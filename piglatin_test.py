import pytest

import piglatin


@pytest.mark.parametrize('word,translation', [
    ('sailor', 'ailorsay'),
    ('ant', 'antay'),
    ('church', 'urchchay')
])
def test_translate(word, translation):
    assert piglatin.translate_word(word) == translation


def test_translate_phrase():
    phrase = 'the dry fish swims alone'

    result = piglatin.translate(phrase)

    assert result == 'ethay ryday ishfay wimssay aloneay'
