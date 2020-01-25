from sympy.physics.units.systems import SI


def set_quantity(unit, dimension, scale_factor):
    SI.set_quantity_dimension(unit, dimension)
    SI.set_quantity_scale_factor(unit, scale_factor)
