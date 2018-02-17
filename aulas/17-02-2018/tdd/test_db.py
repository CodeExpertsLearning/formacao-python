import os
import simple_db
import sqlite3
import unittest
 
class TestMusicDatabase(unittest.TestCase):
    """
    Test the music database
    """
 
    def setUp(self):
        """
        Setup a temporary database
        """
        simple_db.create_database()

    def test_updating_artist(self):
        """
        Tests that we can successfully update an artist's name
        """
        simple_db.update_artist('Anthrax', 'Anthrat')
        actual = simple_db.select_all_albums('Anthrat')
        expected = [('Among The Living', 'Anthrat',
                    '1987')]
        self.assertListEqual(expected, actual)
 
    def test_artist_does_not_exist(self):
        """
        Test that an artist does not exist
        """
        result = simple_db.select_all_albums('Iron Maiden')
        self.assertFalse(result)
 
    def tearDown(self):
        """
        Delete the database
        """
        os.remove("mydatabase.db")