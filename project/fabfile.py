from fabric.api import run, env, local, shell_env
from fabric.operations import put
from fabric.context_managers import cd

from unipath import Path


def dev():
    env.hosts = ['']
    env.user = 'dev'
    env.port = 2020

    env.shell = '/bin/sh -c'

    env.django_settings_module = 'settings.development'

    project_path = Path('')
    env.env_path = project_path.child('env', 'bin')
    env.django_path = project_path.child('multiad', 'project')
    gunicorn_wsgi = 'wsgi:application'
    gunicorn_port = 9324
    env.gunicorn_pid = project_path.child('gunicorn.pid')
    settings = 'settings.development'
    worker_count = 3
    cfg_template = '{} -b 127.0.0.1:{} -w{} --max-requests=500 -D --pid {}'
    env.gunicorn_cfg = cfg_template.format(
        gunicorn_wsgi, gunicorn_port, worker_count, env.gunicorn_pid
    )

def _virtualenv(command):
    run('{}/{}'.format(env.env_path, command), pty=False)



def deploy():
    with cd(env.django_path):
        local('git pull -u upstream master')
        run('git pull -u origin master')
        static()
        gunicorn('restart')
        

def collectstatic():
    django('collectstatic --noinput')

def django(command):
    with shell_env(DJANGO_SETTINGS_MODULE=env.django_settings_module):
        for_run = '{} {} {}'.format(
            env.env_path.child('python'), 
            env.django_path.child('manage.py'),
            command,
        )
        run(for_run, pty=False)

def static():
    # remove old static
    local('rm -rf static')
    run('rm -rf static')
    # prepare new and copy 
    local('grunt build')
    local('tar -c --bzip2 -f static.tar.bz2 static')
    put('static.tar.bz2', '.')
    run('tar xvjf static.tar.bz2')
    django('collectstatic --noinput')



def gunicorn(action=None):
    def _run():
        with cd(env.django_path):
            with shell_env(DJANGO_SETTINGS_MODULE=env.django_settings_module):
                _virtualenv('gunicorn {}'.format(env.gunicorn_cfg))

    def _stop():
        g_pid = run('cat {}'.format(env.gunicorn_pid))
        run('kill {}'.format(g_pid))

    def _restart():
        g_pid = run('cat {}'.format(env.gunicorn_pid))
        run('kill -HUP {}'.format(g_pid))

    handlers = {
        'run': _run,
        'start': _run,
        'stop': _stop,
        'restart': _restart,
    }
    assert action in handlers
    handlers[action]()

