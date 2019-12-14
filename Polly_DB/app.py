"""
    A simple and lightweight databse application to store information of bird sightings
"""
# ================  MODULES ===============
from tkinter import *
import tkinter.ttk as tkk
import sqlite3
import tkinter.messagebox as ttkMsBox
import app_crud

# ================ SETTINGS ================

root = Tk()
root.title("PollyDB v. 1.0.1 (MyBirdsDB)")
color1 = 'gray77'
color2 = 'gray60'
font1 = 'arial', 11
font2 = 'arial', 12
white = 'white'
dgreen = 'olive drab'
sblue = 'LightSkyBlue3'
gold = 'goldenrod3'
red = 'tomato3'
sienna = 'sienna3'
gray = 'dim gray'
root.geometry('890x680')
root.configure(bg=color1)
root.resizable()

# ================ METHODS ================

def get_selected_row(event):
    try:
        global selected_tuple
        index = list_all.curselection()[0]
        selected_tuple = list_all.get(index)
        species_entry.delete(0,END)
        species_entry.insert(END,selected_tuple[1])
        lname_entry.delete(0,END)
        lname_entry.insert(END,selected_tuple[2])
        year_entry.delete(0,END)
        year_entry.insert(END,selected_tuple[3])
        month_entry.delete(0,END)
        month_entry.insert(END,selected_tuple[4])
        day_entry.delete(0,END)
        day_entry.insert(END,selected_tuple[5])
        hour_entry.delete(0,END)
        hour_entry.insert(END,selected_tuple[6])
        number_entry.delete(0,END)
        number_entry.insert(END,selected_tuple[7])
        city_entry.delete(0,END)
        city_entry.insert(END,selected_tuple[8])
        country_entry.delete(0,END)
        country_entry.insert(END,selected_tuple[9])
        habitat_entry.delete(0,END)
        habitat_entry.insert(END,selected_tuple[10])
        xcoord_entry.delete(0,END)
        xcoord_entry.insert(END,selected_tuple[11])
        ycoord_entry.delete(0,END)
        ycoord_entry.insert(END,selected_tuple[12])
        notes_entry.delete(0,END)
        notes_entry.insert(END,selected_tuple[13])
        author_entry.delete(0,END)
        author_entry.insert(END,selected_tuple[14])
    except IndexError:
        pass

def view_command():
    list_all.delete(0,END)
    for row in app_crud.view():
        list_all.insert(END,row)

def clear_command():
    species_entry.delete(0,END)
    lname_entry.delete(0,END)
    year_entry.delete(0,END)
    month_entry.delete(0,END)
    day_entry.delete(0,END)
    hour_entry.delete(0,END)
    number_entry.delete(0,END)
    city_entry.delete(0,END)
    country_entry.delete(0,END)
    habitat_entry.delete(0,END)
    xcoord_entry.delete(0,END)
    ycoord_entry.delete(0,END)
    notes_entry.delete(0,END)
    author_entry.delete(0,END)
    status.config(text="Polly wants a cracker", fg="orange")

def search_command():
    list_all.delete(0,END)
    rows  = app_crud.search(species_txt.get(),lname_txt.get(),year_txt.get(),month_txt.get(),day_txt.get(),hour_txt.get(),number_txt.get(),city_txt.get(),country_txt.get(),habitat_txt.get(),xcoordinates_txt.get(),ycoordinates_txt.get(),notes_txt.get(),author_txt.get())
    if rows == []:
        status.config(text="Entry NOT found!", fg="red")
    else:
        for row in rows:
            list_all.insert(END,row)
            status.config(text="Entry found!", fg="green")

