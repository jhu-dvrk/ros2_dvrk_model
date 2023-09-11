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
        (os.path.join('share', package_name, 'model/Si'), glob.glob('model/Si/*')),
        (os.path.join('share', package_name, 'model/Classic'), glob.glob('model/Classic/*')),
        (os.path.join('share', package_name, 'rviz'), glob.glob('rviz/*.rviz')),
	(os.path.join('share', package_name, 'ros2_control'), glob.glob('ros2_control/*.*')),
	(os.path.join('share', package_name, 'config'), glob.glob('config/*')),
        (os.path.join('share', package_name, 'meshes/Classic'), glob.glob('meshes/Classic/*.stl')),
        (os.path.join('share', package_name, 'meshes/Classic/psm'), glob.glob('meshes/Classic/psm/*.*')),
        (os.path.join('share', package_name, 'meshes/Classic/ecm'), glob.glob('meshes/Classic/ecm/*.*')),
        (os.path.join('share', package_name, 'meshes/Classic/mtm'), glob.glob('meshes/Classic/mtm/*.*')),
	(os.path.join('share', package_name, 'meshes/Si'), glob.glob('meshes/Si/*.STL')),
        (os.path.join('share', package_name, 'meshes/Si/PSM_ECM'), glob.glob('meshes/Si/PSM_ECM/*.*')),
        (os.path.join('share', package_name, 'meshes/Si/SUJ/ECM'), glob.glob('meshes/Si/SUJ/ECM/*.*')),
        (os.path.join('share', package_name, 'meshes/Si/SUJ/PSM/12'), glob.glob('meshes/Si/SUJ/PSM/12/*.*')),
        (os.path.join('share', package_name, 'meshes/Si/SUJ/PSM/3'), glob.glob('meshes/Si/SUJ/PSM/3/*.*')),
	(os.path.join('share', package_name, 'meshes/instruments/420006'), glob.glob('meshes/instruments/420006/*.*')),
        (os.path.join('share', package_name, 'meshes/instruments/SF0826001'), glob.glob('meshes/instruments/SF0826001/*.*')),
    ],
    install_requires = ['setuptools'],
    zip_safe = True,
    maintainer = 'Anton Deguet',
    maintainer_email = 'anton.deguet@jhu.edu',
    description = 'URDF and STL files for the dVRK',
    license = 'MIT'
)
