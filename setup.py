import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='pyChainedProxy',  
     version='1.1',
     author="Aman Kumar",
     author_email="akdapunk@gmail.com",
     description="A python module for Chaining of Proxies.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/nighthawkk/pyChainedProxy",
     packages=["pyChainedProxy"],
     entry_points = {
         'console_scripts': [
             'pyChainedProxy = pyChainedProxy:Main'
         ]
     },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

     

 )