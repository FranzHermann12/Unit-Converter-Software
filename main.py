
from core.engine import ConversionEngine

engine = ConversionEngine()

tests = [
    (1, "Torque", "Kilonewton-metre", "Newton-metre"),
    (1, "Torque", "Pound-foot", "Newton-metre"),
    (1, "Torque", "Pound-inch", "Newton-metre"),
    (1, "Torque", "Kilogram-force metre", "Newton-metre"),
    (100, "Torque", "Newton-centimetre", "Newton-metre"),
]

print("UNIVERSAL CONVERTER")
print("ENGINEERING EDITION")
print("=" * 60)

for value, category, from_unit, to_unit in tests:
    result = engine.convert(value, category, from_unit, to_unit)
    print(f"{value} {from_unit} = {result} {to_unit}")

print("=" * 60)
print("Torque tests completed.")
