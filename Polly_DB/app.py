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
city = StringVar()
country = StringVar()
habitat = StringVar()
xcoordinates = IntVar()
ycoordinates = IntVar()
notes = StringVar()
author = StringVar()

# ================ FRAMES ================

Left = Frame(root, width=400, height=300)
Left.pack(side=LEFT, fill=BOTH)
Right = Frame(root, width=1200, height=800, bd=8, relief=RAISED)
Right.pack(side=LEFT)
Forms1 = Frame(Left, width=400, height=550)
Forms1.pack(side=TOP)
Forms2 = Frame(Left, width=400, height=550)
Forms2.pack(side=TOP)
Forms3 = Frame(Left, width=400, height=550)
Forms3.pack(side=TOP)
Buttons2 = Frame(Left, width=400, height=100, bd=1, relief=RAISED)
Buttons2.pack(side=BOTTOM)
Buttons = Frame(Left, width=400, height=100, bd=1, relief=RAISED)
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

year_lbl = Label(Forms2,text="Year: ",font=font1)
year_lbl.pack(side=LEFT,padx=5,pady=5)
year_entry = Entry(Forms2,font=font1,width=5,bd=2,textvariable=year)
year_entry.pack(side=LEFT,ipady=2,padx=5,pady=5)

month_lbl = Label(Forms2,text="Month: ",font=font1)
month_lbl.pack(side=LEFT,padx=5,pady=5)
month_entry = Entry(Forms2,font=font1,width=3,bd=2,textvariable=month)
month_entry.pack(side=LEFT,ipady=2,padx=5,pady=5)

day_lbl = Label(Forms2,text="Day: ",font=font1)
day_lbl.pack(side=LEFT,padx=5,pady=5)
day_entry = Entry(Forms2,font=font1,width=3,bd=2,textvariable=day)
day_entry.pack(side=LEFT,ipady=2,padx=5,pady=5)

city_lbl = Label(Forms3, text="   City:   ", font=font1, bd=15)
city_lbl.grid(row=0)
city_entry = Entry(Forms3, textvariable=city,font=font2,width=20)
city_entry.grid(row=0,ipady=2,column=2)

country_lbl = Label(Forms3, text="Country:", font=font1, bd=15)
country_lbl.grid(row=1)
country_entry = Entry(Forms3, textvariable=country,font=font2,width=20)
country_entry.grid(row=1,ipady=2,column=2)

habitat_lbl = Label(Forms3, text="Habitat:", font=font1, bd=15)
habitat_lbl.grid(row=2)
habitat_entry = Entry(Forms3, textvariable=country,font=font2,width=20)
habitat_entry.grid(row=2,ipady=2,column=2)

xcoord_lbl = Label(Forms3, text="X Coordinates:", font=font1, bd=15)
xcoord_lbl.grid(row=3)
xcoord_entry = Entry(Forms3, textvariable=xcoordinates,font=font2,width=20)
xcoord_entry.grid(row=3,ipady=2,column=2)

xcoord_lbl = Label(Forms3, text="Y Coordinates:", font=font1, bd=15)
xcoord_lbl.grid(row=4)
xcoord_entry = Entry(Forms3, textvariable=ycoordinates,font=font2,width=20)
xcoord_entry.grid(row=4,ipady=2,column=2)

notes_lbl = Label(Forms3, text="Notes:", font=font1, bd=15)
notes_lbl.grid(row=5)
notes_entry = Entry(Forms3, textvariable=notes,font=font2,width=20)
notes_entry.grid(row=5,ipady=2,column=2)

author_lbl = Label(Forms3, text="Author:", font=font1, bd=15)
author_lbl.grid(row=6)
author_entry = Entry(Forms3, textvariable=author,font=font2,width=20)
author_entry.grid(row=6,ipady=2,column=2)

# ================ BUTTONS ================

create_btn = Button(Buttons, width=10, text="Create", command=DISABLED)
create_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)
read_btn = Button(Buttons, width=10, text="Read", command=DISABLED)
read_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)
update_btn = Button(Buttons, width=10, text="Update", command=DISABLED)
update_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)
delete_btn = Button(Buttons2, width=10, text="Delete", command=DISABLED)
delete_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)
exit_btn = Button(Buttons2, width=10, text="About", command=DISABLED)
exit_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)
about_btn = Button(Buttons2, width=10, text="Exit", command=DISABLED)
about_btn.pack(side=LEFT,ipady=2,padx=5,pady=5)

# ================ DATABASE VIEW ================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = tkk.Treeview(Right, columns=("Species", "Latin", 
                                    "Count", "Year", "Mont",
                                    "Day", "City", "Country","Habitat",
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
tree.heading('Mont', text="Month", anchor=CENTER)
tree.heading('Day', text="Day", anchor=CENTER)
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
tree.column('#9', stretch=NO, minwidth=0, width=120)
tree.column('#10', stretch=NO, minwidth=0, width=80)
tree.column('#11', stretch=NO, minwidth=0, width=80)
tree.column('#12', stretch=NO, minwidth=0, width=120)
tree.column('#13', stretch=NO, minwidth=0, width=120)
tree.pack()




# ================ RESULT ================
if __name__ == '__main__':
    root.mainloop()