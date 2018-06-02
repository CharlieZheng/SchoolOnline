'''Router for org-list.html'''
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import PageNotAnInteger, Paginator

from .models import CityDict, CourseOrg

# Create your views here.


class OrgView(View):
    '''课程机构'''

    def get(self, request):
        '''Render'''
        # 所有课程机构
        all_orgs = CourseOrg.objects.all()
        # 类别筛选
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)
        # 有多少家机构
        org_nums = all_orgs.count()
        # 所有城市
        all_citys = CityDict.objects.all()

        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 对课程机构进行分页
        # 尝试获取前台get请求传递过来的page参数
        # 如果是不合法的配置参数默认返回第一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 这里指从allorg中取五个出来，每页显示5个
        fewfew = Paginator(all_orgs, 2, request=request)
        orgs = fewfew.page(page)

        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "category": category,
            "org_nums": org_nums,
            'city_id': city_id,
        })
