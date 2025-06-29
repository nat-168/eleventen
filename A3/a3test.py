"""
Unit Test for Assignment A3

This module implements several test cases for a3.  It is incomplete.  You should look
though this file for places to add tests.

River Strumwasser (rns88) and Katherine Son (ks2395)
10/2/23
"""
import introcs
import a3


def test_complement():
    """
    Test function complement
    """
    print('Testing complement')

    # One test is really good enough here
    comp = a3.complement_rgb(introcs.RGB(250, 0, 71))
    introcs.assert_equals(255-250, comp.red)
    introcs.assert_equals(255-0,   comp.green)
    introcs.assert_equals(255-71,  comp.blue)

    # One more for good measure
    comp = a3.complement_rgb(introcs.RGB(128, 64, 255))
    introcs.assert_equals(255-128, comp.red)
    introcs.assert_equals(255-64,  comp.green)
    introcs.assert_equals(255-255, comp.blue)


def test_str5():
    """
    Test function str5
    """
    introcs.assert_equals('130.6',  a3.str5(130.59))
    introcs.assert_equals('130.5',  a3.str5(130.54))
    introcs.assert_equals('100.0',  a3.str5(100))
    introcs.assert_equals('100.6',  a3.str5(100.56))
    introcs.assert_equals('99.57',  a3.str5(99.566))
    introcs.assert_equals('99.99',  a3.str5(99.99))
    introcs.assert_equals('100.0',  a3.str5(99.995))
    introcs.assert_equals('22.00',  a3.str5(21.99575))
    introcs.assert_equals('21.99',  a3.str5(21.994))
    introcs.assert_equals('10.01',  a3.str5(10.013567))
    introcs.assert_equals('10.00',  a3.str5(10.000000005))
    introcs.assert_equals('10.00',  a3.str5(9.9999))
    introcs.assert_equals('9.999',  a3.str5(9.9993))
    introcs.assert_equals('1.355',  a3.str5(1.3546))
    introcs.assert_equals('1.354',  a3.str5(1.3544))
    introcs.assert_equals('0.046',  a3.str5(.0456))
    introcs.assert_equals('0.045',  a3.str5(.0453))
    introcs.assert_equals('0.006',  a3.str5(.0056))
    introcs.assert_equals('0.001',  a3.str5(.0013))
    introcs.assert_equals('0.000',  a3.str5(.0004))
    introcs.assert_equals('0.001',  a3.str5(.0009999))
    introcs.assert_equals('0.000',  a3.str5(1e-9))


def test_str5_color():
    """
    Test the str5 functions for cmyk and hsv.
    """
    print('Testing str5_cmyk and str5_hsv')

    # Tests for str5_cmyk
    # We need to make sure the coordinates round properly
    text = a3.str5_cmyk(introcs.CMYK(98.448, 25.362, 72.8, 1.0))
    introcs.assert_equals('(98.45, 25.36, 72.80, 1.000)',text)

    text = a3.str5_cmyk(introcs.CMYK(0.0, 1.5273, 100.0, 57.846))
    introcs.assert_equals('(0.000, 1.527, 100.0, 57.85)',text)

    # Tests for str5_hsv (add two)
    text = a3.str5_hsv(introcs.HSV(99.9999, 0.9984, 0.013))
    introcs.assert_equals('(100.0, 0.998, 0.013)',text)

    text = a3.str5_hsv(introcs.HSV(359.94, 1.0, 0.00))
    introcs.assert_equals('(359.9, 1.000, 0.000)',text)

    # places carried (99.999 for H)
    # edge cases (359.9 for H, 1 for S, 0 for V)
    # all positions for decimal (100.0, 10.0, 0.0 for H, 0.0 for SV)
    # add 0s necessary (1.0 --> 1.000, str len 3, 4, 5+)
    # round up, round down


def test_rgb_to_cmyk():
    """
    Test translation function rgb_to_cmyk
    """
    print('Testing rgb_to_cmyk')

    # The function should guarantee accuracy to three decimal places
    rgb = introcs.RGB(255, 255, 255)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(0.0, round(cmyk.black,3))

    rgb = introcs.RGB(0, 0, 0)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(100.0, round(cmyk.black,3))

    rgb = introcs.RGB(217, 43, 164)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(80.184, round(cmyk.magenta,3))
    introcs.assert_equals(24.424, round(cmyk.yellow,3))
    introcs.assert_equals(14.902, round(cmyk.black,3))


