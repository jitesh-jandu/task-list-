# this is is a to do app make by jitesh jandu using json 


import json
undo = []
try :
    with open ("tsk.json","r") as f :
        tasks = json.load(f)
        

except FileNotFoundError :
    tasks = []        
    
#function starting :---

def view () :
    print(f"{'tasks ':=^42}")
    if not tasks :
        print("no tasks yet !")
        return

    print("your task :-") 
    for indox,dic in enumerate (tasks , start=1):
        status = "✅ Done" if dic["status"] else "❌ Pending" # finaly ye shortcut sikh hi liya hurrrrrryyyyyyyy !
        print(f"{indox}. {dic['item']:<25} {status:>10}")               # just for visiter dont laugh am making this project before college start amd for the first time

    print(" "*42)
    print(" "*42)
def add () :
    ad = input("enter what to add:--").strip().lower()
    if ad :
        tasks.append({"item":ad,"status":False})
        undo.append({"action":"add","item":ad})

        print(f"task {ad} added !")

        with open ("tsk.json","w") as f :
            json.dump(tasks,f)


def delete () :

    dele = int(input("enter task to delete:--"))
    dele = dele - 1

    if 0 <= dele < (len(tasks)) :
        delet = tasks[dele]["item"]
        undo.append({"action":"delete","index":dele,"data": tasks[dele]})
        del tasks[dele]

        print(f"task {delet} deleted !")

        with open ("tsk.json","w") as f :
          json.dump(tasks,f)

    else :
        print("not a valid task !")   
  

def mark ():
    mar = int(input("whitch task is done:--"))

    marks = mar - 1

    if 0 <= marks < (len(tasks)) :
        undo.append({"action":"mark","index":marks})

        tasks[marks]["status"] = not tasks[marks]["status"]

        print("task updated !")

        with open ("tsk.json","w") as f :
         json.dump(tasks,f)

    else :
        print("not a valid task !") 




def undof() :
    if not undo :
        print("nothing to undo !")
        return
    lastchange = undo.pop()

    if lastchange["action"] == "add" :
        del tasks[-1] 
        print("add action undone !")

    elif lastchange["action"] == "mark":
        target = lastchange["index"]

        tasks[target]["status"] = not tasks[target]["status"]  
        print("mark as undone !")

    elif lastchange["action"] == "delete" :

        tasks.insert(lastchange["index"],lastchange["data"])

        print("data restored !")   





    
# main loop starting :--

while True :
    print(f"{' task app ':=^42}")
    print("1. view task ")
    print("2. add task ")
    print("3. delete task ")
    print("4. mark as read ")
    print("5. undo ")
    print("6. exit ")

    try :
        print("-"*42)
        choice = int(input("enter what you want:--"))
        print("="*42)
    except Exception as err:
        print("enter correct number value !")

    if choice == 1 :
        view()

    elif choice == 2 :
        add()

    elif choice == 3 :
        delete()

    elif choice == 4 :
        mark()
    elif choice == 5 :
        undof()

    if choice == 6 :
        print("you are exiting")
        print(" "*42)
        print("made by * jitesh jandu *")
        print("="*42)

        break



# ============================================================
#        📝 PYTHON TO-DO APP REVISION NOTES (BY JITESH)
# ============================================================

# 1. LOOP VARIABLE KA JADOO:
# --------------------------
# * Code: for indox, dic in enumerate(tasks):
# * Jab loop chalta hai, toh 'dic' KHUD ek dictionary variable ban jata hai.
# * Isiliye uske andar ka saaman nikalne ke liye dic['item'] likhte hain.

# 2. ITEM['ITEM'] KA CONFUSION:
# -----------------------------
# * Bahar wala (dic ya item) ek temporary variable hai, ise aap 'dabba' bhi likh sakte hain.
# * Brackets ke andar wala ['item'] dictionary ki fixed KEY (label) hai.

# 3. ENUMERATE() KYUN USE KIYA?:
# ------------------------------
# * Temporary variable toh normal loop se bhi mil jata.
# * Enumerate humne SIRF serial numbers (1, 2, 3...) generate karne ke liye lagaya.
# * Isiliye do variables bante hain: for indox, dic in ... (indox = number, dic = dictionary).

# 4. 1-LINE IF-ELSE SHORTCUT:
# ---------------------------
# * Formula: [ value_if_true  if  condition  else  value_if_false ]
# * Example: status = "✅ Done" if dic["status"] else "❌ Pending"
# * Number check karna ho toh: if dic["status"] == 2 else ...

# 5. .STRIP() AUR CASE HANDLING:
# ------------------------------
# * .strip() sirf AAGE aur PEECHE ke spaces hatata hai, beech ke nahi.
# * .lower() sabko choti ABC mein badalta hai taaki matching ke waqt crash na ho.

# 6. JSON FILE: "w" MODE VS "a" MODE:
# -----------------------------------
# * "w" (Write): File saaf karke naye sire se likhta hai. JSON mein yahi use hoga kyunki hamara backup RAM (tasks list) mein pehle se safe hai.
# * "a" (Append): JSON mein use nahi karte kyunki do-do brackets [] lagne se file corrupt ho jati hai.

# 7. DATA TRANSFER: DUMP VS LOAD:
# -------------------------------
# * json.dump(tasks, f): Python list ko file ke ANDAR daalta (save) hai. (Data aur File dono chahiye).
# * json.load(f): File se data BAHAR nikal kar Python list mein bharta hai. (Sirf File chahiye).

# ============================================================

