"""dstocks URL Configuration

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
from django.urls import path 
from django.conf import settings 
from django.contrib.auth import views as auth_views
from authentication import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('index/',views.index,name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/',views.about,name="about"),
    path('forget_password/',views.forget_password,name="forget_password"),
    path('change_password/',views.change_password,name="change_password"),
    path('login/',views.u_login,name="login"),
    path('d_excel/',views.d_excel,name="d_excel"),
    #path('a_login/',views.a_login,name="a_login"),
    #path('add_to_cart',views.add_to_cart,name="add_to_cart"),
    path('login_a/',views.login_a,name="login_a"),
    path('contact/',views.contact,name="contact"),
    path('admin/a_contact/',views.a_contact,name="a_contact"),
    path('admin/available_stock/',views.available_stock,name="available_stock"),
    path('admin/add_product/',views.add_product,name="add_product"),
    path('purchase/',views.purchase ,name="purchase"),
    path('register/',views.registations,name="register"),
    path('del_contact/',views.del_contact,name="del_contact"),
    path('logout/',views.logout,name="logout"),
    path('a_logout/',views.a_logout,name="a_logout"),
    path('services/',views.services,name="services"),
    path('pencil/',views.pencil,name="pencil"),
    path('pen/',views.pen,name="pen"),
    path('colour/',views.colour,name="colour"),
    path('drawing/',views.Drawing,name="Drawing"),
    path('single/',views.single,name="single"),
    path('insertdata/',views.insertdata,name='insertdata'),
    path('admin/add_product/',views.add_product,name='add_product'),
    path('admin/a_purchase/',views.a_purchase,name='a_purchase'),
    path('admin/a_sales/',views.a_sales,name='a_sales'),
    path('a_stock/',views.a_stock,name="a_stock"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   






# <!-- <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}"> Bootstrap-Core-CSS
# 	<link rel="stylesheet" href="{% static 'css/style.css' %}" type="text/css" media="all" /> Style-CSS 
# 	<link rel="stylesheet" href="{% static 'css/fontawesome-all.css' %}"> Font-Awesome-Icons-CSS -->
# 	<!-- //css files -->

# 
# 	<script type="text/javascript" src="{% static 'js/jquery-2.2.3.min.js' %}"></script>
# 	<script type="text/javascript" src="{% static 'js/bootstrap.js' %}"></script> <!-- Necessary-JavaScript-File-For-Bootstrap --> 
# 	<!-- //js -->
	
# 	<!-- start-smoth-scrolling -->
# 	<script src="{% static 'js/SmoothScroll.min.js' %}"></script>
# 	<script type="text/javascript" src="{% static 'js/move-top.js' %}"></script>
# 	<script type="text/javascript" src="{% static 'js/easing.js' %}"></script>
# 	<script type="text/javascript">
# 		jQuery(document).ready(function($) {
# 			$(".scroll").click(function(event){		
# 				event.preventDefault();
# 				$('html,body').animate({scrollTop:$(this.hash).offset().top},1000);
# 			});
# 		});
# 	</script>
# 	<!-- here stars scrolling icon -->
# 	<script type="text/javascript">
# 		$(document).ready(function() {
# 			/*
# 				var defaults = {
# 				containerID: 'toTop', // fading element id
# 				containerHoverID: 'toTopHover', // fading element hover id
# 				scrollSpeed: 1200,
# 				easingType: 'linear' 
# 				};
# 			*/
								
# 			$().UItoTop({ easingType: 'easeOutQuart' });
								
# 			});
# 	</script>