import os
from setuptools import setup, find_packages
PACKAGES = find_packages()

opts = dict(name = 'WA-Crash-Viz-and-Analysis',
            maintainer='Katharine Chen, Tianqi Fang, Yutong Liu, Shuyi Yin',
            maintainer_email= 'wacrashvizandanalysis@gmail.com',
            description = 'Visualization Tool of Traffice Crash in Washington State',
            long_description = 'WA-Crash-Viz-and-Analysis is an online platform that\
                    integrates various sources related to highway crashes in Washington\
                    State over the last 5 years. This tool facilitates visualization,\
                    exploration and analysis by average driver, professional users and\
                    professional developers.',
            url= 'https://github.com/syin3/WA-Crash-Viz-and-Analysis/',
            license = 'MIT',
            classifiers= ["Development Status :: Alpha",
                        "Environment :: Console",
                        "Intended Audience :: General",
                        "License :: MIT License",
                        "Operating System :: OS Independent",
                        "Programming Language :: Python",
                        "Topic :: Scientific/Engineering"],
            author='Katharine Chen, Tianqi Fang, Yutong Liu, Shuyi Yin',
            author_email = 'wacrashvizandanalysis@gmail.com',
            version='0.1',
            packages=PACKAGES,
            package_data={'data': ['*']},
            )

if __name__ == '__main__':
        setup(**opts)