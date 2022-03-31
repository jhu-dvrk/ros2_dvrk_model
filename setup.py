import os
from glob import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'dvrk_model'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.py')),
        (os.path.join('share', package_name, 'model'), glob('model/*')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.stl')),
        (os.path.join('share', package_name, 'meshes/psm'), glob('meshes/psm/*.*')),
        (os.path.join('share', package_name, 'meshes/ecm'), glob('meshes/ecm/*.*')),
        (os.path.join('share', package_name, 'meshes/mtm'), glob('meshes/mtm/*.*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Laura Connolly',
    maintainer_email='15lpc1@queensu.ca',
    description='URDF and STL files for Sensable Omni',
    license='MIT',
    entry_points={
        'console_scripts': [ 'joint_state_publisher = dvrk_model.joint_state_publisher:main'
        ],
    },
)
