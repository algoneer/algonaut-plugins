from distutils.core import setup
from setuptools import find_packages

setup(
    name='algonaut_contact',
    python_requires='>=3',
    version='0.0.1',
    author='Andreas Dewes - 7scientists',
    author_email='andreas.dewes@7scientists.com',
    license='proprietary',
    url='https://gitlab.com/7s-algonaut/plugins/contact',
    packages=find_packages(),
#    package_data={'': ['*.ini']},
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    entry_points={
        'console_scripts': []
    },
    description='Algonaut-Contact Form plugin.',
    long_description="""Our Algonaut Contact Form plugin.
"""
)
