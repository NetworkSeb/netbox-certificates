from setuptools import setup, find_packages

version = '0.0.1'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

# setup(
#     name='netbox-certificates',
#     version=version,
#     description='A plugin to help manage SSL Certificates',
#     long_description=long_description,
#     long_description_content_type='text/markdown',
#     license='GPL 3.0',
#     author='Seb Harrington',
#     author_email='seb@cdal.co.uk',
#     url='https://github.com/NetworkSeb/netbox-certificates',
#     download_url='https://github.com/NetworkSeb/netbox-certificates/archive/v{}.zip'.format(version),
#     python_requires='>3.9',
#     classifiers=[
#         'Environment :: Plugins',
#         'Environment :: Web Environment',
#         'Framework :: Django',
#         'License :: OSI Approved :: GPL 3.0',
#         'Topic :: System :: Networking',
#         'Topic :: System :: Systems Administration'
#     ],
#     packages=find_packages(),
#     include_package_data=True,
#     zip_safe=False,
# )

setup(
    name='netbox-certificates',
    version='0.0.1',
    description='A plugin to help manage SSL Certificates',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)