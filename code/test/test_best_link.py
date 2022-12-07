from controllers.BestLink import BestLink
from common.BaseClass import BaseClass

""" 
Best Link will
   - Call the MediaFinder class to get a list of links
   - It will filter out any non-related resutls
   - It will review the number of seeds and size and 
        pick the best file
"""

def test_best_link_tv()->None:
    bc = BaseClass('./config.ini')
    tv=BestLink(bc)
    resutls=tv.best_link('tv','Searcher')
    assert result['status']=='202'
