from setuptools import setup
import os
from glob import glob

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='osustam',
    maintainer_email='obensustam2@gmail.com',
    description='Examples of minimal publisher/subscriber using rclpy',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = py_pubsub.publisher_member_function:main',
                'listener = py_pubsub.subscriber_member_function:main',
                'custom_msg_pub_py = py_pubsub.custom_msg_pub:main',
                'custom_msg_sub_py = py_pubsub.custom_msg_sub:main',
            ],
    },
)
