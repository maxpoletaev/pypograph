import re


class BaseRule(object):
    """
    Basic processor object.
    """
    config = {}

    def __init__(self, **config):
        self.name = self.__class__.__name__.replace('Rule', '').lower()
        if config: self.config.update(config)
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
        '©': ['(c)','(C)'],
        '™': ['(TM)'],
        '®': ['(R)'],
        '…': ['...'],
    }

    def process(self, text):
        new_text = text.split()

        for symbol, aliases in self.mnemonics_table.items():
            for alias in aliases:
                text = text.replace(alias, symbol)

        return text


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


class OneSpaceRule(BaseRule):
    def process(self, text):
        return re.sub('\s+', ' ', text).strip()


class DashRule(BaseRule):
    mdash = re.compile(r'\-{1,2}(\s|&nbsp;)')
    ndash = re.compile(r'(\d+)-(\d+)')

    def process(self, text):
        text = self.mdash.sub(r'—\1', text)
        text = self.ndash.sub(r'\1–\2', text)
        return text


class PunctuationRule(BaseRule):
    config = {
        'symbols': '.,!?:',
    }

    _regexps = {}

    def prepare(self):
        for symbol in self.config['symbols']:
            self._regexps[symbol] = re.compile(r'(\s*)(%s)(\s*)' % ('\\' + symbol))

    def process(self, text):
        for symbol, regex in self._regexps.items():
            text = regex.sub(r'\2 ', text)

        return text.strip()
