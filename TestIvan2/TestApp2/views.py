from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
from .models import RegisteredUser
from django.core.exceptions import ObjectDoesNotExist
import pandas as pd
import os
import sys


def app_homepage(request):
    try:
        if usrnme:
            userdetails = {'username': usrnme}
            return render(request, "loggedin.html", userdetails)
    except NameError:
        return render(request, "homepage.html")
    
    
def about_us(request):
    try:
        if usrnme:
            return render(request, "aboutUs.html")
    except NameError:
        return render(request, "aboutUs.html")
   

def services(request):
    try:
        if usrnme:
            return render(request, "services.html")
    except NameError:
        return render(request,"services.html")
    
    
def contact_us(request):
    try:
        if usrnme:
            return render(request, "contactUs.html")
    except NameError:
        return render(request,"contactUs.html")
    
    
def tableau_dashboard(request):
    try:
        if usrnme:
            return render(request, "C:/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/Templates/Productions_KPI/tableau.html")
    except NameError:
        return render(request,"C:/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/Templates/Productions_KPI/tableau.html")
    
    
def tableau(request):
    try:
        if usrnme:
            return render(request, "C:/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/Templates/Productions_KPI/tableau.html")
    except NameError:
        return render(request,"C:/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/Templates/Productions_KPI/tableau.html")
    

def signin(request):
    global usrnme
    if request.method == 'POST':
        usrnme = request.POST['username']
        psswrd = request.POST['pswd']
        
        try:
            user = RegisteredUser.objects.get(name=usrnme)
            if usrnme == user.name and psswrd == user.password:
                return redirect("loggedin")
            else:
                messages.info(request, "Incorrect password")
                return redirect("signin")
        except ObjectDoesNotExist:
            messages.info(request, "The user does not exist")
            return redirect ("signin")
        
    else:
        return render(request, "signin.html")
    
    
def loggedin(request):
    userdetails ={'username': usrnme}
    return render(request,"loggedin.html", userdetails)

def logout(request):
    global usrnme
    del usrnme
    return render(request,"logout.html")
 
    
 
    
# # def Finaltracking(request):
#     df = pd.read_excel (r'C:/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/PMstorage/PM_data/EQrecord.xlsx')
#     df = df.rename(columns = {"equip_id": "Equipment (ID)",
#                          "equip_desc": "Equipment Description", 
#                          "equip_type_id": "Equipment Type (ID)", 
#                          "physical_location": "Physical Location", 
#                          "equip_state_id": "Equipment State (ID)", 
#                          "equip_state_in_datetime": "Equipment State Datetime (IN)",
#                          "equip_state_out_datetime": "Equipment State Datetime (Out)",
#                          "event_code_id": "Event code (ID)",
#                          "event_hist_emp_no": "Event History employee no",
#                          "semi_state_id": "Semi Sate (ID)"})
    
#     # df = df.astype({'Event History employee no': 'int32'}).dtypes
  
#     # df['Event History employee no'] = df['Event History employee no'].astype('int')
#     df = df.head(100)
#     myColumns = ['Equipment (ID)','Equipment Description','Equipment Type (ID)','Physical Location','Equipment State (ID)','Equipment State Datetime (IN)','Equipment State Datetime (Out)','Event code (ID)','Event History employee no','Semi Sate (ID)']
#     df = df.drop(columns=['Unnamed: 0'])
   
    
#     df_html = df.to_html(classes = 'sortable" id = "myTable" contenteditable = "true', index=False)
#     # df['Event History employee no'] = df['Event History employee no'].astype('int')
#     print(len(myColumns))
#     for i in range(len(myColumns)):
#         df_html = df_html.replace('<th>%s'%(myColumns[i]),'<th onclick="sortTable(%s)">%s'%(str(i),myColumns[i]))
       
#     # df = df.astype({'Event History employee no': 'int32'}).dtypes
    
#     mydict = {    
#         "df": df_html
#     }
    
#     # write html to file
#     text_file = open("/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/Templates/Equipment_tracking/Equipment_tracking_page/tracking.html", "w")
#     text_file.write(df_html)
#     text_file.close()
    
