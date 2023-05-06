import re

class Language:

    def __init__(self, text=None, *args, **kwargs):
        self.text = text

    @staticmethod
    def regex_match(pattern, text):
        match = re.match(pattern, text)
        if bool(match):
            return text
        return None

    def match(self):
        pattern = {
            'jp': r"[\u3040-\u309F|\u30A0-\u30FF]",
            'zh': r"[\u4e00-\u9fff]+",
            'en': r"[A-Za-z ]+"
        }
        for value in pattern:
            match = self.regex_match(pattern[value], self.text)
            if match is not None:
                return value, match

