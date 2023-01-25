#############################################################
## python utils// jingshentai@micron.com  				   ##
## 09/09/21   Added tte_query_ssh function 			       ##
## 11/30/21   Added snapshot function                      ##
## 11/30/21   Added createHtml function                    ##
## 11/30/21   Enhanced sendEmail function                  ##
## 12/06/21   Added to close paramiko ssh client           ##  
## 12/22/21   sql setup                                    ##  
#############################################################

#'''
import paramiko
import subprocess
import csv
from timeit import default_timer as timer

import sys
import os
import datetime

from six.moves import urllib
from sqlalchemy import create_engine

def tte_query_ssh(cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="siltse03", 
                username="jingshentai", 
                password="Mu716617123")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
    stdout_read=ssh_stdout.read()
    x = (stdout_read)
    ssh.close()
    return x

def sql_setup(serverName,databaseName,username,password):
    params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s"%(serverName,databaseName,username,password))
    params_str = "mssql+pyodbc:///?odbc_connect={}".format(params)
    return create_engine(params_str)

def get_dts(): #tte format
  time_end1=  datetime.datetime.now().replace(microsecond=0)- datetime.timedelta(days=1)
  time_end=time_end1.time()
  time_start1= datetime.datetime.now().replace(microsecond=0) - datetime.timedelta(days=8)
  time_start=time_start1.time()
  time_end2=  datetime.datetime.now().replace(microsecond=0)
  
  dd_minus1=time_end1.strftime("%d/%b/%Y")
  session=time_start.strftime("%p")
  start=time_start1.strftime("%d/%b/%Y")
  dd=time_end2.strftime("%d/%b/%Y")
  return dd_minus1,session,start,dd
  
def get_dts_2(): #tte format
  time_end1=  datetime.datetime.now().replace(microsecond=0)- datetime.timedelta(days=1)
  time_end=time_end1.time()
  time_start1= datetime.datetime.now().replace(microsecond=0) - datetime.timedelta(days=7)
  time_start=time_start1.time()
  time_end2=  datetime.datetime.now().replace(microsecond=0)
  
  dd_minus1=time_end1.strftime("%d/%b/%Y")
  session=time_start.strftime("%p")
  start=time_start1.strftime("%d/%b/%Y")
  dd=time_end2.strftime("%d/%b/%Y")
  dd_minus7=time_start1.strftime("%d/%b/%Y")
  return dd_minus7,dd_minus1,dd
  
def get_dts_wtd(): #mamrpt format
  time_end1=  datetime.datetime.now().replace(microsecond=0)- datetime.timedelta(days=1)
  time_end=time_end1.time()
  time_start1= datetime.datetime.now().replace(microsecond=0) - datetime.timedelta(days=7)
  time_start=time_start1.time()
  time_end2=  datetime.datetime.now().replace(microsecond=0)
  
  dd_minus1=time_end.strftime("%m-%d-%Y")
  session=time_start.strftime("%p")
  dd_minus7=time_start1.strftime("%m-%d-%Y")
  dd=time_end2.strftime("%m-%d-%Y") #02-18-2021
  return dd_minus7,dd_minus1,dd

def create_htmlTable_str(main_dict, summary_attr,header_color,email_str):
    email_str += '<table border="1" cellpadding="20" cellspacing="0" width="200px">'
    for each_summary_attr in summary_attr:
        #text_str += '<td style="color:#0000ff">'
        email_str += '<td bgcolor="%s">'%(header_color)
        email_str += each_summary_attr
        email_str += '</td>'
    main_dict_backup = main_dict
    for myKey in main_dict_backup.keys():
        email_str += '<tr>'
        email_str += '<td>%s</td>'%(myKey)
        for attribute in main_dict_backup[myKey].keys():
            email_str += '<td>'
            email_str += main_dict_backup[myKey][attribute]
            email_str += '</td>'
        email_str += '</tr>'
    
    email_str += '</table>'
    email_str += '\n\n'
    #print(text_str)
    return email_str
  