def add_command():
    app_crud.insert(species_txt.get(),lname_txt.get(),year_txt.get(),month_txt.get(),day_txt.get(),hour_txt.get(),number_txt.get(),city_txt.get(),country_txt.get(),habitat_txt.get(),xcoordinates_txt.get(),ycoordinates_txt.get(),notes_txt.get(),author_txt.get())
    list_all.delete(0,END)
    list_all.insert(END,(species_txt.get(),lname_txt.get(),year_txt.get(),month_txt.get(),day_txt.get(),hour_txt.get(),number_txt.get(),city_txt.get(),country_txt.get(),habitat_txt.get(),xcoordinates_txt.get(),ycoordinates_txt.get(),notes_txt.get(),author_txt.get()))
    status.config(text="Data created!", fg="green")
    view_command()

def delete_command():
    app_crud.delete(selected_tuple[0])
    status.config(text="This bird is no more!", fg="red")
    view_command()

def update_command():
    app_crud.update(selected_tuple[0],species_txt.get(),lname_txt.get(),year_txt.get(),month_txt.get(),day_txt.get(),hour_txt.get(),number_txt.get(),city_txt.get(),country_txt.get(),habitat_txt.get(),xcoordinates_txt.get(),ycoordinates_txt.get(),notes_txt.get(),author_txt.get())
    status.config(text="Data updated", fg="green")
    view_command()

def about():
    status.config(text="I am an Norwegian Blue Parrot", fg="blue")
    ttkMsBox.showinfo('About','''   Created by @kostyrko (GitHub)
                        \n(use under under the GPLv3 license)''')

