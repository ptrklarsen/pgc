import workingDFs
import pandas as pd
import date_objects
import firstNames as fn

#todo: Incorporate the rest of DEV ENV Schedule Change tracker into this module


class Person:

    def __init__(self, name):
        # self.df_today = return_df_today(string)
        # self.df_yesterday = return_df_yesterday(string)
        # self.email = string + '@fordav.com'
        # df1 = self.df_today
        # df2 = self.df_yesterday
        # df1.loc[:, "hash"] = df1.apply(lambda x: hash(tuple(x)), axis=1)
        # df2.loc[:, "hash"] = df2.apply(lambda x: hash(tuple(x)), axis=1)
        # self.difference = df1.loc[~df1["hash"].isin(df2["hash"]), :]
        self.first_name = fn.first_name[name]
        # self.slackName = '@' + string
        # self.phr = workingDFs.BaseDFs.basePhrDf[workingDFs.BaseDFs.basePhrDf['Cntrl_Prgmr'] == name.upper()]
        self.phr = workingDFs.WorkingDFs.phr[workingDFs.WorkingDFs.phr['Cntrl_Prgmr'] == name.upper()]


armbp = Person('armbp')
vannp = Person('vannp')
montj = Person('montj')
trevl = Person('trevl')
ramoe = Person('ramoe')
lanej = Person('lanej')
wriga = Person('wriga')
betca = Person('betca')
bootk = Person('bootk')
navaj = Person('navaj')
presl = Person('presl')



with pd.ExcelWriter(f"Programmer_ERPH_Report_{date_objects.today}.xlsx") as writer:
    armbp.phr.to_excel(writer, sheet_name=f'{armbp.first_name}')
    vannp.phr.to_excel(writer, sheet_name=f'{vannp.first_name}')
    montj.phr.to_excel(writer, sheet_name=f'{montj.first_name}')
    trevl.phr.to_excel(writer, sheet_name=f'{trevl.first_name}')
    ramoe.phr.to_excel(writer, sheet_name=f'{ramoe.first_name}')
    lanej.phr.to_excel(writer, sheet_name=f'{lanej.first_name}')
    wriga.phr.to_excel(writer, sheet_name=f'{wriga.first_name}')
    betca.phr.to_excel(writer, sheet_name=f'{betca.first_name}')
    bootk.phr.to_excel(writer, sheet_name=f'{bootk.first_name}')
    navaj.phr.to_excel(writer, sheet_name=f'{navaj.first_name}')
    presl.phr.to_excel(writer, sheet_name=f'{presl.first_name}')