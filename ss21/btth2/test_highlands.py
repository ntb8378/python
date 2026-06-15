import unittest

from pos_logic import (
    calculate_total
)


class TestHighlands(unittest.TestCase):

    def test_calculate_total(self):

        order = [
            {
                "code": "P1",
                "quantity": 2
            },
            {
                "code": "F1",
                "quantity": 1
            }
        ]

        result = calculate_total(order)

        self.assertEqual(
            result,
            125000
        )

    def test_empty_order(self):

        result = calculate_total([])

        self.assertEqual(
            result,
            0
        )


if __name__ == "__main__":
    unittest.main()