def test_cmyk_to_rgb():
    """
    Test translation function cmyk_to_rgb
    """
    print('Testing cmyk_to_rgb')

    #flipped from rgb to cmyk — given by introcs lab
    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(255, round(rgb.red,3))
    introcs.assert_equals(255, round(rgb.green,3))
    introcs.assert_equals(255, round(rgb.blue,3))

    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 100.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, round(rgb.red,3))
    introcs.assert_equals(0, round(rgb.green,3))
    introcs.assert_equals(0, round(rgb.blue,3))

    #ints instead of float
    cmyk = introcs.CMYK(0, 0, 0, 100)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, round(rgb.red,3))
    introcs.assert_equals(0, round(rgb.green,3))
    introcs.assert_equals(0, round(rgb.blue,3))

    cmyk = introcs.CMYK(0.0, 80.184, 24.424, 14.902)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(217, round(rgb.red,3))
    introcs.assert_equals(43, round(rgb.green,3))
    introcs.assert_equals(164, round(rgb.blue,3))


def test_rgb_to_hsv():
    """
    Test translation function rgb_to_hsv
    """
    print('Testing rgb_to_hsv')

    # low extreme (black), cmax = cmin, cmax = 0
    rgb = introcs.RGB(0, 0, 0)
    hsv = a3.rgb_to_hsv(rgb)
    introcs.assert_equals(0.0, round(hsv.hue,3))
    introcs.assert_equals(0.0, round(hsv.saturation,3))
    introcs.assert_equals(0.0, round(hsv.value,3))

    #high extreme (white), cmax != 0
    rgb = introcs.RGB(255, 255, 255)
    hsv = a3.rgb_to_hsv(rgb)
    introcs.assert_equals(0.0, round(hsv.hue,3))
    introcs.assert_equals(0.0, round(hsv.saturation,3))
    introcs.assert_equals(1.0, round(hsv.value,3))

    # asic test, redprime greatest w/ greenprime < blueprime
    rgb = introcs.RGB(217, 43, 164)
    hsv = a3.rgb_to_hsv(rgb)
    introcs.assert_equals(318.276, round(hsv.hue,3))
    introcs.assert_equals(0.802, round(hsv.saturation,3))
    introcs.assert_equals(0.851, round(hsv.value,3))

    # redprime greatest w/ greenprime > blueprime
    rgb = introcs.RGB(217, 164, 43)
    hsv = a3.rgb_to_hsv(rgb)
    introcs.assert_equals(41.724, round(hsv.hue,3))
    introcs.assert_equals(0.802, round(hsv.saturation,3))
    introcs.assert_equals(0.851, round(hsv.value,3))

    # greenprime greatest
    rgb = introcs.RGB(83, 223, 52)
    hsv = a3.rgb_to_hsv(rgb)
    introcs.assert_equals(109.123, round(hsv.hue,3))
    introcs.assert_equals(0.767, round(hsv.saturation,3))
    introcs.assert_equals(0.875, round(hsv.value,3))

    # blueprime greatest
    rgb = introcs.RGB(22, 97, 186)
    hsv = a3.rgb_to_hsv(rgb)
    introcs.assert_equals(212.561, round(hsv.hue,3))
    introcs.assert_equals(0.882, round(hsv.saturation,3))
    introcs.assert_equals(0.729, round(hsv.value,3))

    # r = g = b
    rgb = introcs.RGB(99, 99, 99)
    hsv = a3.rgb_to_hsv(rgb)
    introcs.assert_equals(0.0, round(hsv.hue,3))
    introcs.assert_equals(0.0, round(hsv.saturation,3))
    introcs.assert_equals(0.388, round(hsv.value,3))


