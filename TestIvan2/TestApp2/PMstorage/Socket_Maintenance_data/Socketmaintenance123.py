# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 16:17:18 2022

@author: itanb
"""

"""
Created on Tue Oct 18 09:38:37 2022

@author: itanb
"""

import pandas as pd
from utils import sql_setup


serverName = 'SIMSSPROD65\SIMSSPROD65'
databaseName = 'equip_tracking_DSS'
username = 'MFGSYS'
password = 'sim2381'

cmd = """
SELECT   
equip_id,equip_desc,equip_type_id,physical_location,equip_state_id,equip_state_in_datetime,equip_state_out_datetime,event_code_id, event_hist_emp_no,semi_state_id --equip_note.note_text


	FROM [equip_tracking_DSS].[dbo].[event_history]
	
	LEFT JOIN [equip_tracking_DSS].[dbo].[equipment]
	ON	event_history.equip_OID = equipment.equip_OID

	LEFT JOIN [equip_tracking_DSS].[dbo].[equipment_state_for_area]
	ON  event_history.equip_state_OID = equipment_state_for_area.equip_state_OID 
	
	LEFT JOIN event_code_history
	ON event_code_history.production_state_change_OID = event_history.production_state_change_OID

	--LEFT JOIN equipment_tracking.dbo.equip_note
	--ON equip_note.production_state_change_OID = event_history.production_state_change_OID  AND equip_note.created_datetime = event_history.equip_state_in_datetime
    
   WHERE  semi_state_id = 'SCHEDULED_DOWNTIME' AND equip_state_in_datetime >'2022-07-10 07:00:00' AND equip_state_id like 'SITE MAINTENANCE%' 
   
   
    --AND equip_state_id like 'CHANGEOVER%' AND equip_id ='TAW-0033'



	
    --WHERE OR equip_state_id like 'SITE MAINTENANCE%' AND event_hist_emp_no = '1412103' AND equip_id ='TAW-0050'OR equip_state_id like 'SITE MAINTENANCE%'
	
	--WHERE  equip_type_id in  ('SMG2P TESTER') AND equip_state_in_datetime >= '2022-06-24' --AND semi_state_id = 'UNSCHEDULED_DOWNTIME' --AND event_code_id = NULL
	


	-- 'SM3016 TESTER','SM3316 TESTER','SMG2P TESTER','MAGNUM 5 GV TESTER'
	--,'TW320SM HANDLER','TW320HM HANDLER','TW322SM HANDLER','TW322HM HANDLER','TWS7P'
	--ORDER BY equip_state_in_datetime
    --equip_status like 'ACTIVE' AND
    -- equipment.equip_id, equipment.equip_OID,event_history.production_state_change_OID, equip_state_in_datetime,equip_state_out_datetime, equip_state_OID, equip_state_by_system, equip_parent_state_OID


"""

cnxn = sql_setup(serverName,databaseName,username,password)

df3 = pd.read_sql(cmd,cnxn)

df3["equip_state_in_datetime"] = pd.to_datetime(df3["equip_state_in_datetime"]).dt.strftime('%Y/%m/%d %H:%M:%S')
df3["equip_state_out_datetime"] = pd.to_datetime(df3["equip_state_out_datetime"]).dt.strftime('%Y/%m/%d %H:%M:%S')


# df2 = df2.drop(columns='1')
# df2 = df2['Event code (ID)'].fillna(0, inplace=True)
df3.to_excel("C:/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/PMstorage/Socket_Maintenance_data/SocketmaintenanceData.xlsx")

