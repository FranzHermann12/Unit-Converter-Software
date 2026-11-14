
import unittest
from decimal import Decimal

from core.engine import ConversionEngine


class TestConversionEngine(unittest.TestCase):

    def setUp(self):
        self.engine = ConversionEngine()

    def test_length(self):
        self.assertEqual(
            self.engine.convert(1, "Length", "Kilometre", "Metre"),
            Decimal("1000")
        )

    def test_temperature(self):
        result = self.engine.convert(
            100, "Temperature", "Celsius", "Fahrenheit"
        )
        self.assertLess(abs(result - Decimal("212")), Decimal("1e-45"))

    def test_mass(self):
        self.assertEqual(
            self.engine.convert(1, "Mass", "Kilogram", "Gram"),
            Decimal("1E+3")
        )

    def test_time(self):
        self.assertEqual(
            self.engine.convert(1, "Time", "Hour", "Second"),
            Decimal("3600")
        )

    def test_area(self):
        self.assertEqual(
            self.engine.convert(1, "Area", "Hectare", "Square Metre"),
            Decimal("10000")
        )

    def test_volume(self):
        self.assertEqual(
            self.engine.convert(1, "Volume", "Litre", "Millilitre"),
            Decimal("1E+3")
        )

    def test_speed(self):
        self.assertEqual(
            self.engine.convert(
                1, "Speed", "Kilometre per Hour", "Metre per Second"
            ),
            Decimal("0.2777777777777777777777777778")
        )

    def test_acceleration(self):
        self.assertEqual(
            self.engine.convert(
                1, "Acceleration", "Standard Gravity",
                "Metre per Second Squared"
            ),
            Decimal("9.80665")
        )

    def test_force(self):
        self.assertEqual(
            self.engine.convert(1, "Force", "Kilonewton", "Newton"),
            Decimal("1000")
        )

    def test_pressure(self):
        self.assertEqual(
            self.engine.convert(1, "Pressure", "Bar", "Pascal"),
            Decimal("100000")
        )

    def test_energy(self):
        self.assertEqual(
            self.engine.convert(1, "Energy", "Kilowatt-hour", "Joule"),
            Decimal("3600000")
        )

    def test_power(self):
        self.assertEqual(
            self.engine.convert(1, "Power", "Kilowatt", "Watt"),
            Decimal("1000")
        )

    def test_torque(self):
        self.assertEqual(
            self.engine.convert(
                1, "Torque", "Kilonewton-metre", "Newton-metre"
            ),
            Decimal("1000")
        )

    def test_density(self):
        self.assertEqual(
            self.engine.convert(
                1, "Density", "Gram per Cubic Centimetre",
                "Kilogram per Cubic Metre"
            ),
            Decimal("1000")
        )

    def test_frequency(self):
        self.assertEqual(
            self.engine.convert(
                1, "Frequency", "Kilohertz", "Hertz"
            ),
            Decimal("1000")
        )

    def test_angle(self):
        self.assertEqual(
            self.engine.convert(1, "Angle", "Revolution", "Degree"),
            Decimal("360")
        )

    def test_current(self):
        self.assertEqual(
            self.engine.convert(1, "Current", "Ampere", "Milliampere"),
            Decimal("1E+3")
        )

    def test_voltage(self):
        self.assertEqual(
            self.engine.convert(1, "Voltage", "Kilovolt", "Volt"),
            Decimal("1000")
        )

    def test_resistance(self):
        self.assertEqual(
            self.engine.convert(1, "Resistance", "Kiloohm", "Ohm"),
            Decimal("1000")
        )

    def test_capacitance(self):
        self.assertEqual(
            self.engine.convert(
                1, "Capacitance", "Microfarad", "Farad"
            ),
            Decimal("0.000001")
        )

    def test_charge(self):
        self.assertEqual(
            self.engine.convert(1, "Charge", "Ampere-hour", "Coulomb"),
            Decimal("3600")
        )

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            self.engine.convert(1, "Unknown", "Metre", "Foot")

    def test_invalid_unit(self):
        with self.assertRaises(ValueError):
            self.engine.convert(1, "Length", "Unknown", "Metre")

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            self.engine.convert("hello", "Length", "Metre", "Foot")

    def test_infinite_number(self):
        with self.assertRaises(ValueError):
            self.engine.convert("Infinity", "Length", "Metre", "Foot")


if __name__ == "__main__":
    unittest.main()
