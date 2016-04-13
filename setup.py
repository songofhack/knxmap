import sys
from distutils.core import setup

install_require = []

if sys.version_info.major < 3:
    print('Python 2 is not supported')
    sys.exit(1)
elif sys.version_info.major > 2 and \
    sys.version_info.minor < 3:
    print('Python 3.3 or newer is required')
    sys.exit(1)
elif sys.version_info.major > 2 and \
    sys.version_info.minor == 3:
    install_require.append('asyncio')

setup(
    name='knxmap',
    version='',
    packages=['libknx'],
    install_requires=install_require,
    extras_require = {
        'CIDR': ['ipaddress']},
    url='https://github.com/takeshixx/knxmap',
    license='',
    author='takeshix',
    author_email='takeshix@adversec.com',
    description='Network and bus scanner for KNX devices'
)