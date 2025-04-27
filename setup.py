from setuptools import setup, find_packages

version='0.0.2'

setup(
    name='netbox-certificates',
    version=version,
    description='A plugin to help manage SSL Certificates',
    author='Seb Harrington',
    author_email='seb+netbox@cdal.co.uk',
    url='https://github.com/NetworkSeb/netbox-certificates',
    download_url='https://github.com/NetworkSeb/netbox-certificates/archive/v{}.zip'.format(version),
    install_requires=[],
    python_requires='>3.11',
    classifiers=[
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: GPL 3.0',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration'
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
