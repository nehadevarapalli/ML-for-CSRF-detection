from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserRegistrationModel, UserSearchUrlModel, CSRFResponse
import json
import subprocess
import pandas as pd
from .UserMachineLearningAlgorithms import MLConcepts


# Create your views here.

def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UsersRegister.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UsersRegister.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
            # return render(request, 'user/userpage.html',{})
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})


def UserHome(request):
    return render(request, "users/UserHome.html", {})


def UserPreProcessForm(request):
    return render(request, "users/UserPreProcessForm.html", {})


def UserCSRFProcessByBolt(request):
    if request.method == "POST":
        urlname = request.POST.get("urlname")
        depth = request.POST.get("depth")
        UserSearchUrlModel.objects.create(urlname=urlname, depthfecth=depth)
        command = "python Bolt-master/bolt.py" + " -u " + urlname + " -l" + " " + depth
        print("path " + command)
        subprocess.call(command)
        f = open('./db/hashes.json', )
        data = json.load(f)
        # print("Data is ",len(data))
        mydict = {}
        for i in data:
            keys = i.keys();
            # print("fu=",keys['regex'])
            # print("fus",keys['matches'])
            for x in keys:
                regex = i['regex']
                matches = i['matches']
                CSRFResponse.objects.create(regex=regex, matches=matches, urlname=urlname)

    data = CSRFResponse.objects.filter(urlname=urlname)
    return render(request, "users/CSRFProcess.html", {"data": data})


def UserMitchProcess(request):
    f = open('./media/dataset/dataset.json', )
    data = json.load(f)
    mydict = {}
    for i in data:
        keys = i.keys()
        data = i['data']
        website = i['website']
        i = 0
        for x in data:
            #print("X value = ",x)
            i = i+1
            mydict.update({i:x})
        #mydict.update({data: website})
        #for x,y in keys.items():
            #data = keys.get('data')
            #website = i['website']
            #print(y)

            #print(data,"<==>",website)

    return render(request, "users/MitchProcessone.html", {"data": mydict})

def UserMachineLearning(request):
    df = pd.read_csv('./media/dataset/features_matrix.csv', sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, dialect=None, error_bad_lines=True, warn_bad_lines=True, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None)
    obj = MLConcepts()
    post_dict = obj.startPOSTProcess(df)
    get_dict = obj.startGETProcess(df)
    option_dict = obj.startOPTIONProcess(df)
    return render(request,"users/UserMachineLearning.html",{'post_dict':post_dict,'get_dict':get_dict,"option_dict":option_dict})
