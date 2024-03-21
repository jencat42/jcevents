from setuptools import setup, find_packages

setup(
    name='jcevents',
    version='1.0.0',
    description='A lightweight event-driven framework for Python',
    long_description=open('README.rst').read(),
    url='https://github.com/jencat42/jcevents',
    author='Your Name',
    author_email='gubenkovalik@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='event-driven framework',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[],
)
