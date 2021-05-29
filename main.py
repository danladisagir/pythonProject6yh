# School Management program
# to accept student data and subjects offered in a nursary and primary school setting
import pickle

# 1. student data
stddata = {}


def stddet():
    admno = input('admission number')
    name = input('studenet name')
    clas = input('class admitted to')
    datebirth = input('date of birth')
    stddata = {'admNo': admno, 'name': name, 'clas': clas, 'DateBirth': datebirth}


a = input('do you want to enter new student detail? if yes, enter yes, else enter no')
stdlst = []
ss = {}
while a == 'yes':
    stddet()

    stdlst.append(stddata)
    print(stdlst)
    if a != 'yes':
        break
    a = input('do you want to enter another student detail? if yes, enter yes, else enter end')

    sd = stdlst
    ss = pickle.dumps(sd)  # Saved name list

# 2. subject detail capture for 3 classes: Nur1, Nur2, Pr1
import pickle

n1k = {}


def n1subjlst():
    x1 = int(input('input the number of nur1 subjects'))
    y1 = x1 + 1
    i = 1
    n1subj = []
    while i < y1:
        n1name = input('input nur1 subject name')
        n1subj.append(n1name)
        i = i + 1
        print(n1subj)
        if i > x1:
            break
        n1nsm = {}
        n1nsm['n1subj'] = n1subj

        n1k = pickle.dumps(n1nsm)  # saved nur1 Subj


n2k = {}


def n2subjlst():
    x2 = int(input('input the number of nur2 subjects'))
    y2 = x2 + 1
    i = 1
    n2subj = []
    while i < y2:
        n2name = input('input nur2 subject name')
        n2subj.append(n2name)
        i = i + 1
        print(n2subj)
        if i > x2:
            break
        n2nsm = {}
        n2nsm['n2subj'] = n2subj

        n2k = pickle.dumps(n2nsm)  # saved nur2 Subj


p1k = {}


def p1subjlst():
    x3 = int(input('input the number of pri1 subjects'))
    y3 = x3 + 1
    i = 1
    p2subj = []
    while i < y3:
        p1name = input('input pri1 subject name')
        p2subj.append(p1name)
        i = i + 1
        print(p2subj)
        if i > x3:
            break
        p1nsm = {}
        p1nsm['p2subj'] = p2subj

        p1k = pickle.dumps(p1nsm)  # saved nur2 Subj


clastyp = input('to add subjects, first input/select class: nur1, nur2 or pri2')
while clastyp != '':
    if clastyp == 'nur1':
        n1subjlst()
    elif clastyp == 'nur2':
        n2subjlst()
    else:
        p1subjlst()

    if clastyp == '':
        break
    clastyp = input('select next class to add subjects: nur2 or pri2')

# 3. for reload inorder to assign stds scores (n1SubJ for all N1std, n2SubJ for all N2SubJ, p1SubJ for all P1std)
namelist = pickle.loads(ss)  #
print(namelist)

n1mynamelst = pickle.loads(n1k)  # nur1 subj
print(n1mynamelst)

n2mynamelst = pickle.loads(n2k)  # nur2 subj
print(n2mynamelst)

p1mynamelst = pickle.loads(p1k)  # nur3 subj
print(p1mynamelst)
