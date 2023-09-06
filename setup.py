from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'numpy==1.21.6',
    'protobuf==3.19.6',
    'Pillow==9.5.0',
    'lxml==4.9.3',
    'Cython==3.0.0',
    'contextlib2==21.6.0',
    'tf-slim==1.1.0',
    'six==1.16.0',
    'matplotlib==3.5.3',
    'scipy==1.7.3',
    'pandas==1.3.5',
    'opencv-python-headless==4.8.0.76',
    'tf-models-official==2.10.1',
    'pycocotools==2.0.6',
    'Flask==2.2.5',
    'Flask-Cors==4.0.0'
]

setup(
    name='tfod2_project',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='TensorFlow Object Detection API Project',
    python_requires='>=3.6',
)
