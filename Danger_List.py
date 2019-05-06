#!/Users/ptrk/.local/share/virtualenvs/testing-fhubOXGg/bin/python

import pandas as pd
from datetime import *


raw_today = date.today()
today = raw_today.strftime("%y%m%d")
raw_yesterday = raw_today - timedelta(days = 1)
yesterday = raw_yesterday.strftime("%y%m%d")


def phr():
    phr = pd.read_csv(f'/Volumes/Quick Reference/CS-Vees/phr_cs_vees/phr_190419.csv', thousands=',', header=None)

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

    phr = phr[(phr['Cntrl_Prgmr'] == 'TBD') & (phr.Cntrl_Prog_Req == 'Yes') & ~(phr['Contract Date'].isna())]
    return phr


def return_prog_jobs_list(dataframe):
    return dataframe["Job #"].tolist()


def jsr():
    jsri_no_trvl = pd.read_csv(f'/Volumes/Quick Reference/CS-Vees/JSRI_cs-vees/jsri_190419.csv', header=None)
    jsri_no_trvl.columns = jsri_no_trvl[jsri_no_trvl.iloc[:, 0] == 'Job #'].iloc[0]
    jsri_no_trvl = jsri_no_trvl.dropna(how='all')
    jsri_no_trvl["Job #"] = jsri_no_trvl['Job #'].ffill()
    jsri_no_trvl = jsri_no_trvl[jsri_no_trvl['Job #'].str.match(r'[0-9]{7}.?')]
    jsri_no_trvl['Cmp'] = jsri_no_trvl.Cmp.fillna('No')
    jsri_no_trvl['Mile'] = jsri_no_trvl.Cmp.fillna('No')
    jsri_no_trvl['Room/Location/Phase'] = jsri_no_trvl['Room/Location/Phase'].fillna('')
    jsri_no_trvl['Float'] = jsri_no_trvl.Float.fillna(0)
    jsri_no_trvl['Start Dt'] = pd.to_datetime(jsri_no_trvl['Start Dt'])
    jsri_no_trvl['Stop Dt'] = pd.to_datetime(jsri_no_trvl['Stop Dt'])
    # jsri_no_trvl.rename(columns={'Job #': 'Job_Number'}, inplace=True)
    jsri_no_trvl = jsri_no_trvl[jsri_no_trvl['Job #'].isin(return_prog_jobs_list(phr()))]
    jsr = jsri_no_trvl
    jsr['Start Dt'] = pd.to_datetime(jsr['Start Dt'], format='%m/%d/%Y')
    jsr['Stop Dt'] = pd.to_datetime(jsr['Stop Dt'], format='%m/%d/%Y')
    jsr = jsr.sort_values('Start Dt')
    return jsr


def generate_danger_list(jsr, phr):
    danger_list = list(set(jsr['Job #']))
    danger_list_df = phr[phr['Job #'].isin(danger_list)]
    return danger_list_df


# def generate_excel_file():
writer = pd.ExcelWriter(f'/Volumes/Quick Reference/Reports/Danger_Lists/Near_Horizon_List_{today}.xlsx')

generate_danger_list(jsr(), phr()).to_excel(writer, 'Near Horizon List')
jsr().to_excel(writer, 'Schedule')

writer.save()

#
# def main():
#     generate_excel_file()


# main()

