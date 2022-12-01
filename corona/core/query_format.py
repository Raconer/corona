# Auth Query
# Create
auth_in = "INSERT INTO `auth`(`pid`, `regDate`) \
            VALUE ({pid}, '{regDate}')"

# Read
auth_get = "SELECT `idx`, `pid`, `regDate` \
            FROM `auth` order by `idx` desc limit 1"

# Delete
auth_del = "DELETE FROM `auth`"

# Local Query
# C
local_in = "INSERT INTO `local`( `deathCnt`, `gubunCn`, `gubunEn`, `isolClearCnt`, `isolIngCnt`, `qurRate`, `updateDt`, `gubun`, `incDec`, `localOccCnt`, `seq`, `createDt`, `defCnt`, `overFlowCnt`, `stdDay`) VALUES {values}"
# R
local_get = "SELECT `idx`,`deathCnt`,`gubunCn`,`gubunEn`,`isolClearCnt`,`isolIngCnt`,`qurRate`,`updateDt`,`gubun`,`incDec`,`localOccCnt`,`seq`,`createDt`,`defCnt`,`overFlowCnt`,`stdDay` FROM `local` WHERE `createDt` >= '{strDt}'  AND `createDt` < '{endDt}' AND `gubun` = '{gubun}' GROUP BY `stdDay`,  `gubun` ORDER BY `seq` DESC LIMIT 1"
local_get_list = "SELECT `idx`,`deathCnt`,`gubunCn`,`gubunEn`,`isolClearCnt`,`isolIngCnt`,`qurRate`,`updateDt`,`gubun`,`incDec`,`localOccCnt`,`seq`,`createDt`,`defCnt`,`overFlowCnt`,`stdDay` FROM `local` WHERE `createDt` >= '{strDt}'  AND `createDt` < '{endDt}' {where} GROUP BY `stdDay`,  `gubun` ORDER BY  `seq` ASC "
local_get_list_all = "SELECT `idx`,`deathCnt`,`gubunCn`,`gubunEn`,`isolClearCnt`,`isolIngCnt`,`qurRate`,`updateDt`,`gubun`,`incDec`,`localOccCnt`,`seq`,`createDt`,`defCnt`,`overFlowCnt`,`stdDay` FROM `local` WHERE `createDt` >= '{strDt}'  AND `createDt` < '{endDt}'  AND `gubun` = '{gubun}' GROUP BY `stdDay`,  `gubun` ORDER BY  `seq`  DESC "
local_get_rank = "SELECT `idx`, `deathCnt`,`gubunCn`,`gubunEn`,`isolClearCnt`,`isolIngCnt`,`qurRate`,`updateDt`,`gubun`,`incDec`,`localOccCnt`,`seq`,`createDt`,`defCnt`,`overFlowCnt`,`stdDay` FROM `local` WHERE `createDt` >= '{strDt}'  AND `createDt` < '{endDt}' AND `gubun` != '합계' GROUP BY `stdDay`,  `gubun` ORDER BY `defCnt` DESC"
local_data_cnt = "SELECT count(*) AS cnt FROM `local` WHERE `seq`= {seq}"

local_get_recently_date = "SELECT max(`createDt`) AS `createDt` FROM `local` LiMIT 1"
# U
local_update = "`deathCnt` = {deathCnt},`isolClearCnt` = {isolClearCnt},`isolIngCnt` = {isolIngCnt},`qurRate` = '{qurRate}',`updateDt` = '{updateDt}',`incDec` = {incDec},`localOccCnt` = {localOccCnt},`defCnt` = {defCnt},`overFlowCnt` = {overFlowCnt},`stdDay` = '{stdDay}'"
# D
local_delete = "DELETE FROM `local`"

# WHERE

# Corona Data
# Update Default
crn_update = "UPDATE `{table}` SET {change} WHERE {where}"
# Value
crn_local_value = "({deathCnt}, '{gubunCn}', '{gubunEn}', {isolClearCnt}, {isolIngCnt}, '{qurRate}', '{updateDt}', '{gubun}', {incDec}, {localOccCnt}, {seq}, '{createDt}', {defCnt}, {overFlowCnt}, '{stdDay}'),"
crn_nation_value = "( {deathCnt}, '{gubunCn}', '{gubunEn}', {isolClearCnt}, {isolIngCnt}, '{qurRate}', '{updateDt}', '{gubun}', {incDec}, {localOccCnt}, {seq}, '{createDt}',{defCnt}, {overFlowCnt}, '{stdDay}', {lazaDeathCnt}, '{lazaGubunCn}', '{lazaGubunEn}', {lazaIsolClearCnt}, {lazaIsolIngCnt}, '{lazaQurRate}', '{lazaUpdateDt}', '{lazaGubun}', {lazaIncDec}, {lazaLocalOccCnt}, '{lazaSeq}', {lazaDefCnt}, {lazaOverFlowCnt}, '{lazaStdDay}' )"
