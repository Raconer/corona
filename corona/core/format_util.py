from corona.core import query_format
from corona.core import date_util
import datetime


def convert_local_items(items):
    values = ""
    if not (len(items) > 0):
        return values

    for item in items:
        stdDay = datetime.datetime.strptime(item["stdDay"], "%Y년 %m월 %d일 %H시")
        updateDt = date_util.get_kst()
        
        values += query_format.crn_local_value.format( 
                                deathCnt = item["deathCnt"],
                                gubunCn = item["gubunCn"],
                                gubunEn = item["gubunEn"],
                                isolClearCnt = item["isolClearCnt"],
                                isolIngCnt = item["isolIngCnt"],
                                qurRate = item["qurRate"],
                                updateDt = updateDt,
                                gubun = item["gubun"],
                                incDec = item["incDec"],
                                localOccCnt = item["localOccCnt"],
                                seq = item["seq"],
                                createDt = item["createDt"],
                                defCnt = item["defCnt"],
                                overFlowCnt = item["overFlowCnt"],
                                stdDay = stdDay)

    return values.rstrip(",")

def set_local_update(item, updateDt):
    stdDay = datetime.datetime.strptime(item["stdDay"], "%Y년 %m월 %d일 %H시")
    values = query_format.local_update.format(
        deathCnt = item["deathCnt"],
        isolClearCnt  = item["isolClearCnt"],
        isolIngCnt = item["isolIngCnt"],
        qurRate = item["qurRate"],
        updateDt = updateDt,
        incDec = item["incDec"],
        localOccCnt = item["localOccCnt"],
        defCnt = item["defCnt"],
        overFlowCnt = item["overFlowCnt"],
        stdDay = stdDay
    )

    return values

# Nation
def convert_nation_items(totalData, lazaData):
    updateDt = date_util.get_kst()
    values = query_format.crn_nation_value.format(
            deathCnt = totalData["deathCnt"],
            gubunCn= totalData["gubunCn"],
            gubunEn= totalData["gubunEn"],
            isolClearCnt= totalData["isolClearCnt"],
            isolIngCnt= totalData["isolIngCnt"],
            qurRate= totalData["qurRate"],
            updateDt= updateDt,
            gubun= totalData["gubun"],
            incDec = totalData["incDec"],
            localOccCnt= totalData["localOccCnt"],
            seq= totalData["seq"],
            createDt= totalData["createDt"],
            defCnt= totalData["defCnt"],
            overFlowCnt= totalData["overFlowCnt"],
            stdDay= datetime.datetime.strptime(totalData["stdDay"], "%Y년 %m월 %d일 %H시"),
            lazaDeathCnt= lazaData["deathCnt"],
            lazaGubunCn= lazaData["gubunCn"],
            lazaGubunEn= lazaData["gubunEn"],
            lazaIsolClearCnt= lazaData["isolClearCnt"],
            lazaIsolIngCnt= lazaData["isolIngCnt"],
            lazaQurRate= lazaData["qurRate"],
            lazaUpdateDt= updateDt,
            lazaGubun= lazaData["gubun"],
            lazaIncDec= lazaData["incDec"],
            lazaLocalOccCnt= lazaData["localOccCnt"],
            lazaSeq= lazaData["seq"],
            lazaDefCnt= lazaData["defCnt"],
            lazaOverFlowCnt= lazaData["overFlowCnt"],
            lazaStdDay= datetime.datetime.strptime(lazaData["stdDay"], "%Y년 %m월 %d일 %H시")
    )
    return values

def set_nation_update(totalData, lazaData):
    updateDt = date_util.get_kst()
    values = query_format.nation_update_change.format(
        deathCnt = totalData["deathCnt"],
        isolClearCnt= totalData["isolClearCnt"],
        isolIngCnt= totalData["isolIngCnt"],
        qurRate= totalData["qurRate"],
        updateDt= updateDt,
        incDec = totalData["incDec"],
        localOccCnt= totalData["localOccCnt"],
        seq= totalData["seq"],
        createDt= totalData["createDt"],
        defCnt= totalData["defCnt"],
        overFlowCnt= totalData["overFlowCnt"],
        stdDay= datetime.datetime.strptime(totalData["stdDay"], "%Y년 %m월 %d일 %H시"),
        lazaDeathCnt= lazaData["deathCnt"],
        lazaIsolClearCnt= lazaData["isolClearCnt"],
        lazaIsolIngCnt= lazaData["isolIngCnt"],
        lazaQurRate= lazaData["qurRate"],
        lazaUpdateDt= updateDt,
        lazaIncDec= lazaData["incDec"],
        lazaLocalOccCnt= lazaData["localOccCnt"],
        lazaSeq= lazaData["seq"],
        lazaDefCnt= lazaData["defCnt"],
        lazaOverFlowCnt= lazaData["overFlowCnt"],
        lazaStdDay= datetime.datetime.strptime(lazaData["stdDay"], "%Y년 %m월 %d일 %H시")
    )
    return values
