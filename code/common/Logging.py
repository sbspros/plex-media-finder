from exceptions.AppExceptions import LoggingException
import logging
import datetime

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"

class Logging():

    def __init__ (self, file_name:str, log_level:int):
        try:

            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logging.basicConfig(filename=file_name, filemode='w', level=log_level,format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')
            self._log_level = int(log_level)
        except:
            raise LoggingException

    def info (self,message):
        if self._log_level ==logging.INFO :
            logging.info(str(datetime.datetime.now())+" - "+message)

    def warning (self,message):
        if self._log_level == logging.WARNING :
            logging.warning(str(datetime.datetime.now())+" - "+message)

    def error (self,message):
        if self._log_level == logging.ERROR :
            logging.error(str(datetime.datetime.now())+" - "+message)

    def debug (self,message):
        if self._log_level == logging.DEBUG :
            logging.debug(str(datetime.datetime.now())+" - "+message)

