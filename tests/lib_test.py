from bbquote_test.lib import get_quote


def test_quote_length():
    quote = get_quote()
    assert len(quote) != 0