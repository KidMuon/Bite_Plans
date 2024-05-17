from enum import StrEnum

class MeasurementNames(StrEnum):
    Teaspoon = 'Teaspoon'
    Tablespoon = 'Tablespoon'
    Cup = 'Cup'
    fl_OZ = 'Fluid Ounce'
    lb = 'lbs'
    Count = 'Count'
    Slice = "Slice"
    Ounce = 'oz'

class Measurement:
    _measurement_lookup = {
    'tsp': MeasurementNames.Teaspoon,
    'Teaspoon': MeasurementNames.Teaspoon,
    'tbsp': MeasurementNames.Tablespoon,
    'Tablespoon': MeasurementNames.Tablespoon,
    'cup': MeasurementNames.Cup,
    'lb': MeasurementNames.lb,
    'count': MeasurementNames.Count,
    'slice': MeasurementNames.Slice,
    'oz': MeasurementNames.Ounce
    }

    def __init__(self, amount_of_measure, measurement):
        self.amount = amount_of_measure
        if self._measurement_lookup.get(measurement, None):
            self.measurement = self._measurement_lookup.get(measurement, None)
        else:
            raise ValueError("Measurement not in lookup table.")

    def adjustMeasurement(self, scale_factor):
        self.amount *= scale_factor