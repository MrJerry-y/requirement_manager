from setuptools import setup, find_packages

setup(
    name='myrequirements',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'myrequirements = myrequirements.requirements_manager:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

