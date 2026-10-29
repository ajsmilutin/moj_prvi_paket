from setuptools import find_packages, setup
from glob import glob
package_name = 'moj_prvi_paket'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*launch.[pxy][yma]*')),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ajsmilutin',
    maintainer_email='ajsmilutin@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'moj_prvi_cvor = moj_prvi_paket.moj_prvi_cvor:main',
            'moj_drugi_cvor = moj_prvi_paket.moj_drugi_cvor:main'
        ],
    },
)
