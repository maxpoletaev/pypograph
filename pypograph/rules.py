class BaseRule(object):
    """
    Basic processor object.
    """

    config = {}

    def __init__(self, config={}):
        self.config.update(config)

    def process(self, text):
        """
        Process text.

        Keyword arguments:
        text -- text for processing
        """

        return text


class MnemoRule(BaseRule):
    mnemonics_table = {
        'mdash': {'html': '&mdash;', 'utf8': '—'},
        'copy': {'html': '&copy;', 'utf8': '©', 'alias': '(c) (C)'},
    }

    config = {
        'mnemo_mode': 'html_to_utf8',
        'mnemo_expand_alias': True,
    }

    def process(self, text):
        new_text = text.split()

        mode = self.config['mnemo_mode'].split('_to_')
        table = self.table_group(mode[0], mode[1])

        for i, symb in enumerate(new_text):
            if symb in table: new_text[i] = table[symb]

        return ' '.join(new_text)

    def table_group(self, key, val):
        table = {}
        for index in self.mnemonics_table.keys():
            table_item = self.mnemonics_table[index]
            table[table_item[key]] = table_item[val]
        return table


class NbspRule(BaseRule):
    """
    Add non-breaking space after short words.

    Keyword arguments:
    text -- the text for processing
    """

    def process(self, text):
        old_text = text.split(' ')
        new_text = []

        text_length = len(old_text)

        for i, word in enumerate(old_text):
            space = ''
            if i < text_length - 1:
                if len(word) < 3:
                    space = '&nbsp;'
                else:
                    space = ' '

            new_text.append(word + space)
        return ''.join(new_text)


class QuoteRule(BaseRule):
    config = {
        'quote_quotes': '«»',
    }


    def process(self, text):
        new_text = list(text)
        match = 0

        for i, char in enumerate(new_text):
            if char == '"':
                match += 1
                q_index = 0 if (match % 2 == 1) else 1
                new_text[i] = self.config['quote_quotes'][q_index]

        return ''.join(new_text)
