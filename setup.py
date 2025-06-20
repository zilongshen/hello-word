from setuptools import setup,find_packages
import versioneer

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    # 补充项目的其他必要信息，如name、packages等
    name='hello-world-pythonbill01',
    packages=find_packages(),
    author='zilongshen',
    author_email='luzipeng01@sina.com',
    description='A simple Hello World Python application.',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license='MIT'
)