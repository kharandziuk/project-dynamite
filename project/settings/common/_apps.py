INSTALLED_APPS = (
    # native
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party
    'django_nose',
    #'rest_framework',
    #'sorl.thumbnail',
    'south',
    # own
    'core',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

#REST_FRAMEWORK = {
#    'DEFAULT_RENDERER_CLASSES': (
#        'djangorestframework_camel_case.CamelCaseJSONRenderer',
#        'rest_framework.renderers.BrowsableAPIRenderer',
#
#    ),
#    'DEFAULT_PARSER_CLASSES': (
#        'djangorestframework_camel_case.CamelCaseJSONParser',
#    )
#}
