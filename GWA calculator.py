import tkinter as tk
from fractions import Fraction
import json

# ---------- PISAY DATA ----------
pisay_json = """
{
 "electives": {
  "10":["Biology","Chemistry","Physics"],
  "11":["Technology","Agricultural Engineering","Engineering","Computer Science"],
  "12":["Technology","Agricultural Engineering","Engineering","Computer Science"]
 },

 "7":[
  {"name":"AdTech","units":1},
  {"name":"Computer Science","units":1},
  {"name":"English","units":1.3},
  {"name":"Filipino","units":1},
  {"name":"Integrated Science","units":1.7},
  {"name":"Mathematics","units":1.7},
  {"name":"PEHM","units":1},
  {"name":"Social Science","units":1}
 ],

 "8":[
  {"name":"Math 2","units":1},
  {"name":"Math 3","units":1},
  {"name":"Biology","units":1},
  {"name":"Chemistry","units":1},
  {"name":"Physics","units":1},
  {"name":"English","units":1.3},
  {"name":"Filipino","units":1},
  {"name":"Social Science","units":1},
  {"name":"Computer Science","units":1},
  {"name":"Earth Science","units":1},
  {"name":"AdTech","units":1},
  {"name":"PEHM","units":1}
 ],

 "9":[
  {"name":"Biology","units":1},
  {"name":"Chemistry","units":1},
  {"name":"Computer Science","units":1},
  {"name":"English","units":1},
  {"name":"Filipino","units":1},
  {"name":"Mathematics","units":1},
  {"name":"PEHM","units":1},
  {"name":"Physics","units":1},
  {"name":"Social Science","units":1},
  {"name":"Statistics","units":1}
 ],

 "10":[
  {"name":"English","units":1},
  {"name":"PEHM","units":1},
  {"name":"Biology","units":1},
  {"name":"Computer Science","units":1},
  {"name":"Physics","units":1},
  {"name":"Chemistry","units":1},
  {"name":"STEM Research","units":1},
  {"name":"Social Science","units":1},
  {"name":"Math","units":1.3},
  {"name":"Filipino","units":1},
  {"name":"Electives","units":1}
 ],

 "11":[
  {"name":"Research","units":2},
  {"name":"Core Science","units":1.7},
  {"name":"Electives","units":1.7},
  {"name":"Mathematics","units":1},
  {"name":"English","units":1},
  {"name":"Filipino","units":1},
  {"name":"Social Science","units":1}
 ],

 "12":[
  {"name":"Mathematics","units":1},
  {"name":"Social Science","units":1},
  {"name":"Research","units":2},
  {"name":"Biology","units":1.7},
  {"name":"Electives","units":1.7},
  {"name":"Filipino","units":1},
  {"name":"English","units":1}
 ]
}
"""
pisay_data = json.loads(pisay_json)
core_subjects = ["Biology", "Chemistry", "Physics"]

# ---------- ROOT ----------
root = tk.Tk()
root.title("Grade Calculator")
root.geometry("680x770")
root.configure(bg="#f2f4f7")

# ---------- VARIABLES ----------
system = tk.StringVar(value="Others")
grading_system = tk.StringVar(value="Percentile")  # Academic Grading System
typ = tk.StringVar(value="Subject")
grade_level = tk.StringVar(value="11")
core_choice = tk.StringVar(value="Biology")
elective_choice = tk.StringVar(value="Technology")

entries = []
generated = False

# ---------- STYLES ----------
HEADER_FONT = ("Segoe UI", 20, "bold")
LABEL_FONT = ("Segoe UI", 12)
ENTRY_FONT = ("Segoe UI", 12)
BTN_FONT = ("Segoe UI", 12, "bold")

BG = "#f2f4f7"
CARD = "#ffffff"
BTN = "#4a86cf"
CLEAR = "#ff4d4d"

# ---------- HELPERS ----------
def ordinal(n):
    return f"{n}th" if 10<=n%100<=20 else f"{n}{['th','st','nd','rd','th','th','th','th','th','th'][n%10]}"