def exit():
    result = ttkMsBox.askquestion('PollyDB', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


# ================ VARIABLES ================
species_txt = StringVar()
lname_txt = StringVar()
year_txt = StringVar()
month_txt = StringVar()
day_txt = StringVar()
hour_txt = StringVar()
number_txt = StringVar()
city_txt = StringVar()
country_txt = StringVar()
habitat_txt = StringVar()
xcoordinates_txt = StringVar()
ycoordinates_txt = StringVar()
notes_txt = StringVar()
author_txt = StringVar()


# ================ FRAMES ================

Left = Frame(root, width=400, height=300,)
Left.pack(side=LEFT, fill=BOTH)

Right = Frame(root, bd=4, relief=RAISED)
Right.pack(fill=BOTH,expand=True,side=LEFT)

Forms1 = Frame(Left, width=200, height=550)
Forms1.pack(side=TOP)

Forms2 = Frame(Left, width=200, height=550)
Forms2.pack(side=TOP)

Forms2_1 = Frame(Left, width=200, height=550)
Forms2_1.pack(side=TOP)

Forms3 = Frame(Left, width=200, height=550)
Forms3.pack(side=TOP)

Stat_bar = Frame(Left,width=200, height=10, bd=1, relief=SUNKEN)
Stat_bar.pack(side=BOTTOM)

Buttons2 = Frame(Left, width=200, height=100, bd=1, relief=RAISED)
Buttons2.pack(side=BOTTOM)

Buttons1 = Frame(Left, width=200, height=100, bd=1, relief=RAISED)
Buttons1.pack(side=BOTTOM)

Buttons = Frame(Left, width=200, height=100, bd=1, relief=RAISED)
Buttons.pack(side=BOTTOM)

# ================ LABELS & ENTRIES ================

species_lbl = Label(Forms1, text="Bird species:", font=font1, bd=15)
species_lbl.grid(row=0)
species_entry = Entry(Forms1, textvariable=species_txt,font=font2,width=18)
species_entry.grid(row=0,ipady=2,column=2)

lname_lbl = Label(Forms1, text="Latin name:", font=font1, bd=15)
lname_lbl.grid(row=1)
lname_entry = Entry(Forms1, textvariable=lname_txt,font=font2,width=18)
lname_entry.grid(row=1,ipady=2,column=2)

year_lbl = Label(Forms2,text="Year:",font=font1)
year_lbl.pack(side=LEFT,padx=5,pady=5)
year_entry = Entry(Forms2,textvariable=year_txt,font=font1,width=5,bd=2)
year_entry.pack(side=LEFT,ipady=2,padx=5,pady=5)

month_lbl = Label(Forms2,text="Month:",font=font1)
month_lbl.pack(side=LEFT,padx=5,pady=5)
month_entry = Entry(Forms2,textvariable=month_txt,font=font1,width=3,bd=2)
month_entry.pack(side=LEFT,ipady=2,padx=5,pady=5)

day_lbl = Label(Forms2,text="Day:",font=font1)
day_lbl.pack(side=LEFT,padx=5,pady=5)
day_entry = Entry(Forms2,textvariable=day_txt,font=font1,width=3,bd=2)
day_entry.pack(side=LEFT,ipady=2,padx=5,pady=5)

hour_lbl = Label(Forms2_1,text="Hour:",font=font1)
hour_lbl.pack(side=LEFT,padx=5,pady=5)
hour_entry = Entry(Forms2_1,textvariable=hour_txt,font=font1,width=5,bd=2)
hour_entry.pack(side=LEFT,ipady=2,padx=5,pady=5)

number_lbl = Label(Forms2_1,text="Number:",font=font1)
number_lbl.pack(side=LEFT,padx=5,pady=5)
number_entry = Entry(Forms2_1,textvariable=number_txt,font=font1,width=3,bd=2)
number_entry.pack(side=LEFT,ipady=2,padx=5,pady=5)

city_lbl = Label(Forms3, text="City:", font=font1, bd=15)
city_lbl.grid(row=1)
city_entry = Entry(Forms3, textvariable=city_txt,font=font2,width=18)
city_entry.grid(row=1,ipady=2,column=2)

country_lbl = Label(Forms3, text="Country:", font=font1, bd=15)
country_lbl.grid(row=2)
country_entry = Entry(Forms3, textvariable=country_txt,font=font2,width=18)
country_entry.grid(row=2,ipady=2,column=2)

habitat_lbl = Label(Forms3, text="Habitat:", font=font1, bd=15)
habitat_lbl.grid(row=3)
habitat_entry = Entry(Forms3, textvariable=habitat_txt,font=font2,width=18)
habitat_entry.grid(row=3,ipady=2,column=2)

xcoord_lbl = Label(Forms3, text="X Coordinates:", font=font1, bd=15)
xcoord_lbl.grid(row=4)
xcoord_entry = Entry(Forms3, textvariable=xcoordinates_txt,font=font2,width=18)
xcoord_entry.grid(row=4,ipady=2,column=2)

ycoord_lbl = Label(Forms3, text="Y Coordinates:", font=font1, bd=15)
ycoord_lbl.grid(row=5)
ycoord_entry = Entry(Forms3, textvariable=ycoordinates_txt,font=font2,width=18)
ycoord_entry.grid(row=5,ipady=2,column=2)

notes_lbl = Label(Forms3, text="Notes:", font=font1, bd=15)
notes_lbl.grid(row=6)
notes_entry = Entry(Forms3, textvariable=notes_txt,font=font2,width=18)
notes_entry.grid(row=6,ipady=2,column=2)

author_lbl = Label(Forms3, text="Author:", font=font1, bd=15)
author_lbl.grid(row=7)
author_entry = Entry(Forms3, textvariable=author_txt,font=font2,width=18)
author_entry.grid(row=7,ipady=2,column=2)

# ================ BUTTONS ================
create_btn = Button(Buttons, width=15, text="View All", bg=white, command=view_command)
create_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)

create_btn = Button(Buttons, width=15, text="Clear Entries", bg=white, command=clear_command)
create_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)

create_btn = Button(Buttons1, width=10, text="Add Data", bg=dgreen, command=add_command)
create_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)

read_btn = Button(Buttons1, width=10, text="Search Entry",bg=sblue, command=search_command)
read_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)

update_btn = Button(Buttons1, width=10, text="Update", bg= gold, command=update_command)
update_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)

delete_btn = Button(Buttons2, width=10, text="Delete",fg=white, bg=red, command=delete_command)
delete_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)

