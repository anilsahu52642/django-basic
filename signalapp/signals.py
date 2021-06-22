# ###############some codes are written iside apps.py and __init__.py file......########################
#
#
#
# ##############################for user login,logout,login failed##############
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
#
# ######## for user logged in (used when user login to admin page)
# @receiver(user_logged_in,sender=User)
# def afterlogin(sender,user,request,**kwargs):
#     print('..................................')
#     print('this is after signed in  user signal')
#     print('sender',sender)
#     print('user',user)
#     print('request',request)
#     print(f'kwargs:{kwargs}')
#     print('..................................')
#
# ######with out writing code for receiver we can use below code for receiver
# #user_logged_in.connect(afterlogin,sender=User)
#
# ######## for user logged out (used when user login out from admin page)
# @receiver(user_logged_out,sender=User)
# def afterlogout(sender,user,request,**kwargs):
#     print('..................................')
#     print('this is after signed out  user signal')
#     print('sender',sender)
#     print('user',user)
#     print('request',request)
#     print(f'kwargs:{kwargs}')
#     print('..................................')
#
#
# ######with out writing code for receiver we can use below code for receiver
# #user_logged_out.connect(afterlogout,sender=User)
#
#
# ######## for user login failed (used when user login failed to admin page)
# @receiver(user_login_failed)
# def loginfailed(sender,request,**kwargs):
#     print('..................................')
#     print('this is after login failed user signal')
#     print('sender',sender)
#     print('request',request)
#     print(f'kwargs:{kwargs}')
#     print('..................................')
#
# ######with out writing code for receiver we can use below code for receiver
# #user_login_failed.connect(loginfailed,sender=User)
#
# ##########################################################################################
# ###########this is for pre save,post save,pre delete,post delete,pre init,post init,pre migrate,post migrate.....
#
#
# from django.db.models.signals import pre_save,post_save,pre_delete,post_delete,pre_init,post_init,pre_migrate,post_migrate
#
#
# ########for pre save(used before save one user to database)........
# @receiver(pre_save,sender=User)
# def beforesave(sender,instance,**kwargs):
#     print('..................................')
#     print('this is before saving a user signal')
#     print('sender:',sender)
#     print('instance:',instance)
#     print(f'kwargs:{kwargs}')
#     print('..................................')
#
#
# ######with out writing code for receiver we can use below code for receiver
# #pre_save.connect(beforesave,sender=User)
#
#
# #######for post save(used after save one user to database)........
# @receiver(post_save,sender=User)
# def aftersave(sender,created,instance,**kwargs):
#     print('..................................')
#     print('this is after saving a user signal')
#     print('sender:',sender)
#     print('instance:',instance)
#     print(f'kwargs:{kwargs}')
#     if created:
#         print('new user created')
#     else:
#         print('user updatd')
#     print('..................................')
#
#
#
# ######with out writing code for receiver we can use below code for receiver
# #post_save.connect(aftersave,sender=User)
#
# #######for pre delete(used before delete a user from database)........
#
# @receiver(pre_delete,sender=User)
# def beforedelete(sender,instance,**kwargs):
#     print('..................................')
#     print('this is before delete a user signal')
#     print('sender:',sender)
#     print('instance:',instance)
#     print(f'kwargs:{kwargs}')
#     print('..................................')
#
#
# ######with out writing code for receiver we can use below code for receiver
# #pre_delete.connect(beforedelete,sender=User)
#
#
# #######for post delete(used after delete a user from database)........
#
# @receiver(post_delete,sender=User)
# def afterdelete(sender,instance,**kwargs):
#     print('..................................')
#     print('this is after delete a user signal')
#     print('sender:',sender)
#     print('instance:',instance)
#     print(f'kwargs:{kwargs}')
#     print('..................................')
#
#
# ######with out writing code for receiver we can use below code for receiver
# #post_delete.connect(afterdelete,sender=User)
#
# #######for pre init(used when a instance is created like refreshing admin.....ect)........
#
# @receiver(pre_init,sender=User)
# def beforeinit(sender,*args,**kwargs):
#     print('..................................')
#     print('this is before init signal')
#     print('sender:',sender)
#     print(f'args:{args}')
#     print(f'kwargs:{kwargs}')
#     print('..................................')
#
#
# ######with out writing code for receiver we can use below code for receiver
# #pre_init.connect(beforeinit,sender=User)
#
#
# #######for pre init(used when a instance is created like refreshing admin page.....ect)........
#
# @receiver(post_init,sender=User)
# def afterinit(sender,*args,**kwargs):
#     print('..................................')
#     print('this is after init signal')
#     print('sender:',sender)
#     print(f'args:{args}')
#     print(f'kwargs:{kwargs}')
#     print('..................................')
#
#
# ######with out writing code for receiver we can use below code for receiver
# #post_init.connect(afterinit,sender=User)
#
#
# #######for pre migrate(used when we makemigratins and migrate........
#
# @receiver(pre_migrate,sender=User)
# def beforemigrte(sender,apps,app_config,plan,verbosity,interactive,using,**kwargs):
#     print('..................................')
#     print('this is pre migrate signal')
#     print('sender:',sender)
#     print('apps:',apps)
#     print('plan:',plan)
#     print('app_config:',app_config)
#     print('verbosity:',verbosity)
#     print('interactive:',interactive)
#     print('using:',using)
#     print(f'kwargs:{kwargs}')
#     print('..................................')
#
#
# ######with out writing code for receiver we can use below code for receiver
# #pre_migrate.connect(beforemigrte,sender=User)
#
#
# #######for post migrate(used when we makemigratins and migrate........
#
# @receiver(post_migrate,sender=User)
# def aftermigrte(sender,apps,app_config,plan,verbosity,interactive,using,**kwargs):
#     print('..................................')
#     print('this is post migrate signal')
#     print('sender:',sender)
#     print('apps:',apps)
#     print('plan:',plan)
#     print('app_config:',app_config)
#     print('verbosity:',verbosity)
#     print('interactive:',interactive)
#     print('using:',using)
#     print(f'kwargs:{kwargs}')
#     print('..................................')
#
#
# ######with out writing code for receiver we can use below code for receiver
# #post_migrate.connect(aftermigrte,sender=User)
#
#
# ########for connection started,connection finished,got connection exception.................
#
#
# from django.core.signals import request_started,request_finished,got_request_exception
#
#
# #######for request starting(used when when we hit url for our view in browser)........
#
# @receiver(request_started)
# def requeststart(sender,environ,**kwargs):
#     print('..................................')
#     print('this is request starting signal')
#     print('sender:',sender)
#     print('environ:',environ)
#     print(f'kwargs:{kwargs}')
#     print('..................................')
#
#
# ######with out writing code for receiver we can use below code for receiver
# #request_started.connect(requeststart,sender=User)
#
# #######for request ending(used when when we hit url for our view in browser)........
#
# @receiver(request_finished)
# def requestend(sender,**kwargs):
#     print('..................................')
#     print('this is request ending signal')
#     print('sender:',sender)
#     print(f'kwargs:{kwargs}')
#     print('..................................')
#
#
# ######with out writing code for receiver we can use below code for receiver
# #request_finished.connect(requestend,sender=User)
#
#
# #######for request exception(used when when we hit url for our view in browser and in views file some error occures)........
# ##########for this go to views.py file and create one view function and give some error...........
#
# ####not working ..........
# @receiver(got_request_exception)
# def requestexception(sender,request,**kwargs):
#     print('..................................')
#     print('this is request error signal')
#     print('request:',request)
#     print('sender:',sender)
#     print(f'kwargs:{kwargs}')
#     print('..................................')
#
#
# ######with out writing code for receiver we can use below code for receiver
# #got_request_exception.connect(requestexception,sender=User)
#
#
# ##############for connection (used when we type py manage.py runserver)
#
#
# from django.db.backends.signals import connection_created
# @receiver(connection_created)
# def connectionstart(sender,**kwargs):
#     print('...................................')
#     print('this is connection starting signal')
#     print('sender:',sender)
#     print(f'kwargs:{kwargs}')
#     print('...................................')
#
# ######with out writing code for receiver we can use below code for receiver
# # connection_created.connect(connectionstart)
#
#
#
#
# #########################################################################################################
# #########################################################################################################
#
#
# #########for own customized signal......................
#
# from django.dispatch import Signal
#
#
# mysignal=Signal(providing_args=['request','user'])
# @receiver(mysignal)
# def myownsignal(sender,**kwargs):
#     print('..............................')
#     print('own created signal started....')
#     print('sender:',sender)
#     print(f'kwargs:{kwargs}')
#     print('..............................')
#
#
# ######after writing above code go to views.py file and create function