def sendEmail(send_from, send_to, send_cc, Subject, email_text, tableau_url, text_str, email_footer, path, pngFile_name, csvFile_name):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    from email.utils import formatdate
    import smtplib
    import csv
    import datetime

    now = datetime.datetime.now()
    dt = now.strftime(" (%Y-%m-%d at %I:%M %p)")
    #print(dt)
            
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = ', '.join(send_to)
    msg['Cc'] = ', '.join(send_cc)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = Subject + dt
       
    with open(path + pngFile_name,'rb') as f:
      msg.attach(MIMEApplication(f.read(),Name=pngFile_name))
    
    with open(path + csvFile_name,'rb') as csv_file:
      msg.attach(MIMEApplication(csv_file.read(),Name=csvFile_name))
    
    text = """
    <html>
       <head></head>
       <body><pre><font face="Courier New"><br>"""
    
    text += email_text  
    
    if tableau_url != '':
        text += """<br><br>For more details, refer to the <a href = "{}">Tableau Link</a> """.format(tableau_url)
    else:
        print('No Tableau link')
    
    text += """<br><br><br>"""
    text += text_str
    text += """<br><br><br>"""
    text += email_footer
    text += """
       </font></pre>
    
    </html>"""
    
    text = '<font face="Courier">' + text + '</font>'
    part = MIMEText(text,"html", "UTF-8")
    msg.attach(part)

    # Send email
    try:
        server = smtplib.SMTP('mail.micron.com',25)
        server.sendmail(msg['From'], [send_to, send_cc], msg.as_string())
        server.quit()
        print("Successfully sent email")
    
    except Exception:
        print("Error: unable to send email")


def snapshot(URL, dir_name, file_name):
    import os
    from time import sleep
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    
    print('\n\nScreenshot capture in progress ...')
    
    driver = webdriver.Chrome(ChromeDriverManager().install())    
    
    options = webdriver.ChromeOptions()
    
    url = '{}:refresh=yes'.format(URL)
    
    
    driver.get(url)
    
    driver.set_window_size(1550, 1100)
    sleep(150)
    driver.find_element_by_tag_name('body').screenshot(dir_name + file_name)
    print('\nDashboard Snapshot successful')
    driver.close()

def tte_query(command):
    lot_info = subprocess.Popen(command, shell=True, 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE)
    return lot_info.communicate()

def get_normal_dicts(PRR, lot_type):
    mso_attr = {'eds_entry_reason'    : 'N/A',
                'signoff_problem'     : 'N/A',
                'eds_entry_notes'     : 'N/A',
                'process_review_reqd' : PRR}
    prev_summary = {'prev_summary_slash'      : 'N/A',
                    'prev_summary_tool_id' : 'N/A',
                    'prev_summary_mfg_workweek'  : 'N/A',
                    'prev_summary_end' : 'N/A'}
    lot_type = {'lot_type' : lot_type}
    return mso_attr, prev_summary, lot_type

def write_csv_headers(file_out,summary_attr_list):
    writer = csv.writer(file_out)
    writer.writerows([summary_attr_list])
  #summary_attr_list // [attr1, attr2, ... ]
    
def write_csv_values(file_out, summary_attr_list, lot_dict):
  writer = csv.DictWriter(file_out, summary_attr_list)
  for key,val in sorted(lot_dict.items()):
    #print(key,val)
    row = {'slash': key}
    row.update(val)
    writer.writerow(row)
  #lot_dict // {lotA:{attr1:val1, attr2:val2...},
  #             lotB:{attr1:val, attr2:val2...}}
  
def write_csv_values1(file_out, summary_attr_list, lot_dict):
  writer = csv.DictWriter(file_out, summary_attr_list)
  for key,val in sorted(lot_dict.items()):
    print(key,val)
    row = {'lot_id': key}
    row.update(val)
    writer.writerow(row)
    
def write_csv_values2(file_out, summary_attr_list, lot_dict, myKey):
  writer = csv.DictWriter(file_out, summary_attr_list)
  for key,val in sorted(lot_dict.items()):
    print(key,val)
    row = {myKey: key}
    row.update(val)
    writer.writerow(row)
    
def elapsed(cs):
  return timer() - cs
  