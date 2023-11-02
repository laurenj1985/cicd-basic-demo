from setuptools import setup 
  
setup( 
    name='my_package', 
    version='0.1', 
    description='A simple Python package', 
    author='LaurenJ', 
    author_email='lchristopher.johnson@gmail.com', 
    packages=['my_package'], 
    install_requires=[ 
        'numpy', 
        'pandas',
        'pytest',
        'flask' 
    ], 
) 