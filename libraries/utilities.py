def limit_words(string: str, limit: int) -> str:
    word_list = string.split(' ')[:limit]
    return ' '.join(word_list)

def slugify(string: str, delimiter: str = '-') -> str:
    return string.lower().replace(" ", delimiter)