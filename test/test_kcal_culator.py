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

        stub_stdin(self, "./data_sheet.csv")
        stub_stdouts(self)

        ds = kcal_culator.DataSheet()
        out = "Specify file location or enter \"d\" for the default file.\n"
        location = ds.gather_location()

        self.assertEqual(sys.stdout.getvalue(), out)
        self.assertEqual(location, "./data_sheet.csv")

    def test_gather_default_location(self):
        """Testing if the default location is being chosen if user types "d"
        """

        stub_stdin(self, "d")

        ds = kcal_culator.DataSheet()
        location = ds.gather_location()

        self.assertEqual(location, "draft_data_sheet.csv")

    def test_gather_default_location_with_capital_d(self):
        """Testing if the default location is being chosen if user types "D"
        """

        stub_stdin(self, "D")

        ds = kcal_culator.DataSheet()
        location = ds.gather_location()

        self.assertEqual(location, "draft_data_sheet.csv")

    def test_open_data_sheet_with_default_local_location(self):
        """Testing if the open funtion is opening the file with local location
        """

        stub_stdouts(self)

        ds = kcal_culator.DataSheet()
        ds.open_data_sheet("draft_data_sheet.csv")

        self.assertIsNotNone(sys.stdout.getvalue())

    def test_open_data_sheet_with_false_location(self):
        """Testing if the open funtion is handling the FileNotFoundError properly
        """

        stub_stdouts(self)
        stub_stdin(self, "n")

        ds = kcal_culator.DataSheet()
        ds.open_data_sheet("/invalid_path/non_existent_file.csv")

        out = "The file /invalid_path/non_existent_file.csv does not exist. \nWould you like to create a new file? Y/N: \n"

        self.assertEqual(sys.stdout.getvalue(), out)

    # def test_1(self):
    #     """Testing
    #     """

    #     #Assetions

if __name__ == "__main__":
    unittest.main()