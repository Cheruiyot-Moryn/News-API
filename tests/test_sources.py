import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('bbc','BBC.',
        'Haiti 400 Mawozo gang leader extradited to US','Haitian authorities say leader of 400 Mawozo gang was extradited to the US for kidnapping Americans.','http://www.bbc.co.uk/news/world-latin-america-61315533')
        
    def test_instance(self):
        '''
        Test to check creation of new article Source instance
        '''
        self.assertTrue(isinstance(self.new_source,Source))