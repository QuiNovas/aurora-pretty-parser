import io
from setuptools import setup


setup(
    name='aurora-prettyparser',
    version='1.0.0',
    description='Parses Aurora responses into a list dictionaries with column names as keys',
    author='Mathew Moon',
    author_email='mmoon@quinovas.com',
    url='https://github.com/QuiNovas/aurora-prettyparser',
    license='Apache 2.0',
    long_description=io.open('README.rst', encoding='utf-8').read(),
    long_description_content_type='text/x-rst',
    packages=['auroraPrettyParser'],
    package_dir={'auroraPrettyParser': 'src/auroraPrettyParser'},
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
    ],
)
