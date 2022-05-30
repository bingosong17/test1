from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'([0-9]{14}.html)', views.report, name='report'),  # 反向传参数，将url中内容传给report函数处理
    # path("paramtest",views.ParamTestView.as_view(),name="paramtest"),
    path("httprunner", views.HttpRunnerView.as_view(), name="httprunner"),
    path("getcurrentpath", views.GetCurrentPathView.as_view(), name="getcurrentpath"),
    path("getfilelist", views.GetFileListView.as_view(), name="getfilelist"),
    path("makecmd", views.MakeCmdView.as_view(), name="makecmd"),
    path("getscriptparams", views.GetScriptParamsView.as_view(), name="getscriptparams"),
    path("getscripttree", views.GetScriptTreeView.as_view(), name="getscripttree"),
    path("getscriptdetail", views.GetScriptDetailView.as_view(), name="getscriptdetail"),
    path("getfilecontent", views.GetFileContentView.as_view(), name="getfilecontent"),
    path("getscriptresult", views.GetScriptResultView.as_view(), name="getscriptresult"),
]
