
from unicodedata import name
from django.shortcuts import render,HttpResponse
from .pat_info_insert import funct1
from .add_doctor import funct2
from .add_appoint import funct3
from .patient_login import login_patients
from .select_patients import selectpatients,getinfo
from .selectdoctors import selectdoctors
from .selectappointments import selectappointments,viewyourappnts
from .removedoctor import removedoct,rmvshft
from .removepatient import removepat
from .addshift import addshiftt
from .selectshifts import viewshiftt
from .appointsetup import setappoint,takeappoint
from .insertreport import report,displayrepnow
from .selectdate import selectdatee
from .selectreppat import selectreport

global pid
def homepage(request):
        return render (request,'base.html')
     
def register_patient(request):
  
   if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        sex=request.POST.get('gender')
        age=request.POST.get('age')
        pphn=request.POST.get('phone')
        paddress=request.POST.get('address')
        pemail=request.POST.get('email')
        funct1(first_name,last_name,sex,age,paddress,pemail,pphn)
       
        return render (request,'base.html')
   else:
        return render (request,'register.html')


def admin(request):
    if request.method=='POST':
        admin_name =request.POST.get('admin_name')
        admin_pwrd =request.POST.get('admin_password')

        if admin_name=='admin' and admin_pwrd=='ssss':
            return render (request,'admin_control.html')
        else:
            return render(request,'admin.html')
    else:
        return render (request,'admin.html')

def adddoc(request):
   
    if request.method=='POST':
        did=request.POST.get('did')
        ddep=request.POST.get('departments')
        d_fname=request.POST.get('dfirst_name')
        d_lname=request.POST.get('dlast_name')
        dexp=request.POST.get('dexp')
        dqual=request.POST.get('dqual')
        dsex=request.POST.get('dgender')
        daddress=request.POST.get('daddress')
        demail=request.POST.get('demail')
        dphn=request.POST.get('dphone')

        print(ddep)
        
        funct2(did,d_fname,d_lname,dsex,dexp,ddep,daddress,dqual,dphn,demail)
        return render (request,'admin_control.html')
       

def addappoint(request):
    
    if request.method=='POST':
        aid=request.POST.get('aid')
        adate=request.POST.get('adate')
   
        did=request.POST.get('did')
        funct3(aid,adate,did)
        return render (request,'admin_control.html')

def patient_login(request):
 
    if request.method=='POST':
            p_lastname=request.POST.get('last_name')
            global pid
            pid=request.POST.get('id')   

            f=login_patients(p_lastname,pid)
            if f!=False:
                dates=selectdatee(pid)
                context={'pname':f[0][1]+" "+f[0][2],'pid':f[0][0],'psex':f[0][3],'page':f[0][4],'paddress':f[0][5],'pemail':f[0][6],'pphn':f[0][7],'dates':dates}
                
                return render (request,'patientpage.html',context)
            else:
                 return render (request,'patient_login.html')
    else:
        return render (request,'patient_login.html')

        
def viewpatients(request):

     a=selectpatients()
     return render (request,'viewpatients.html',{'patient_info':a})

def viewdoctors(request):

     b=selectdoctors()
     return render (request,'viewdoctor.html',{'doctor_info':b})


def viewappointments(request):
   
     s=selectappointments()
     return render (request,'viewappointments.html',{'appointments':s})

def removedoctor(request):
    
    if request.method=='POST':
        rdid=request.POST.get('rdid')
        rd_lname=request.POST.get('rdlast_name')
        removedoct(rdid,rd_lname)
        
        return render (request,'admin_control.html')

def removepatient(request):
    s=False
    if request.method=='POST':
        rpid=request.POST.get('rpid')
        rp_lname=request.POST.get('rplast_name')
        removepat(rpid,rp_lname)
        s=True
        return render (request,'admin_control.html',{'d':s})

def addshift(request):
    try:
        if request.method=='POST':
            did=request.POST.get('didshift')
            shiftday=request.POST.get('shiftday')
            print(shiftday)
            fromtime=request.POST.get('fromtime')
            totime=request.POST.get('totime')
            addshiftt(did,shiftday,fromtime,totime)
        
            return render (request,'admin_control.html')
    except:
        return render (request,'errorpage.html')

def viewshift(request):
     b=viewshiftt()
     return render (request,'viewshifts.html',{'shifts':b})
       
def setapp(request):
     
     if request.method=='POST':
        dep=request.POST.get('departments')
        datee=request.POST.get('takeadate')
        b=setappoint(dep,datee)
        return render (request,'appointsetup.html',{'bb':b})

def takeapp(request):
    
    if request.method=='POST':
        aid=request.POST.get('aid')
        takeappoint(aid,pid)
        return render (request,'appointsetup.html')


def viewyourappoints(request):
    global pid

    appo=viewyourappnts(pid)
    return render (request,'viewyourapp.html',{'appontments':appo})

def removeshift(request):
    dctrid=request.POST.get('didshift')
    day=request.POST.get('shiftday')
    rmvshft(dctrid,day)
    return render (request,'viewyourapp.html')


  
def insertrep(request):
     if request.method=='POST':
        global rpid
        rpid=request.POST.get('rpid')
        global l
        l=getinfo(rpid)
        tests=displayrepnow(rpid)
        context={'pname':l[0][1]+" "+l[0][2],'phone':l[0][7],'pid':l[0][0],'tests':tests}
        return render (request,'insertreport.html',context)

  
def inserttest(request):
     if request.method=='POST':
        test=request.POST.get('test')
        value=request.POST.get('value')
        rpid=l[0][0]
        report(rpid,test,value)
        tests=displayrepnow(rpid)
        context={'pname':l[0][1]+" "+l[0][2],'phone':l[0][7],'pid':l[0][0],'tests':tests }
        return render (request,'insertreport.html',context)


def viewreport(request):
    if request.method=='POST':
        datte=request.POST.get('datee')
        l=getinfo(pid)
        r=selectreport(pid,datte)
        context={'pname':l[0][1]+" "+l[0][2],'phone':l[0][7],'pid':l[0][0],'psex':l[0][3],'page':l[0][4],'paddress':l[0][5],'pemail':l[0][6],'report':r,'datee':datte}
        return render (request,'viewreport.html',context)

def adviewreport(request):
    if request.method=='POST':
        global patid
        patid=request.POST.get('patid')
        l=getinfo(patid)
        dat=selectdatee(patid)
        context={'pname':l[0][1]+" "+l[0][2],'phone':l[0][7],'pid':l[0][0],'psex':l[0][3],'page':l[0][4],'paddress':l[0][5],'pemail':l[0][6],'dat':dat}
        return render (request,'adminviewreport.html',context)

    else:
        return render (request,'adminviewreport.html')

def viewreportadmin(request):
    print('helo')
    if request.method=='POST':
        print('hyy')
        daate=request.POST.get('datees')
        print('hyy')
        print(daate)
        print(patid)
        l=getinfo(patid)
        dat=selectdatee(patid)
        print(dat)
        r=selectreport(patid,daate)
        context={'pname':l[0][1]+" "+l[0][2],'phone':l[0][7],'pid':l[0][0],'psex':l[0][3],'page':l[0][4],'paddress':l[0][5],'pemail':l[0][6],'dat':dat,'rep':r,'date':daate}
        return render (request,'adminviewreport.html',context)