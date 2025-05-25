import MySQLdb
import unittest
from unittest import skipIf
import os
from console import HBNBCommand
from io import StringIO
import sys


class TestDBStorage(unittest.TestCase):
    """Tests for the database storage engine"""

    @skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Only for DB storage")
    def test_create_state_db(self):
        """Test that create State adds a record to the database"""
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor = db.cursor()
        
        # Get initial count of states
        cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = cursor.fetchone()[0]
        
        # Execute the console command to create a state
        cmd = HBNBCommand()
        cmd.onecmd('create State name="California"')
        
        # Get new count of states
        cursor.execute("SELECT COUNT(*) FROM states")
        new_count = cursor.fetchone()[0]
        
        # Verify one state was added
        self.assertEqual(new_count, initial_count + 1)
        
        # Clean up
        cursor.close()
        db.close()