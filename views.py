from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse
from myapp.models import Member
from myapp.models import Profile
from myapp.models import User
from myapp.models import Offer
from myapp.models import Story
from myapp.models import Exp
import os

#startpage register
def index(request):
	return render(request,'project.html')

def register(request):
    user = User(
        email=request.POST.get('email'),
        password=request.POST.get('password'),
    )
    user.save()
    return redirect('login')

def read2(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, "userlogin.html", context)

def delete2(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return render(request,'userlogin.html')

def admind(request):
    return render(request,'admin.html')

def admindash(request):
    m2=Member.objects.exclude(firstname='').count()
    m1=Member.objects.filter(age__gte=20, age__lte=26).count()
    m3=Member.objects.filter(gender='female').count()
    m4=Member.objects.filter(gender='male').count()
    m6 = Member.objects.filter(education__in=['BE', 'B.Sc', 'B.Com', 'M.Sc', 'B.Tech', 'Ph.D', 'BBA', 'BCA', 'MCA', 'LLB', 'MBBS', 'MBA', 'BA','MA','M.Com','ME','M.Tech']).count()
    m5=Member.objects.filter(age__gte=25, age__lte=41).count()
    m8=Member.objects.filter(education__in=['BE','B.Tech','M.Tech','ME']).count()
    m9=Member.objects.filter(salary__gte=39000).count()
    m7=Member.objects.filter(education__in=['BA','B.Sc','BBA','BCA','MCA','B.Com','M.Com','MA','M.Sc','MBA']).count()
    return render(request,'admindash.html',{'m1':m1, 'm2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'m7':m7,'m8':m8,'m9':m9})

# def membercount(request):
#     members=Member.objects.filter(firstname='naveen', status=0).count()
#     context={'members':members}
#     return render(request,'admindash.html',context)

def adminuser(request):
    member = Member.objects.all()
    context = {
        'member' :member
    }
    return render(request,'adminusers.html',context)

def about(request):
    return render(request,'about.html')

def admindata(request):
    member = Member.objects.all()
    context = {
        'member':member
    }
    return render(request,'admindatas.html',context)

def login (request):
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     if email and password:
    #         if User.objects.filter(email=email, password=password).exists():
    #             user = User.objects.get(email=email, password=password)
    #             return render(request, 'profile.html', {'user': user})
    #         else:
    #             context = {'msg': 'Invalid email or password'}
    #             return render(request, 'userlogin.html', context)
    #     else:
    #         context = {'msg': 'Please enter both email and password'}
    #         return render(request, 'userlogin.html', context)
    return render(request,'userlogin.html')

def profile2(request):
    return render(request,'profile2.html')

def profilematch(request):
    member = Member.objects.all()
    context = {
        'member':member
    }
    return render(request,'profiledata.html',context)

def profiledata1(request):
    member = Member.objects.all()
    context = {
        'member':member
    }
    return render(request,'profiledata1.html',context)

def membership(request):
    return render(request,'membership.html')

def offer(request):
    return render(request,'memberoffer.html')

def moneyback(request):
    return render(request,'moneyback.html')

def payment(request):
    return render(request,'payment.html')

def adminprofit(request):
    return render(request,'adminprofit.html')

def admindmail(request,id):
    member = Member.objects.get(id=id)
    context={'member':member}
    return render(request,'admindashmail.html',context)

def adminuserdays(request,id):
    member = get_object_or_404(Member, id=id)
    context = {'member': member}
    return render(request, 'adminuserdays.html', context)

#sessions
def home(request):
    member=Member.objects.all()
    request.session['a'] =request.POST.get('email')
    context={'member':member}
    return render(request,'profile.html',context)
   
#profile full register
def create(request):
    if request.method == "POST":
        member = Member(
            firstname=request.POST.get('firstname'),
            lastname=request.POST.get('lastname'),
            age=request.POST.get('age'),
            date=request.POST.get('date'),
            gender=request.POST.get('gender'),
            mobile=request.POST.get('mobile'),
            email=request.POST.get('email'),
            star=request.POST.get('star'),
            rassi=request.POST.get('rassi'),
            fathername=request.POST.get('fathername'),
            mothername=request.POST.get('mothername'),
            fathercontact=request.POST.get('fathercontact'),
            religion=request.POST.get('religion'),
            caste=request.POST.get('caste'),
            lang=request.POST.get('lang'),
            education=request.POST.get('education'),
            profession=request.POST.get('profession'),
            country=request.POST.get('country'),
            state=request.POST.get('state'),
            pincode=request.POST.get('pincode'),
            address1=request.POST.get('address1'),
            address2=request.POST.get('address2'),
            height=request.POST.get('height'),
            weight=request.POST.get('weight'),
            hobby=request.POST.get('hobby'),
            salary=request.POST.get('salary'),
            family=request.POST.get('family'),
            work=request.POST.get('work'),
        )
        
        # Handle image upload
        if 'image' in request.FILES:
            member.image = request.FILES['image']
        
        member.save() 
        return redirect('read')
    context ={'member':member}
    return render(request, "profile2.html",context)

def read(request):
    email=request.session['a']
    member =Member.objects.raw('select * from myapp_member where email =%s',[email])
    context = {'member': member,'email':email}
    return render(request, "profile2.html", context)

def edit(request, id):
    member = Member.objects.get(id=id)
    context = {'member': member}
    return render(request, 'editprofile.html', context)
 
def update(request, id):
    member = Member.objects.get(id=id)   
    if request.method == "POST":
        member.firstname = request.POST.get('firstname')
        member.lastname = request.POST.get('lastname')
        member.age = request.POST.get('age')
        member.date = request.POST.get('date')
        member.gender = request.POST.get('gender')
        member.mobile = request.POST.get('mobile')
        member.email = request.POST.get('email')
        member.star = request.POST.get('star')
        member.rassi = request.POST.get('rassi')
        member.fathername = request.POST.get('fathername')
        member.mothername = request.POST.get('mothername')
        member.fathercontact = request.POST.get('fathercontact')
        member.religion = request.POST.get('religion')
        member.caste = request.POST.get('caste')
        member.lang = request.POST.get('lang')
        member.education = request.POST.get('education')
        member.profession = request.POST.get('profession')
        member.country = request.POST.get('country')
        member.state = request.POST.get('state')
        member.pincode = request.POST.get('pincode')
        member.address1 = request.POST.get('address1')
        member.address2 = request.POST.get('address2')
        member.height = request.POST.get('height')
        member.weight = request.POST.get('weight')
        member.hobby = request.POST.get('hobby')
        member.salary = request.POST.get('salary')
        member.family = request.POST.get('family')
        member.work = request.POST.get('work')

        if 'image' in request.FILES:
            member.image = request.FILES['image']

        member.save()
        return redirect('read')

def delete(request, id):
    member =Member.objects.get(id=id)
    member.delete()
    return redirect('/')

#offers admin side 
def adminoffer(request):
    return render(request,'adminoffer.html')

def createoff(request):
    offer = Offer(
        name=request.POST.get('name'),
        validation=request.POST.get('validation'),
        amount=request.POST.get('amount'),
        requests=request.POST.get('requests')
    )
    offer.save()
    return redirect('adminoffer')

def readoff(request):
    offer = Offer.objects.all()
    context = {'offer': offer}
    return render(request, "adminoffer.html", context)

def deleteoff(request, id):
    offer = Offer.objects.get(id=id)
    offer.delete()
    return redirect('/')

#successstory
def successstory(request):
    images = Story.objects.all()
    context = {'images': images}
    return render(request, 'sucessstory.html', context)

def createnew(request):
    if request.method == "POST":
        images = Story()
        images.bridename = request.POST.get('bridename')
        images.date = request.POST.get('date')
        images.description = request.POST.get('description')

        if len(request.FILES) != 0:
            images.image = request.FILES['image']
            
        images.save()
        return redirect('successstory')
    return render(request, "adminstory.html")

def adminstory(request):
    images=Story.objects.all()
    context={'images':images}
    return render(request,'adminstory.html',context)

def storyedit(request, edit_id):
    images = get_object_or_404(Story, id=edit_id)  
    if request.method == 'POST':
        images.bridename = request.POST.get('bridename')
        images.date = request.POST.get('date')
        images.description = request.POST.get('description')

        if len(request.FILES) != 0:
            if images.image:  
                if os.path.isfile(images.image.path):
                    os.remove(images.image.path)  
            images.image = request.FILES['image']
        
        images.save()
        return redirect('adminstory')
    
    context = {'images': images}
    return render(request, "adminstory.html", context)

def remove(request, id):
    images = Story.objects.get(id=id)
    if images.image:  
        if os.path.isfile(images.image.path):
            os.remove(images.image.path)
    images.delete()
    return redirect('adminstory')

# expense

def adminexpense(request):
    return render(request,'adminexpense.html')

def createexp(request):
    expense = Exp(
        name=request.POST.get('name'),
        type=request.POST.get('type'),
        amount=request.POST.get('amount'),
        cashtype=request.POST.get('cashtype'),
        remarks=request.POST.get('remarks')
    )
    expense.save()
    return redirect('displayexp')

def displayexp(request):
    expense = Exp.objects.all()
    context = {'expense': expense}
    return render(request, "adminexpense.html", context)

def deleteexp(request, id):
    expense = Exp.objects.get(id=id)
    expense.delete()
    return redirect('/')

#mail

def send_admin_mail(request, id):
    if request.method == "POST":
        email = request.POST.get("email")
        textbox = request.POST.get("textbox")
        
        htmlgen = f'<p>Thank you for registering your profile on our website. <strong>{textbox}</strong></p>'
        
        send_mail(
            subject='Profile Registration Confirmation',  
            message=textbox,  
            from_email='matrimonyf4y@gmail.com',  
            recipient_list=[email],  
            fail_silently=False,
            html_message=htmlgen  
        )
        
        # Return a response confirming the email was sent
        return HttpResponse(f"Email sent to {email} with message: {textbox}")
    
    # Render the template for GET request
    return render(request, 'admindashmail.html')

def displaydata(request,id):
    member = get_object_or_404(Member, id=id)
    context = {'member': member}
    return render(request, 'userdata.html', context)

def toggle_status(request, id):
    member = Member.objects.get(id=id)
    if member.status == 1:
        member.status = 0  
    else:
        member.status = 1  
    member.save()
    return redirect('adminuser')

def toggle_block(request,id):
    if request.method == 'POST':
        try:
            member = Member.objects.get(id=id)
            member.status = 3  # 3 for blocked
            member.save()
            return redirect(f'/displaydata/{id}')
        except Member.DoesNotExist:
            return HttpResponse("Member not found", status=404)

def toggle_unblock(request, id):
    if request.method == 'POST':
        try:
            member = Member.objects.get(id=id)
            member.status = 4  # 4 for unblocked
            member.save()
            return redirect(f'/displaydata/{id}')
        except Member.DoesNotExist:
            return HttpResponse("Member not found", status=404)

# def toggle_block(request, id):
#     if request.method == 'POST':
#         if id in block_status_dict:
#             del block_status_dict[id]  # Unblock the member
#             status = 4  # Unblocked
#         else:
#             block_status_dict[id] = True  # Block the member
#             status = 3  # Blocked
        
#         return JsonResponse({'block_status': status})
