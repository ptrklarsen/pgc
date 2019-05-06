import pandas as pd
from date_objects import today




class BaseDFs:
    basePhrDf = pd.read_csv(f'/Volumes/Quick Reference/CS-Vees/phr_cs_vees/phr_{today}.csv', thousands=',', header=None)
    baseJSR = pd.read_csv(f'/Volumes/Quick Reference/CS-Vees/JSRI_cs-vees/jsri_l_{today}.csv', thousands=',', header=None)

