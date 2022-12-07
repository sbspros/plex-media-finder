from models.MediaFinder.py import MediaFinder
from common.BaseClass import BaseClass

def test_tv_query()->None:
        bc = BaseClass('./config.ini')
        query=MediaFinder(bc)
        results = query('tv','Seacher')
        assert result['status']=='202'

def test_movie_query()->None:
        bc = BaseClass('./config.ini')
        query=MediaFinder(bc)
        results = query('movies','Seacher')
        assert result['status']=='202'

def test_book_query()->None:
        bc = BaseClass('./config.ini')
        query=MediaFinder(bc)
        results = query('movies','Seacher')
        assert result['status']=='202'

if __name__ == "__main__":
    bc = BaseClass('./config.ini')
    
