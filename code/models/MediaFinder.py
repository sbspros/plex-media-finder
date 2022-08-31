from py1337x import py1337x
from common.BaseClass import BaseClass
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"


class MediaFinderFailed(Exception):
    def __init__(self):
        self.msg = 'Media Finder failed to initialize'
        super().__init__(self.msg)

class MediaFinder(BaseClass):
    """ This call the py1337x library functions.  This will be a centralized class 
        call from a few places    """

    def __init__(self,bc:BaseClass)->None:
        try:
            self._bc=bc
            self._bc.log.info("\tStarting class "+self.__class__.__name__) 
            self._raw_model = py1337x(proxy=None)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise MediaFinderFailed

    def query(self,category:str,search_str:str)->[]:
        """ Runs the py1337x search funtion and returns the results"""
        try:
            self._bc.log.info("\tInside search")
            return self._raw_model.search(search_str,category=category,sortBy='seeders')['items']
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise MediaFinderFailed       
  
    def trend(self,category:str)->[]:
        """ Runs the py1337x trending funtion and returns the results"""
        try:
            self._bc.log.info("\tInside trendList")
            return self._raw_model.trending(category=category, week=True)['items']
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise MediaFinderFailed

    def popular(self,category:str)->[]:
        """ Runs the py1337x popular funtion and returns the results"""
        try:
            self._bc.log.info("\tInside popular_list")
            return self._raw_model.popular(category=category)['items']
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise MediaFinderFailed

    def top(self,category:str)->[]:
        """ Runs the py1337x top funtion and returns the results"""
        try:
            self._bc.log.info("\tInside top_list")
            return self._raw_model.top(category=category)['items']
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise MediaFinderFailed

