
from decimal import Decimal, getcontext

from data.units import UNIT_DATABASE

getcontext().prec = 50


class ConversionEngine:
    """High-precision engineering unit conversion engine."""

    def __init__(self):
        self.units = {}
        self.load_default_units()

    def load_default_units(self):
        """Load units from the central database."""

        for category, category_units in UNIT_DATABASE.items():
            self.units[category] = {}

            for unit_name, definition in category_units.items():

                if isinstance(definition, tuple):
                    factor, offset = definition
                else:
                    factor, offset = definition, Decimal("0")

                self.register_unit(
                    category,
                    unit_name,
                    factor,
                    offset
                )

    def register_unit(self, category, unit_name, factor, offset=0):
        """Register a unit relative to its category's base unit."""

        factor = Decimal(str(factor))
        offset = Decimal(str(offset))

        if not factor.is_finite() or factor <= 0:
            raise ValueError("Unit factor must be finite and positive.")

        if not offset.is_finite():
            raise ValueError("Unit offset must be finite.")

        self.units.setdefault(category, {})
        self.units[category][unit_name] = (factor, offset)

    def convert(self, value, category, from_unit, to_unit):
        """Convert a value between compatible units."""

        try:
            value = Decimal(str(value))
        except Exception as error:
            raise ValueError("Please enter a valid number.") from error

        if not value.is_finite():
            raise ValueError("The value must be finite.")

        if category not in self.units:
            raise ValueError(f"Unknown category: {category}")

        available_units = self.units[category]

        if from_unit not in available_units:
            raise ValueError(f"Unknown unit: {from_unit}")

        if to_unit not in available_units:
            raise ValueError(f"Unknown unit: {to_unit}")

        from_factor, from_offset = available_units[from_unit]
        to_factor, to_offset = available_units[to_unit]

        base_value = value * from_factor + from_offset
        result = (base_value - to_offset) / to_factor

        return result
