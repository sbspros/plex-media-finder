from common.BaseClass import BaseClass
from exceptions.ShowTitleMissing import ShowTitleMissing
from models.PlexSearch import PlexSearch
from models.MediaFinder import MediaFinder,MediaFinderFailed
from views.DisplayTorrentLinks import DisplayTorrnetLinks
import argparse
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"
""" A ulitity to find and update plex media"""

if __name__ == '__main__':
    bc=BaseClass('config.ini')     
    media_finder = MediaFinder(bc)
    dl=DisplayTorrnetLinks(bc)
    parser = argparse.ArgumentParser(description = 'A ulitity to find and update plex media')

    parser.add_argument('-s',
        '--show', 
        type=str,
        help='The show you want to look for.  If season is not indicated, it will do must recent season')
    
    parser.add_argument('-e', 
        '--season',
        type=str, 
        help='The season to search for')


    arg = parser.parse_args()
    try:
        if arg.show == None:
            raise ShowTitleMissing
        plex = PlexSearch(bc)
        if arg.season == None:
            ## this will run MediaFinder.query()
            show_search=plex.show(arg.show)            
        else:
            ## this will run MediaFinder.{top(),trending(),popular()}
            show_search=plex.season(arg.show,arg.season)            

        if show_search == []:
            bc.log.error("\tShow {show} for season {season} not found".format(show=arg.show,season=arg.season)) 
            raise ShowTitleMissing
        
        links=media_finder.query(media_finder,'query')
        dl.display_links(links)

    except  MediaFinderFailed:
        exit()
    except:
        bc.log.error("\t"+":"+traceback.format_exc()) 
        exit()
