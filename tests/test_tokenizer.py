import pytest

from whisper.tokenizer import get_tokenizer


@pytest.mark.parametrize("multilingual", [True, False])
def test_tokenizer(multilingual):
    tokenizer = get_tokenizer(multilingual=False)
    assert tokenizer.sot in tokenizer.sot_sequence
    assert len(tokenizer.all_language_codes) == len(tokenizer.all_language_tokens)
    assert all(c < tokenizer.timestamp_begin for c in tokenizer.all_language_tokens)


def test_multilingual_tokenizer():
    gpt2_tokenizer = get_tokenizer(multilingual=False)
    multilingual_tokenizer = get_tokenizer(multilingual=True)

    text = "다람쥐 헌 쳇바퀴에 타고파"
    gpt2_tokens = gpt2_tokenizer.encode(text)
    multilingual_tokens = multilingual_tokenizer.encode(text)

    assert gpt2_tokenizer.decode(gpt2_tokens) == text
    assert multilingual_tokenizer.decode(multilingual_tokens) == text
    assert len(gpt2_tokens) > len(multilingual_tokens)


def test_split_on_unicode():
    multilingual_tokenizer = get_tokenizer(multilingual=True)

    tokens = [8404, 871, 287, 6, 246, 526, 3210, 20378]
    words, word_tokens = multilingual_tokenizer.split_tokens_on_unicode(tokens)

    assert words == [" elle", " est", " l", "'", "\ufffd", "é", "rit", "oire"]
    assert word_tokens == [[8404], [871], [287], [6], [246], [526], [3210], [20378]]

def test_encode_decode():
    tokenizer = get_tokenizer(multilingual=False)
    text = "Testing encode and decode functionality."
    encoded_tokens = tokenizer.encode(text)
    decoded_text = tokenizer.decode(encoded_tokens)
    assert decoded_text == text

def test_decode_with_timestamps():
    tokenizer = get_tokenizer(multilingual=False)
    tokens = [tokenizer.timestamp_begin, tokenizer.eot, tokenizer.sot]
    decoded_text = tokenizer.decode_with_timestamps(tokens)
    assert decoded_text.startswith("<|0.00|>")


def test_split_to_word_tokens():
    tokenizer = get_tokenizer(multilingual=True)
    text = "This is a test sentence."
    tokens = tokenizer.encode(text)
    words, word_tokens = tokenizer.split_to_word_tokens(tokens)
    
    # Trim spaces from each word in the list
    words = [word.strip() for word in words]
    
    assert words == ["This", "is", "a", "test", "sentence", "."]


def test_get_tokenizer_unknown_language():
 with pytest.raises(ValueError, match="Unsupported language: xyz"):
    get_tokenizer(multilingual=True, language="xyz")
