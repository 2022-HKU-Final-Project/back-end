"""HKU_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView
from jobRecommend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/products', views.products),
    path('api/jobs', views.jobs),
    path('api/job-filters', views.job_filters),
    path('api/recommend', views.recommend),
    path('api/jobs/<int:id>', views.job_detail),
    path('api/job-categories', views.job_categories),
    path('api/dashboard/Map', views.dashboard_map),
    path('api/dashboard/heatmap', views.dashboard_diploma),
    path('api/dashboard/jobCount', views.dashboard_count),
    path('api/dashboard/salary', views.dashboard_salary),
    # path('jobs', TemplateView.as_view(template_name='index.html')),
    # path('recommend', TemplateView.as_view(template_name='index.html')),
    # path('cs', TemplateView.as_view(template_name='index.html')),
]
