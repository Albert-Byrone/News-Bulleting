import unittest
from ..models import Sources

class SourcesTest:
    def setUp(self):
        self.new_source = Sources('buzzfeed','Buzzfeed','BuzzFeed is a cross-platform, global network for news and entertainment that generates seven billion views each month',
                                'https://www.buzzfeed.com','entertainment','en','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))


if __name__ == '__main__':
    unittest.main()
