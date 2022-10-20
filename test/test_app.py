import unittest
from pathlib import PosixPath
import main

class TestApp(unittest.TestCase):

    def test_ctrl_BASE_DIR(self):
        self.assertEqual(main.BASE_DIR, PosixPath('/home/john/Documentos/sistemas/python/desktop/gtk4/ctrl'))
        self.assertEqual(main.BASE_DIR, PosixPath('/home/john/Documentos/sistemas/python/desktop/gtk4/ctrl/'))
        self.assertNotEqual(main.BASE_DIR, PosixPath('/home/john/Documentos/sistemas/python/desktop/gtk4/'))

    def test_ctrl_ROOT_DIR(self):
        self.assertEqual(main.ROOT_DIR, PosixPath('/home/john/Documentos/sistemas/python/desktop'))
        self.assertEqual(main.ROOT_DIR, PosixPath('/home/john/Documentos/sistemas/python/desktop/'))
        self.assertNotEqual(main.ROOT_DIR, PosixPath('/home/john/Documentos/sistemas/python/'))

if __name__ == '__main__':
    unittest.main()