exit_btn = Button(Buttons2, width=10, text="About",fg=white, bg=gray, command=about)
exit_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)

about_btn = Button(Buttons2, width=10, text="Exit",fg=white, bg=gray, command=exit)
about_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)

# ================= STATUS BAR ===============

status = Label(Stat_bar)
status.pack(ipady=2,padx=5,pady=5)

# ================ DATABASE VIEW -> Listbox ================
scr_bar1 = Scrollbar(Right)
scr_bar1.pack(side=RIGHT,fill=Y)
scr_bar2 = Scrollbar(Right,orient=HORIZONTAL)
scr_bar2.pack(side=BOTTOM,fill=X)
list_all=Listbox(Right, font=font1,yscrollcommand=scr_bar1.set,xscrollcommand=scr_bar2.set)
list_all.pack(fill=BOTH,expand=True)
scr_bar1.config(command=list_all.yview)
scr_bar2.config(command=list_all.xview )
list_all.bind('<<ListboxSelect>>', get_selected_row)

# integration co be continued >>>
# scrollbary = Scrollbar(Right, orient=VERTICAL)
# scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
# tree = tkk.Treeview(Right, columns=("Species", "Latin", 
#                                     "Count", "Year", "Month",
#                                     "Day","Hour", "City", "Country","Habitat",
#                                     "X Coord", "Y Coord", "Notes",
#                                     "Author"), selectmode="extended",
#                                     height=500, yscrollcommand=scrollbary.set,
#                                     xscrollcommand=scrollbarx.set)
# scrollbary.config(command=tree.yview)
# scrollbary.pack(side=RIGHT, fill=Y)
# scrollbarx.config(command=tree.xview)
# scrollbarx.pack(side=BOTTOM, fill=X)
# tree.heading('Species', text="Species", anchor=CENTER)
# tree.heading('Latin', text="Latin", anchor=CENTER)
# tree.heading('Count', text="Count", anchor=CENTER)
# tree.heading('Year', text="Year", anchor=CENTER)
# tree.heading('Month', text="Month", anchor=CENTER)
# tree.heading('Day', text="Day", anchor=CENTER)
# tree.heading('Hour', text="Hour", anchor=CENTER)
# tree.heading('City', text="City", anchor=CENTER)
# tree.heading('Country', text="Country", anchor=CENTER)
# tree.heading('Habitat', text="Habitat", anchor=CENTER)
# tree.heading('X Coord', text="X Coord", anchor=CENTER)
# tree.heading('Y Coord', text="Y Coord", anchor=CENTER)
# tree.heading('Notes', text="Notes", anchor=CENTER)
# tree.heading('Author', text="Author", anchor=CENTER)
# tree.column('#0', stretch=NO, minwidth=0, width=0)
# tree.column('#1', stretch=NO, minwidth=0, width=120)
# tree.column('#2', stretch=NO, minwidth=0, width=120)
# tree.column('#3', stretch=NO, minwidth=0, width=80)
# tree.column('#4', stretch=NO, minwidth=0, width=80)
# tree.column('#5', stretch=NO, minwidth=0, width=80)
# tree.column('#6', stretch=NO, minwidth=0, width=80)
# tree.column('#7', stretch=NO, minwidth=0, width=80)
# tree.column('#8', stretch=NO, minwidth=0, width=80)
# tree.column('#9', stretch=NO, minwidth=0, width=80)
# tree.column('#10', stretch=NO, minwidth=0, width=120)
# tree.column('#11', stretch=NO, minwidth=0, width=80)
# tree.column('#12', stretch=NO, minwidth=0, width=80)
# tree.column('#13', stretch=NO, minwidth=0, width=120)
# tree.column('#14', stretch=NO, minwidth=0, width=120)
# tree.pack()


# ================ RESULT ================
view_command()
status.config(text="Connection with database established", fg="green")
if __name__ == '__main__':
    root.mainloop()