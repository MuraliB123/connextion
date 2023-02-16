from multiprocessing import context
from django.shortcuts import render
import mysql.connector as m
con = m.connect(host='localhost',user='root',password='Murali123$',database='service',auth_plugin='mysql_native_password')
cur = con.cursor()
def search(r):
    profession=r.GET["profession"]
    a=r.GET["credential"]
    kw = r.GET["search"]
    q = "select profession,price,name from "+profession+";"
    print(profession)
    cur.execute(q)
    l = []
    for i in cur.fetchall():  
        if (kw in i[0]):
            l.append(i)
    context = {"values":l,"detail":a}
    print(l)
    if(profession == "doctor"):
        return render(r,"doctor.html",context)
    if(profession == "repair"):
        return render(r,"repair.html",context)
    if(profession=="restaurant"):
        return render(r,"restaurant.html",context)
    if(profession=="needs"):
        return render(r,"needs.html",context)
    if(profession=="beauticians"):
        return render(r,"beauty.html",context)
    if(profession=="loans"):
        return render(r,"loans.html",context)
    if(profession=="housekeep"):
        return render(r,"housekeep.html",context)
    if(profession=="baby"):
        return render(r,"baby.html",context)
    if(profession=="education"):
        return render(r,"education.html",context)
    if(profession=="sports"):
        return render(r,"sports.html",context)

def create(r):
    a=r.POST['tname']
    b=r.POST['tmail']
    c=r.POST['tmobile']
    d=r.POST['tgender']
    e=r.POST['tpass']
    f=r.POST['cpass']
    g=r.POST['userrole']
    h=r.POST['tdob']
    i=r.POST['tcategory']
    j=r.POST['tpincode']
    k=r.POST['tlanguages']
    l=r.POST['trecentcourse']
    m=r.POST['tuniv']
    n=r.POST['t-com-or-pur']
    #q=r.POST['texpy']
    #o=r.POST['tchargeph']
    s=r.POST['tdescription']
    
    sql='''INSERT into users values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"null","null");'''
    z=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,s)
    cur.execute(sql,z)
    con.commit()
    return render(r,'home.html')
    

def profile(r):
    w=r.POST['slmail']
    x=r.POST['slpass']
    y=r.POST['userrole']
    sql='''select * from users where name=%s and password=%s and role=%s;'''
    t=(w,x,y)
    k=cur.execute(sql,t)
    print(k)
    a=cur.fetchall()
    c=0
    
    for i in a:
        c=1
        name=i[0]
        mail=i[1]
        no=i[2]
        role=i[6]
        print(name)
        print(c)
        return render(r,'home.html',{'name':"Welcome"+name+"!",'mail':mail,'no':no,'role':role,'detail':name})
    if(c==0):
        return render(r,"login.html",{'error':'Login Credentials are incorrect'})
    

def contact(r):
    na=r.POST['Name']
    ma=r.POST['Email']
    sub=r.POST['Subject']
    msg=r.POST['Message']
    sql='''INSERT into queries values(%s,%s,%s,%s);'''
    z=(na,ma,sub,msg)
    cur.execute(sql,z)
    con.commit()
    return render(r,'Project.htm')
    


def land(r):
    profession=r.GET["profession"]
    a=r.GET["btn"]
    # print(r.GET['credential'],'hi')
    name1=r.GET['credential']
    print(name1,"credential")
    sql="select * from "+profession+" where name=%s;"
    p=(a,)
    cur.execute(sql,p)
    l=[]
    for i in cur.fetchall():
        for j in i:
            l.append(j)
    name=l[0]
    job=l[1]
    email=l[2]
    no=l[3]
    city=l[4]
    pay=l[5]    
    print(name1)
    context={'name':name,'job':job,'email':email,'no':no,'city':city,'pay':pay,"detail":name1}
    if(profession=="doctor"):
        return render(r,'doct1.html',context)
    if(profession=="repair"):
        return render(r,"doct1.html",context)
    if(profession=="restaurant"):
        return render(r,"doct1.html",context)
    if(profession=="needs"):
        return render(r,"doct1.html",context)
    if(profession=="beauticians"):
        return render(r,"doct1.html",context)
    if(profession=="loans"):
        return render(r,"doct1.html",context)
    if(profession=="housekeep"):
        return render(r,"doct1.html",context)
    if(profession=="baby"):
        return render(r,"doct1.html",context)
    if(profession=="education"):
        return render(r,"doct1.html",context)
    if(profession=="sports"):
        return render(r,"doct1.html",context)

def verify(r):
    name=r.GET["credential"]
    if(len(name)>0):
        sql='''select * from users where name=%s;'''
        p=(name,)
        print(name)
        cur.execute(sql,p)
        l=[]
        for i in cur.fetchall():
            for j in i:
                l.append(j)
        print(l[0],l[1],l[2],l[3],l[4],l[5],l[6])
        name=l[0]
        mail=l[1]
        no=l[2]
        gen=l[3]
        dup=l[4]
        dop=l[5] 
        role=l[6]
        dob=l[7]
        context={'name':name,'mail':mail,'no':no,'gen':gen,'role':role,'dob':dob}
        return render(r,"doct2.html",context)
    else:
         return render(r,"login.html")
         

def viewprofile(r):
        name=r.GET['credential']
        sql='''select * from users where name=%s;'''
        p=(name,)
        print(name)
        cur.execute(sql,p)
        l=[]
        for i in cur.fetchall():
            for j in i:
                l.append(j)
        print(l[0],l[1],l[2],l[3],l[4],l[5],l[6])
        name1=l[0]
        mail=l[1]
        no=l[2]
        role=l[6]
        context={'name':name1,'mail':mail,'no':no,'role':role}
        return render(r,"home.html",context)