import re


class BaseRule(object):
    """
    Basic processor object.
    """

    config = {}
    deps = []

    def __init__(self, **config):
        self.name = self.__class__.__name__.replace('Rule', '').lower()
        if config:
            self.config.update(config)
        self.prepare()

    def prepare(self):
        """Prepare rule."""
        pass

    def process(self, text):
        """
        Process text.

        Keyword arguments:
        text -- text for processing
        """

        return text


class MnemoRule(BaseRule):
    mnemonics_table = {
        'copy': {'html': '&copy;', 'hex_code': '&#169;', 'utf8': '©', 'alias': '(c) (C)'},
        'trade': {'html': '&trade;', 'hex_code': '&#8482;', 'utf8': '™', 'alias': '(TM)'},
        'reg': {'html': '&reg;', 'hex_code': '&#174;', 'utf8': '®', 'alias': '(R)'},
    }

    config = {
        'mode': 'html_to_utf8',
        'expand_alias': True,
    }

    def process(self, text):
        new_text = text.split()

        mode = self.config['mode'].split('_to_')
        table = self.make_table(mode[0], mode[1])

        for f, to in table.items():
            text = text.replace(f, to)

        return text

    def make_table(self, key, val):
        table = {}
        expand_alias = self.config['expand_alias']

        for index, item in self.mnemonics_table.items():
            table[item[key]] = item[val]

            if expand_alias and 'alias' in item:
                for alias in item['alias'].split():
                    table[alias] = item[val]

        return table


class NbspRule(BaseRule):
    """
    Add non-breaking space after short words.
    """

    def process(self, text):
        new_text = []
        old_text = text.split(' ')
        text_length = len(old_text)

        for i, word in enumerate(old_text):
            space = ''
            if i < text_length - 1:
                space = '&nbsp;' if len(word) < 3 and word.strip() else ' '

            new_text.append(word + space)
        return ''.join(new_text)


class QuoteRule(BaseRule):
    config = {
        'quotes': '«»',
    }

    def process(self, text):
        new_text = list(text)
        match = 0

        for i, char in enumerate(new_text):
            if char == '"':
                match += 1
                q_index = 0 if (match % 2 == 1) else 1
                new_text[i] = self.config['quotes'][q_index]

        return ''.join(new_text)


class TabRule(BaseRule):
    def process(self, text):
        return re.sub('\t+', ' ', re.sub('\t+$', '', re.sub('^\t+', '', text)))


class OneSpaceRule(BaseRule):
    def process(self, text):
        return re.sub('\s+', ' ', text).strip()


class MdashRule(BaseRule):
    regex = re.compile(r'\-(\s|&nbsp;)')

    def process(self, text):
        return self.regex.sub(r'—\1', text)
