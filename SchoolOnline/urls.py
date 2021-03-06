"""SchoolOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
import xadmin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.views.static import serve

from SchoolOnline.settings import MEDIA_ROOT
from users.views import (ActiveUserView, ForgetPwdView, LoginView,
                         ModifyPwdView, RegisterView, ResetView)

urlpatterns = [
    # 公共
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    re_path('active/(?P<active_code>.*)/',
            ActiveUserView.as_view(), name='user_active'),
    path('captcha/', include('captcha.urls')),
    path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    path('login/', LoginView.as_view(), name='login'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    path('register/', RegisterView.as_view(), name='register'),
    re_path('reset/(?P<active_code>.*)/',
            ResetView.as_view(), name='reset_pwd'),
    path('xadmin/', xadmin.site.urls),

    # 机构
    # path('org_list/', OrgView.as_view(), name='org_list'),
    path("org/", include('organization.urls', namespace="org")),
]
