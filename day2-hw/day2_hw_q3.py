#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

metadata_output = "/Users/cmdb/cmdb-bootcamp-homework/day2-hw/samples.csv"

df = pd.read_table(metadata_output)


plt.figure ()
plt.plot(metadata_output)
plt.savefig("plot_fexpression.png")

samples_file = "/Users/cmdb/data/day2/samples.csv"
