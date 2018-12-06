class Preprocessor():

    def preprocess(self, polymer: str, unit_type: str):
        unit_types = unit_type + unit_type.swapcase()
        table = str.maketrans(unit_types, '  ', unit_types)
        preprocessed_polymer = polymer.translate(table)
        return preprocessed_polymer
