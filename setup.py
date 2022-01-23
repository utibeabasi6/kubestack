from setuptools import setup
import glob

manifests = glob.glob("manifests/templates/*.yaml")

setup(
    name='kubestack',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'kubestack=kubestack:main'
        ]
    },
    include_package_data=True,
     packages=["", "manifests"],
     package_data={
        "manifests": ["**/*.yaml"],
    },
    description='A CLI tool for generating common Kubernetes manifests',
    author='Utibeabasi Umanah',
    author_email='utibeabasiumanah6@@gmail.com',
    url='https://github.com/utibeabasi6/kubestack',
)