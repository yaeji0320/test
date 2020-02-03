from setuptools import setup, find_packages

setup(
    name                = 'yjpip',
    version             = '0.1',
    description         = 'pip test',
    author              = 'yaeji',
    author_email        = 'dldpwl0320@gmail.com',
    url                 = 'https://github.com/yjl32/test',
    install_requires    =  [],
    packages            = find_packages(exclude = []),
    keywords            = ['piptest'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
