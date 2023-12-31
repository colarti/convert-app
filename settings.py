list_distance = ['nm', 'um', 'cm', 'mm', 'm', 'km', 'in', 'ft', 'yd', 'mi', 'knot']
list_fluid = ['oz', 'pint', 'liter', 'gallon']

WIDTH = 500
HEIGHT = 200

CONVERT_LIST = {
    'nm':{'nm':1, 'um':0.001, 'mm':0.000001, 'cm':0.0000001, 'm':0.000000001, 'km':0.000000000001, 'in':0.00000003937, 'ft':0.0000000032808, 'yd':0.0000000010936, 'mi':0.00000000000062137},
    'um':{'nm':1000, 'um':1, 'mm':0.001, 'cm':0.0001, 'm':0.000001, 'km':0.000000001, 'in':0.00003937, 'ft':0.000032808, 'yd':0.0000010936, 'mi':0.00000000062137},
    'cm':{'nm':10000000, 'um':10000, 'mm':10, 'cm':1, 'm':0.01, 'km':0.00001, 'in':0.3937, 'ft':0.0328084, 'yd':0.010936, 'mi':0.0000062137},
    'mm':{'nm':1000000, 'um':1000, 'mm':1, 'cm':0.1, 'm':0.001, 'km':0.000001, 'in':0.03937, 'ft':0.00328084, 'yd':0.0010936, 'mi':0.0000062137},
    'm':{'nm':1000000000, 'um':1000000, 'mm':1000, 'cm':100, 'm':1, 'km':0.001, 'in':39.3701, 'ft':3.28084, 'yd':1.0936, 'mi':0.00000062137},
    'km':{'nm':1000000000000, 'um':1000000000, 'mm':1000000, 'cm':100000, 'm':1000, 'km':1, 'in':39370.1, 'ft':3280.84, 'yd':1093.61, 'mi':0.62137},
    'in':{'nm':25400000, 'um':25400, 'mm':25.4, 'cm':2.54, 'm':0.0254, 'km':0.0000254, 'in':1, 'ft':0.0833333, 'yd':0.0277778, 'mi':0.000015783},
    'ft':{'nm':304800000, 'um':304800, 'mm':304.8, 'cm':30.48, 'm':0.3048, 'km':0.0003048, 'in':12, 'ft':1, 'yd':0.333333, 'mi':0.000189394},
    'yd':{'nm':914400000, 'um':914400, 'mm':914.4, 'cm':91.44, 'm':0.9144, 'km':0.0009144, 'in':36, 'ft':3, 'yd':1, 'mi':0.000568182},
    'mi':{'nm':1609000000000, 'um':1609000000, 'mm':1609000, 'cm':160934, 'm':1609.34, 'km':1.60934, 'in':63360, 'ft':5280, 'yd':1760, 'mi':1},
}