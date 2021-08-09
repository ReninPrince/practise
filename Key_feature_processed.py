

import os
import pandas as pd
from datetime import datetime
import time

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

###################################################################################

def long_way(server_name,data_raw):
    temp_df = data_raw[data_raw['Server'] == server_name]
    unique_features = temp_df['Feature'].unique()
    result_df = pd.DataFrame()
    for feature in unique_features:
        max_row = temp_df[temp_df[temp_df.Server == server_name].Feature == feature].max()
        try:
            Usage_calc = str(int((max_row.Max/max_row.Total)*100))+'%'
        except:
            Usage_calc = None
        entry = {
                'Date':max_row.Time,
                'Server':max_row.Server,
                'Feature':max_row.Feature,
                'Quantity':max_row.Total,
                'Used':max_row.Max,
                'Usage':Usage_calc
            }
        entry_df = pd.DataFrame.from_dict([entry])
        result_df = result_df.append(entry_df)
    result_df = result_df.reset_index()
    result_df = result_df.drop(columns=['index'])
    return result_df

def get_time(col):
    try:
        time_row = str(col.time().strftime("%H%M"))
        return time_row.rjust(3, "0")
    except:
        return None

def heart(file,op_path):
    if file.split('.')[1] == 'csv':
        data_raw = pd.read_csv(str(file))
    else:
        data_raw = pd.read_excel(str(file))

    data_raw['Time']= pd.to_datetime(data_raw['Time'])
    
    raw_servers = data_raw['Server'].unique()

    final_sample = pd.DataFrame()
    for server in raw_servers:
        df = long_way(server,data_raw)
        final_sample = final_sample.append(df)

    final_sample.reset_index().drop(columns=['index'])

    final_sample['Time'] = final_sample['Date'].apply(get_time)

    final_sample.to_csv(op_path)
    
    return 'File Created'

########################################################################################

browser_file = None
browser_path = None

def loginemp():
    root3 = Tk()
    root3.overrideredirect(True)
    root3.geometry("{0}x{1}+0+0".format(root3.winfo_screenwidth(), root3.winfo_screenheight()))
    root3.title("Key Feature Processor")
    #-------------------------------------------------------------------------------------------------------------------------------------------
    Titlecard = Frame(root3, width = 1280, height = 100, bd = 7, bg = 'dodgerblue', relief = GROOVE)
    Titlecard.pack(side = 'top', anchor = CENTER, fill = X)
    rt = time.strftime("%d/%m/%y")
    body  = Frame(root3, width = 1280, height = 600, bd = 9, bg = 'dodgerblue3', relief = FLAT)
    body.pack(side = 'top',expand = 1 ,fill = BOTH)
    login = Frame(body, width = 600, height = 400, bd = 7, bg = 'Steelblue2', relief = RAISED)
    login.pack(side = TOP, anchor = CENTER ,expand = 1, fill = BOTH, ipady = 20,ipadx = 10)
    loginbtns = Frame(body, width = 700, height = 30, bd = 7, bg = 'Steelblue2', relief = RAISED)
    loginbtns.pack(side = BOTTOM,anchor = CENTER, fill = X)
    #-------------------------------------------------------------------------------------------------------------------------------------------
    op_file_path = StringVar()
    #-------------------------------------------------------------------------------------------------------------------------------------------
    def exiit():
         qexit = messagebox.askyesno("CGPA","DO YOU WISH TO EXIT")
         if qexit > 0:
              root3.destroy()

    def browser():
        global browser_file,browser_path
        browser_file = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))

        browser_path = os.path.normpath(browser_file)

    def okay():
        global browser_file,browser_path

        Output_path =  os.path.dirname(browser_file)

        Output_name = op_file_path.get() + '.csv'

        final_op_path = os.path.abspath(Output_path+'/'+Output_name)

        heart(browser_path,final_op_path)
       
        root3.destroy()
        
    #-------------------------------------------------------------------------------------------------------------------------------------------
    date1 = Label(Titlecard, text = "DATE:" + rt,relief = GROOVE, width = 17, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    date1.pack(side = RIGHT, anchor = NW, pady = 15)

    Title = Label(Titlecard, text = "Key Feature Processor", relief = GROOVE, width = 20 , bd = 7, bg = 'dodgerblue4',
                  fg = 'lightSkyblue2', font = ('arial', 20, 'italic'))
    Title.pack(side = LEFT,pady = 15, ipadx = 35, padx =45)

    Label(login, text = "Predicted values :", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
                       fg = 'Steelblue2', font = ('arial', 20, 'italic')).grid(row = 0, column = 1)

    Label(login, text = "Enter Path :\n", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'Steelblue2', font = ('arial', 30, 'italic')).grid(row = 1, column = 2)

    Label(login, text = "Enter Path :\n", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'Steelblue2', font = ('arial', 30, 'italic')).grid(row = 1, column = 4)
 

    #heading

    Label(login, text = "Select File :\n", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 30, 'italic')).grid(row = 2, column = 2)
    

    btn1 = Button(login, text = "Browse" ,command = browser,  relief = RAISED, width = 20 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).grid(row=2,column=4)

    Label(login, text = "Enter Output\n filename :\n", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 30, 'italic')).grid(row = 3, column = 2)
    

    Entry(login,relief=SUNKEN,font = ('arial', 25, 'italic'), textvariable = op_file_path,
               bd = 9, insertwidth = 5).grid(row=3,column=4)
    


    btn2 = Button(loginbtns, text = "NEXT" ,command = okay,  relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X,ipady = 6)
    
    btn3 = Button(loginbtns, text = "EXIT" ,command = exiit, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X,ipady = 6)


   #-------------------------------------------------------------------------------------------------------------------------------------------
    root3.mainloop()

loginemp()

































































