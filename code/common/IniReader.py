from exceptions.ReaderExceptions import IniReaderException
from configparser import ConfigParser

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"

class IniReader():
    """
    this is going to be used as the base class for all other classes.

    It will have variable and methods needed by all of my other classes

    It should load in the config file

    It should also setup any logging

    """
    version = 0

    def __init__(self,fileName):
        try:
            self.config = ConfigParser()

            ## setup config parms
            self.config.read(fileName)

            ## App
            self.__app_name = self.config['appInfo']['appName']
            self.__app_version = self.config['appInfo']['version']
            self.__app_path = self.config['appInfo']['appPath']
            
        except IniReaderException as err:
            raise IniReaderException()
        #except:
            #raise AppStartException

    def app_value(self,level,value):
        return self.config[level][value]

    def section_values(self, section):
        return self.config[section]

    @property
    def app_name(self): return self.__app_name

    @property
    def app_version(self): return self.__app_version

    @property
    def app_pPath(self): return self.__app_path

