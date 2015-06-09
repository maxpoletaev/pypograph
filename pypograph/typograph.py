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
        if type(rules) in [list, tuple]:
            self._load_rules_list(rules)

    def _load_rules_list(self, rules):
        config = dict()
        for rule in rules:
            if type(rule) in (list, tuple):
                rule, config = rule

            if isinstance(rule, str):
                package_name, class_name = rule.rsplit('.', 1)
                rule_cls = getattr(import_module(package_name), class_name)
                rule = rule_cls(**config)
            elif isinstance(rule, type):
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
