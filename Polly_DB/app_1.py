"""
    A simple and lightweight databse application to store information of bird sightings
"""
# ================  MODULES ===============
from tkinter import *
import tkinter.ttk as tkk
import tkinter.messagebox as tkMsBox
# from pollyDB import Database,Create,Read,Exit

# ================ SETTINGS ================

root = Tk()
root.title("Polly-DB v. 0.9 (MyBirdsDB_light)")
color1 = 'gray77'
color2 = 'gray60'
font1 = 'arial', 11
font2 = 'arial', 12
white = 'white'
dgreen = 'DarkSeaGreen3'
sblue = 'LightSkyBlue3'
gold = 'goldenrod3'
red = 'red3'
sienna = 'sienna3'
gray = 'dim gray'
root.geometry('950x650')
root.configure(bg=color1)
root.resizable()

# ================ VARIABLES ================

common_name = StringVar()
latin_name = StringVar()
number = IntVar()
year = IntVar()
month = IntVar()
day = IntVar()
hour = IntVar()
city = StringVar()
country = StringVar()
habitat = StringVar()
xcoordinates = IntVar()
ycoordinates = IntVar()
notes = StringVar()
author = StringVar()
status = StringVar()

# ================ FRAMES ================

Left = Frame(root, width=400, height=300,)
Left.pack(side=LEFT, fill=BOTH)
Right = Frame(root, width=1200, height=800, bd=8, relief=RAISED)
Right.pack(side=LEFT)
Forms1 = Frame(Left, width=200, height=550)
Forms1.pack(side=TOP)
Forms2 = Frame(Left, width=200, height=550)
Forms2.pack(side=TOP)
Forms3 = Frame(Left, width=200, height=550)
Forms3.pack(side=TOP)
Stat_bar = Frame(Left,width=200, height=10, bd=1, relief=SUNKEN)
Stat_bar.pack(side=BOTTOM)
Buttons2 = Frame(Left, width=200, height=100, bd=1, relief=RAISED)
Buttons2.pack(side=BOTTOM)
Buttons = Frame(Left, width=200, height=100, bd=1, relief=RAISED)
Buttons.pack(side=BOTTOM)

# ================ LABELS & ENTRIES ================

species_lbl = Label(Forms1, text="Bird species:", font=font1, bd=15)
species_lbl.grid(row=0)
species_entry = Entry(Forms1, textvariable=common_name,font=font2,width=20)
species_entry.grid(row=0,ipady=2,column=2)

latin_lbl = Label(Forms1, text="Latin name:", font=font1, bd=15)
latin_lbl.grid(row=1)
latin_entry = Entry(Forms1, textvariable=latin_name,font=font2,width=20)
latin_entry.grid(row=1,ipady=2,column=2)

number_lbl = Label(Forms1, text="Number/Count:", font=font1, bd=15)
number_lbl.grid(row=2)
number_entry = Entry(Forms1, textvariable=number,font=font2,width=20)
number_entry.grid(row=2,ipady=2,column=2)

year_lbl = Label(Forms2,text="Year:",font=font1)
year_lbl.pack(side=LEFT,padx=5,pady=5)
year_entry = Entry(Forms2,font=font1,width=5,bd=2,textvariable=year)
year_entry.pack(side=LEFT,ipady=2,padx=5,pady=5)

month_lbl = Label(Forms2,text="Month:",font=font1)
month_lbl.pack(side=LEFT,padx=5,pady=5)
month_entry = Entry(Forms2,font=font1,width=3,bd=2,textvariable=month)
month_entry.pack(side=LEFT,ipady=2,padx=5,pady=5)

day_lbl = Label(Forms2,text="Day:",font=font1)
day_lbl.pack(side=LEFT,padx=5,pady=5)
day_entry = Entry(Forms2,font=font1,width=3,bd=2,textvariable=day)
day_entry.pack(side=LEFT,ipady=2,padx=5,pady=5)

hour_lbl = Label(Forms3, text="Hour:",font=font1)
hour_lbl.grid(row=0)
hour_entry = Entry(Forms3,font=font1,width=3,bd=2,textvariable=hour)
hour_entry.grid(row=0,ipady=2,pady=5,column=2)

city_lbl = Label(Forms3, text="City:", font=font1, bd=15)
city_lbl.grid(row=1)
city_entry = Entry(Forms3, textvariable=city,font=font1,width=19)
city_entry.grid(row=1,ipady=2,column=2)

