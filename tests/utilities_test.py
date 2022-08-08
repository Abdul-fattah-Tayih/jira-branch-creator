from unittest import TestCase
from libraries.utilities import limit_words, slugify

class UtilitiesTest(TestCase):
    def test_limit_words_limits_words_delimited_by_spaces_into_given_number(self):
        paragraph = 'Lorem ipsum dolor'
        self.assertEquals('Lorem ipsum', limit_words(paragraph, 2))

    def test_limit_words_doesnt_split_words_not_delimited_by_spaces(self):
        paragraph = 'LoremIpsumDolor'
        self.assertEquals('LoremIpsumDolor', limit_words(paragraph, 2))

    def test_limit_words_accepts_string_limit_and_converts_it_to_string(self):
        paragraph = 'LoremIpsumDolor'
        self.assertEquals('LoremIpsumDolor', limit_words(paragraph, '2'))

    def test_slugify_converts_string_to_lower_case(self):
        paragraph = 'LOREM'
        self.assertEquals('lorem', slugify(paragraph))

    def test_slugify_converts_replaces_spaces_with_dashes_by_default(self):
        paragraph = 'Lorem ipsum dolor'
        self.assertEquals('lorem-ipsum-dolor', slugify(paragraph))

    def test_slugify_converts_replaces_spaces_with_given_delimiter(self):
        paragraph = 'Lorem ipsum dolor'
        self.assertEquals('lorem_ipsum_dolor', slugify(paragraph, '_'))