#     return render(request, '/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/Templates/Equipment_tracking/Equipment_tracking_page/Finaltracking.html', context=mydict)





def PM(request):
    df = pd.read_excel (r'C:/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/PMstorage/PM_data/pmrecord.xlsx')
    df["equip_state_in_datetime"] = pd.to_datetime(df["equip_state_in_datetime"]).dt.strftime('%Y/%m/%d %H:%M:%S')
    df["equip_state_out_datetime"] = pd.to_datetime(df["equip_state_out_datetime"]).dt.strftime('%Y/%m/%d %H:%M:%S')

    df = df.rename(columns = {"equip_id": "Equipment (ID)",
                         "equip_desc": "Equipment Description", 
                         "equip_type_id": "Equipment Type (ID)", 
                         "physical_location": "Physical Location", 
                         "equip_state_id": "Equipment State (ID)", 
                         "equip_state_in_datetime": "Equipment State Datetime (IN)",
                         "equip_state_out_datetime": "Equipment State Datetime (Out)",
                         "event_code_id": "Event code (ID)",
                         "event_hist_emp_no": "Event History employee no",
                         "semi_state_id": "Semi Sate (ID)"})
    
  
    # df = df.astype({'Event History employee no': 'int32'}).dtypes
  
    # df['Event History employee no'] = df['Event History employee no'].astype('int')
    
    myColumns = ['Equipment (ID)','Equipment Description','Equipment Type (ID)','Physical Location','Equipment State (ID)','Equipment State Datetime (IN)','Equipment State Datetime (Out)','Event code (ID)','Event History employee no','Semi Sate (ID)']
    df = df.drop(columns=['Unnamed: 0'])
    # df = df.head(1000)
   
    
    df_html = df.to_html(classes = 'sortable" id = "myTable" contenteditable = "true', index=False)
    # df['Event History employee no'] = df['Event History employee no'].astype('int')
    print(len(myColumns))
    for i in range(len(myColumns)):
        df_html = df_html.replace('<th>%s'%(myColumns[i]),'<th onclick="sortTable(%s)">%s'%(str(i),myColumns[i]))
       
    # df = df.astype({'Event History employee no': 'int32'}).dtypes
    
    mydict = {    
        "df": df_html
    }
    
    # write html to file
    text_file = open("/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/Templates/Equipment_tracking/Pm_page/PM_tracking.html", "w")
    text_file.write(df_html)
    text_file.close()
    
    return render(request, 'C:/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/Templates/Equipment_tracking/Pm_page/PM.html', context=mydict)



# C:\Users\itanb\test_site2\Scripts\TestIvan2\TestApp2\Templates\Equipment_tracking\Pm_page\PM.html

