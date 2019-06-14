from distutils.core import setup
from setuptools import find_packages

setup(
    name='py_ask_sdk_test',
    version='1.1',
    license='MIT',
    description='A framework for testing Alexa Skills developed in Python with the alexa-skills-kit-sdk-for-python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Jonathan Loos',
    author_email='loos.jonathan.martin@gmail.com',
    url='https://github.com/BananaNosh/py_ask_sdk_test',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    download_url='https://github.com/BananaNosh/py_ask_sdk_test/archive/v1.1.tar.gz',
    keywords=['alexa', 'skill', 'alexa skill', 'test', 'testing', 'framework',
              'testing framework', 'ask_sdk', 'python', 'pytest'],
    install_requires=[
        'ask-sdk-core',
        'responses',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
