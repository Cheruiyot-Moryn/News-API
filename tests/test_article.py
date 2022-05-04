import unittest
from app.main import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Brian Cheung','The Fed is about to do something it has not done in two decades: Morning Brief - Yahoo Finance','2022-05-04T10:00:29Z','https://finance.yahoo.com/news/the-fed-is-about-to-do-something-it-has-not-done-in-two-decades-morning-brief-100029366.html','https://s.yimg.com/ny/api/res/1.2/OkT5vhOIJnzAFu.rNM9ELA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD04MDA-/https://s.yimg.com/os/creatr-uploaded-images/2022-05/a91676e0-cb1b-11ec-8efe-6491b7708537')

    def test_instance(self):
        '''
        Test to check creation of new article instance
        '''
        self.assertTrue(isinstance(self.new_article,Article))