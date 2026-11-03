"""纯函数：去空白、按长度截断、统计词数。"""


def strip_whitespace(text: str) -> str:
    """去掉首尾空白。"""
    return text.strip()


def truncate(text: str, max_length: int) -> str:
    """按字符数截断。长度刚好等于 max_length 时原样返回。"""
    if max_length < 0:
        raise ValueError("max_length 不能为负数")
    return text[:max_length]


def count_words(text: str) -> int:
    """按空白分词后统计词数。空白字符串计为 0。"""
    words = text.split()
    return len(words)
