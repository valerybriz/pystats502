#!/usr/bin/env python

"""Este codigo toma 4 variables:
- sexo
- fecha de nacimiento
- peso
- talla

y da como resultado los siguientes indices:
- peso para edad
- talla para edad
- peso-talla

en base a las tablas de referencia:
http://www.who.int/childgrowth/standards/en/
"""

import os
import numpy as np

class Growth(object):
    def __init__(self, indicator, measurement, age_in_months, sex,
                 height, american):
        self.age = float(age_in_months)
        self.sex = sex.upper()
        self.height = float(height)
        self.indicator = indicator
        self.measurement = measurement
        self.position = None
        self.american = american

        self.table_indicator = None
        self.table_age = None
        self.table_sex = None

def age_in_weeks(self):
    return ((self.age * 30.4374) / 7.0)


