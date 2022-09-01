
from common.BaseClass import BaseClass
from plexapi.server import PlexServer
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"


class PlexSearcShowhFailed(Exception):
    def __init__(self):
        self.msg = 'Media Finder failed to initialize'
        super().__init__(self.msg)

class PlexConnectionFailed(Exception):
    def __init__(self):
        self.msg = 'Media Finder failed to initialize'
        super().__init__(self.msg)

class PlexSearchShow():
    """ This call the py1337x library functions.  This will be a centralized class 
        call from a few places    """

    def __init__(self,bc:BaseClass,plex_section:str,baseUrl:str,token:str)->None:
        try:
            self._bc=bc
            self._bc.log.info("\tStarting class "+self.__class__.__name__) 
            self._section=plex_section
            self.plex_connection(baseUrl,token)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise PlexSearcShowhFailed

    def plex_connection(self,baseUrl,token):
        try:
            
            self._plex_connect=PlexServer(baseUrl,token)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise PlexConnectionFailed

    def show_next_episode(self,show:str)->{}:
        """ Queries a Plex Server to find out last episode information on a tv show"""
        ## Last episode was
        last_episode = self._plex_connect.library.section(self._section).get(show).episodes()[-1]
        return {'name':show,'season':int(last_episode.seasonNumber),'episode':(last_episode.episodeNumber)}
  
    def season_next_episode(self,show:str,season:str)->{}:
        """ Runs the py1337x trending funtion and returns the results"""
        last_episode =self._plex_connect,plex.library.section(section).get(tv).seasons().episodes()[-1]
        return {'name':show,'season':int(last_episode.seasonNumber),'episode':(last_episode.episodeNumber)}
