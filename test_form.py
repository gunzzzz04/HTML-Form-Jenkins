from pathlib import Path
import unittest

HTML_FILE = Path(__file__).resolve().parents[1] / "index.html"

class RegistrationFormTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = HTML_FILE.read_text(encoding="utf-8")

    def test_form_exists(self):
        self.assertIn('<form id="registrationForm">', self.html)

    def test_name_input_exists_and_required(self):
        self.assertIn('id="name"', self.html)
        self.assertIn('name="name" required', self.html)

    def test_email_input_exists_and_required(self):
        self.assertIn('type="email"', self.html)
        self.assertIn('id="email"', self.html)
        self.assertIn('name="email" required', self.html)

    def test_contact_input_exists_and_required(self):
        self.assertIn('type="tel"', self.html)
        self.assertIn('id="contact"', self.html)
        self.assertIn('pattern="[0-9]{10}" required', self.html)

    def test_submit_button_exists(self):
        self.assertIn('<button type="submit">Submit</button>', self.html)

if __name__ == "__main__":
    unittest.main(verbosity=2)
