import pandas as pd
import workingDFs
import date_objects

# pd.set_option('display.max_columns', 50 )
# pd.set_option('isplay.max_rows', 10000 )

phr = workingDFs.WorkingDFs.phr
jsr = workingDFs.WorkingDFs.jsr

jsr.Activity = jsr.Activity.str.lower()

result = pd.merge(phr, jsr, on='Job #', how='left')

typos = ['cntrl sys tp submi', 'cntrl sys ui meeti', 'cntrl sys prog cmp']
corrections = ['cntrl sys tp submit', 'cntrl sys ui meeting', 'cntrl sys prog cmplt']

result.replace(typos, corrections, inplace=True)

worktype = result['Work Typ'] == 'Eng-Prog'

checkJobCountonResult = result[result['Work Typ'] == 'Eng-Prog']
checkJobCountonJSR = jsr[jsr['Work Typ'] == 'Eng-Prog']


def GetJobList(df):
    jobList = list(df["Job #"])
    return jobList


resultJobLIst = set(GetJobList(checkJobCountonResult))

jsrJobList = set(GetJobList(checkJobCountonJSR))

checktheseJobsforProgrammingNeedsStatusInAnita = list(jsrJobList - resultJobLIst)

getProgrammingMilestones = result[result['Work Typ'] == 'Eng-Prog']

engProgItemsList = list(set(getProgrammingMilestones['Activity']))


def returnListOfWrongTerms(lst):
    wrongTerms = []
    rightTerms = ['cntrl sys tp submit', 'cntrl sys jim', 'cntrl sys ui meeting', 'cntrl sys prog cmplt']
    for term in lst:
        if term not in rightTerms:
            wrongTerms.append(term)
    return wrongTerms


def returnListOfJobNumbersWithWrongTerms(lst):
    jobNumbersBigList = []
    for term in lst:
        df = result[result['Activity'] == term]
        jobNumbersBigList.extend(list(df['Job #']))
    return jobNumbersBigList


JobsWithWrongTerms = returnListOfJobNumbersWithWrongTerms(returnListOfWrongTerms(engProgItemsList))

EngPRog = result[result['Work Typ'] == 'Eng-Prog']

DF_GuiTeamReport = EngPRog.groupby(['Job #', 'Job Name', 'PE_x', 'PM_x', 'Cmp', 'Activity'])[
    "Stop Dt"].first().unstack()

# todo: add DF_GuiTeam Report to Excel Doc
with pd.ExcelWriter(f"/Volumes/Quick Reference/Reports/Comp_Reports/Weekly_Milestone_Report_{date_objects.today}.xlsx") as writer:
    DF_GuiTeamReport.to_excel(writer, 'Weekly Report')

    writer.save()