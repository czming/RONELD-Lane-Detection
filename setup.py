from setuptools import setup

setup(
    name='RONELD Lane Detection',
    version='1.0',
    url='https://github.com/czming/RONELD-Lane-Detection',
    license='LGPL-3.0 License',
    author='Zhe Ming Chng',
    author_email='zchng3@gatech,edu',
    description='Enhancement method to improve lane detection outputs from deep learning lane ' +
                'detection models',
    install_requires=['opencv-python>=3.2.0', 'numpy>=1.17', 'scipy>=1.4', 'numba>=0.46.0']
)
