import re

def split_by_level(lines, symbol=' ', sep='', indented=True):
    contents = []
    block_level = prev_level = level = 0
    level_re = re.compile(f'(?:({re.escape(symbol)}+){re.escape(sep)})?')
    for line in lines:
        if line.strip():
            level = len(level_re.match(line).groups()[0] or '')
        if (indented and prev_level != level) or (not indented and level):
            yield block_level, contents
            contents = []
            block_level = level
        prev_level = level
        contents.append(line)
    yield block_level, contents
