import unittest
import findinfile

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

if __name__ == '__main__':
    unittest.main()
