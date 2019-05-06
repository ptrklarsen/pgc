from workingDFs import WorkingDFs


class PresentableData(WorkingDFs):
    newJobs = WorkingDFs.phr[WorkingDFs.phr['PM'] == 'TBD']
    needsDSP = WorkingDFs.phr[(WorkingDFs.phr['DSP_Req'] == "Yes") & (WorkingDFs.phr['DSP_Prgmr'] == "TBD") &
                              (WorkingDFs.phr["PE"] != 'TBD')]
    noLEP = WorkingDFs.phr.loc[
        WorkingDFs.phr['LEP Budget'] == 0]  # assign to a dataframe the jobs which have no LEP sold
    overBudget = WorkingDFs.phr[WorkingDFs.phr['LEP Variance'] < 0]
    needsProg = WorkingDFs.phr[WorkingDFs.phr['Cntrl_Prgmr'] == 'TBD']  # needs Prog


