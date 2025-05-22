from django.shortcuts import render
from django.http import HttpResponse
from.models import *
# Create your views here.


def products(request):
    return HttpResponse('Products_page')

def customer(request):
    return HttpResponse('Customer_page')

def mengheng(request):
    return HttpResponse('Mengheng')

def ViewIndex(request, CustomerID):    
    DTOCustomerByID = Customer.objects.get(id=CustomerID) 
    DTOCustomer = Customer.objects.all()
    UseExclude = Customer.objects.exclude(id=4)
    UseOrderBy = Customer.objects.order_by('id')
    UseOrderByDesc = Customer.objects.order_by('-id')
    UseFirst = Customer.objects.first()
    UseLast = Customer.objects.last()
    UseCount = Customer.objects.count()
    UseExists = Customer.objects.filter(id=6).exists
    UseGet =  Customer.objects.get(id=3)
    UseFilter = Customer.objects.filter(id=4)

    context = {
        'DTOCustomers' : DTOCustomer,
        'UseExcludes' : UseExclude,
        'UseOrderBys' : UseOrderBy,
        'UseOrderByDescs' : UseOrderByDesc,
        'UseFirsts' : UseFirst,
        'UseLasts' : UseLast,
        'UseCounts' : UseCount,
        'UseExistss' : UseExists,
        'UseGets' : UseGet,
        'UseFilters' : UseFilter,
        'DTOCustomerByIDs' : DTOCustomerByID,
    }

    return render(request, 'accounts/selectdata.html', context)


def home(request):
    return render(request, 'accounts/test.html')

def index(request):

    DTOImageBanner = Image.objects.filter(ImageTypeID = 1)
    DTOImageLogo = Image.objects.filter(ImageTypeID =2 )
    DTOImageSlideShow = Image.objects.filter(ImageTypeID = 3)
    DTOSidebarLeft = Image.objects.filter(ImageTypeID = 4)
    DTOSIdebarRight = Image.objects.filter(ImageTypeID = 6)
    DTOFooter = Image.objects.filter(ImageTypeID = 7)

    DTOMenu= Menu.objects.all()


    context = {
        'DTOImageBanners' : DTOImageBanner,
        'DTOImageLogos' : DTOImageLogo,
        'DTOImageSlideShows' : DTOImageSlideShow,
        'DTOSidebarLefts' : DTOSidebarLeft,
        'DTOSIdebarRights' : DTOSIdebarRight,
        'DTOFooters' : DTOFooter,

        'DTOMenus': DTOMenu,
    }

    return render(request, 'accounts/index.html', context)

def Aboutus(request):
    return render(request, 'accounts/AboutUs.html')


def MenuDetailMethod(request, pk):

    DTOMenuDetail = MenuDetail.objects.filter(MenuID=pk)
    DTOImageBanner = Image.objects.filter(ImageTypeID = 1)
    DTOImageLogo = Image.objects.filter(ImageTypeID =2 )
    DTOImageSlideShow = Image.objects.filter(ImageTypeID = 3)
    DTOSidebarLeft = Image.objects.filter(ImageTypeID = 4)
    DTOSIdebarRight = Image.objects.filter(ImageTypeID = 6)
    DTOFooter = Image.objects.filter(ImageTypeID = 7)
    DTOMenu= Menu.objects.all()

    context = {
        'DTOMenuDetails' : DTOMenuDetail,
        'DTOImageBanners' : DTOImageBanner,
        'DTOImageLogos' : DTOImageLogo,
        'DTOImageSlideShows' : DTOImageSlideShow,
        'DTOSidebarLefts' : DTOSidebarLeft,
        'DTOSIdebarRights' : DTOSIdebarRight,
        'DTOFooters' : DTOFooter,
        'DTOMenus': DTOMenu,
    }
    return render(request, 'accounts/MenuDetail.html', context)


def ogani(request):
    return render(request, 'ogani/index.html')

def shopdetails(request):
    return render(request, 'ogani/shop-details.html')

def shopingCart(request):
    return render(request, 'ogani/shoping-cart.html')

def checkout(request):
    return render(request, 'ogani/checkout.html')

def shopgrid(request):
    return render(request, 'ogani/shop-grid.html')

def Blog(request):
    return render(request, 'ogani/blog.html')

def BlogDetails(request):
    return render(request, 'ogani/blog-details.html')