
from common.BaseClass import BaseClass
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"


class PlexSearchFailed(Exception):
    def __init__(self):
        self.msg = 'Media Finder failed to initialize'
        super().__init__(self.msg)

class PlexSearch(BaseClass):
    """ This call the py1337x library functions.  This will be a centralized class 
        call from a few places    """

    def __init__(self,bc:BaseClass)->None:
        try:
            self._bc=bc
            self._bc.log.info("\tStarting class "+self.__class__.__name__) 
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise PlexSearchFailed

    def show(self,show:str)->[]:
        """ Runs the py1337x search funtion and returns the results"""
        pass
  
    def season(self,show:str,season:str)->[]:
        """ Runs the py1337x trending funtion and returns the results"""
        pass
