from datetime import datetime
from itertools import chain

# tuples are faster and more efficient than list

class names_perm:
    def __init__(self, names):

        # convert full names into single word names: john doe => (john, doe)
        single_names = tuple(chain.from_iterable([ name.split(' ') for name in names ]))

        # all lowercase, uppercase, capitalized and reversed names
        self.words = tuple(chain.from_iterable([ (p.lower(), p.upper(), p.capitalize(), p[::-1]) for p in single_names ]))

        #initials
        _initials = lambda name: ''.join((w[0] for w in name.split(' ')))
        self.initials = tuple(_initials(name) for name in names)

class dates_perm:
    def __init__(self, dates):
        # lambda function to parse dates
        _converter = lambda date: datetime.strptime(date, "%d-%m-%Y")

        # all dates
        self.dates = tuple(_converter(date) for date in dates)
        # all days
        self.days = tuple(chain.from_iterable( (str(date.day) for date in self.dates) ))
        # all months
        self.months = tuple(chain.from_iterable( (str(date.month) for date in self.dates) ))
        # all years in format: 1997 and 97
        self.years = tuple(chain.from_iterable( (yr, yr[-2:]) for yr in ( str(date.year) for date in self.dates ) ))

class oldpwds_perm:
    def __init__(self, passwords):

        # remove special characters
        self.passwords = tuple(''.join(l for l in pwd if l.isalnum() for pwd in passwords))

        # Add lowercase, uppercase, capitalized and reverse passwords to the list
        self.passwords = tuple(chain.from_iterable([(p.lower(), p.upper(), p.capitalize(), p[::-1])] for p in self.passwords))
