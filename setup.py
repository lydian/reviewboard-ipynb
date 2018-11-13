from reviewboard.extensions.packaging import setup
from setuptools import find_packages


setup(
    name='reviewboard-ipynb',
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
            'reviewboard_ipynb = reviewboard_ipynb.extension:IpynbReviewUIExtension',
        ],
    },
    package_data={
        'reviewboard_ipynb': [
            'templates/*.html',
            'static/css/*.css',
        ]
    },
    install_requires = [
        'beautifulsoup4',
        'nbconvert',
    ]
)
