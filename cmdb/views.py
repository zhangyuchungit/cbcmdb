
from django.shortcuts import render,render_to_response,redirect
from django.http.response import HttpResponse,HttpResponseRedirect
from cmdb import  models
from django.db.models import Q
import json,math
import ssl
# Create your views here.
def Check_Login(func):  #自定义登录验证装饰器
    def warpper(request,*args,**kwargs):
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            return func(request,*args,**kwargs)
        else:
            return redirect("/cmdb/login/")
    return warpper

@Check_Login
def order(request):
    #查
    #   resave = models.Projectinfo.objects.all()
    #   for i in resave:
    #       print(i.id,i.name )
    pagenumlist= []
    if request.method == "GET":
        search = request.GET.get('searchthing')
        print('--------------')
        print(search)
        print('-------------')
        if search is None:
            #初始页面去重显示15条下一版本
            #result = models.hostinfo.objects.all().order_by('insertip')[:15]
            result = models.hostinfo.objects.all().order_by('insertip')[:15]
            #result = models.hostinfo.objects.all().values_list('insertip',flat=True).distinct()[:15]
            #result = models.hostinfo.objects.filter('ip','name','insertip','useport','passwd').values_list('insertip',flat=True).distinct()[:15]
            #result = models.hostinfo.objects.filter(projectname=promes).values_list('insertip').distinct()
            #result = models.hostinfo.objects.all().order_by('insertip')
            newresult = []
            for row in result:
                newresult.append(row)

            length = len(newresult)
            pagenum = length // 10 + 1
            print(pagenum)
            for i in range(1, pagenum + 1):
                pagenumlist.append(i);

            print(pagenumlist)
        else:
            print(type(search))
            #去掉空格和tab
            rightstr = str(search.replace(" ","").replace("\t","").strip())
            print(rightstr)
            searchthing = models.hostinfo.objects.filter(Q(name__icontains=rightstr)|
                                                         Q(insertip__icontains=rightstr)|
                                                         Q(DBschame__icontains=rightstr)|
                                                         Q(DBschamename__icontains=rightstr)|
                                                         Q(notice__icontains=rightstr)
                                                         ).order_by('name').order_by('DBschamename')
            newresult = []
            for searchrow in searchthing:
                newresult.append(searchrow)
            print('not none')
            print(searchthing)
            print(newresult)

        #redic = json.dumps(newresult)
        return render_to_response( 'order-list.html',{'redic':newresult,'pagenum':pagenumlist,})
        #return render(request, 'order-list.html')
    elif request.method == "POST":

        return render(request, 'order-list.html')
    else:
        return HttpResponseRedirect('/login')

@Check_Login
def projectname(request):
    if request.method == "GET":
        projectsearch = request.GET.get('getprojectname')
        print(projectsearch)
        if projectsearch is None:
            # 查找projectname order_by('id').values()
            projectnameresult = models.hostinfo.objects.values_list('projectname', flat=True).distinct()
            print(projectnameresult)

        else:
            print(type(projectsearch))
            #去掉空格和tab
            rightstr = str(projectsearch.replace(" ","").replace("\t","").strip())
            print(projectsearch)
            #select projectname from cmdb_hostinfo where projectname = "CDN" ;
            searchthing = models.hostinfo.objects.filter(projectname=rightstr).values_list('projectname', flat=True).distinct()
            projectnameresult = []
            for searchrow in searchthing:
                projectnameresult.append(searchrow)
        return render_to_response('projectname.html', {'projectnameresult': projectnameresult, })
        #return render(request, 'projectname.html')
    elif request.method == "POST":
        return render(request, 'projectname.html')
    else:
        return render(request, 'projectname.html')

@Check_Login
def adminlist(request):
    return render(request, 'admin-list.html')

@Check_Login
def addproject(request):
    return render(request, 'order-add.html')

@Check_Login
def cate(request):
    return render(request, 'cate.html')

