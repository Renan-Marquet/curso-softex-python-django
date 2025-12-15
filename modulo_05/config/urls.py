
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import ( 
    TokenObtainPairView, # Login (obter access e refresh tokens)
    TokenRefreshView, 
    # Renovar token 
    )

urlpatterns = [
    path('admin/', admin.site.urls),
        # App core
        # URLs do app core (prefixo: /api/)
    path('api/', include('core.urls')), 
   
    # JWT: Endpoints de autenticação 
    path('api/token/', 
         TokenObtainPairView.as_view(), 
         name='token_obtain_pair'), 
    path('api/token/refresh/', 
         TokenRefreshView.as_view(), 
         name='token_refresh'), 
   
    
]
