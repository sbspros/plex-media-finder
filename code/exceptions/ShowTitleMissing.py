__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"



class ShowTitleMissing(Exception):
    def __init__(self):
        self.msg = 'Show titles not entered.  Please retry but with show titles'
        super().__init__(self.msg)