@Check_Login
def hostadd(request):
    if request.method == "GET":

        return render(request, 'host-add.html')
    elif request.method == "POST":
        result = request.POST.getlist('data')
        ##projectname,name,insertip,useport,username,passwd,DBschame,DBschamename,DBschamepasswd,notice

        projectname = result[0]
        name = result[1]
        insertip = result[2]
        useport = result[3]
        username = result[4]
        passwd = result[5]
        DBschame = result[6]
        DBschamename = result[7]
        DBschamepasswd = result[8]
        notice = result[9]

        save_obj = models.hostinfo.objects.create(
            projectname=projectname,
            name=name,
            insertip=insertip,
            useport=useport,
            username=username,
            passwd=passwd,
            DBschame=DBschame,
            DBschamename=DBschamename,
            DBschamepasswd=DBschamepasswd,
            notice=notice, )
        save_obj.save()
        print(123)
        str='增加成功'
        print(result)
        fetch_dic = {'fetch':str}

        return HttpResponse(json.dumps(fetch_dic, ensure_ascii=False))


    else:
        print(789)
        return redirect('/index')


#分页
@Check_Login
def currentpage(request):
    pagenumlist = []
    if request.method == "GET":
        currentthing = request.GET.get('searchthing')
        if currentthing is not None:
            rightstr = str(currentthing.replace(" ","").replace("\t","").strip())
            print(rightstr)
            searchthing = models.hostinfo.objects.filter(Q(name__icontains=rightstr)|
                                                         Q(insertip__icontains=rightstr)|
                                                         Q(DBschame__icontains=rightstr)|
                                                         Q(DBschamename__icontains=rightstr)|
                                                         Q(notice__icontains=rightstr)
                                                         ).order_by('name').order_by('DBschamename')
            newresult = []
            for searchrow in searchthing:
                newresult.append(searchrow)


            return render_to_response('order-list.html',{'redic':newresult,'pagenum':pagenumlist,})
        else:
            currentnum = request.GET.get('page')
            print(int(currentnum))

            result = models.hostinfo.objects.all().order_by('insertip')
            newresult = []
            for row in result:
                newresult.append(row)

            print(len(newresult))

            beginmum =  (int(currentnum) - 1) * 10
            endnum = int(currentnum)* 10 - 1


            length = len(newresult)
            pagenum = length // 10 + 1
            print(pagenum)
            for i in range(1,pagenum + 1):
                pagenumlist.append(i);

            print("总共",+len(pagenumlist),"页")

            #redic = json.dumps(newresult)
            return render_to_response( 'order-list.html',{'redic':newresult[beginmum:endnum],'pagenum':pagenumlist})
        #return render(request, 'order-list.html')
    elif request.method == "POST":


        return render(request, 'order-list.html')
    else:
        return render(request, 'order-list.html')

@Check_Login
def edit(request):
    if request.method == "GET":
        idnum = request.GET.get('dataid')

        newresultbyidlist = []
        print(123)
        print (idnum)
        resultbyid = models.hostinfo.objects.filter(id = idnum)

        newresultbyid = []
        for rowbyid in resultbyid:
            newresultbyid.append(rowbyid)
        print(resultbyid)

        print(newresultbyid)

        #return render_to_response('host-edit.html', {'redic': redic, })
        return render_to_response('host-edit.html', {'newresultbyid':newresultbyid,})
        #return HttpResponse(json.dumps(newresultbyid, ensure_ascii=False))
        #return render(request, 'host-edit.html', {'resultbyid':resultbyid,})

    elif request.method == "POST":

        result = request.POST.getlist('datalist')
        ##name,insertip,useport,username,passwd,DBschame,DBschamename,DBschamepasswd,notice
        print(result)
        projectname = result[0]
        name = result[1]
        insertip = result[2]
        useport = result[3]
        username = result[4]
        passwd = result[5]
        DBschame = result[6]
        DBschamename = result[7]
        DBschamepasswd = result[8]
        notice = result[9]
        idnum = result[10]
        print(111111111)
        print(idnum)
        save_obj = models.hostinfo.objects.filter(id=idnum).update(
            projectname=projectname,
            name=name,
            insertip=insertip,
            useport=useport,
            username=username,
            passwd=passwd,
            DBschame=DBschame,
            DBschamename=DBschamename,
            DBschamepasswd=DBschamepasswd,
            notice=notice, )
        print(123)
        str='更新成功'
        print(result)
        fetch_dic = {'fetch':str}

        return HttpResponse(json.dumps(fetch_dic, ensure_ascii=False))

        #return render(request, 'host-edit.html')

    else:

        return render(request, 'host-edit.html')

