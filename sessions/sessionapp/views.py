from django.shortcuts import render

# Create your views here.



def setsession(request):
    request.session['name']='somesh'
    request.session['lname']='sharma'
    request.session['address']='dhar'
    request.session['contact']='8818808249'
    return render(request,'setsession.html')


def getsession(request):
    sname=request.session.get('name',default='guest')
    slname=request.session.get('lname',default='guest')
    saddress=request.session.get('address',default='guest')
    scontact=request.session.get('contact',default='guest')
    cookie_age=request.session.get_session_cookie_age()
    expiry_age=request.session.get_expiry_age()
    expiry_date=request.session.get_expiry_date()
    expiry_browser_close=request.session.get_expire_at_browser_close()
    request.session.set_expiry(6)
    return render(request,'getsession.html',{'sname':sname,'slname':slname,'saddress':saddress,'scontact':scontact,'cookie_age':cookie_age,'expiry_age':expiry_age,'expiry_date':expiry_date,'expiry_browrse':expiry_browser_close})

def deletesession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'deletesessions.html')


# to set test cookie

def settestcookie(request):
    res=request.session.set_test_cookie()
    print(res)
    return render(request,'testcookie/testset.html',{'res':res})

def testcookieworked(request):
    res=request.session.test_cookie_worked()
    print(res)
    return render(request,'testcookie/testworked.html',{'res':res})

def deletetestcookie(request):
    request.session.delete_test_cookie()
    request.session.flush()
    request.session.clear_expired()
    return render(request,'testcookie/deletetest.html')