def test_hsv_to_rgb():
    """
    Test translation function hsv_to_rgb
    """
    print('Testing hsv_to_rgb')

    # low extreme (black), int for hsv.hue intead of float
    hsv = introcs.HSV(0, 0.0, 0.0)
    rgb = a3.hsv_to_rgb(hsv)
    introcs.assert_equals(0, round(rgb.red,3))
    introcs.assert_equals(0, round(rgb.green,3))
    introcs.assert_equals(0, round(rgb.blue,3))

    # high extreme (white)
    hsv = introcs.HSV(0.0, 0.0, 1.0)
    rgb = a3.hsv_to_rgb(hsv)
    introcs.assert_equals(255, round(rgb.red,3))
    introcs.assert_equals(255, round(rgb.green,3))
    introcs.assert_equals(255, round(rgb.blue,3))

    # basic test, math.floor(hsv.hue/60) = 5
    hsv = introcs.HSV(318.276, 0.802, 0.851)
    rgb = a3.hsv_to_rgb(hsv)
    introcs.assert_equals(217, round(rgb.red,3))
    introcs.assert_equals(43, round(rgb.green,3))
    introcs.assert_equals(164, round(rgb.blue,3))

    # math.floor(hsv.hue/60) = 0
    hsv = introcs.HSV(41.724, 0.802, 0.851)
    rgb = a3.hsv_to_rgb(hsv)
    introcs.assert_equals(217, round(rgb.red,3))
    introcs.assert_equals(164, round(rgb.green,3))
    introcs.assert_equals(43, round(rgb.blue,3))

    # math.floor(hsv.hue/60) = 1
    hsv = introcs.HSV(109.123, 0.767, 0.875)
    rgb = a3.hsv_to_rgb(hsv)
    introcs.assert_equals(83, round(rgb.red,3))
    introcs.assert_equals(223, round(rgb.green,3))
    introcs.assert_equals(52, round(rgb.blue,3))

    # math.floor(hsv.hue/60) = 2
    hsv = introcs.HSV(130.0, 0.5, 0.6)
    rgb = a3.hsv_to_rgb(hsv)
    introcs.assert_equals(76, round(rgb.red,3))
    introcs.assert_equals(153, round(rgb.green,3))
    introcs.assert_equals(89, round(rgb.blue,3))

    # math.floor(hsv.hue/60) = 3
    hsv = introcs.HSV(212.561, 0.882, 0.729)
    rgb = a3.hsv_to_rgb(hsv)
    introcs.assert_equals(22, round(rgb.red,3))
    introcs.assert_equals(97, round(rgb.green,3))
    introcs.assert_equals(186, round(rgb.blue,3))

    # math.floor(hsv.hue/60) = 4
    hsv = introcs.HSV(250.0, 0.324, 0.234)
    rgb = a3.hsv_to_rgb(hsv)
    introcs.assert_equals(44, round(rgb.red,3))
    introcs.assert_equals(40, round(rgb.green,3))
    introcs.assert_equals(60, round(rgb.blue,3))


def test_contrast_value():
    """
    Test translation function contrast_value
    """
    print('Testing contrast_value')

    # contrast == -1.0 (extreme)
    result = a3.contrast_value(0.0,-1.0)
    introcs.assert_floats_equal(0.5,result)

    result = a3.contrast_value(1.0,-1.0)
    introcs.assert_floats_equal(0.5,result)

    # contrast < 0, bottom part of sawtooth
    result = a3.contrast_value(0.1,-0.5)
    introcs.assert_floats_equal(0.3,result)

    # contrast < 0, middle of sawtooth
    result = a3.contrast_value(0.4,-0.4)
    introcs.assert_floats_equal(0.4571429,result)

    # contrast < 0, upper part of sawtooth
    result = a3.contrast_value(0.9,-0.3)
    introcs.assert_floats_equal(0.8142857,result)

    # contrast == 0.0, bottom part of sawtooth
    result = a3.contrast_value(0.1,0.0)
    introcs.assert_floats_equal(0.1,result)

    # contrast == 0, middle of sawtooth
    result = a3.contrast_value(0.6,0.0)
    introcs.assert_floats_equal(0.6,result)

    # contrast == 0.0, upper part of sawtooth
    result = a3.contrast_value(0.9,0.0)
    introcs.assert_floats_equal(0.9,result)

    # contrast > 0, bottom part of sawtooth
    result = a3.contrast_value(0.1,0.3)
    introcs.assert_floats_equal(0.05384615,result)

    # contrast > 0, middle of sawtooth
    result = a3.contrast_value(0.4,0.5)
    introcs.assert_floats_equal(0.2,result)

    # contrast > 0, upper part of sawtooth
    result = a3.contrast_value(0.9,0.4)
    introcs.assert_floats_equal(0.95714286,result)

    # contrast == 1.0 (extreme)
    result = a3.contrast_value(0.2,1.0)
    introcs.assert_floats_equal(0.0,result)

    result = a3.contrast_value(0.6,1.0)
    introcs.assert_floats_equal(1.0,result)


