import pandas as pd
from baseDFs import BaseDFs


def phr_scrubber(phr):
    phr.dropna(how='all', inplace=True)
    phr.dropna(subset=[0], inplace=True)
    fltr = phr[0].str.match(r'[0-9]{7}.?')
    indexedtodrop = phr[~fltr].index
    phr.drop(indexedtodrop, inplace=True)
    phr[4] = pd.to_datetime(phr[4], format='%m/%d/%Y')
    phr[5] = pd.to_datetime(phr[5], format='%m/%d/%Y')
    cols = [12, 13, 14, 15, 16, 17, 18, 19]
    phr[cols] = phr[cols].replace({',': ''}, regex=True)
    phr[cols] = phr[cols].apply(pd.to_numeric, downcast='integer', errors='coerce')  # added 4/04/2019
    values = {4: 'N/A', 7: 'TBD', 9: "TBD", 10: "TBD", 11: "TBD", 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0,
              19: 0}
    phr.fillna(value=values, inplace=True)
    phr.columns = ['Job #', 'Job Name', 'Div', 'Sta', 'Sta Date', 'Contract Date', 'Cntrl_Prog_Req',
                   'Cntrl_Prgmr', 'DSP_Req', 'DSP_Prgmr', 'PE', 'PM', 'Contr. Amt', 'LEP Budget', 'LEP Actual',
                   'LEP Variance', 'EstRem', 'LED Budget', 'LED Actual', 'LED Variance']
    return phr


def jsr_scrubber(jsr):
    # get find a row with the column headers
    indexesOfPotentialHeaderRows = list(jsr[jsr[0] == 'Job #'].index)
    columns = indexesOfPotentialHeaderRows[0]
    header = list(jsr.loc[columns])
    # find and drop rows with NA values in the 8th column
    s = pd.isna(jsr[8])
    drop_these = jsr[s.values].index
    jsr.drop(drop_these, inplace=True)
    # isolate rows with target data and remove unwanted rows
    pattern = "[0-9]+[/]"
    filter = jsr[8].str.contains(pattern)
    indexesOfKeeperRows = jsr[filter].index
    droptheRest = jsr.loc[~jsr.index.isin(indexesOfKeeperRows)].index
    jsr.drop(droptheRest, inplace=True)
    jsr[0].ffill(inplace=True)
    values = {4: 'No', 7: 'No', 16: 0}
    jsr.fillna(value=values, inplace=True)
    # set column names
    jsr.columns = header
    return jsr


class WorkingDFs(BaseDFs):
    phr = phr_scrubber(BaseDFs.basePhrDf.copy())
    jsr = jsr_scrubber(BaseDFs.baseJSR.copy())
