#!/usr/bin/env python

import numpy
import numpy.random
import subprocess

import textwrap

numpy.random.seed(12345678)

def random_sequence():
    return "".join(numpy.random.choic(list("ACGT", n)))
    
for i in range(1000):
    
    print ">%d" % i
    
    print "\n".join(textwrap.wrap(random_sequence(1000), 60))
 