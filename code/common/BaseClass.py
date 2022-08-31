from common.Logging import Logging
from common.IniReader import IniReader
import platform

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"


class BaseClass:
    """ 
    This class sets up the logging and ini variables 
    for other objects to use. It 
        - Will have variable and methods needed by other objects
        - Load in the config file
        - Setup any logging

    """
    def __init__(self,file_name):
        #self._log_error=False
        self.line_feed='\n'
        if platform.platform()[0:7]=='Windows':
            self.line_feed='\r\n'
            
        self.ini_file = IniReader(file_name)
        try:
            self.log = Logging(self.ini_file.config['logging']['fileName'],\
                int(self.ini_file.config['logging']['logLevel']))
            self.log.info("\tStarting class "+self.__class__.__name__)
            
        except LoggingException as err:
            self._log_error=True




