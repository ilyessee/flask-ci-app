from app.utils import is_valid_index, sanitize_item


class TestSanitizeItem:
    def test_strips_whitespace(self):
        assert sanitize_item("  hello  ") == "hello"

    def test_empty_string_returns_empty(self):
        assert sanitize_item("") == ""

    def test_none_returns_empty(self):
        assert sanitize_item(None) == ""

    def test_normal_string_unchanged(self):
        assert sanitize_item("apple") == "apple"


class TestIsValidIndex:
    def test_valid_index_first(self):
        assert is_valid_index(0, ["a", "b", "c"]) is True

    def test_valid_index_last(self):
        assert is_valid_index(2, ["a", "b", "c"]) is True

    def test_index_out_of_bounds(self):
        assert is_valid_index(5, ["a", "b"]) is False

    def test_negative_index(self):
        assert is_valid_index(-1, ["a", "b"]) is False

    def test_empty_list(self):
        assert is_valid_index(0, []) is False
