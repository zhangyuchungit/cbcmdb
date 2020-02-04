from django.db import models

# Create your models here.


class Projectinfo(models.Model):
    projectname = models.CharField(max_length=64, verbose_name=u'是何项目')
    name = models.CharField(max_length=64, verbose_name=u'项目名称')
    env = models.CharField(max_length=32, blank=True, verbose_name=u'环境选项')
    insertip = models.CharField(max_length=128, blank=True, verbose_name=u'内网地址')
    outip = models.CharField(max_length=32, blank=True, verbose_name=u'外网地址')
    useport = models.CharField(max_length=128, blank=True, verbose_name=u'使用端口')
    address = models.TextField(max_length=128,blank=True, verbose_name=u'主机位置')
    deployapps = models.TextField(max_length=128,blank=True, verbose_name=u'部署应用')
    usedinfo = models.CharField(max_length=32, blank=True, verbose_name=u'使用情况')
    ship = models.TextField(max_length=128,blank=True, verbose_name=u'外内关系')
    urlinfo = models.TextField(max_length=128,blank=True, verbose_name=u'访问url')
    cpuinfo = models.CharField(max_length=32, blank=True, verbose_name=u'cpuinfo')
    diskinfo = models.CharField(max_length=32, blank=True, verbose_name=u'diskinfo')
    meminfo = models.CharField(max_length=32, blank=True, verbose_name=u'meminfo')


class hostinfo(models.Model):
    projectname = models.CharField(max_length=64, verbose_name=u'是何项目')
    name = models.CharField(max_length=64, verbose_name=u'项目名称')
    insertip = models.CharField(max_length=128, verbose_name=u'内网地址')
    useport = models.CharField(max_length=128, blank=True, verbose_name=u'使用端口')
    username = models.CharField(max_length=32, blank=True, verbose_name=u'用户名')
    passwd = models.CharField(max_length=32, blank=True, verbose_name=u'密码')
    DBschame = models.CharField(max_length=128, blank=True, verbose_name=u'URLDBschame')
    DBschamename = models.CharField(max_length=32, blank=True, verbose_name=u'URLDBschamename')
    DBschamepasswd = models.CharField(max_length=32, blank=True, verbose_name=u'URLDBschamepasswd')
    notice = models.TextField(max_length=128,blank=True, verbose_name=u'备注')


class svninfo(models.Model):
    username = models.CharField(max_length=64, verbose_name=u'姓名')
    ipinfo = models.CharField(max_length=64,blank=True, verbose_name=u'ip信息')
    svnuser = models.CharField(max_length=128, blank=True,verbose_name=u'svnuser')
    svnpasswd = models.CharField(max_length=128, blank=True, verbose_name=u'svnpasswd')
    otherpasswd = models.CharField(max_length=32, blank=True, verbose_name=u'otherpasswd')
    notices = models.CharField(max_length=32, blank=True, verbose_name=u'notices')

class userinfo(models.Model):
    username = models.CharField(max_length=64, verbose_name=u'姓名')
    passwd = models.CharField(max_length=64,blank=True, verbose_name=u'密码')
    email = models.CharField(max_length=128, blank=True,verbose_name=u'邮件')
    phonenum = models.CharField(max_length=128, blank=True, verbose_name=u'电话')



'''
class ouath(models.Model):
    inname = models.CharField(max_length=64, unique=True, verbose_name=u'登录名')
    phone = models.CharField(max_length=128, blank=True, verbose_name=u'手机')
    mail = models.CharField(max_length=128, blank=True, verbose_name=u'邮箱')
    rule = models.CharField(max_length=128, blank=True, verbose_name=u'角色')
'''