def to_num(v, is_gwa=False):
    if not v: 
        return None
    try:
        v = v.strip()
        if not is_gwa:
            # Accept percentages
            if v.endswith("%"):
                val = float(v[:-1]) / 100
            else:
                # Accept fractions like 19/20
                val = float(Fraction(v))
                # If user entered 95 as a whole number, convert to decimal
                if val > 1:
                    val /= 100
            return val if 0 <= val <= 1 else None
        else:
            # GWA values: must be 1-5
            val = float(Fraction(v))
            return val if 1 <= val <= 5 else None
    except:
        return None

def clear_all():
    global generated
    generated=False
    entries.clear()
    for w in input_frame.winfo_children(): w.destroy()
    result_label.config(text="")

# ---------- ARROW NAV ----------
def bind_navigation():
    cols = 2
    for i, e in enumerate(entries):
        def up(ev,i=i): j=i-cols; entries[j].focus() if j>=0 else None
        def down(ev,i=i): j=i+cols; entries[j].focus() if j<len(entries) else None
        def left(ev,i=i): entries[i-1].focus() if i%cols==1 else None
        def right(ev,i=i): entries[i+1].focus() if i%cols==0 and i+1<len(entries) else None
        e.bind("<Up>",up)
        e.bind("<Down>",down)
        e.bind("<Left>",left)
        e.bind("<Right>",right)

def move_up(e):
    info=e.widget.grid_info(); r,c=info.get("row",0)-1, info.get("column",0)
    for child in input_frame.grid_slaves(row=r,column=c): child.focus(); return
def move_down(e):
    info=e.widget.grid_info(); r,c=info.get("row",0)+1, info.get("column",0)
    for child in input_frame.grid_slaves(row=r,column=c): child.focus(); return
def move_left(e):
    info=e.widget.grid_info(); r,c=info.get("row",0), info.get("column",0)-1
    for child in input_frame.grid_slaves(row=r,column=c): child.focus(); return
def move_right(e):
    info=e.widget.grid_info(); r,c=info.get("row",0), info.get("column",0)+1
    for child in input_frame.grid_slaves(row=r,column=c): child.focus(); return

root.bind("<Up>",move_up)
root.bind("<Down>",move_down)
root.bind("<Left>",move_left)
root.bind("<Right>",move_right)

# ---------- UPDATE LABEL ----------
def update_label(*a):
    if typ.get()=="Subject":
        number_label.config(text="Input number of subjects:")
        number_label.grid(row=2,column=0,sticky="w")
        number.grid(row=2,column=1)
    else:
        number_label.config(text="Input current quarter (for GWA)" if grading_system.get()=="GWA" else "Input number of quarters:")
        number_label.grid(row=2,column=0,sticky="w")
        number.grid(row=2,column=1)

# ---------- UPDATE VISIBILITY ----------
def update_visibility(*a):
    # Hide all widgets first
    for widget in [grade_label, grade_menu, elective_label, elective_menu, core_label, core_menu, number_label, number]:
        widget.grid_forget()

    if system.get() == "Pisay":
        grading_system.set("GWA")
        mode_menu.config(state="disabled")
        type_menu.config(state="normal")  # allow switching between Subject/Overall

        # Only show subject-related options if Subject is selected
        if typ.get() == "Subject":
            grade_label.grid(row=3, column=0)
            grade_menu.grid(row=3, column=1)

            # Elective picker only for grade 10+
            if grade_level.get() in pisay_data["electives"] and int(grade_level.get()) >= 10:
                electives = pisay_data["electives"][grade_level.get()]
                elective_menu["menu"].delete(0, "end")
                for e in electives:
                    elective_menu["menu"].add_command(label=e, command=lambda val=e: elective_choice.set(val))
                elective_choice.set(electives[0])
                elective_label.grid(row=4, column=0)
                elective_menu.grid(row=4, column=1)

            # Core picker only for grade 11+
            if int(grade_level.get()) >= 11:
                core_label.grid(row=5, column=0)
                core_menu.grid(row=5, column=1)

            # Auto-fill number of subjects
            subjects = pisay_data.get(grade_level.get(), [])
            number.delete(0, tk.END)
            number.insert(0, str(len(subjects)))
            number_label.grid(row=2, column=0, sticky="w")
            number.grid(row=2, column=1)

        else:  # Overall selected
            # Only show number of quarters
            number_label.config(text="Input number of quarters:")
            number_label.grid(row=2, column=0, sticky="w")
            number.grid(row=2, column=1)

    #DepEd
    elif system.get() == "DepEd":
        grading_system.set("Percentile")
        mode_menu.config(state="disabled")
        type_menu.config(state="normal")
        number_label.grid(row=2, column=0, sticky="w")
        number.grid(row=2, column=1)
    
    #Others
    else:
        mode_menu.config(state="normal")
        type_menu.config(state="normal")
        number_label.grid(row=2, column=0, sticky="w")
        number.grid(row=2, column=1)

