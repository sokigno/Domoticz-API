#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import platform
import os
import subprocess
"""
    Utilities
"""
VERSION_MAJOR = 0
VERSION_MINOR = 7
VERSION_PATCH = 1
VERSION_IDENTIFIER = "beta"

VERSION_SHORT = '{}.{}'.format(VERSION_MAJOR, VERSION_MINOR)
VERSION = "{}.{}.{}-{}".format(VERSION_MAJOR,
                               VERSION_MINOR, VERSION_PATCH, VERSION_IDENTIFIER)


def machine():
    return platform.machine()


def node():
    return platform.node()


def os_command(command):
    p = subprocess.Popen(command, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    data, errors = p.communicate()
    if p.returncode != 0:
        r = None
    else:
        r = data.decode("utf-8", "ignore")
    return r


def os_release():
    return platform.release()


def os_version():
    return platform.version()


def processor():
    return platform.processor()


def python_version():
    return platform.python_version()


def system():
    return platform.system()


def version():
    return VERSION


def version_identifier():
    return VERSION_IDENTIFIER


def version_major():
    return VERSION_MAJOR


def version_minor():
    return VERSION_MINOR


def version_patch():
    return VERSION_PATCH


def version_short():
    return VERSION_SHORT

# Temperature conversion from Celsius to Fahrenheit


def c_2_f(value):
    return (value * 1.8) + 32


# Temperature conversion from Fahrenheit to Celsius
def f_2_c(value):
    return (value - 32) / 1.8

# Convert bearing in degrees to a direction


def bearing_2_status(d):
    """
    Based on https://gist.github.com/RobertSudwarts/acf8df23a16afdb5837f
    """
    dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

    count = len(dirs)  # Number of entries in list
    step = 360 / count  # Wind direction is in steps of 22.5 degrees (360/16)
    ix = int((d + (step / 2)) / step)  # Calculate index in the list
    return dirs[ix % count]
