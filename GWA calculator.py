import tkinter as tk
from fractions import Fraction

# --- ROOT WINDOW ---
root=tk.Tk()
root.title("Grade Calculator")
root.geometry("650x700")
root.configure(bg="#f2f4f7")

# -------- VARIABLES --------
mode=tk.StringVar(value="Percentile")
typ=tk.StringVar(value="Subject")
entries=[]
generated=False

HEADER_FONT=("Segoe UI",20,"bold")  
LABEL_FONT=("Segoe UI",12)
ENTRY_FONT=("Segoe UI",12)
BTN_FONT=("Segoe UI",12,"bold")

BG="#f2f4f7"
CARD="#ffffff"
BTN="#4a86cf"
CLEAR="#ff4d4d"

# ------------------ HELPERS ------------------
def ordinal(n):
    return f"{n}th" if 10<=n%100<=20 else f"{n}{['th','st','nd','rd','th','th','th','th','th','th'][n%10]}"

def clear_all():
    global generated
    generated=False
    entries.clear()
    for w in input_frame.winfo_children(): w.destroy()
    result_label.config(text="")

def to_num(v,is_gwa=False):
    if not v: return None
    try:
        v=v.strip()
        if not is_gwa:
            val=float(v[:-1])/100 if v.endswith("%") else float(Fraction(v))
            if val>1: val/=100
            return val if 0<=val<=1 else None
        val=float(Fraction(v))
        return val if 1<=val<=5 else None
    except:
        return None

def update_label(*a):
    if typ.get()=="Subject":
        number_label.config(text="Input number of subjects:")
    else:
        number_label.config(text="Input current quarter" if mode.get()=="GWA" else "Input number of quarters:")

# --------- GENERATE INPUTS ---------
def generate_inputs():
    global generated
    clear_all()
    if not number.get().isdigit(): return
    n=int(number.get())
    if n<=0: return
    if typ.get()=="Overall" and mode.get()=="GWA" and n==1:
        result_label.config(text="Cannot generate inputs: No previous quarter")
        return
    generated=True

    if typ.get()=="Overall" and mode.get()=="Percentile":
        for i in range(n):
            tk.Label(input_frame,text=f"Quarter {i+1} overall grade:",font=LABEL_FONT,bg=CARD)\
            .grid(row=i,column=0,padx=5,pady=4,sticky="w")
            e=tk.Entry(input_frame,font=ENTRY_FONT,width=20)
            e.grid(row=i,column=1,padx=5,pady=4)
            entries.append(e)
        return

    if typ.get()=="Overall" and mode.get()=="GWA":
        labels=["Previous quarter grade (1-5)","Weight of previous grade:",f"{ordinal(n)} quarter grade:","Weight of current grade:"]
        for i,t in enumerate(labels):
            tk.Label(input_frame,text=t,font=LABEL_FONT,bg=CARD)\
            .grid(row=i,column=0,padx=5,pady=4,sticky="w")
            e=tk.Entry(input_frame,font=ENTRY_FONT,width=20)
            e.grid(row=i,column=1,padx=5,pady=4)
            entries.append(e)
        return

    if mode.get()=="GWA":
        tk.Label(input_frame,text="Grade",bg=CARD).grid(row=0,column=1)
        tk.Label(input_frame,text="Units",bg=CARD).grid(row=0,column=2)
        for i in range(n):
            tk.Label(input_frame,text=f"Subject {i+1}:",font=LABEL_FONT,bg=CARD)\
            .grid(row=i+1,column=0,padx=5,pady=4,sticky="w")
            g=tk.Entry(input_frame,font=ENTRY_FONT,width=10)
            u=tk.Entry(input_frame,font=ENTRY_FONT,width=10)
            g.grid(row=i+1,column=1,padx=5)
            u.grid(row=i+1,column=2,padx=5)
            entries.extend([g,u])
    else:
        tk.Label(input_frame,text="Grade",bg=CARD).grid(row=0,column=1)
        for i in range(n):
            tk.Label(input_frame,text=f"Subject {i+1} Grade:",font=LABEL_FONT,bg=CARD)\
            .grid(row=i+1,column=0,padx=5,pady=4,sticky="w")
            e=tk.Entry(input_frame,font=ENTRY_FONT,width=10)
            e.grid(row=i+1,column=1,padx=5)
            entries.append(e)

