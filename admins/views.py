from django.shortcuts import render,HttpResponse
from django.contrib import messages
from users.models import UserRegistrationModel,CSRFResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pandas as pd
# Create your views here.
def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'admins/AdminHome.html')
        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'AdminLogin.html', {})

def AdminHome(request):
    return render(request, 'admins/AdminHome.html')

def AdminViewUsers(request):
    data = UserRegistrationModel.objects.all()
    return render(request, 'admins/RegisteredUsers.html', {'data': data})

def AdminActivaUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        UserRegistrationModel.objects.filter(id=id).update(status=status)
        data = UserRegistrationModel.objects.all()
        return render(request,'admins/RegisteredUsers.html',{'data':data})


def adminviewallcsrfs(request):
    data_list = CSRFResponse.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(data_list, 60)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'admins/viewAllCSRFS.html', {'users': users})

def PostRequestdata(request):
    df = pd.read_csv('./media/dataset/features_matrix.csv', sep=',', delimiter=None, header='infer', names=None,
                     index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None,
                     engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False,
                     skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True,
                     verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False,
                     keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False,
                     chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None,
                     quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None,
                     dialect=None, error_bad_lines=True, warn_bad_lines=True, delim_whitespace=False, low_memory=True,
                     memory_map=False, float_precision=None)
    data = df[['numOfParams', 'numOfBools', 'numOfIds', 'numOfBlobs', 'reqLen', 'isPOST']]
    data = data.to_html()
    #print(data)

    return render(request, "admins/PostviewData.html",{"data":data})

def GetRequestdata(request):
    df = pd.read_csv('./media/dataset/features_matrix.csv', sep=',', delimiter=None, header='infer', names=None,
                     index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None,
                     engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False,
                     skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True,
                     verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False,
                     keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False,
                     chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None,
                     quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None,
                     dialect=None, error_bad_lines=True, warn_bad_lines=True, delim_whitespace=False, low_memory=True,
                     memory_map=False, float_precision=None)
    data = df[['numOfParams', 'numOfBools', 'numOfIds', 'numOfBlobs', 'reqLen', 'isGET']]
    data = data.to_html()

    return render(request, "admins/GetviewData.html", {"data": data})
