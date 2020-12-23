#  Copyright (c) 2020 getcarrier.io
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='arbiter',
    version='1.0.0',
    description='Distributed queue',
    long_description='Lightweight distributed task queue',
    url='https://getcarrier.io',
    license='Apache License 2.0',
    author='arozumenko, LifeDJIK',
    author_email='artem_rozumenko@epam.com, ivan_krakhmaliuk@epam.com',
    packages=find_packages(),
    install_requires=required
)
