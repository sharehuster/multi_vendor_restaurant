# multi_vendor_restaurant

###
About static folder :

static will into foodOnline_main folder  (folder project)

we will create other static file like global with command : python manage.py collectstatic  
(this folder will have addition folder : admin)

foodOnline_Main
    foodOnline_Main
        static
    static (by collectstatic)

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR /'static'
STATICFILES_DIRS = [
    'foodOnline_main/static'
]