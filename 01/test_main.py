import unittest
from main import part1


class TestPart1Function(unittest.TestCase):
    def test_example_input(self):
        input_data = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".strip()  # .strip() removes leading/trailing whitespace including the first newline
        expected_result = 3
        actual_result = part1(input_data)

        # Assert that the actual result matches the expected result
        self.assertEqual(
            actual_result,
            expected_result,
            "The part1 function did not return the expected value of 3.",
        )


if __name__ == "__main__":
    unittest.main()


class TestPart1Function(unittest.TestCase):
    def test_example_input(self):
        input_data = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".strip()  # .strip() removes leading/trailing whitespace including the first newline
        expected_result = 3
        actual_result = part1(input_data)

        # Assert that the actual result matches the expected result
        self.assertEqual(
            actual_result,
            expected_result,
            "The part1 function did not return the expected value of 3.",
        )


if __name__ == "__main__":
    unittest.main()
