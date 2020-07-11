from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from work.models import Lost,Found
from django.core.mail import send_mail
# Create your views here.

def work_view(request):
    return render(request, 'work/random.html')


def lost_view(request):
    if not request.user.is_authenticated:
        return render(request, 'loginredirect.html')
    if request.method=='POST':
        name=request.POST['name']
        uid=request.POST['uid']
        card=request.POST['cardtype']
        email=request.POST['email']
        details=request.POST['details']
        lostcard=Lost(name=name,uid=uid,card=card,email=email,details=details)
        lostcard.save()
        found =Found.objects.filter(uid__gt=1).values('uid')
        flag=False
        ls=Lost.objects.filter(uid__gt=1).values('uid')
        if(len(ls)>0):
            temp=ls[len(ls)-1]['uid']
            print("current lost card inserted ",temp)
            for item in found:
                if item['uid']==temp:
                    print("SOMEBODY found the card in, in lost view")
                    flag=True
                   
                    lostquery=Lost.objects.filter(uid__exact=temp).values('name','card','email','uid')
                    lost_user_name=lostquery[0]['name']
                    print(lost_user_name)
                    lost_user_email=lostquery[0]['email']
                    lost_user_uid=lostquery[0]['uid']
                    lost_user_card=lostquery[0]['card']
                    foundquery=Found.objects.filter(uid__exact=temp).values('email','name')
                    found_user_name=foundquery[0]['name']
                    found_user_email=foundquery[0]['email']  
                    lostdel=Lost.objects.get(uid__exact=temp)
                    founddel=Found.objects.get(uid__exact=temp)
                    messagelost='{} Found your card. Please contact them at "{}".'.format(found_user_name,found_user_email)
                    messagefound='{} - The owner of the {} with unique id {} has registered for the card. Please contact them at "{}".'.format(lost_user_name,lost_user_card,lost_user_uid,lost_user_email)
                    print(messagelost)
                    print(messagefound)
                    messages.success(request,"Your lost card has been found!")
                    send_mail('LOFO mail',messagelost,'deepapandey364@gmail.com',[lost_user_email], fail_silently=False,)
                    send_mail('LOFO mail',messagefound,'deepapandey364@gmail.com',[found_user_email], fail_silently=False,)
                    print("Sent mail")
                    lostdel.delete()
                    founddel.delete()
                    messages.success(request,"Your email has been sent!")
                    break
            if(not flag):
                print("Not found the card,in lost_view")
    return render(request, 'work/lostcard.html')


def found_view(request):
    if not request.user.is_authenticated:
        return render(request, 'loginredirect.html')
    if request.method=='POST':
        foundername=request.POST['foundername']
        foundname=request.POST['foundname']
        founduid=request.POST['founduid']
        foundemail=request.POST['foundemail']
        foundcard=request.POST['foundcardtype']
        details=request.POST['founddetails']
        foundcard=Found(name=foundername,cardholder_name=foundname,uid=founduid,card=foundcard,email=foundemail,details=details)
        foundcard.save()
        lost =Lost.objects.filter(uid__gt=1).values('uid')  #getting all uid of lost cards
        ls=Found.objects.filter(uid__gt=1).values('uid')    #getting all uid of found cards
        if(len(ls)>0):
            temp=ls[len(ls)-1]['uid']             #getting the recently added  card in found cards 
            print("current found card inserted ",temp)
            flag=False
            for item in lost:
                if item['uid']==temp:
                    messages.success(request,"Congratulations you found,someone has already registered for this lot card!")
                    flag=True
                    lostquery=Lost.objects.filter(uid__exact=temp).values('name','card','email','uid')
                    lost_user_name=lostquery[0]['name']
                    print(lost_user_name)
                    lost_user_email=lostquery[0]['email']
                    lost_user_uid=lostquery[0]['uid']
                    lost_user_card=lostquery[0]['card']
                    foundquery=Found.objects.filter(uid__exact=temp).values('email','name')
                    itemfound=foundquery[0]
                    found_user_name=foundquery[0]['name']
                    found_user_email=foundquery[0]['email']  
                    lostdel=Lost.objects.get(uid__exact=temp)
                    founddel=Found.objects.get(uid__exact=temp)
                    messagelost='{} Found your card. Please contact them at "{}".'.format(found_user_name,found_user_email)
                    messagefound='{} - The owner of the {} with unique id {} has registered for the card. Please contact them at "{}".'.format(lost_user_name,lost_user_card,lost_user_uid,lost_user_email)
       

                    
                    send_mail('LOFO mail',messagelost,'deepapandey364@gmail.com',[lost_user_email], fail_silently=False,)
                    send_mail('LOFO mail',messagefound,'deepapandey364@gmail.com',[found_user_email], fail_silently=False,)

                    print("sent mail")
                    lostdel.delete()
                    founddel.delete()
                    messages.success(request,"your mail has been sent!")
                    break
            if(not flag):
                print("didnt found the card,in found_View")
    return render(request, 'work/foundcard.html')
    

    #Notification specific view
# def notification_view(request):
#     q1=Found.objects.filter(uid__gt=1).values('uid')
#     print(q1)
#     q3=[]
#     send=False
#     for i in q1:
#         comp=i['uid']
#         q2=Lost.objects.filter(uid__exact=comp).values('name','card','email','uid')
#         if len(q2)!=0:
#             allVal=q2[0]
#             q4=Found.objects.filter(uid__exact=allVal['uid']).values('email','name')
#             foundval=q4[0]
#             foundemail=foundval['email']
#             lostemail=allVal['email']
#             messagelost='{} Found your card. Please contact them at "{}".'.format(foundval['name'],foundval['email'])
#             messagefound='{} - The owner of the {} with unique id {} has registered for the card. Please contact them at "{}".'.format(allVal['name'],allVal['card'],allVal['uid'],allVal['email'])
#             # send_mail('LOFO mail',messagelost,'deepapandey364@gmail.com',[allVal['email']], fail_silently=False,)
#             # send_mail('LOFO mail',messagefound,'deepapandey364@gmail.com',[foundval['email']], fail_silently=False,)
#             #send=True
#             d={"foundemail":foundemail}
#             allVal.update(d)
#             q3.append(allVal)
#     # if send==True:
#     #     messages.success(request,'Found')
#     # else:
#     #     messages.warning(request,'Will update you')
#     return render(request,'work/notifications.html',{'q3':q3})







        #delete record view
def recorddelete_view(request,uid):
    lost=Lost.objects.get(uid__exact=uid)
    print(lost)
    found=Found.objects.get(uid__exact=uid)
    print(found)
    lost.delete()
    found.delete()
    #return render(request,'work/notifications.html')
    #return redirect('home')
    #return HttpResponse('done')



   


