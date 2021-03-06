#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
   packages=['mcr_pose_generator', 'mcr_pose_generator_ros'],
   package_dir={'mcr_pose_generator': 'common/src/mcr_pose_generator',
                'mcr_pose_generator_ros': 'ros/src/mcr_pose_generator_ros'}
)

setup(**d)
