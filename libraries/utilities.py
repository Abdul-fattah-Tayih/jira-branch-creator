def limit_words(string: str, limit) -> str:
    if limit is None:
        return string

    if isinstance(limit, str):
        limit = int(limit)

    word_list = string.split(' ')[:limit]
    return ' '.join(word_list)

def slugify(string: str, delimiter: str = '-') -> str:
    return string.lower().replace(" ", delimiter)