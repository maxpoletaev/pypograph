from importlib import import_module
from pypograph import rules, utils
import re

DEFAULT_RULES = [
    rules.MnemoRule,
    rules.QuoteRule,
    rules.DashRule,
    rules.PunctuationRule,
    rules.NbspRule,
]


class Typograph(object):
    rules = []

    def __init__(self, rules=DEFAULT_RULES):
        if type(rules) == list:
            self._load_rules_list(rules)
        elif type(rules) == dict:
            self._load_rules_dict(rules)

    def _load_rules_dict(self, rules):
        for rule_class, config in rules.items():
            if isinstance(rule_class, str):
                rule_class = importlib.import_module(rule_class)

            rule = rule_class(**config)
            self.rules.append(rule)

    def _load_rules_list(self, rules):
        config = dict()
        for rule in rules:
            if isinstance(rule, str):
                rule = importlib.import_module(rule)
            if isinstance(rule, type):
                rule = rule(**config)
            self.rules.append(rule)

    def typo(self, text):
        text = utils.pack_html(text)
        for rule in self.rules:
            text = rule.process(text)

        return utils.unpack_html(text)


def typo(text, rules=DEFAULT_RULES):
    typograph = Typograph(rules)
    return typograph.typo(text)
