from common.BaseClass import BaseClass
from exceptions.ShowTitleMissing import ShowTitleMissing
from models.PlexSearchShow import PlexSearchShow, PlexConnectionFailed,PlexSearcShowhFailed
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
    
    tv_section=bc.ini_file.config['Plex']['tvSection']     
    server_url=bc.ini_file.config['Plex']['server']     
    server_token=bc.ini_file.config['Plex']['key']   

    media_finder = MediaFinder(bc)
    plex = PlexSearchShow(bc,tv_section,server_url,server_token)
    display_torrents=DisplayTorrnetLinks(bc)
    parser = argparse.ArgumentParser(description = 'A ulitity to find and update plex media')

    parser.add_argument('-s',
        '--show', 
        type=str,
        help='Specify the show you are looking for.')
    
    parser.add_argument('-e', 
        '--season',
        type=str, 
        help='Specify the season for the show you are looking for.')

    parser.add_argument('-l', 
        '--link_style',
        type=str, 
        default='link',
        help='what type of link to return {link,magnet}')        
    
    arg = parser.parse_args()
    try:
        if arg.show == None:
            raise ShowTitleMissing

        if arg.season == None:
            show_search=plex.show_next_episode(arg.show)            
        else:
            show_search=plex.season_next_episode(arg.show,arg.season)     
       
        if show_search == []:
            bc.log.error("\tShow {show} for season {season} not found".format(show=arg.show,season=arg.season)) 
            raise ShowTitleMissing
        
        show_search['episode']=show_search['episode']+1
        search_str=media_finder.show_to_search(show_search)
        print(search_str)
        ## search_str has last episode and we want the next one
        links=media_finder.query('tv',search_str)
        if arg.link_style=='link':
            display_torrents.display_links(links)
        else:
            display_torrents.display_mag_link(links)

    except  (MediaFinderFailed,PlexConnectionFailed,PlexSearcShowhFailed):
        ## Error logged by calling program
        exit()
    except:
        bc.log.error("\t"+":"+traceback.format_exc()) 
        exit()