@Check_Login
def projectview(request):
    if request.method == "GET":
        #保存项目信息
        projectinfo=[]
        #查询项目
        projectmes=[]
        #保存数据库返回的ip信息
        insertipinfo=[]
        viewprojectname = request.GET.get('projectname')
        print(viewprojectname)
        #直接传的大项目的名称
        print(projectinfo)
        print(111111)
        promes = viewprojectname
        #
        #获取projectname SELECT * from cmdb_hostinfo where id =33
        resultbyprojectname = models.hostinfo.objects.filter(projectname = viewprojectname)[:1]
        for project in resultbyprojectname:
            projectinfo.append(project)


        #SELECT DISTINCT insertip from cmdb_hostinfo where projectname="测试中间库"
        resultinsertip = models.hostinfo.objects.filter(projectname = promes).values_list('insertip',flat=True).distinct()
        for ipinfo in resultinsertip:
            insertipinfo.append(ipinfo)
        print(resultinsertip)
        #notice备注返回
        noticemsg = []
        resultnotice = models.hostinfo.objects.filter(projectname = promes).values_list('notice',flat=True)
        for notices in resultnotice:
            noticemsg.append(notices)
        #返回数据库账户信息

        datainfo = []
        resultdata = models.hostinfo.objects.filter(projectname = promes).order_by('DBschame').order_by('insertip')
        for datames in resultdata:
            datainfo.append(datames)
        return render_to_response('host-view.html', {'projectinfo': projectinfo,'insertipinfo':insertipinfo,'noticemsg':noticemsg,'datainfo':datainfo })

        #return render(request, 'host-view.html')

    elif  request.method == "POST":

        return render(request, 'host-view.html')

    else:
        return render(request, 'host-view.html')


@Check_Login
def view(request):
    if request.method == "GET":
        #保存项目信息
        projectinfo=[]
        #查询项目
        projectmes=[]
        #保存数据库返回的ip信息
        insertipinfo=[]
        viewname = request.GET.get('viewname')
        print(viewname)
        whichid = request.GET.get('whichid')
        print(whichid)
        #先通过id找到projectname 然后利用projectname 找到内网地址
        #获取projectname SELECT * from cmdb_hostinfo where id =33
        resultbyprojectname = models.hostinfo.objects.filter(id = whichid)

        for project in resultbyprojectname:
            projectinfo.append(project)
            projectmes.append(project.projectname)


        print(projectinfo)
        print(111111)
        promes = projectmes[0]

        #SELECT DISTINCT insertip from cmdb_hostinfo where projectname="测试中间库"
        resultinsertip = models.hostinfo.objects.filter(projectname = promes).values_list('insertip',flat=True).distinct()
        for ipinfo in resultinsertip:
            insertipinfo.append(ipinfo)
        print(resultinsertip)
        #notice备注返回
        noticemsg = []
        resultnotice = models.hostinfo.objects.filter(projectname = promes).values_list('notice',flat=True)
        for notices in resultnotice:
            noticemsg.append(notices)
        #返回数据库账户信息

        datainfo = []
        resultdata = models.hostinfo.objects.filter(projectname = promes).order_by('DBschame').order_by('insertip')
        for datames in resultdata:
            datainfo.append(datames)
        return render_to_response('host-view.html', {'projectinfo': projectinfo,'insertipinfo':insertipinfo,'noticemsg':noticemsg,'datainfo':datainfo })

        #return render(request, 'host-view.html')

    elif  request.method == "POST":

        return render(request, 'host-view.html')

    else:
        return render(request, 'host-view.html')

