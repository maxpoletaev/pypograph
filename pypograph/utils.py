from base64 import b64encode, b64decode
import re


def pack_html(text):
    match_set = set()

    for match in re.findall('<.*?>', text):
        match_set.add(match)

    for match in match_set:
        encoded = b64encode(match.encode('UTF-8'))
        text = text.replace(match, '[[%s]]' % str(encoded)[2:-1])

    return text


def unpack_html(text):
    match_set = set()

    for match in re.findall('[[.*?]]', text):
        match_set.add(match)

    for match in match_set:
        text = text.replace(match, b64decode(match))

    return text
