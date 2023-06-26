from setuptools import setup, find_packages

setup(
    name='Phoenix',
    version='0.2',
    packages=find_packages(),
    description='An AI CLI Bot',
    author='Colby Brown',
    author_email='csbrown10@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='cli',
    entry_points={
        'console_scripts': [
            'Phoenix=Phoenix.app:main',
        ],
    },
)