country_lbl = Label(Forms3, text="Country:", font=font1, bd=15)
country_lbl.grid(row=2)
country_entry = Entry(Forms3, textvariable=country,font=font2,width=20)
country_entry.grid(row=2,ipady=2,column=2)

habitat_lbl = Label(Forms3, text="Habitat:", font=font1, bd=15)
habitat_lbl.grid(row=3)
habitat_entry = Entry(Forms3, textvariable=habitat,font=font2,width=20)
habitat_entry.grid(row=3,ipady=2,column=2)

xcoord_lbl = Label(Forms3, text="X Coordinates:", font=font1, bd=15)
xcoord_lbl.grid(row=4)
xcoord_entry = Entry(Forms3, textvariable=xcoordinates,font=font2,width=20)
xcoord_entry.grid(row=4,ipady=2,column=2)

xcoord_lbl = Label(Forms3, text="Y Coordinates:", font=font1, bd=15)
xcoord_lbl.grid(row=4)
xcoord_entry = Entry(Forms3, textvariable=ycoordinates,font=font2,width=20)
xcoord_entry.grid(row=4,ipady=2,column=2)

notes_lbl = Label(Forms3, text="Notes:", font=font1, bd=15)
notes_lbl.grid(row=6)
notes_entry = Entry(Forms3, textvariable=notes,font=font2,width=20)
notes_entry.grid(row=6,ipady=2,column=2)

author_lbl = Label(Forms3, text="Author:", font=font1, bd=15)
author_lbl.grid(row=7)
author_entry = Entry(Forms3, textvariable=author,font=font2,width=20)
author_entry.grid(row=7,ipady=2,column=2)

# ================ BUTTONS ================

create_btn = Button(Buttons, width=10, text="Create", bg=dgreen, command=DISABLED)
create_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)
read_btn = Button(Buttons, width=10, text="Read",bg=sblue, command=DISABLED)
read_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)
update_btn = Button(Buttons, width=10, text="Update", bg= gold, command=DISABLED)
update_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)
delete_btn = Button(Buttons2, width=10, text="Delete",fg=white, bg=red, command=DISABLED)
delete_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)
exit_btn = Button(Buttons2, width=10, text="About",fg=white, bg=gray, command=DISABLED)
exit_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)
about_btn = Button(Buttons2, width=10, text="Exit",fg=white, bg=gray, command=DISABLED)
about_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)

# ================= STATUS BAR ===============
stat_lbl = Label(Stat_bar, text=status, anchor=W)
stat_lbl.pack(ipady=2,padx=5,pady=5)


# ================ DATABASE VIEW ================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = tkk.Treeview(Right, columns=("Species", "Latin", 
                                    "Count", "Year", "Month",
                                    "Day","Hour", "City", "Country","Habitat",
                                    "X Coord", "Y Coord", "Notes",
                                    "Author"), selectmode="extended",
                                    height=500, yscrollcommand=scrollbary.set,
                                    xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Species', text="Species", anchor=CENTER)
tree.heading('Latin', text="Latin", anchor=CENTER)
tree.heading('Count', text="Count", anchor=CENTER)
tree.heading('Year', text="Year", anchor=CENTER)
tree.heading('Month', text="Month", anchor=CENTER)
tree.heading('Day', text="Day", anchor=CENTER)
tree.heading('Hour', text="Hour", anchor=CENTER)
tree.heading('City', text="City", anchor=CENTER)
tree.heading('Country', text="Country", anchor=CENTER)
tree.heading('Habitat', text="Habitat", anchor=CENTER)
tree.heading('X Coord', text="X Coord", anchor=CENTER)
tree.heading('Y Coord', text="Y Coord", anchor=CENTER)
tree.heading('Notes', text="Notes", anchor=CENTER)
tree.heading('Author', text="Author", anchor=CENTER)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=120)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=80)
tree.column('#7', stretch=NO, minwidth=0, width=80)
tree.column('#8', stretch=NO, minwidth=0, width=80)
tree.column('#9', stretch=NO, minwidth=0, width=80)
tree.column('#10', stretch=NO, minwidth=0, width=120)
tree.column('#11', stretch=NO, minwidth=0, width=80)
tree.column('#12', stretch=NO, minwidth=0, width=80)
tree.column('#13', stretch=NO, minwidth=0, width=120)
tree.column('#14', stretch=NO, minwidth=0, width=120)
tree.pack()




# ================ RESULT ================
if __name__ == '__main__':
    root.mainloop()