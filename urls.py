from django.urls import path
from . import views

urlpatterns = [
    path('oidc_auth/', views.oidc_auth, name='oidc_auth'),
    path('oidc_callback/', views.oidc_callback, name='oidc_callback'),
    path('social_login/facebook/', views.social_media_login, name='fb_login', kwargs={'platform': 'facebook'}),
    path('social_login/twitter/', views.social_media_login, name='twitter_login', kwargs={'platform': 'twitter'}),
    path('social_login/instagram/', views.social_media_login, name='instagram_login', kwargs={'platform': 'instagram'}),
    path('social_login/linkedin/', views.social_media_login, name='linkedin_login', kwargs={'platform': 'linkedin'}),
    path('social_login/google/', views.social_media_login, name='google_login', kwargs={'platform': 'google'}),
    path('index/', views.index, name='index'),
    path('form_submit/', views.form_submit, name='form_submit'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('new_feature/', views.new_feature, name='new_feature'),
    path('another_new_feature/', views.another_new_feature, name='another_new_feature'),
    # Newly added paths for React pages
    path('', views.MainPage, name='MainPage'),
    path('user-authentication/', views.MainPage, name='UserAuthenticationPage'),
    path('dashboard/', views.MainPage, name='DashboardPage'),
    path('file-upload/', views.MainPage, name='FileUploadPage'),
    path('button-actions/', views.MainPage, name='ButtonActionsPage'),
    path('form-validation/', views.MainPage, name='FormValidationPage'),
    path('ui-ux-design/', views.MainPage, name='UIDesignPage'),
    path('state-management/', views.MainPage, name='StateManagementPage'),
    path('routing/', views.MainPage, name='RoutingPage'),
    path('api-integration/', views.MainPage, name='APIIntegrationPage'),
    path('watch-page/', views.MainPage, name='WatchPage'),
    path('cloning-page/', views.MainPage, name='CloningPage'),
    path('menu-page/', views.MainPage, name='MenuPage'),
    path('banking-page/', views.MainPage, name='BankingPage'),
    // Added routes for help documents, FAQS, and feedback form
    path('help/', views.help, name='help'),  // New route for help page
    path('faq/', views.faq, name='faq'), // New route for FAQ page
    path('feedback/', views.feedback, name='feedback'), // New route for feedback form
    # Added API paths for each page and feedback submission
    path('api/<str:page_id>/', views.api_serve, name='api_serve'),
    path('api/submit_feedback/', views.submit_feedback, name='submit_feedback'),  // New API path for feedback submission
    path('ai_predict/', views.ai_predict, name='ai_predict'),
]
