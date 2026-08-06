import unittest
from analyze import analyze


class AnalysisTests(unittest.TestCase):
    def test_reports_positive_lift(self):
        result = analyze(100, 1000, 120, 1000)
        self.assertGreater(result["relative_lift"], 0)
