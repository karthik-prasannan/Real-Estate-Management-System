from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import logout
# Create your views here.

def index(request):
    return render(request,'0.index.html')

def realestate_register(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        a=admin_reg(email=email,password=password)
        a.save()
        return HttpResponse('Registered successfully')
    return render(request,'1.register.html')

def admin_login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        a = admin_reg.objects.all()
        for i in a:
            if i.email==email and i.password==password:
                request.session['id1']=i.id
                return redirect(admin_disp)
        else:
            return HttpResponse('invalid Username or Password')
    return render(request,'2.admin_login.html')

def property_upload(request):
    if request.method=='POST':
        image1=request.FILES.get('profile')
        property_name1=request.POST.get('name')
        address1=request.POST.get('address')
        location1=request.POST.get('location')
        features1=request.POST.get('features')
        a=property(image=image1,property_name=property_name1,address=address1,location=location1,features=features1)
        a.save()
        return HttpResponse('Uploaded successfully')
    return render(request,'3.property_upload.html')

def property_disp(request):
    id=[]
    img=[]
    name=[]
    address=[]
    location=[]
    features=[]
    a=property.objects.all()
    for i in a:
        id1=i.id
        id.append(id1)
        img1=str(i.image).split('/')[-1]
        img.append(img1)
        name1=i.property_name
        name.append(name1)
        address1=i.address
        address.append(address1)
        location1=i.location
        location.append(location1)
        features1=i.features
        features.append(features1)
    mylist=zip(id,img,name,address,location,features)
    return render(request,'4.property_display.html',{'data':mylist})

def room_upload(request,id):
    b=property.objects.get(id=id)
    if request.method=='POST':
        image=request.FILES.get('rimage')
        type=request.POST.get('type')
        roomno=request.POST.get('roomno')
        cost=request.POST.get('cost')
        features=request.POST.get('features')
        property_name=request.POST.get('property_name')
        a=rooms(img=image,type=type,room_no=roomno,cost=cost,features=features,property_name=property_name)
        a.save()
        return HttpResponse('Successfully added')
    return render(request,'5.room_upload.html',{'user':b})


def room_disp(request,id):
    bb=property.objects.get(id=id)
    id=[]
    img=[]
    type=[]
    roomno=[]
    cost=[]
    features=[]
    property_name=[]
    a=rooms.objects.all()
    for i in a:
        id1=i.id
        id.append(id1)
        img1=str(i.img).split('/')[-1]
        img.append(img1)
        type1=i.type
        type.append(type1)
        roomno1=i.room_no
        roomno.append(roomno1)
        cost1=i.cost
        cost.append(cost1)
        features1=i.features
        features.append(features1)
        property_name1=i.property_name
        property_name.append(property_name1)
    mylist=zip(id,img,type,roomno,cost,features,property_name)
    return render(request,'6.room_display.html',{'data':mylist,'user':bb})

def tenent_register(request):
    if request.method=='POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        type = request.POST.get('type')
        image = request.FILES.get('image')
        password = request.POST.get('password')
        a=tenent_profile(name=name,address=address,email=email,type=type,proof=image,password=password)
        a.save()
        return redirect(tenent_login)
    return render(request,'7.tenent_registration.html')

def tenent_disp(request):
    id4=request.session['id2']
    a=tenent_profile.objects.get(id=id4)
    img=str(a.proof).split('/')[-1]
    return render(request,'8.tenent_display.html',{'data':a,'img1':img})

def tenent_login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        a = tenent_profile.objects.all()
        for i in a:
            if i.email==email and i.password==password:
                request.session['id2']=i.id
                return redirect(customer_disp)
        else:
            return HttpResponse('invalid Username or Password')
    return render(request,'9.tenent_login.html')


def customer_disp(request):
    id1=request.session['id2']
    bb=tenent_profile.objects.get(id=id1)
    id = []
    img = []
    name = []
    address = []
    location = []
    features = []
    a = property.objects.all()
    for i in a:
        id1 = i.id
        id.append(id1)
        img1 = str(i.image).split('/')[-1]
        img.append(img1)
        name1 = i.property_name
        name.append(name1)
        address1 = i.address
        address.append(address1)
        location1 = i.location
        location.append(location1)
        features1 = i.features
        features.append(features1)
    mylist = zip(id, img, name, address, location, features)
    return render(request,'10.customer_display.html',{'data':bb,'type':mylist})

def customer_logout(request):
    logout(request)
    return redirect(tenent_login)

def booking_reg(request,id):
    b=rooms.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        property_name=request.POST.get('property_name')
        property_type=request.POST.get('type')
        room_no=request.POST.get('room_no')
        date_of_arrival=request.POST.get('date_of_arrival')
        if booking.objects.filter(date_of_arrival=date_of_arrival).exists():
            return HttpResponse('Already Booked')
        a=booking(name=name,email=email,address=address,phone=phone,property_name=property_name,property_type=property_type,room_no=room_no,date_of_arrival=date_of_arrival)
        a.save()
        return HttpResponse('BOOKED')
    return render(request,'11.booking_registration.html',{'user':b})

def admin_disp(request):
    a=booking.objects.all()

    return render(request,'12.admin_disp.html',{'data':a})

def prop_disp(request):
    id=[]
    img=[]
    name=[]
    address=[]
    location=[]
    features=[]
    a=property.objects.all()
    for i in a:
        id1=i.id
        id.append(id1)
        img1=str(i.image).split('/')[-1]
        img.append(img1)
        name1=i.property_name
        name.append(name1)
        address1=i.address
        address.append(address1)
        location1=i.location
        location.append(location1)
        features1=i.features
        features.append(features1)
    mylist=zip(id,img,name,address,location,features)
    return render(request,'13.property_display2.html',{'data':mylist})

def admin_room_disp(request):
    id=[]
    img=[]
    type=[]
    roomno=[]
    cost=[]
    features=[]
    a=rooms.objects.all()
    for i in a:
        id1=i.id
        id.append(id1)
        img1=str(i.img).split('/')[-1]
        img.append(img1)
        type1=i.type
        type.append(type1)
        roomno1=i.room_no
        roomno.append(roomno1)
        cost1=i.cost
        cost.append(cost1)
        features1=i.features
        features.append(features1)
    mylist=zip(id,img,type,roomno,cost,features)
    return render(request,'14.room_disp2.html',{'data':mylist})

def tenent_edit(request,id):
    bb=tenent_profile.objects.get(id=id)
    img=str(bb.proof).split('/')[-1]
    if request.method=='POST':
        bb.name = request.POST.get('name')
        bb.address = request.POST.get('address')
        bb.email = request.POST.get('email')
        bb.type = request.POST.get('type')
        if request.FILES.get('image')==None:
            bb.save()
        else:
            bb.proof = request.FILES['image']
        bb.save()
        return redirect(customer_disp)
    return render(request,'15.edit.html',{'img1':img,'data':bb})