# ---------- TRACES ----------
system.trace_add("write", update_visibility)
grade_level.trace_add("write", update_visibility)
typ.trace_add("write", update_visibility)  # <--- Added: triggers visibility on type change
grading_system.trace_add("write", update_label)
typ.trace_add("write", update_label)

# ---------- GENERATE INPUTS ----------
def generate_inputs():
    global generated
    clear_all()

    # --- Pisay Subject ---
    if system.get()=="Pisay" and typ.get()=="Subject":
        subjects=pisay_data.get(grade_level.get(),[])
        tk.Label(input_frame,text="Grade",bg=CARD).grid(row=0,column=1)
        tk.Label(input_frame,text="Units",bg=CARD).grid(row=0,column=2)
        for i,s in enumerate(subjects):
            name=s["name"]
            if name=="Electives": name=f"{elective_choice.get()} Elective"
            if name=="Core Science" or name=="Biology": name=f"{core_choice.get()} Core"
            tk.Label(input_frame,text=name,bg=CARD).grid(row=i+1,column=0,padx=6,pady=4,sticky="w")
            g=tk.Entry(input_frame,width=10,font=ENTRY_FONT)
            u=tk.Entry(input_frame,width=10,font=ENTRY_FONT)
            g.grid(row=i+1,column=1,padx=4)
            u.grid(row=i+1,column=2,padx=4)
            u.insert(0,str(s["units"]))
            entries.extend([g,u])
        generated=True
        bind_navigation()
        return

    # --- Overall / Others ---
    if not number.get().isdigit(): return
    n=int(number.get())
    if n<=0: return
    generated=True

    # --- Overall Percentile ---
    if typ.get()=="Overall" and grading_system.get()=="Percentile":
        for i in range(n):
            tk.Label(input_frame,text=f"Quarter {i+1} overall grade:",font=LABEL_FONT,bg=CARD)\
            .grid(row=i,column=0,padx=5,pady=4,sticky="w")
            e=tk.Entry(input_frame,font=ENTRY_FONT,width=20)
            e.grid(row=i,column=1,padx=5,pady=4)
            entries.append(e)
        return

    # --- Overall GWA ---
    if typ.get()=="Overall" and grading_system.get()=="GWA":
        labels=["Previous quarter grade:","Weight of previous grade:",f"{ordinal(n)} quarter grade:","Weight of current grade:"]
        for i,t in enumerate(labels):
            tk.Label(input_frame,text=t,font=LABEL_FONT,bg=CARD).grid(row=i,column=0,padx=5,pady=4,sticky="w")
            e=tk.Entry(input_frame,font=ENTRY_FONT,width=20)
            e.grid(row=i,column=1,padx=5,pady=4)
            entries.append(e)
        return

    # --- Subject mode ---
    if grading_system.get()=="GWA":
        tk.Label(input_frame,text="Grade",bg=CARD).grid(row=0,column=1)
        tk.Label(input_frame,text="Units",bg=CARD).grid(row=0,column=2)
        for i in range(n):
            tk.Label(input_frame,text=f"Subject {i+1}:",font=LABEL_FONT,bg=CARD).grid(row=i+1,column=0,padx=5,pady=4,sticky="w")
            g=tk.Entry(input_frame,font=ENTRY_FONT,width=10)
            u=tk.Entry(input_frame,font=ENTRY_FONT,width=10)
            g.grid(row=i+1,column=1,padx=5)
            u.grid(row=i+1,column=2,padx=5)
            entries.extend([g,u])
    else:
        tk.Label(input_frame,text="Grade",bg=CARD).grid(row=0,column=1)
        for i in range(n):
            tk.Label(input_frame,text=f"Subject {i+1} Grade:",font=LABEL_FONT,bg=CARD).grid(row=i+1,column=0,padx=5,pady=4,sticky="w")
            e=tk.Entry(input_frame,font=ENTRY_FONT,width=10)
            e.grid(row=i+1,column=1,padx=5)
            entries.append(e)

