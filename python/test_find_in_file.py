import unittest
import findinfile
from phpclass import PhpClass

class TestFindInFIle (unittest.TestCase):
    
    def test_find_usage(self):
        file_dir = "./tests"
        needle = "elephant"

        hitlist = findinfile.find_usage(file_dir, needle)
        self.assertEqual(5, len(hitlist))

        needle = "fox"

        hitlist = findinfile.find_usage(file_dir, needle, [])
        self.assertEqual(5, len(hitlist))

        # Testing with the result list not initialized (results are added to previous results)
        hitlist = findinfile.find_usage(file_dir, needle)
        self.assertEqual(10, len(hitlist))

    def test_php_class(self):
        file_path = "./tests/TestPhpClass.php"

        phpClass = PhpClass(file_path)

        self.assertEqual('My\\Namespace\\Path', phpClass.namespace)
        self.assertEqual('TestPhpClass', phpClass.classname)
        self.assertEqual('My\\Namespace\\Path\\TestPhpClass', phpClass.fullnamespace)

if __name__ == '__main__':
    unittest.main()