def test_hsv_gamma():
    """
    Test translation procedure hsv_gamma
    """
    print('Testing hsv_gamma')
    # ADD TESTS TO ME (AT LEAST THREE)

    #basic test, int instead of float, lightening
    hsv = introcs.HSV(222, 0.75, 0.24)
    a3.hsv_gamma(hsv, 0.7)
    introcs.assert_equals(222.0, round(hsv.hue,3))
    introcs.assert_equals(0.75, round(hsv.saturation,3))
    introcs.assert_equals(0.368, round(hsv.value,3))

    #low extreme
    hsv = introcs.HSV(0.0, 0.0, 0.0)
    a3.hsv_gamma(hsv, 0.3)
    introcs.assert_equals(0.0, round(hsv.hue,3))
    introcs.assert_equals(0.0, round(hsv.saturation,3))
    introcs.assert_equals(0.0, round(hsv.value,3))

    #high ext
    hsv = introcs.HSV(0.0, 0.0, 1.0)
    a3.hsv_gamma(hsv, 0.6)
    introcs.assert_equals(0.0, round(hsv.hue,3))
    introcs.assert_equals(0.0, round(hsv.saturation,3))
    introcs.assert_equals(1.0, round(hsv.value,3))

    #darkening
    hsv = introcs.HSV(120, 0.5, 0.7)
    a3.hsv_gamma(hsv, 1.2)
    introcs.assert_equals(120.0, round(hsv.hue,3))
    introcs.assert_equals(0.5, round(hsv.saturation,3))
    introcs.assert_equals(0.652, round(hsv.value,3))


def test_rgb_gamma():
    """
    Test translation function rgb_gamma
    """
    print('Testing rgb_gamma')
    # ADD TESTS TO ME (AT LEAST THREE)

    # basic test, lightening
    rgb = introcs.RGB(162, 22, 39)
    rgbgam = a3.rgb_gamma(rgb, 0.5)
    introcs.assert_equals(203, round(rgbgam.red,3))
    introcs.assert_equals(28, round(rgbgam.green,3))
    introcs.assert_equals(49, round(rgbgam.blue,3))

    # low extreme
    rgb = introcs.RGB(0, 0, 0)
    rgbgam = a3.rgb_gamma(rgb, 0.2)
    introcs.assert_equals(0, round(rgbgam.red,3))
    introcs.assert_equals(0, round(rgbgam.green,3))
    introcs.assert_equals(0, round(rgbgam.blue,3))

    # high extreme
    rgb = introcs.RGB(255, 255, 255)
    rgbgam = a3.rgb_gamma(rgb, 0.2)
    introcs.assert_equals(255, round(rgbgam.red,3))
    introcs.assert_equals(255, round(rgbgam.green,3))
    introcs.assert_equals(255, round(rgbgam.blue,3))

    # darkening
    rgb = introcs.RGB(102, 65, 38)
    rgbgam = a3.rgb_gamma(rgb, 1.2)
    introcs.assert_equals(85, round(rgbgam.red,3))
    introcs.assert_equals(54, round(rgbgam.green,3))
    introcs.assert_equals(32, round(rgbgam.blue,3))


# Script Code
# THIS PREVENTS THE TESTS RUNNING ON IMPORT
if __name__ == '__main__':
    test_complement()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    test_hsv_gamma()
    test_rgb_gamma()
    print('Module a3 passed all tests.')