# ---------- CALCULATE ----------
def calculate():
    if not generated:
        result_label.config(text="Generate inputs first")
        return
    try:
        # ---------------- Subject GWA ----------------
        if system.get()=="Pisay" or "Others" and typ.get()=="Subject" and grading_system.get()=="GWA":
            total = units = 0
            for i in range(0,len(entries),2):
                g = to_num(entries[i].get(), True)
                u = float(entries[i+1].get())
                total += g * u
                units += u
            result_label.config(text=f"GWA: {total/units:.2f}")
            return
       # ---------------- Subject Percentile ----------------
        elif system.get()=="DepEd" or "Others" and grading_system.get()=="Percentile":
            vals=[to_num(e.get()) for e in entries]
            if None in vals: raise ValueError
            if typ.get()=="Subject":
                result_label.config(text=f"Quarter Percentile Grade: {sum(vals)/len(vals)*100:.2f}%")
        # ---------------- Overall Percentile ----------------
            else:
                result_label.config(text=f"Average Percentile: {sum(vals)/len(vals)*100:.2f}%")
            
        # ---------------- Overall GWA ----------------
        elif typ.get()=="Overall" and grading_system.get()=="GWA":
            p=to_num(entries[0].get(),True)
            pw=to_num(entries[1].get())
            c=to_num(entries[2].get(),True)
            cw=to_num(entries[3].get())
            if None in [p,pw,c,cw]: raise ValueError
            result_label.config(text=f"Final Quarter Grade: {p*pw+c*cw:.2f}")
    except:
        result_label.config(text="Invalid input")
                
