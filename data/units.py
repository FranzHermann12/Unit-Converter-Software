
from decimal import Decimal, getcontext

# Set precision before calculating any conversion factors.
getcontext().prec = 50


UNIT_DATABASE = {

    # LENGTH — Base: metre
    "Length": {
        "Metre": Decimal("1"),
        "Kilometre": Decimal("1000"),
        "Centimetre": Decimal("0.01"),
        "Millimetre": Decimal("0.001"),
        "Micrometre": Decimal("0.000001"),
        "Nanometre": Decimal("0.000000001"),
        "Mile": Decimal("1609.344"),
        "Yard": Decimal("0.9144"),
        "Foot": Decimal("0.3048"),
        "Inch": Decimal("0.0254"),
        "Nautical Mile": Decimal("1852"),
    },

    # TEMPERATURE — Base: Kelvin
    "Temperature": {
        "Celsius": (Decimal("1"), Decimal("273.15")),
        "Fahrenheit": (
            Decimal("5") / Decimal("9"),
            Decimal("459.67") * Decimal("5") / Decimal("9")
        ),
        "Kelvin": (Decimal("1"), Decimal("0")),
        "Rankine": (Decimal("5") / Decimal("9"), Decimal("0")),
    },

    # MASS — Base: kilogram
    "Mass": {
        "Kilogram": Decimal("1"),
        "Gram": Decimal("0.001"),
        "Milligram": Decimal("0.000001"),
        "Microgram": Decimal("0.000000001"),
        "Metric Tonne": Decimal("1000"),
        "Pound": Decimal("0.45359237"),
        "Ounce": Decimal("0.028349523125"),
        "Stone": Decimal("6.35029318"),
    },

    # TIME — Base: second
    "Time": {
        "Second": Decimal("1"),
        "Millisecond": Decimal("0.001"),
        "Microsecond": Decimal("0.000001"),
        "Nanosecond": Decimal("0.000000001"),
        "Minute": Decimal("60"),
        "Hour": Decimal("3600"),
        "Day": Decimal("86400"),
        "Week": Decimal("604800"),
        "Julian Year": Decimal("31557600"),
    },

    # AREA — Base: square metre
    "Area": {
        "Square Metre": Decimal("1"),
        "Square Kilometre": Decimal("1000000"),
        "Square Centimetre": Decimal("0.0001"),
        "Square Millimetre": Decimal("0.000001"),
        "Hectare": Decimal("10000"),
        "Acre": Decimal("4046.8564224"),
        "Square Foot": Decimal("0.09290304"),
        "Square Inch": Decimal("0.00064516"),
        "Square Yard": Decimal("0.83612736"),
    },

    # VOLUME — Base: cubic metre
    "Volume": {
        "Cubic Metre": Decimal("1"),
        "Cubic Centimetre": Decimal("0.000001"),
        "Cubic Millimetre": Decimal("0.000000001"),
        "Litre": Decimal("0.001"),
        "Millilitre": Decimal("0.000001"),
        "US Gallon": Decimal("0.003785411784"),
        "US Quart": Decimal("0.000946352946"),
        "US Pint": Decimal("0.000473176473"),
        "US Cup": Decimal("0.0002365882365"),
        "US Fluid Ounce": Decimal("0.0000295735295625"),
        "Cubic Foot": Decimal("0.028316846592"),
        "Cubic Inch": Decimal("0.000016387064"),
    },

    # SPEED — Base: metre per second
    "Speed": {
        "Metre per Second": Decimal("1"),
        "Kilometre per Hour": Decimal("0.2777777777777777777777777778"),
        "Mile per Hour": Decimal("0.44704"),
        "Foot per Second": Decimal("0.3048"),
        "Knot": Decimal("0.5144444444444444444444444444"),
        "Centimetre per Second": Decimal("0.01"),
    },

    # ACCELERATION — Base: metre per second squared
    "Acceleration": {
        "Metre per Second Squared": Decimal("1"),
        "Foot per Second Squared": Decimal("0.3048"),
        "Standard Gravity": Decimal("9.80665"),
        "Gal": Decimal("0.01"),
        "Kilometre per Hour Squared": Decimal("0.00007716049382716049382716049"),
    },

    # FORCE — Base: newton
    "Force": {
        "Newton": Decimal("1"),
        "Kilonewton": Decimal("1000"),
        "Millinewton": Decimal("0.001"),
        "Dyne": Decimal("0.00001"),
        "Pound-force": Decimal("4.4482216152605"),
        "Kilogram-force": Decimal("9.80665"),
    },

    # PRESSURE — Base: pascal
    "Pressure": {
        "Pascal": Decimal("1"),
        "Kilopascal": Decimal("1000"),
        "Megapascal": Decimal("1000000"),
        "Bar": Decimal("100000"),
        "Millibar": Decimal("100"),
        "Standard Atmosphere": Decimal("101325"),
        "Torr": Decimal("133.3223684210526315789473684"),
        "PSI": Decimal("6894.757293168"),
        "Technical Atmosphere": Decimal("98066.5"),
    },

    # ENERGY — Base: joule
    "Energy": {
        "Joule": Decimal("1"),
        "Kilojoule": Decimal("1000"),
        "Megajoule": Decimal("1000000"),
        "Calorie": Decimal("4.184"),
        "Kilocalorie": Decimal("4184"),
        "Watt-hour": Decimal("3600"),
        "Kilowatt-hour": Decimal("3600000"),
        "Electronvolt": Decimal("1.602176634E-19"),
        "British Thermal Unit": Decimal("1055.05585262"),
        "Foot-pound": Decimal("1.3558179483314004"),
    },

    # POWER — Base: watt
    "Power": {
        "Watt": Decimal("1"),
        "Kilowatt": Decimal("1000"),
        "Megawatt": Decimal("1000000"),
        "Milliwatt": Decimal("0.001"),
        "Mechanical Horsepower": Decimal("745.6998715822702"),
        "Metric Horsepower": Decimal("735.49875"),
        "BTU per Hour": Decimal("0.2930710701722222"),
        "Foot-pound per Second": Decimal("1.3558179483314004"),
    },

    # TORQUE — Base: newton metre
    "Torque": {
        "Newton-metre": Decimal("1"),
        "Kilonewton-metre": Decimal("1000"),
        "Newton-centimetre": Decimal("0.01"),
        "Pound-foot": Decimal("1.3558179483314004"),
        "Pound-inch": Decimal("0.1129848290276167"),
        "Kilogram-force metre": Decimal("9.80665"),
    },

    # DENSITY — Base: kilogram per cubic metre
    "Density": {
        "Kilogram per Cubic Metre": Decimal("1"),
        "Gram per Cubic Centimetre": Decimal("1000"),
        "Gram per Litre": Decimal("1"),
        "Kilogram per Litre": Decimal("1000"),
        "Pound per Cubic Foot": Decimal("16.01846337396"),
        "Pound per Cubic Inch": Decimal("27679.9047102"),
    },

    # FREQUENCY — Base: hertz
    "Frequency": {
        "Hertz": Decimal("1"),
        "Kilohertz": Decimal("1000"),
        "Megahertz": Decimal("1000000"),
        "Gigahertz": Decimal("1000000000"),
        "Terahertz": Decimal("1000000000000"),
        "Revolutions per Minute": Decimal("0.01666666666666666666666666667"),
        "Revolutions per Second": Decimal("1"),
    },

    # ANGLE — Base: degree
    "Angle": {
        "Degree": Decimal("1"),
        "Radian": Decimal("57.29577951308232087679815481"),
        "Gradian": Decimal("0.9"),
        "Arcminute": Decimal("0.01666666666666666666666666667"),
        "Arcsecond": Decimal("0.0002777777777777777777777778"),
        "Revolution": Decimal("360"),
    },

    # ELECTRICAL CURRENT — Base: ampere
    "Current": {
        "Ampere": Decimal("1"),
        "Milliampere": Decimal("0.001"),
        "Microampere": Decimal("0.000001"),
        "Kiloampere": Decimal("1000"),
    },

    # VOLTAGE — Base: volt
    "Voltage": {
        "Volt": Decimal("1"),
        "Millivolt": Decimal("0.001"),
        "Kilovolt": Decimal("1000"),
        "Megavolt": Decimal("1000000"),
    },

    # ELECTRICAL RESISTANCE — Base: ohm
    "Resistance": {
        "Ohm": Decimal("1"),
        "Milliohm": Decimal("0.001"),
        "Kiloohm": Decimal("1000"),
        "Megohm": Decimal("1000000"),
    },

    # CAPACITANCE — Base: farad
    "Capacitance": {
        "Farad": Decimal("1"),
        "Millifarad": Decimal("0.001"),
        "Microfarad": Decimal("0.000001"),
        "Nanofarad": Decimal("0.000000001"),
        "Picofarad": Decimal("0.000000000001"),
    },

    # ELECTRIC CHARGE — Base: coulomb
    "Charge": {
        "Coulomb": Decimal("1"),
        "Millicoulomb": Decimal("0.001"),
        "Microcoulomb": Decimal("0.000001"),
        "Ampere-hour": Decimal("3600"),
        "Milliampere-hour": Decimal("3.6"),
    },

}
