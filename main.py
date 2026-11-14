
from decimal import Decimal, getcontext
from core.engine import ConversionEngine

getcontext().prec = 50

engine = ConversionEngine()

tests = [
    (100, "Temperature", "Celsius", "Fahrenheit"),
    (0, "Temperature", "Celsius", "Kelvin"),
    (1, "Angle", "Radian", "Degree"),
    (1, "Length", "Kilometre", "Metre"),
    (1, "Energy", "Kilowatt-hour", "Joule"),
    (1, "Capacitance", "Microfarad", "Farad"),
]

print("UNIVERSAL CONVERTER")
print("PRECISION VERIFICATION")
print("=" * 65)

for value, category, from_unit, to_unit in tests:
    result = engine.convert(value, category, from_unit, to_unit)
    print(f"{value} {from_unit} = {result} {to_unit}")

print("=" * 65)
print("Decimal precision:", getcontext().prec)
print("All precision checks completed.")
