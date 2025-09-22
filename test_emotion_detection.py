import unittest

from emotion_detection import emotion_detector
class MyTestModule(unittest.TestCase):
    def testEmotions(self):
        self.assertEqual(emotion_detector("I am glad this happened"), 'joy')

if __name__ == '__main__':
    unittest.main()