# ------------------- CALCULATE -------------------
def calculate():
    if not generated:
        result_label.config(text="Generate inputs first")
        return
    try:
        if typ.get()=="Overall" and mode.get()=="Percentile":
            vals=[to_num(e.get()) for e in entries]
            if None in vals: raise ValueError
            result_label.config(text=f"Average Percentile: {sum(vals)/len(vals)*100:.2f}%")

        elif typ.get()=="Overall" and mode.get()=="GWA":
            p=to_num(entries[0].get(),True)
            pw=to_num(entries[1].get())
            c=to_num(entries[2].get(),True)
            cw=to_num(entries[3].get())
            if None in [p,pw,c,cw]: raise ValueError
            result_label.config(text=f"Final Quarter Grade: {p*pw+c*cw:.2f}")

        elif typ.get()=="Subject" and mode.get()=="GWA":
            total=units=0
            for i in range(0,len(entries),2):
                g=to_num(entries[i].get(),True)
                u=float(entries[i+1].get())
                if g is None: raise ValueError
                total+=g*u
                units+=u
            result_label.config(text=f"GWA: {total/units:.4f}")

        else:
            vals=[to_num(e.get()) for e in entries]
            if None in vals: raise ValueError
            result_label.config(text=f"Quarter Percentile Grade: {sum(vals)/len(vals)*100:.2f}%")

    except:
        result_label.config(text="Invalid input")

# ------------------- GUI LAYOUT -------------------
tk.Label(root,text="Grade Calculator",font=HEADER_FONT,bg=BG).pack(pady=15)

opt=tk.Frame(root,bg=CARD,padx=15,pady=15,bd=1,relief="solid")
opt.pack(fill="x",padx=20,pady=10)

tk.Label(opt,text="Mode:",font=LABEL_FONT,bg=CARD).grid(row=0,column=0,sticky="w")
tk.OptionMenu(opt,mode,"Percentile","GWA").grid(row=0,column=1)

tk.Label(opt,text="Type:",font=LABEL_FONT,bg=CARD).grid(row=1,column=0,sticky="w")
tk.OptionMenu(opt,typ,"Subject","Overall").grid(row=1,column=1)

number_label=tk.Label(opt,text="Input number of subjects:",font=LABEL_FONT,bg=CARD)
number_label.grid(row=2,column=0,sticky="w")

number=tk.Entry(opt,font=ENTRY_FONT,width=15)
number.grid(row=2,column=1)

tk.Button(opt,text="Clear",bg=CLEAR,fg="white",font=BTN_FONT,width=10,command=clear_all)\
.grid(row=3,column=0,pady=10)

tk.Button(opt,text="Generate Inputs",bg=BTN,fg="white",font=BTN_FONT,width=18,command=generate_inputs)\
.grid(row=3,column=1,pady=10)

# --------- SCROLLABLE INPUT ---------
container=tk.Frame(root,bg=CARD,bd=1,relief="solid")
container.pack(fill="both",expand=True,padx=20,pady=10)

canvas=tk.Canvas(container,bg=CARD,highlightthickness=0)
scroll=tk.Scrollbar(container,command=canvas.yview)
canvas.configure(yscrollcommand=scroll.set)

scroll.pack(side="right",fill="y")
canvas.pack(side="left",fill="both",expand=True)

input_frame=tk.Frame(canvas,bg=CARD)
canvas.create_window((0,0),window=input_frame,anchor="nw")

input_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# -------------- CALCULATE BUTTON --------------
tk.Button(root,text="Calculate",bg=BTN,fg="white",font=BTN_FONT,width=20,command=calculate)\
.pack(pady=10)

# ----- RESULT BOX -----
result_box=tk.Frame(root,bg=CARD,bd=1,relief="solid")
result_box.pack(fill="x",padx=20,pady=10)

result_label=tk.Label(result_box,text="",font=("Segoe UI",14),bg=CARD)
result_label.pack(pady=20)

# ------------- TRACE VARIABLES -------------    
mode.trace_add("write",update_label)
typ.trace_add("write",update_label)

# ------- MAINLOOP -------
root.mainloop()
