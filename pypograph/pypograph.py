from pypograph import rules
import re


class Text(str):
    chain = []

    def split_char():
        return enumerate(list(self))

    def split_word():
        return


class Pypograph(object):
    rules = [
        rules.TabRule,
        rules.NbspRule,
        rules.MnemoRule,
    ]

    _rules_instances = []

    def __init__(self, config={}):
        for Rule in self.rules:
            self._rules_instances.append(Rule(config))

    def typo(self, text):
        text = Text(text)

        for rule in self._rules_instances:
            text = rule.process(text)

        return text


def typo(text, config={}):
    pypograph = Pypograph(config)
    return pypograph.typo(text)
