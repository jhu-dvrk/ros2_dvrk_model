import os
import glob
import setuptools

package_name = 'dvrk_model'

setuptools.setup(
    name = package_name,
    version = '0.0.0',
    packages = [package_name],
    data_files = [
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob.glob('launch/*.py')),
        (os.path.join('share', package_name, 'model'), glob.glob('model/*')),
        (os.path.join('share', package_name, 'rviz'), glob.glob('rviz/*.rviz')),
        (os.path.join('share', package_name, 'meshes'), glob.glob('meshes/*.stl')),
        (os.path.join('share', package_name, 'meshes/psm'), glob.glob('meshes/psm/*.*')),
        (os.path.join('share', package_name, 'meshes/ecm'), glob.glob('meshes/ecm/*.*')),
        (os.path.join('share', package_name, 'meshes/mtm'), glob.glob('meshes/mtm/*.*')),
    ],
    install_requires = ['setuptools'],
    zip_safe = True,
    maintainer = 'Anton Deguet',
    maintainer_email = 'anton.deguet@jhu.edu',
    description = 'URDF and STL files for the dVRK',
    license = 'MIT'
)
