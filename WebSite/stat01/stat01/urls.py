#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""stat01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from home import views

from _news.views import news_01
from _about.views import about_01,about_03, about_04,about_05,about_07
from _teacher.views import teacher_01,teacher_02,teacher_03
from _class.views import class_01
#from _join.views import
from _student.views import student_01,student_04
from _association.views import association_06,association_07
from _research.views import research_01,research_02,research_03,research_04
from _bonus.views import bonus_04,bonus_05,bonus_07
from _download.views import download_01,download_02,download_03,download_04,download_05,download_07
from _contact.views import contact_01
from _sitemap.views import sitemap_01
from _sitemember.views import sitemember_01

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"), ####首頁

    path('news_01/', news_01), ###最新公告

    path('about_01/', about_01), ###本系簡介
    path('about_03/', about_03),
    path('about_04/', about_04),
    path('about_05/', about_05),
    path('about_07/', about_07),

    path('teacher_01/', teacher_01), ###師資陣容
    path('teacher_02/', teacher_02),
    path('teacher_03/', teacher_03),

    path('class_01/', class_01), ###課程資訊

    path('sitemap_01', sitemap_01), ###網站導覽

    path('sitemember_01/', sitemember_01), ###網站製作團隊

#    path('join', join),

    path('student_01/', student_01),
    path('student_04/', student_04),

    path('association_06/', association_06),
    path('association_07/', association_07),

    path('research_01/', research_01),
    path('research_02/', research_02),
    path('research_03/', research_03),
    path('research_04/', research_04),

    path('bonus_04/', bonus_04),
    path('bonus_05/', bonus_05),
    path('bonus_07/', bonus_07),

    path('download_01/', download_01),
    path('download_02/', download_02),
    path('download_03/', download_03),
    path('download_04/', download_04),
    path('download_05/', download_05),
    path('download_07/', download_07),

    path('contact_01/', contact_01),

    
]
