from distutils.core import setup
from pathlib import Path

setup(
    name='i4u',
    version='0.0.3',
    packages=['i4u'],
    url='https://github.com/ofersadan85/i4u-py',
    license='MIT License',
    author='Ofer Sadan',
    author_email='ofersadan85@gmail.com',
    description='Python package to interact with Invoice4U API',
    long_description=Path(__file__).with_name('README.md').read_text(encoding='utf-8'),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True,
    install_requires=["requests>=2.25.1", "zeep>=0.0.0"],
)
