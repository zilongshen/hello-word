from setuptools import setup
import versioneer

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    # 补充项目的其他必要信息，如name、packages等
    name='hello-world-pythonbill01',
    packages=['hello_world'],
)