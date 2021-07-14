from sympy.physics.units.systems import SI


def set_quantity(quantity, dimension, scale_factor):
    """
    Set value and unit to physical quantity.
    Example:

        >>> import sympy.physics.units as un
        >>> from sympy.functions import *
        >>> from sympy.physics.units import Quantity
        >>> from utils import *
        >>> from sympy.physics.units import convert_to
        >>>
        >>> E = Quantity("E")
        >>> c = Quantity("c")

        >>> set_quantity(E, un.energy, 2.15e12 * un.kilo * un.watts * un.hour)
        >>> set_quantity(c, un.speed,  3.00e8  * un.m / un.s)
        >>> E = convert_to(E, un.joule).n()
        >>> m = E/c**2
        7.74e+18*joule/c**2

        convert_to(m, un.kg).n()
        86.0*kilogram

    :param quantity: physical quantity, for example length, mass or energy
    :param dimension: time, length, mass ... based on sympy.physics.units
    :param scale_factor: value to be set to `quantity` parameter
    """
    SI.set_quantity_dimension(quantity, dimension)
    SI.set_quantity_scale_factor(quantity, scale_factor)


def get_quantity(quantity, dimension, scale_factor):
    """
    Create physical quantity with value and unit preset.
    Example:

        >>> import sympy.physics.units as un
        >>> from sympy.functions import *
        >>> from sympy.physics.units import Quantity
        >>> from utils import *
        >>> from sympy.physics.units import convert_to
        >>>
        >>> s = get_quantity(Quantity("s"), un.length, 3.6 * un.km)
        >>> t = get_quantity(Quantity("t"), un.time, 1 * un.h)
        >>> v = s / t
        >>> convert_to(v, un.m / un.s).n()
        1.0*meter/second

    :param quantity: physical quantity, for example length, mass or energy
    :param dimension: time, length, mass ... based on sympy.physics.units
    :param scale_factor: value to be set to `quantity` parameter
    :return: quantity with parameters preset
    """
    set_quantity(quantity, dimension, scale_factor)
    return quantity
