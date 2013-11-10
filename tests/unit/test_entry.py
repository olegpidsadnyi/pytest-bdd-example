import pytest


def count_o(value):
    """Count occurences of the 'o' in a string."""
    return value.count('o')


@pytest.mark.parametrize(
    ('title', 'o_count'),
    (
        ('Hello', 1),
        ('World', 1),
        ('Hello World', 2),
    )
)
def test_count_o(entry, o_count):
    """Test count_o counts 'o' in the string.

    :note: entry depends on the title fixture.

    """
    title, text = entry
    assert count_o(title) == o_count
