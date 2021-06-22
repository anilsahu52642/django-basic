"""
Django settings for basic_project1 project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_=q_2i2xnm40!3i+2*n$4uj1&n*b3hybsdiypkn)8os16m(^_h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

##########for adding allwed host (initially this was a empty list)
ALLOWED_HOSTS = ['basicproject.org','localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homeapp',
    'timeapp',
    'calculatorapp',
    'nauthentication',
    'nauthentication2',
    'nauthentication3',
    'nauthentication4',
    'cookie',
    'cache',
    'signalapp',
    'middlewares',
    'querysetapp',
    'modelinheritanse',
    'model_relationship',
    'class_based_view',
    'authentication_view',
    'pagination',
    'image_upload',
    'faker_app',
    'others',
    'real_authentication',
    'hostingapp',
    'noteapp',

    ########### for giving http connection to website and creating certificate.....
    'django_extensions',
    ########### for social authentication............
    'social_django',



]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    ##########for cache................
    #'django.middleware.cache.UpdateCacheMiddleware',

    'django.middleware.common.CommonMiddleware',

    ##########for cache................
    #'django.middleware.cache.FetchFromCacheMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


    #########for middleware mention below in the format 'appname.filename.middleware function or class name'

    # 'middlewares.middlewares.mymiddleware1',
    # 'middlewares.middlewares.mymiddleware2',

    # 'middlewares.middlewares.anil1',
    # 'middlewares.middlewares.anil2',
    # 'middlewares.middlewares.anil3',

    #######for process view........
    # 'middlewares.middlewares.processmiddleware',

    ######for exception view............
    # 'middlewares.middlewares.myexceptionmiddleware',

    ######for template response middleware............
    # 'middlewares.middlewares.mytemplateresponsemiddleware',

    ##########for site under construction project.....
    # 'middlewares.middlewares.siteunderconstructionmiddleware',

    ########## for social authentication...............
    'social_django.middleware.SocialAuthExceptionMiddleware',

]

ROOT_URLCONF = 'basic_project1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                ########## for social authentication..............
                'social_django.context_processors.backends',  # <-- Here
                'social_django.context_processors.login_redirect', # <-- Here
            ],
        },
    },
]

WSGI_APPLICATION = 'basic_project1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
# STATIC_ROOT=os.path.join(BASE_DIR,'static/')

#for Cookies operations............

#default expiry date of all cookies is 14 days after creation of cookies to change
# SESSION_COOKIE_AGE=10

#for changing cookie name of by default
SESSION_COOKIE_NAME='cookiename'

#for path of cookie
# SESSION_COOKIE_PATH='/home'

#for http and javascript cookie(see in browser cookie)
# SESSION_COOKIE_HTTPONLY=True

#to save cookie to our own files
#create one folder inside project
SESSION_ENGINE='django.contrib.sessions.backends.file'
SESSION_FILE_PATH=os.path.join(BASE_DIR,'savedcookies')


#SESSION_EXPIRE_AT_BROWSER_CLOSE=True


#CACHE PAGE...........

#for database caching.......(after writing below code to create table...py manage.py migrate  ,  py manage.py createcachetable)

# CACHE_MIDDLEWARE_SECONDS=15
# CACHES={
# 'default':{
# 'BACKEND':'django.core.cache.backends.db.DatabaseCache',
# 'LOCATION':'mycachetable',
# }
# }


#for file system caching...

CACHE_MIDDLEWARE_SECONDS=15
CACHES={
'default':{
'BACKEND':'django.core.cache.backends.filebased.FileBasedCache',
'LOCATION':'C:\django\mycache111',

}
}




#for local memory caching......

# CACHE_MIDDLEWARE_SECONDS=15
# CACHES={
# 'default':{
# 'BACKEND':'django.core.cache.backends.locmem.LocMemCache',
# 'LOCATION':'unique_snowflake'
# }
# }





#######################for password reset in authentication_view #####################################
########## for getting a link in console ......
# EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'


########for getting a link in email. you must write correct email and email password for host user...and login to the mail of host user in browser and set allow for less secure app(setting-security-less secure app-on) otherwise(SMTPAuthentication error)
########## turn on the data connnection otherwise it will show error (gaierror)
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='anil.sipun52642@gmail.com'
EMAIL_HOST_PASSWORD='@anilsahu52642@'
EMAIL_USE_TLS=True

###########after login by default it goes to page http://127.0.0.1:8000/accounts/profile/  to changE it ...write below code   here after login it will hit url http://127.0.0.1:8000/auth1
# LOGIN_REDIRECT_URL='/auth1/'


########customising full authentication form.............

##########If we are using above codes then after succcessful password reset and other similar like that we are redirecting to the django's default template to change it we can customise it....

LOGIN_REDIRECT_URL='/profile33333/'





############for giving media url....like uploaded inages or ther files...to find path of image when clicking on admin page
############because of below codes all images will stored in the folder ='BASE_DIR/all media files/uploaded images'
MEDIA_URL='/image_upload/media/'
MEDIA_ROOT=BASE_DIR/'image_upload/media'



###########################################################################################

############ giving http connection to the website...................................
########## after succesful authentication we can go to local host but some authentication site doesnot accepts localhost as url so for this we have to give the domain name..
########## for setting domain name ...go to (C:\Windows\System32\drivers\etc) and open the file 'hosts' and add this line in bottom (127.0.0.1	basicproject.org)(if unable to rename then copy the file to any other location and rename and move and bring that file to origional position and replace)
########## after this in settings.py-ALLOWED_HOSTS   add this ....(see ALLOWED_HOSTS in settngs)....and save..
########## now you can access your page by using  'http://basicproject.org:8000/' or 'http://localhost:8000/' or 'http://127.0.0.1:8000/'

############ after these we have to run server through https......for this we needs TLS(transfer layer security) protocol which is used for secure connection......for this we have to install django extension (in cmd install all  ((pip install django-extensions)and(pip install werkzeug)and (pip install pyOpenSSL))
############ after this go to settings-INSTALLED_APPS and add app('django_extensions')
############ after this go to cmd and type (python manage.py runserver_plus --cert-file cert.crt)
############ after this our project is ready for http connections now you can access your website(https://basicproject.org:8000/) and before that turn on internet connection
############ if after this it is showing error of your connection is not private then click advance and at bottom click 'proceed to basicproject.org(Unsafe)' this error is because we are using a self generated certificate


#######################################################################################################
########### for social authentication(facebook,google....etc).....................................
############# inside command write (pip install social-auth-app-django)..............
############# and after this we have to write('social_django'     inside settings.py-installed apps (it is the default app name for social authentication))
############# and after this we have to migrate(py manage.py migrate social_django)
############# after this we have to add one middaleware ('social_django.middleware.SocialAuthExceptionMiddleware')
############# after this add some line in settings->templates->options->context_processors('social_django.context_processors.backends','social_django.context_processors.login_redirect',)
############# after this add authentication backends like below.........

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',

    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
)

############# after this create a url for social authentication inside project level urls.py file (path('oauth/', include('social_django.urls', namespace='social')))
############# after this proovide default value for login,logout and login redirect(where we have to go after login ,logout and profile)
LOGIN_URL = 'reallogin'
LOGOUT_URL = 'rlogout'
LOGIN_REDIRECT_URL = 'rprofile'


###########for giving authenticatio via facebook ............................................
############ for facebook authentication visit https://developers.facebook.com/   and signup and sign in and go to (myapps -> create app ->consumer ->give app display name(any name) and email id and create app id(submit) ->select facebook login(Setup) ->web ->give site url (https://basicproject.org:8000/ or http://localhost:8000) ->continue ->next ->next->next...and after this go to settings ->basic and note the appid and app secret key which are unique for every app and set app domain (basicproject.org or localhost) and save the changes)
############ after this go to settings ->basic(left side of the site) note the app id and app secret(which are unique for all app created)(app id->289648922832635,app secret->10298aa45ebb31b8785d59425d5da23b) and set app domain (localhost) and set website(site url)(http://localhost:8000/) and hit save changes
############ after this add below lines with your own app id and app secret

######### these are for project if our project have not http connection available for our project (localhost:8000/)
# SOCIAL_AUTH_FACEBOOK_KEY = '289648922832635'  # App ID
# SOCIAL_AUTH_FACEBOOK_SECRET = '10298aa45ebb31b8785d59425d5da23b'  # App Secret


######### these are for project if our project have https connections (https://basicproject.org:8000/)
######## for this same as above but changes are(app domain->basicproject.org)
######## after this go to facebook login->settings(available left side of site) and these should be yes (Client OAuth Login,Web OAuth Login,Enforce HTTPS,Embedded Browser OAuth Login)  and set Valid OAuth Redirect URIs(https://basicproject.org:8000/social-auth/complete/facebook/) and save changes
SOCIAL_AUTH_FACEBOOK_KEY = '1163663650814436'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '1a09f0263d5f2b4821397cdf0d995ad9'  # App Secret

########### if after login it shows erro like redirect uri failed then hit ok and from next page copy the url from address bar and add that url to developers.facebook.com's facebook login->settings->Valid OAuth Redirect URIs(https://basicproject.org:8000/oauth/complete/facebook/) and save changes..
########### to avoid this erro user url as like we are using inside our project level url file path i.e.(oauth) not(social-auth)


############ after this give link in your html page for facebook with this link(<a href="{% url 'social:begin' 'facebook' %}">Login with Facebook</a>).....(see rlogin.html)
############ this will work when we access our site using (localhost:8000/) because we are mentinend during creating app in develepores.facebook.com    (it will not work in 127.0.0.1:8000/)
############ after login successfully automatically a new user is created with username,first_name,last_name and password of facebook account of user and next time we login it will not ask for passeord any more

############ facebook developer email id(anil.sipun52642@gmail.com) password(@anilsahu52642@)
############ for more visit studygyaan.com


####################### for google authentication...........

######### login to console.cloud.google.com and create project (let basicproject) and inside basicproject->click three lines in left side of website and click credintials->create credintials->oauth client id->configure consent screen->user type=(external)->app name=(basic app) and authorized domain=(basicproject.org) and developer contact information=(anil.sipun52642@gmail.com) and click save and continue
######### afte this add ('social_core.backends.google.GoogleOAuth2') inside AUTHENTICATION_BACKENDS
######### after this go to console.cloud.google.com->credintials->create credintials->OAuth client Id->application type(web applications) and name=(name of project  basicproject) and authorized redirect URI=(https://basicproject.org:8000/oauth/complete/google-oauth2/) and click create and get client id and secret key use in below
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '814871923783-olsjor2ds710n11jaerqll40lq5q5pv0.apps.googleusercontent.com'  # App ID
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'rlD-f-VtuG5QhXTC0WQlHcxq'  # App Secret

######### after this go to html file(rlogin.html) and link for google sign in
######### after this go to console.cloud.google.com->api and services->dashboard->enable api and services->search google plus->select google plus api->click Enable
######### this will work only when we accessing our page through https://basicproject:8000/(http connection is required)

######### some chages are happening during giving link and while giving socila auth secret key and id incase of google authentication system
############ console.cloud.google.com email id(anil.sipun52642@gmail.com) password(@anilsahu52642@)

################### if these are showing error (AuthAllreadyAssociated) then in your browser goto inconginto mode and try




#########################################################################################

######### for github (username=anilsahu52642,password=@sipunsahu52642@,email=anil.sipun52642@gmail.com)