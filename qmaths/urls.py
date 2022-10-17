"""qmaths URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import imp
from django.contrib import admin
from django.urls import path
from kelassatu.views import isikelassatu
from kelasdua.views import isikelasdua
from kelastiga.views import isikelastiga
from kelasempat.views import isikelasempat
from kelaslima.views import isikelaslima
from kelasenam.views import isikelasenam
from kamus.views import isikamus
from tokoh.views import isitokoh
from visit.views import isivisit
from latsol.views import isilatsol
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kelassatu/', isikelassatu),
    path('kelasdua/', isikelasdua),
    path('kelastiga/', isikelastiga),
    path('kelasempat/', isikelasempat),
    path('kelaslima/', isikelaslima),
    path('kelasenam/', isikelasenam),
    path('kamus/', isikamus),
    path('tokoh/', isitokoh),
    path('visit/', isivisit),
    path('latsol/', isilatsol),
    path('', views.isiqmaths),
]
