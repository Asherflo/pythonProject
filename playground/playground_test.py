import unittest
import playground
class playgroundTest(unittest.TestCase):
    def setUp(self) -> None:
        print("i run before")
    def tearDown(self) -> None:
        print("i'm runnig on my own")
