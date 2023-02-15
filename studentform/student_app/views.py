
import requests
from django.shortcuts import render
from django.http import HttpResponse
import pymongo


# Create your views here.
def index(requests):

    return render(requests,"student_app/form.html",{})
def details(requests):

    firstname = requests.GET["fname"]
    lastname = requests.GET["lname"]
    sex1 = requests.GET["membership"]
    date = requests.GET["birthday"]

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["testdatabase"]
    mycol = mydb["testcollection"]
    mydict = {"firstname": firstname, "lastname": lastname,"sex":sex1,"Date_of_birth":date}
    x = mycol.insert_one(mydict)
    text="details saved"
    return render(requests,"student_app/msg.html",{'text':text})

def display(requests):

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["user_detail_database"]
    mycol = mydb["user_detail_collection"]
    y = mycol.find({})
    list = []
    for data in y:
        print(data)
        # with open('studentapp/templates/studentapp/test.txt', 'w') as f:
        #     f.write(data)
        # text = "Text write on file"
        list.append(data)
        print(list)


    return render(requests, "student_app/msg.html", {'displaydata': list})

