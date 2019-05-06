import pandas as pd
from presentableData import PresentableData
import date_objects
import programmerClasses as pc
import Danger_List as dl


class MakeExcel(PresentableData):

    @staticmethod
    def write_to_doc():
        with pd.ExcelWriter(f"/Volumes/Quick Reference/Reports/Comp_Reports/Report_{date_objects.today}.xlsx") as writer:
            dl.generate_danger_list(dl.jsr(), dl.phr()).to_excel(writer, 'Near Horizon List')
            dl.jsr().to_excel(writer, 'Schedule')
            PresentableData.noLEP.to_excel(writer, 'No LEP was budgeted')
            PresentableData.needsDSP.to_excel(writer, 'Jobs need DSP prog assigned')
            PresentableData.needsProg.to_excel(writer, 'Jobs need a prog assigned')
            PresentableData.newJobs.to_excel(writer, 'New Jobs-No PM Yet')
            PresentableData.overBudget.to_excel(writer, 'Over Budget')
            pc.armbp.phr.to_excel(writer, sheet_name=f'{pc.armbp.first_name}')
            pc.vannp.phr.to_excel(writer, sheet_name=f'{pc.vannp.first_name}')
            pc.montj.phr.to_excel(writer, sheet_name=f'{pc.montj.first_name}')
            pc.trevl.phr.to_excel(writer, sheet_name=f'{pc.trevl.first_name}')
            pc.ramoe.phr.to_excel(writer, sheet_name=f'{pc.ramoe.first_name}')
            pc.lanej.phr.to_excel(writer, sheet_name=f'{pc.lanej.first_name}')
            pc.wriga.phr.to_excel(writer, sheet_name=f'{pc.wriga.first_name}')
            pc.betca.phr.to_excel(writer, sheet_name=f'{pc.betca.first_name}')
            pc.bootk.phr.to_excel(writer, sheet_name=f'{pc.bootk.first_name}')
            pc.navaj.phr.to_excel(writer, sheet_name=f'{pc.navaj.first_name}')
            pc.presl.phr.to_excel(writer, sheet_name=f'{pc.presl.first_name}')

            writer.save()
