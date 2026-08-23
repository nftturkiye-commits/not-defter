import unittest
import tempfile
from src.core.file_manager import FileManager

class TestFileManager(unittest.TestCase):
    def test_write_and_read(self):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tf:
            path = tf.name
        content = "Merhaba Dünya!\nİkinci satır."
        FileManager.write(path, content)
        read_back = FileManager.read(path)
        self.assertEqual(content, read_back)

if __name__ == "__main__":
    unittest.main()
