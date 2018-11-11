from reviewboard.extensions.packaging import setup
from setuptools import find_packages


PACKAGE = 'rb_ipynb'

setup(
    name=PACKAGE,
    version='0.2.0',
    description='Display ipynb in a better format',
    url='https://www.reviewboard.org/',
    author='Lydian Lee',
    author_email='lydianly@gmail.com',
    maintainer='Lydian Lee',
    maintainer_email='lydianly@gmail.com',
    packages=find_packages(),
    entry_points={
        'reviewboard.extensions': [
            'rb_ipynb = rb_ipynb.extension:IpynbReviewUIExtension',
        ],
    },
    package_data={
        'rb_ipynb': [
            'templates/rb_ipynb/*.html',
        ]
    },
    install_requires = [
        'beautifulsoup4b',
        'nbconvert',
        'nbdime'
    ]
)
