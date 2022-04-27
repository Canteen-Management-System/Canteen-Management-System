import platform
import setuptools
import subprocess

setuptools.setup(
    name='Analysis',
    version='1.0.0',
    description='',
    long_description='',
    url='',
    author='',
    author_email='',
    license='',
    packages=['Analysis'],
    install_requires=['streamlit', 'click'],
    zip_safe=False,  # install source files not egg
    entry_points={'console_scripts': [
        'Analysis = Analysis.wrapped_cli_tool:main'
    ]},
)