# ---------- HELP PANEL ----------
def show_help():
    # Check if help window already exists
    if hasattr(root, "help_window") and root.help_window.winfo_exists():
        root.help_window.lift()  # bring it to front
        return
    
    # Create a new Toplevel window
    root.help_window = tk.Toplevel(root)
    root.help_window.title("Help / Tutorial")
    root.help_window.geometry("500x450")
    root.help_window.configure(bg=BG)
    
    tutorial_text = """
    SYSTEM
    • Pisay: Locks Academic Grading System to GWA.
    • DepEd: Locks Academic Grading System to Percentile.
    • Others: Allows free selection between Percentile and GWA.

    ACADEMIC GRADING SYSTEM
    • Percentile: Grades are calculated in percentages.
    • GWA: Grades are calculated using a general weighted average.

    TYPE
    • Subject: Enter individual subjects with units.
    • Overall: Enter overall grades per quarter.

    NUMBER OF SUBJECTS / QUARTERS
    • Fill out the number required for your calculation.
    • Pisay Subject automatically fills the required subjects and units.

    CORE SCIENCE / ELECTIVES (Pisay)
    • Only available in Subject mode.
    • Choose the appropriate core science and electives.

    GENERATING INPUTS
    • Click "Generate Inputs" to create grade entry fields.
    • Use arrow keys to move between fields quickly.


    CALCULATING GRADES
    • Click "Calculate" to compute your results.
    • The result box displays either GWA or Percentile.
    """

    # Scrollable text
    text_frame = tk.Frame(root.help_window, bg=CARD)
    text_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
    canvas = tk.Canvas(text_frame, bg=CARD, highlightthickness=0)
    scrollbar = tk.Scrollbar(text_frame, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
        
    content_frame = tk.Frame(canvas, bg=CARD)
    canvas.create_window((0,0), window=content_frame, anchor="nw")
        
    tk.Label(content_frame, text=tutorial_text, justify="left", anchor="nw", bg=CARD, font=LABEL_FONT).pack(padx=5, pady=5)
    content_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

# ---------- GUI ----------
tk.Label(root,text="Grade Calculator",font=HEADER_FONT,bg=BG).pack(pady=15)

opt = tk.Frame(root, bg=CARD, padx=15, pady=15, bd=1, relief="solid")
opt.pack(fill="x", padx=20, pady=10)

# System
tk.Label(opt, text="System:", font=LABEL_FONT, bg=CARD).grid(row=0, column=0)
system_menu = tk.OptionMenu(opt, system, "Pisay", "DepEd", "Others")
system_menu.grid(row=0, column=1)

# Academic Grading System / Mode
tk.Label(opt, text="Academic Grading System:", font=LABEL_FONT, bg=CARD).grid(row=1, column=0, sticky="w")
mode_menu = tk.OptionMenu(opt, grading_system, "Percentile", "GWA")
mode_menu.grid(row=1, column=1)

# Type
tk.Label(opt, text="Type:", font=LABEL_FONT, bg=CARD).grid(row=1, column=2, sticky="w")
type_menu = tk.OptionMenu(opt, typ, "Subject", "Overall")
type_menu.grid(row=1, column=3)

# Grade
grade_label = tk.Label(opt, text="Grade:", font=LABEL_FONT, bg=CARD)
grade_menu = tk.OptionMenu(opt, grade_level, "7", "8", "9", "10", "11", "12")

# Elective
elective_label = tk.Label(opt, text="Elective:", font=LABEL_FONT, bg=CARD)
elective_menu = tk.OptionMenu(opt, elective_choice, "Technology")

# Core Science
core_label = tk.Label(opt, text="Core Science:", font=LABEL_FONT, bg=CARD)
core_menu = tk.OptionMenu(opt, core_choice, *core_subjects)

# Number of subjects / quarters
number_label = tk.Label(opt, text="Input number of subjects:", font=LABEL_FONT, bg=CARD)
number = tk.Entry(opt, font=ENTRY_FONT, width=15)

# Buttons
tk.Button(opt, text="Clear", bg=CLEAR, fg="white", font=BTN_FONT, width=10, command=clear_all).grid(row=7, column=0, pady=10)
tk.Button(opt, text="Generate Inputs", bg=BTN, fg="white", font=BTN_FONT, width=18, command=generate_inputs).grid(row=7, column=1, pady=10)
help_btn = tk.Button(opt, text="Help", bg="#ffa500", fg="white", font=BTN_FONT, command=show_help)
help_btn.grid(row=7, column=3, padx=5, pady=5, sticky="se")

tk.Button(opt,text="Clear",bg=CLEAR,fg="white",font=BTN_FONT,width=10,command=clear_all).grid(row=7,column=0,pady=10)
tk.Button(opt,text="Generate Inputs",bg=BTN,fg="white",font=BTN_FONT,width=18,command=generate_inputs).grid(row=7,column=1,pady=10)

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

tk.Button(root,text="Calculate",bg=BTN,fg="white",font=BTN_FONT,width=20,command=calculate).pack(pady=10)

result_box=tk.Frame(root,bg=CARD,bd=1,relief="solid")
result_box.pack(fill="x",padx=20,pady=10)
result_label=tk.Label(result_box,text="",font=("Segoe UI",14),bg=CARD)
result_label.pack(pady=20)

system.trace_add("write",update_visibility)
grade_level.trace_add("write",update_visibility)
grading_system.trace_add("write",update_label)
typ.trace_add("write",update_label)

# ---------- HELP BUTTON ----------
help_btn = tk.Button(opt, text="Help", bg="#ffa500", fg="white", font=BTN_FONT, command=show_help)
help_btn.grid(row=7, column=3, padx=5, pady=5, sticky="se")  # bottom-right of options card

update_visibility()
root.mainloop()
