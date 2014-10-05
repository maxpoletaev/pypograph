from pypograph import processors as proc
import re


class Pypograph(object):
    processors = []

    processor_classes = [
        proc.NbspProcessor,
        proc.MnemoProcessor,
    ]

    def __init__(self, config={}):
        for Proc in self.processor_classes:
            processors.append(Proc(config))

    def typo(self, text):
        for processor in self.processors:
            text = processor.process(text)
        return text


def typo(text, config={}):
    pypograph = Pypograph(config)
    return pypograph.typo(text)