# ============================================================
#   📝 PYTHON TO-DO APP REVISION NOTES (PART 2 - BY JITESH)
# ============================================================

# 8. INDEX SAFETY CHECK & BOUNDS:
# -------------------------------
# * Formula: if 0 <= dele < len(tasks):
# * Python mein list index humesha 0 se shuru hota hai aur 'len(tasks) - 1' tak jata hai.
# * Isliye user ke input mein se 1 minus karna zaroori hai (dele = dele - 1).
# * Strictly Less Than (<) isliye lagaya taaki agar length 3 hai, toh index 3 par crash na ho (max index 2 hi hoga).

# 9. THE 'DEL' STATEMENT VS '.POP()':
# -----------------------------------
# * Code: del tasks[dele]
# * 'del' ek keyword (statement) hai, isme round brackets () nahi lagte.
# * Yeh kisi bhi item ko memory se seedhe uda deta hai.
# * Rule: Delete karne se theek pehle task ka naam temporary variable mein save karna padta hai (deleted_item = tasks[dele]["item"]), warna delete hone ke baad naam nahi milega!

# 10. `TRY-EXCEPT` KA REAL POWER & ATTACHMENT:
# -------------------------------------------
# * Try aur Except humesha ek JODI (pair) mein hote hain, inko alag nahi kiya ja sakta.
# * File Load ke time: `except FileNotFoundError` khud hi `tasks = []` (khaali list) bana deta hai agar file na mile. Isliye alag se bahar `tasks = []` likhne ki zaroorat nahi hai (warna data reset ho jayega).

# 11. THE 'CONTINUE' KEYWORD TRAP:
# -------------------------------
# * Jab while loop ke andar input galat ho (jaise "abc"), toh 'choice' variable ban hi nahi paata.
# * Agar variable nahi bana, toh neeche 'if choice == 1' check karte hi NameError (Crash) aayega.
# * Solution: Except block ke andar `continue` lagao! Yeh niche wale crash-prone code ko bypass karke seedhe loop ke start par jump karwa deta hai.

# 12. CURRENT WORKING DIRECTORY (CWD):
# -------------------------------------
# * Code: with open("tsk.json", "w")
# * Jab hum poora path (C:/ folder/...) nahi likhte, toh Python automatic usi folder mein file banata ya dhoodhta hai jahan hamari main .py file chal rahi hai.
# * Isiliye 'import os' ki zaroorat is project mein nahi padi!

# 13. BOARDS SHORTCUTS FOR SPEED:
# -------------------------------
# * Shift + Tab: Poore selected code block ko ek sath 4 spaces PEECHE (left) khisakane ke liye (Indentation thik karne ke liye).
# * Ctrl + Delete: Cursor ke RIGHT side wale poore word ko ek jhatke mein delete karne ke liye.
# ============================================================

# ============================================================
#   📝 PYTHON TO-DO APP REVISION NOTES (PART 3 - BY JITESH)
# ============================================================

# 14. STACK DATA STRUCTURE & LIFO LOGIC:
# --------------------------------------
# * Stack ka matlab hota hai dabbe ke upar dabba (like a stack of plates).
# * Yeh LIFO (Last In, First Out) principle par kaam karta hai.
# * `.append()` se hum data ko stack ke top par PUSH (save) karte hain.
# * `.pop()` se hum stack ke sabse aakhri (latest) element ko memory se nikaalte (POP) hain.

# 15. NAME COLLISION TRAP (VARIABLE VS FUNCTION):
# ------------------------------------------------
# * Agar list ka naam 'undo' hai, toh function ka naam 'def undo():' nahi rakh sakte.
# * Aisa karne par Python confuse ho jata hai aur 'TypeError: function object has no attribute pop' ka crash deta hai.
# * Solution: Function ka naam 'def undo_action():' rakha taaki dono alag pehchane jayein.

# 16. THE PYTHON '.INSERT()' MAGIC:
# ----------------------------------
# * Formula: list_name.insert(index_position, data_packet)
# * Jab hum beech se delete hua task wapas laate hain, toh `.insert()` use karte hain.
# * Yeh function automatic baaki saare elements ko ek-ek seat aage khisakane (indexes adjust karne) ka kaam khud kar leta hai.

# 17. NEGATIVE INDEXING FOR QUICK DELETE:
# ----------------------------------------
# * Code: del tasks[-1]
# * Python mein [-1] ka matlab hota hai list ka sabse aakhri element (peeche se pehla).
# * Jab hum 'add' action ko undo karte hain, toh bina kisi calculation ke direct 'del tasks[-1]' chalakar last added element ko uda sakte hain.

# 18. STATE SNAPSHOT (NO EXTRA STATUS UPDATE NEEDED):
# ---------------------------------------------------
# * Jab hum 'tasks[dele]' ko 'undo' stack mein append karte hain, toh sirf naam nahi, balki poori dictionary (item + status) ka snapshot copy hota hai.
# * Isiliye undo karte waqt hume status ko alag se True/False nahi karna padta, task jaisa delete hua tha (Pending ya Done), waisa ka waisa hi restore ho jata hai!

# 19. AI/ML CONNECTION (BACKTRACKING & BACKPROPAGATION):
# ------------------------------------------------------
# * AI algorithms (jaise chess bots ya LLM token generation) jab galat raste par jaate hain, toh stack ka use karke Backtrack (Undo) karte hain.
# * Neural Networks ke training mein (Backpropagation), forward pass ka data stack mein push hota hai, aur errors ko theek karne ke liye backward pass mein use pop kiya jata hai.
# ============================================================




