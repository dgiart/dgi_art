import os
import sys

from database_client import setup_database


settings = {
    'admin_email': 'admin@epam.com',
    'default_timeout': 10,
}


def main():
    print('Initializing application.')
    setup_database()
    print('Set-up complete. Sending e-mail to: %s' % settings['admin_email'])


if __name__ == '__main__':
    main()
