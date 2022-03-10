import unittest
import sys
import io

from main import kcal_culator

def stub_stdin(test, inputs):
    stdin = sys.stdin

    def revert():
        sys.stdin = stdin

    test.addCleanup(revert)
    sys.stdin = io.StringIO(inputs)

def stub_stdouts(test): 
    stdout = sys.stdout
    stderr = sys.stderr

    def revert():
        sys.stdout = stdout
        sys.stderr = stderr

    test.addCleanup(revert)
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()

class TestKcalCulator(unittest.TestCase):
    def test_gather_custom_location(self):
        """Testing if the input prompt is displayed and if the custom location is gathered from the user
        """

        ds = kcal_culator.DataSheet()

        stub_stdin(self, "./data_sheet.csv")
        stub_stdouts(self)

        out = "Specify file location or enter \"d\" for the default file.\n"
        location = ds.gather_location()

        self.assertEqual(sys.stdout.getvalue(), out)
        self.assertEqual(location, "./data_sheet.csv")

    def test_gather_default_location(self):
        """Testing if the default location is being chosen if user types "d"
        """

        ds = kcal_culator.DataSheet()

        stub_stdin(self, "d")
        location = ds.gather_location()

        self.assertEqual(location, "/Users/martapodziewska/Documents/01_Coding/01_GitHub_working_repos/kcal-culator/main/draft_data_sheet.csv")

    def test_gather_default_location_with_capital_d(self):
        """Testing if the default location is being chosen if user types "D"
        """

        ds = kcal_culator.DataSheet()

        stub_stdin(self, "D")
        location = ds.gather_location()

        self.assertEqual(location, "/Users/martapodziewska/Documents/01_Coding/01_GitHub_working_repos/kcal-culator/main/draft_data_sheet.csv")

    # def test_1(self):
    #     """Testing
    #     """

    #     #Assetions

if __name__ == "__main__":
    unittest.main()