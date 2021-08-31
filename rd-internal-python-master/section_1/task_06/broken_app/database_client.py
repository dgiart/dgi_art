from app import settings


def setup_database():
    print('setting-up database..')
    print('database connection timeout = %s' % settings['default_timeout'])
    # database setup code goes here
    print('database set-up complete!')
