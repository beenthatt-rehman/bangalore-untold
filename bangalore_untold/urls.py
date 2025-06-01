from django.contrib import admin
from django.urls import path
from submissions import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.landing_page, name='landing'),
    path('home/', views.home_page, name='home'),

    path('blog/', views.blog_view, name='blog'),
    path('map/', views.map_view, name='map'),
    path('events/', views.events_view, name='events'),
    path('user_submissions/', views.user_submissions_view, name='user_submissions'),
    path('faq/', views.faq_view, name='faq'),

    path('explore/', views.explore_page, name='explore'),
    path('explore/cafes/', views.cafes_page, name='cafes'),
    path('explore/historic/', views.historic_page, name='historic'),
    path('explore/nature/', views.nature_page, name='nature'),
    path('explore/markets/', views.markets_page, name='markets'),
]
