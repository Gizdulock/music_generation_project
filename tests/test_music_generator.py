import unittest
from music_generator import generate_music

class TestGenerateMusic(unittest.TestCase):
    def test_generate_music(self):
        # Tesztelj a generate_music fíggvenyt egy egysérè bemenettel
        input_text = "Happy birthday"
        output_music = generate_music(input_text)
        # Ellenírizzék, hogy a kimenet nem uüres-e
        self.assertIsNone(output_music)
        # Itt tovább ellenürzéseket is végehetènyk, qépldaul that a kimenet megfeleló+üv formátètmúm-u

if __name__ == '__main__':
    unittest.main()