@Check_Login
def svninfo(request):
    pagenumlist= []
    if request.method == "GET":
        search = request.GET.get('svninfosearchthing')
        print('--------------')
        print(search)
        print('-------------')
        if search is None:
            #初始页面去重显示15条下一版本
            #result = models.hostinfo.objects.all().order_by('insertip')[:15]
            svninforesult = models.svninfo.objects.all().order_by('username')
            newsvninfonresult = []
            for row in svninforesult:
                newsvninfonresult.append(row)
            '''
            length = len(svninforesult)
            pagenum = length // 10 + 1
            print(pagenum)
            
            for i in range(1, pagenum + 1):
                pagenumlist.append(i);
             '''
            return render_to_response('svninfo-list.html', {'newsvninfonresult': newsvninfonresult,})
        else:
            print(type(search))
            #去掉空格和tab
            rightstr = str(search.replace(" ","").replace("\t","").strip())
            print(rightstr)
            searchthing = models.svninfo.objects.filter(Q(username__icontains=rightstr)|
                                                         Q(ipinfo__icontains=rightstr)|
                                                         Q(svnuser__icontains=rightstr)|
                                                         Q(svnpasswd__icontains=rightstr)|
                                                         Q(notices__icontains=rightstr)
                                                         ).order_by('username')
            newsvninfonresult = []
            for searchrow in searchthing:
                newsvninfonresult.append(searchrow)
            print('not none')
            print(searchthing)
            return render_to_response('svninfo-list.html', {'newsvninfonresult': newsvninfonresult,})

@Check_Login
def svninfoadd(request):
    if request.method == "GET":

        return render(request, 'svninfo-add.html')
    elif request.method == "POST":
        result = request.POST.getlist('data')
        username = result[0]
        ipinfo = result[1]
        svnuser = result[2]
        svnpasswd = result[3]
        otherpasswd = result[4]
        notices = result[5]
        save_obj = models.svninfo.objects.create(
            username=username,
            ipinfo=ipinfo,
            svnuser=svnuser,
            svnpasswd=svnpasswd,
            otherpasswd=otherpasswd,
            notices=notices, )
        save_obj.save()
        print(123)
        str='增加成功'
        print(result)
        fetch_dic = {'fetch':str}

        return HttpResponse(json.dumps(fetch_dic, ensure_ascii=False))

    else:
        print(789)
        return render(request, 'svninfo-add.html')

@Check_Login
def svninfoedit(request):
    if request.method == "GET":
        svnidnum = request.GET.get('svninfoid')

        newresultbyidlist = []
        print(123)
        print (svnidnum)
        resultsvnbyid = models.svninfo.objects.filter(id = svnidnum).order_by('username')

        newresultsvnbyid = []
        for rowbyid in resultsvnbyid:
            newresultsvnbyid.append(rowbyid)
        print(resultsvnbyid)

        print(newresultsvnbyid)

        #return render_to_response('host-edit.html', {'redic': redic, })
        return render_to_response('svninfo-edit.html', {'newresultsvnbyid':newresultsvnbyid,})
        #return HttpResponse(json.dumps(newresultbyid, ensure_ascii=False))
        #return render(request, 'host-edit.html', {'resultbyid':resultbyid,})

    elif request.method == "POST":

        result = request.POST.getlist('datasvnlist')
        ##name,insertip,useport,username,passwd,DBschame,DBschamename,DBschamepasswd,notice
        print(result)
        username = result[0]
        ipinfo = result[1]
        svnuser = result[2]
        svnpasswd = result[3]
        otherpasswd = result[4]
        notices = result[5]
        idnum = result[6]
        print(111111111)
        print(idnum)
        save_obj = models.svninfo.objects.filter(id=idnum).update(
            username=username,
            ipinfo=ipinfo,
            svnuser=svnuser,
            svnpasswd=svnpasswd,
            otherpasswd=otherpasswd,
            notices=notices,)
        print(123)
        str='更新成功'
        print(result)
        fetch_dic = {'fetch':str}

        return HttpResponse(json.dumps(fetch_dic, ensure_ascii=False))

        #return render(request, 'host-edit.html')

    else:
        return render(request, 'svninfo-edit.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        #验证通过跳index 未通过还是再login
        reusername = request.POST.get('username')
        repasswd = request.POST.get('password')
        print(reusername,repasswd)
        #SELECT * from cmdb_userinfo WHERE username="zhangyuchun" and passwd=123457
        isdui = models.userinfo.objects.filter(username=reusername).filter(passwd=repasswd)
        isuser=len(isdui)
        print(isuser)
        if isuser == 0:
            print('login.html')
            return render(request, 'login.html')
        elif isuser == 1:
            print('index.html')
            request.session['IS_LOGIN'] = True  # 设置session的随机字段值
            request.session['uname'] = reusername  # 设置uname字段为登录用户
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

@Check_Login
def Index(request):
    return render(request, 'index.html')












