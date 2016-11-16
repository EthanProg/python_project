from distutils.core import setup

setup(
    name='nester',
    version='1.0.0',
    py_modules=['nester'],
    author='ethan',
    author_email='prograncccethan@gmail.com',
    url='http://ethanprog.github.io/ethan-prog/',
    description='A python sample'
)

#
# D:\python_project\module>setup.py sdist
# running sdist
# running check
# warning: sdist: manifest template 'MANIFEST.in' does not exist (using default file list)
#
# warning: sdist: standard file not found: should have one of README, README.txt
#
# writing manifest file 'MANIFEST'
# creating nester-1.0.0
# making hard links in nester-1.0.0...
# hard linking nester.py -> nester-1.0.0
# hard linking setup.py -> nester-1.0.0
# creating dist
# creating 'dist\nester-1.0.0.zip' and adding 'nester-1.0.0' to it
# adding 'nester-1.0.0\nester.py'
# adding 'nester-1.0.0\PKG-INFO'
# adding 'nester-1.0.0\setup.py'
# removing 'nester-1.0.0' (and everything under it)

# D:\python_project\module>setup.py install
# running install
# running build
# running build_py
# creating build
# creating build\lib
# copying nester.py -> build\lib
# running install_lib
# copying build\lib\nester.py -> D:\Program Files\python\Lib\site-packages
# byte-compiling D:\Program Files\python\Lib\site-packages\nester.py to nester.cpython-34.pyc
# running install_egg_info
# Writing D:\Program Files\python\Lib\site-packages\nester-1.0.0-py3.4.egg-info

