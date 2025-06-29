"""
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the stubs
with your own implementations.

River Strumwasser (rns88) and Katherine Son (ks2395)
10/2/23
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.

    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    # THIS IS WRONG.  FIX IT
    return introcs.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.

    The decimal point counts as one of the five characters.

    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.

    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Remember that the rounding takes place at a different place depending
    # on how big value is. Look at the examples in the specification.
    valuenew = str(float(value))

    if float(valuenew) < 0.00001:
        return '0.000'

    dec = valuenew.index('.')

    if len(valuenew) < 6:
        valuenew = valuenew + (6-len(valuenew)) * '0'

    if int(valuenew[5]) > 4:
        valuenew = str(float(valuenew[:5]) + 1 / (10.0 ** (4-dec)))
    else:
        valuenew = valuenew[:5]

    if len(valuenew) < 5:
        valuenew = valuenew + (5-len(valuenew)) * '0'

    return valuenew[:5]


def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".

    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)

    Example: if str(cmyk) is

          '(0.0,31.3725490196,31.3725490196,0.0)'

    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.

    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    return ('('+str5(cmyk.cyan)+', '+str5(cmyk.magenta)+', '+
    str5(cmyk.yellow)+', '+str5(cmyk.black)+')')


def str5_hsv(hsv):
    """
    Returns the string representation of hsv in the form "(H, S, V)".

    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)

    Example: if str(hsv) is

          '(0.0,0.313725490196,1.0)'

    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.

    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    return ('('+str5(hsv.hue)+', '+str5(hsv.saturation)+', '+
    str5(hsv.value)+')')


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.

    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html

    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to the range 0..1 by dividing them by 255.0.
    rx = rgb.red/255
    gx = rgb.green/255
    bx = rgb.blue/255
    k = 1 - max(rx, gx, bx)

    if k != 1:
        c = (1-rx-k)/(1-k)
        m = (1-gx-k)/(1-k)
        y = (1-bx-k)/(1-k)
    else:
        return introcs.CMYK(0.0,0.0,0.0,100.0)

    return introcs.CMYK(100*c, 100*m, 100*y, 100*k)


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk

    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html

    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0.
    # Deal with them the same way as the RGB numbers in rgb_to_cmyk()
    c = cmyk.cyan
    m = cmyk.magenta
    y = cmyk.yellow
    k = cmyk.black

    r = round(255*(1-c/100)*(1-k/100))
    g = round(255*(1-m/100)*(1-k/100))
    b = round(255*(1-y/100)*(1-k/100))

    #print(str(introcs.RGB(r, g, b)))
    return introcs.RGB(r, g, b)


def rgb_to_hsv(rgb):
    """
    Return an HSV object equivalent to rgb

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter hsv: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    rx = rgb.red/255
    gx = rgb.green/255
    bx = rgb.blue/255
    cmax = max(rx, gx, bx)
    cmin = min(rx, gx, bx)
    delt = cmax - cmin

    if delt == 0:
        h = 0
    elif cmax == rx:
        if gx >= bx:
            h = 60 * (gx - bx)/delt
        else:
            h = 60 * (gx - bx)/delt + 360
    elif cmax == gx:
        h = 60 * (bx - rx)/delt + 120
    else:
        h = 60 * (rx - gx)/delt + 240

    if cmax == 0:
        s = 0
    else:
        s = 1 - cmin/cmax

    v = cmax

    return introcs.HSV(h, s, v)


def hsv_to_rgb(hsv):
    """
    Returns an RGB object equivalent to hsv

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    hi = math.floor(hsv.hue/60)
    f = hsv.hue/60 - hi
    p = hsv.value*(1-hsv.saturation)
    q = hsv.value*(1-f*hsv.saturation)
    t = hsv.value*(1-(1-f)*hsv.saturation)

    if hi == 0 or hi == 5:
        r = hsv.value
    elif hi == 1:
        r = q
    elif hi == 2 or hi == 3:
        r = p
    else:
        r = t

    if hi == 0:
        g = t
    elif hi == 1 or hi == 2:
        g = hsv.value
    elif hi == 3:
        g = q
    else:
        g = p

    if hi == 0 or hi == 1:
        b = p
    elif hi == 2:
        b = t
    elif hi == 3 or hi == 4:
        b = hsv.value
    else:
        b = q

    return introcs.RGB(round(255*r),round(255*g),round(255*b))


def hsv_gamma(hsv,gamma):
    """
    Applies the gamma to the given HSV object.

    This function is a PROCEDURE. It modifies hsv and has no return value. It applies
    the gamma value by raising the value to that exponent.

    Parameter hsv: the color to adjust
    Precondition: hsv is a HSV object

    Parameter gamma: the gamm value (1.0 for no gamma)
    Precondition: gamma is a float in 0..2
    """
    v = hsv.value ** gamma
    hsv.value = v


def rgb_gamma(rgb,gamma):
    """
    Returns a new RGB with the given gamma value applied.

    This function should convert the RGB object to an HSV object, apply the gamma,
    and convert it back.

    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object

    Parameter gamma: the gamm value (1.0 for no gamma)
    Precondition: gamma is a float in 0..2
    """
    hsv = rgb_to_hsv(rgb)
    hsv_gamma(hsv, gamma)
    rgbnew = hsv_to_rgb(hsv)
    return rgbnew
