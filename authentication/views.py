from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Contact,Stocks,registation
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail 
from django.http import HttpResponse
import xlwt
# from django.
@login_required     
def home(request):
    if not is_login(request):
        return redirect('/login')
    return render(request,"login.html")

def index(request):
    return render(request,"index.html")

def about(request):
    if not is_login(request):
        return redirect('/login')
    return render(request,"about.html")

def forget_password(request):
    if request.method == "POST":
        username=request.POST.get('username')
        question=request.POST.get('question')
        answer=request.POST.get('answer')
        password1=request.POST.get('password1')
        registation.objects.filter(username=username,question=question,answer=answer).update(password1=password1)
        return redirect('login')
    else:
        return render(request,"forget_password.html")

def change_password(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        npass=request.POST.get('password1')
        registation.objects.filter(username=username,password1=password).update(password1=npass)
        return redirect('login')
    else:
        return render(request,"change_password.html")

def add_product(request):
    return render(request,"admin/add_product.html",{})

def contact(request):
    if not is_login(request):
        return redirect('/login')
    return render(request,"contact.html",{})

def pencil(request):
    if not is_login(request):
        return redirect('/login')
    pencil=Stocks.objects.filter(p_category='Pencil')
    return render(request,"pencil.html",{'pencil':pencil})
# def cart(request):
#      if not is_login(request):
#         return redirect('/login')
#     pencil=Stocks.objects.all()
#     return render(request,"cart.html",{'cart':cart})
def pen(request):
    if not is_login(request):
        return redirect('/login')
    pen=Stocks.objects.filter(p_category='Pen')
    return render(request,"pen.html",{'pen':pen})

def colour(request):
    if not is_login(request):
        return redirect('/login')
    colour=Stocks.objects.filter(p_category='Colour')
    return render(request,"colour.html",{'colour':colour})

def Drawing(request):
    if not is_login(request):
        return redirect('/login')
    Drawing=Stocks.objects.filter(p_category='Drawing')
    return render(request,"drawing.html",{'Drawing':Drawing})

def a_contact(request):
    if not a_is_login(request):
        return redirect('/a_login')
    con=Contact.objects.all()
    return render(request,"admin/a_contact.html",{'con':con})

def available_stock(request):
    stock=Stocks.objects.all()
    return render(request,"admin/available_stock.html",{'stock':stock})


def a_purchase(request):
    if not a_is_login(request):
        return redirect('/a_login')
    return render(request,"admin/a_purchase.html")

def a_sales(request):
    if not a_is_login(request):
        return redirect('/a_login')
    if request.method == "POST":
        p_category=request.POST.get('p_category')
        p_company=request.POST.get('p_company')
        st=Stocks.objects.get(p_category=p_category,p_company=p_company)
        stock=request.POST.get('stock')
        newstock=int(st.stock)-int(stock)
        a=Stocks.objects.filter(p_category=p_category,p_company=p_company).update(stock=newstock)
        try:
            subject="Sales Entry for Stationary Stock Management."
            message="Sales Entry in Stationary Stock Management. Product Category "+ p_category +" Product Company "+ p_company +" Number of Stock Sales "+ stock 
            from_mail=settings.EMAIL_HOST_USER
            to_list=[a.email]
            s=send_mail(subject,message,from_mail,to_list)
        except Exception as e:
            print(e)
    return render(request,"admin/a_sales.html")

def purchase(request):
    if request.method == "POST":
        p_category=request.POST.get('p_category')
        p_company=request.POST.get('p_company')
        st=Stocks.objects.get(p_category=p_category,p_company=p_company)
        stock=request.POST.get('stock')
        newstock=int(stock)+int(st.stock)
        a=Stocks.objects.filter(p_category=p_category,p_company=p_company).update(stock=newstock)
        try:
            subject="Purchase Entry for Stationary Stock Management."
            message="Purchase Entry in Stationary Stock Management. Product Category "+ p_category +" Product Company "+ p_company +" Number of Stock Purchase "+ stock 
            from_mail=settings.EMAIL_HOST_USER
            to_list=[a.email]
            s=send_mail(subject,message,from_mail,to_list)
        except Exception as e:
            print(e)
    return render(request,"admin/a_purchase.html")
def d_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['p_name', 'p_company', 'p_category', 'Stock', 'Price', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    #remening Rows
    font_style = xlwt.XFStyle()
    rows = Stocks.objects.all().values_list('p_name', 'p_company', 'p_category', 'stock', 'price')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,row[col_num],font_style)
    wb.save(response)
    return response
def login_a(request):
    return render(request, 'admin/a_login.html')
# def add_to_cart(request,p_id):
#         if request.user.is_authenticated():
#             try:
#                 p = Stocks.objects.get(pk=p_id)
#             except ObjectDoesNotExist:
#                 pass
#             else :
#                 try:
#                     cart = Cart.objects.get(user = request.user, active = True)
#                 except ObjectDoesNotExist:
#                     cart = Cart.objects.create(user = request.user)
#                     cart.save()
#                     cart.add_to_cart(p_id)
#                     return redirect('cart')
#                 else:
#                     return redirect('index')
# email1=""
# password2=""
# def a_login(request):
#     if request.method == 'POST':
#         email1=request.POST.get('email1')
#         password2=request.POST.get('password')
#         try:
#             login_obj=a_login.objects.get(email=email1,password=password2)
#             request.session['email'] = email1
#             return redirect('/available_stock')    
#         except:
#             return render(request, 'admin/a_login.html')   
#     else:
#         return render(request,'admin/a_login.html')

def single(request):
    return render(request,"single.html")
   
username=""
password1=""
def u_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        try:
            if username=="admin" and password1=="admin":
                request.session['email'] = username
                return render(request,"admin/available_stock.html")
            login_obj=registation.objects.get(username=username,password1=password1)
            request.session['username'] = username
            return render(request, 'index.html')  
            
        except:
            return render(request, 'login.html')   
    else:
        return render(request,'login.html')

# email=""
# password=""
# def a_login(request):
#     if request.method == 'POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         try:
#             login_obj=a_registation.objects.get(username=username,password=password)
#             request.session['username'] = username
#             return render(request, 'available_stock.html')  
            
#         except:
#             return render(request, 'a_login.html')   
#     else:
#         return render(request,'a_login.html')


    #     username = request.POST['username']
    #     password = request.POST['password']

    #     user = auth.authenticate(username=username, password=password)
    #     if user is not None:
    #         if user.is_superuser: 
    #             auth.login(request, user)
    #             return redirect('/a_contact')
    #         else:
    #             return redirect('/index')
    #     else:
    #         messages.info(request, 'Invalid Username Or/And Password')
    #         return redirect('/login')
    # else:
    #     return render(request, 'login.html') 
def is_login(request):
    if 'username' in request.session:
        return True
    return False
def a_is_login(request):
    if 'email' in request.session:
        return True
    return False
def registations(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        init=registation(first_name=first_name,last_name=last_name,username=username,email=email,password1=password1,question=question,answer=answer)
        init.save()
        try:
            subject="Conform Mail for Stationary Stock Management."
            message="Thanks for Register in Stationary Stock Management. Your Username is "+ username +" and password is "+ password1 
            from_mail=settings.EMAIL_HOST_USER
            to_list=[init.email]
            s=send_mail(subject,message,from_mail,to_list)
        except Exception as e:
            print(e)
        return redirect('/login')
        # if password1 == password2:
        #     if User.objects.filter(username=username).exists():
        #        messages.info(request, 'The username is Taken') 
        #        return redirect('/register')
        #     elif User.objects.filter(email=email).exists():
        #         messages.info(request, 'The Email is Taken')
        #         return redirect('/register') 
        #     else:
        #         user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        #         user.save()
        #         return redirect('/login')
        # else:
        #     messages.info(request, 'Password Is Not Maching..!') 
        #     return redirect('/register')

    else:
        return render(request, 'register.html') 


def logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('login')
def a_logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect('login')
def insertdata(request):
    if  request.method == 'POST':
        c_name=request.POST.get('Name')
        c_email=request.POST.get('Email')
        c_phoneno=request.POST.get('Telephone')
        c_subject=request.POST.get('Subject')
        c_massage=request.POST.get('Message')
        inst=Contact(c_name=c_name,c_email=c_email,c_phoneno=c_phoneno,c_subject=c_subject,c_massage=c_massage)
        inst.save()
        return redirect('contact')

def del_contact(request):
    if request.method == 'GET':
        pk=request.GET.get('pk')   
        Contact.objects.filter(c_id=pk).delete()
        return redirect('a_contact')
    else:
        print("Error")

def services(request):
    return redirect('services')

def a_stock(request):
    if not a_is_login(request):
        return redirect('/a_login')
    if request.method=='POST':
        fs=FileSystemStorage()
        p_name=request.POST.get('p_name')
        p_category=request.POST.get('p_category')
        p_company=request.POST.get('p_company')
        pa_img=request.FILES['p_img']
        fs.save(pa_img.name,pa_img)
        stock=request.POST.get('stock')
        price=request.POST.get('price')
        m=Stocks(p_name=p_name,p_category=p_category,p_company=p_company,p_img=pa_img,stock=stock,price=price)
        m.save()
        return redirect('add_product')
def cart(request):
    if not a_is_login(request):
        return redirect('/a_login')
    if request.method=='POST':
        fs=FileSystemStorage()
        p_name=request.POST.get('p_name')
        p_category=request.POST.get('p_category')
        p_company=request.POST.get('p_company')
        pa_img=request.FILES['p_img']
        fs.save(pa_img.name,pa_img)
        stock=request.POST.get('stock')
        price=request.POST.get('price')
        m=Cart(p_name=p_name,p_category=p_category,p_company=p_company,p_img=pa_img,stock=stock,price=price)
        m.save()
        return redirect('cart')
    # else:
    #     print("error")
#hve kr insert