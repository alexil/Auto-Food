from Tkinter import *

class Dummy: pass
var = Dummy()

root = Tk()
root.title('Checkbutton')
for castmember, row, col, status in [
    ('BBB', 0,0,NORMAL)
    , ('SOHO', 1,0,NORMAL)
    , ('Pepper', 2,0,NORMAL)
    , ('River',3,0,NORMAL)
    , ('Prusot', 4,0,NORMAL)
    , ('Lehem Vered', 5,0,NORMAL)
    ]:
    setattr(var, castmember, IntVar())
    Checkbutton(root, text=castmember, state=status, anchor=W,
    variable = getattr(var, castmember)).grid(row=row, column=col, sticky=W)

root.mainloop()