def Socketmaintenance(request):
    df = pd.read_excel (r'C:/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/PMstorage/Socket_Maintenance_data/SocketmaintenanceData.xlsx')
    df["equip_state_in_datetime"] = pd.to_datetime(df["equip_state_in_datetime"]).dt.strftime('%Y/%m/%d %H:%M:%S')
    df["equip_state_out_datetime"] = pd.to_datetime(df["equip_state_out_datetime"]).dt.strftime('%Y/%m/%d %H:%M:%S')

    df = df.rename(columns = {"equip_id": "Equipment (ID)",
                         "equip_desc": "Equipment Description", 
                         "equip_type_id": "Equipment Type (ID)", 
                         "physical_location": "Physical Location", 
                         "equip_state_id": "Equipment State (ID)", 
                         "equip_state_in_datetime": "Equipment State Datetime (IN)",
                         "equip_state_out_datetime": "Equipment State Datetime (Out)",
                         "event_code_id": "Event code (ID)",
                         "event_hist_emp_no": "Event History employee no",
                         "semi_state_id": "Semi Sate (ID)"})
    
    # df = df.astype({'Event History employee no': 'int32'}).dtypes
  
    # df['Event History employee no'] = df['Event History employee no'].astype('int')
    #df = df.head(100)
    myColumns = ['Equipment (ID)','Equipment Description','Equipment Type (ID)','Physical Location','Equipment State (ID)','Equipment State Datetime (IN)','Equipment State Datetime (Out)','Event code (ID)','Event History employee no','Semi Sate (ID)']
    df = df.drop(columns=['Unnamed: 0'])
    
    # df["equip_state_in_datetime"] = pd.to_datetime(df["equip_state_in_datetime"]).dt.strftime('%Y/%m/%d %H:%M:%S')
    # df["equip_state_out_datetime"] = pd.to_datetime(df["equip_state_out_datetime"]).dt.strftime('%Y/%m/%d %H:%M:%S')

    
    df_html = df.to_html(classes = 'sortable" id = "myTable" contenteditable = "true', index=False)
    # df['Event History employee no'] = df['Event History employee no'].astype('int')
    print(len(myColumns))
    for i in range(len(myColumns)):
        df_html = df_html.replace('<th>%s'%(myColumns[i]),'<th onclick="sortTable(%s)">%s'%(str(i),myColumns[i]))
       
    # df = df.astype({'Event History employee no': 'int32'}).dtypes
    
    mydict = {    
        "df": df_html
    }
    
    # write html to file
    text_file = open("/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/Templates/Equipment_tracking/Socketmaintenance_page/Socketmaintenance_tracking.html", "w")
    text_file.write(df_html)
    text_file.close()
    
    return render(request, '/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/Templates/Equipment_tracking/Socketmaintenance_page/Socketmaintenance.html', context=mydict)







def Changeover(request):
    df = pd.read_excel (r'C:/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/PMstorage/Changeover_data/EQrecord.xlsx')
    df = df.rename(columns = {"equip_id": "Equipment (ID)",
                         "equip_desc": "Equipment Description", 
                         "equip_type_id": "Equipment Type (ID)", 
                         "physical_location": "Physical Location", 
                         "equip_state_id": "Equipment State (ID)", 
                         "equip_state_in_datetime": "Equipment State Datetime (IN)",
                         "equip_state_out_datetime": "Equipment State Datetime (Out)",
                         "event_code_id": "Event code (ID)",
                         "event_hist_emp_no": "Event History employee no",
                         "semi_state_id": "Semi Sate (ID)"})
    
    # df = df.astype({'Event History employee no': 'int32'}).dtypes
  
    # df['Event History employee no'] = df['Event History employee no'].astype('int')
    #df = df.head(100)
    myColumns = ['Equipment (ID)','Equipment Description','Equipment Type (ID)','Physical Location','Equipment State (ID)','Equipment State Datetime (IN)','Equipment State Datetime (Out)','Event code (ID)','Event History employee no','Semi Sate (ID)']
    df = df.drop(columns=['Unnamed: 0'])
   
    
    df_html = df.to_html(classes = 'sortable" id = "myTable" contenteditable = "true', index=False)
    # df['Event History employee no'] = df['Event History employee no'].astype('int')
    print(len(myColumns))
    for i in range(len(myColumns)):
        df_html = df_html.replace('<th>%s'%(myColumns[i]),'<th onclick="sortTable(%s)">%s'%(str(i),myColumns[i]))
       
    # df = df.astype({'Event History employee no': 'int32'}).dtypes
    
    mydict = {    
        "df": df_html
    }
    
    # write html to file
    text_file = open("/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/Templates/Equipment_tracking/Changeover_page/Changeover_tracking.html", "w")
    text_file.write(df_html)
    text_file.close()
    
    return render(request, 'C:/Users/itanb/test_site2/Scripts/TestIvan2/TestApp2/Templates/Equipment_tracking/Changeover_page/Changeover.html', context=mydict)

# Once button is click then df.html

# to overwrite tracking.html

# value updated

# save as df.to.excel

# and insert df.to.sql

# force auto refresh


    
# def Finaltracking(request):
#     try:
#         if usrnme:
#             return render(request,"Finaltracking.html")
#     except NameError:
#         return render(request,"Finaltracking.html")
    
    


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("signin")
    else:
        form = RegisterForm()
        user_info = {'form': form}
        return render(request, "register.html", user_info)