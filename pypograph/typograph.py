from pypograph import rules
import re

DEFAULT_RULES = [
    rules.MnemoRule,
    rules.QuoteRule,
    rules.MdashRule,
    rules.NbspRule,
]


class Typograph(object):
    rules = []

    def __init__(self, rules=None, config=None):
        if not rules:
            rules = DEFAULT_RULES

        for Rule in rules:
            rule = Rule(config)
            self.rules.append(rule)

    def typo(self, text):
        for rule in self.rules:
            text = rule.process(text)

        return text


def typo(text, config=None):
    typograph = Typograph(DEFAULT_RULES, config)
    return typograph.typo(text)
