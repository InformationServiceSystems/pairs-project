import sys
import re
import string



class RegularExpressions(object):

    def __init__(self):
        # frequently mis-tokenized tokens
        self.tokens = {
                    '(b)(4)' : r'\(\s?b\s?\)\s?\(\s?4\s?\)',        # Anonymized
                    '(b)(6)' : r'\(\s?b\s?\)\s?\(\s?6\s?\)',        # Anonymized
                    'mg/dl' : r'\s?mg\s?\/\s?dl\s?',                # Unit
                    'mmol/l' : r'\s?mmol\s?\/\s?l\s?',              # Unit
                    'age1' :  r'\s?[0-9]*\s?-\s?years\s?-\s?old',   # Age/Year
                    'age2' :  r'\s?[0-9]*\s?-\s?year\s?-\s?old',    # Age/Year
                    'age3' :  r'\s?[0-9]*\s?-\s?yrs\s?-\s?old',     # Age/Year
                    'f/u' : r'\sf\s?\/\s?u',                        # Abbreviation (f/u = follow up)
                    'e/a' : r'\se\s?\/\s?a',                        # Abbreviation (e/a = posibl. emergency admission?)
                    'al.' : r'\sal\s?\.',                           # Abbreviation (et al.)
                    'e.g.' : r'\se\.g\s?\.',                        # Abbreviation (e.g.)
                    'i.e.' : r'\si\.e\s?\.',                        # Abbreviation (i.e.)
                    'c.f.r.' : r'\sc\.f\s?\.r\s\.',                 # Abbreviation (c.f.r. = case fatality rate)
                    '#' : r'#\s?[0-9]+\s?'                          # Number (#1, #2 ...)
                    }

        self.units = [
                     'm/z',
                     'mg/kg',
                     'μg/ml',
                     'μl',
                     'µl',      # different my/mü!
                     'µa',      # micro-Ampere
                     'ng/ml',
                     '°c',
                     'g',       # gram
                     'ml',      # milliliter
                     'l',
                     'mmol/l',
                     'mg/ml',
                     'mg/dl',
                     'am',      # time
                     'pm',      # time
                     'min',
                     'mg',
                     'mm',
                     'cm',      # centimeter
                     'm',       # meter
                     'ncm',     # newton centimeter
                     'ncms',    # newton centimeter
                     'n.cm',    # newton centimeter
                     ]

        self.citations = [
                     r'studies,?([0-9]+–[0-9]+,?|[0-9]+,?)+',
                     # cite by author name (+ et al.)
                     r'([a-z]+\sand\s)?[^\s]+ et al\.(\s\([0-9]\)|\[[0-9]\])?',
                     # cite by number in brackets
                     r'\([0-9]{1,3}(,[0-9]{1,3})*\)|\[[0-9]{1,3}(,[0-9]{1,3})*\]'
                     ]

        self.url = re.compile(r'(http(s)?|www)[^(\s|\)|,)]*', re.DOTALL)

        self.dates = [
                    r'(0|1|2|3)?[0-9]\-?(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\-?(19|20)[0-9][0-9]',
                    r'(19|20)[0-9][0-9]\-?(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\-?(0|1|2|3)?[0-9]',
                    r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\-?(0|1|2|3)?[0-9]'
                    ]

        self.times =    [
                        r'(0|1|2)?[0-9]:[0-9][0-9](:[0-9][0-9])?',
                        r'(0|1|2)?[0-9]:[0-9][0-9](am|pm|AM|PM)'
                        ]

        self.power_number = r'[0-9]+\.?[0-9]+e-[0-9]+'

        self.ages = [
                    r'\s?[0-9]*\s?-\s?years\s?-\s?old',
                    r'\s?[0-9]*\s?-\s?year\s?-\s?old',
                    r'\s?[0-9]*\s?-\s?yrs\s?-\s?old'
                    ]

        self.numerals = [
                        r'^[0-9|-|.|,]+?$',
                        r'[#|<|>]\s?[0-9]+\s?'
                        #power numbers
                        r'[0-9]+\.?[0-9]+e-[0-9]+'
                        ]

        # based on the assupmtion that all latex snippets start with \documentclass
        # and end with \end{document}
        self.latex_regex = re.compile(r'\\documentclass.*\\end{document}', re.DOTALL)
        self.latex_regex2 = re.compile(r'\\documentclass.*', re.DOTALL)

        self.unwanted_chars = ['®', '©', '•', '○']

    ############################################################################
    # Text operations

    # shorten all characer repetition where a char occurs more than 3 times (except digits)
    def shorten_char_repetitions(self, text):
        punct = string.punctuation
        regex = r'([^0-9])\1{3,}'
        text = re.sub(regex, r'\1', text)
        return text

    # delete numeral, only keep
    def uniformize_units(self, text):
        for unit in self.units:
            regex = r'[≥|≤|<|>|~]?[0-9]+(\.[0-9]+)?(-[0-9]+(\.[0-9]+)?)?\s'+re.escape(unit)+r'\s?'
            matches = [match.group() for match in re.finditer(regex, text)]
            for match in matches:
                text = text.replace(match+" ", unit)
        return text.split()

    ############################################################################
    # Token operations

    # check if date in format like 24-jan-2020 or apr-09
    def is_date(self, token):
        for regex in self.dates:
            if self.compare_regex_and_token(regex, token):
                return True
        return False

    # check if temporal expression
    def is_time(self, token):
        # format like 15:30 or 15:30:34
        for regex in self.times:
            if self.compare_regex_and_token(regex, token):
                return True
        return False

    # all dates into the same format: day-month-year or placeholder
    def standardize_dates(self, token_list, placeholder=True):
        for token in token_list:
            if self.is_date(token):
                if placeholder:
                    return "DATE"
            else:
                # return certain format
                return token

    # there are no ages in the 100000_entries file!
    def is_age(self, token):
        for regex in self.ages:
            if self.compare_regex_and_token(regex, token):
                return True
        return False

    # check if digit+unit combinations, e.g. 160g, 5mmol/l ...
    def is_unit(self, token):
        for unit in self.units:
            regex = r'[<|>|~]?[0-9]+(\.[0-9]+)?(-[0-9]+(\.[0-9]+)?)?'+re.escape(unit)
            if self.compare_regex_and_token(regex, token):
                return True
        return False

    def is_numeral(self, token):
        for regex in self.numerals:
            if self.compare_regex_and_token(regex, token):
                return True
        return False

    def is_URL(self, token):
        return self.compare_regex_and_token(self.url, token)

    def is_citation(self, token):
        for regex in self.citations:
            if self.compare_regex_and_token(regex, token):
                return True
        return False

    def compare_regex_and_token(self, regex, token):
        match = re.search(regex, token)
        if match and match.group(0) == token:
            return True
        else:
            return False

    def is_valid_token(self, token):
        funcs = [self.is_date, self.is_time, self.is_unit, self.is_age, self.is_numeral, self.is_URL, self.is_citation]
        for func in funcs:
            if func(token):
                return True
        return False
