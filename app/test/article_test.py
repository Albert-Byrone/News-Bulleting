import unittest
from ..models import Articles

# News = news.Article
class ArticleTest(unittest.TestCase):
    '''
    a class to test the behaviour of the Article class
    '''
    def setUp(self):
        '''
        a method that will run before any test
        '''
        self.new_article = Articles('Gizmodo.com','Daniel Kolitz','What\'s Going to Happen With Bitcoin?','Since its inception in 2009, Bitcoin has made and ruined fortunes, helped sell fentanyl and books about cryptocurrency',
                                    'www.gizmodo.com','https://cdn.vox-cdn.com/thumbor/QjYjrRLVMwCgjZSfE7JjC7URQns=/0x300:3733x2254/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/19253276/1040241490.jpg.jpg','2019-10-02T17:40:33Z')

    def test_instance(self):

        self.assertTrue(isinstance(self.new_article,Articles))


        
if __name__ == '__main__':
    unittest.main()