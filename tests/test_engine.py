
import unittest
from decimal import Decimal

from core.engine import ConversionEngine


class TestConversionEngine(unittest.TestCase):

    def setUp(self):
        self.engine = ConversionEngine()

        # Length units
        self.engine.register_unit("Length", "Metre", 1)
        self.engine.register_unit("Length", "Kilometre", 1000)
        self.engine.register_unit("Length", "Centimetre", 0.01)

        # Temperature units
        self.engine.register_unit(
            "Temperature", "Celsius", 1, "273.15"
        )

        self.engine.register_unit(
            "Temperature",
            "Fahrenheit",
            Decimal(5) / Decimal(9),
            Decimal("459.67") * Decimal(5) / Decimal(9)
        )

        self.engine.register_unit(
            "Temperature", "Kelvin", 1, 0
        )

    def test_kilometre_to_metre(self):
        result = self.engine.convert(
            5, "Length", "Kilometre", "Metre"
        )
        self.assertEqual(result, Decimal("5000"))

    def test_centimetre_to_metre(self):
        result = self.engine.convert(
            100, "Length", "Centimetre", "Metre"
        )
        self.assertEqual(result, Decimal("1"))

    def test_celsius_to_kelvin(self):
        result = self.engine.convert(
            0, "Temperature", "Celsius", "Kelvin"
        )
        self.assertEqual(result, Decimal("273.15"))

    def test_celsius_to_fahrenheit(self):
        result = self.engine.convert(
            100, "Temperature", "Celsius", "Fahrenheit"
        )
        self.assertLess(
            abs(result - Decimal("212")),
            Decimal("1e-12")
        )

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            self.engine.convert(10, "Unknown", "A", "B")

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            self.engine.convert(
                "hello", "Length", "Metre", "Kilometre"
            )


if __name__ == "__main__":
    unittest.main()
