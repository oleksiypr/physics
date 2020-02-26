from sympy.physics.units.systems import SI


def set_quantity(unit, dimension, scale_factor):
    """
    set value and unit to physical quantity
    :param unit:
    :param dimension:
    :param scale_factor:
    :return:
    """
    SI.set_quantity_dimension(unit, dimension)
    SI.set_quantity_scale_factor(unit, scale_factor)
