from reviewboard.extensions.packaging import setup
from setuptools import find_packages

with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='reviewboard-ipynb',
    version='0.2.3',
    description='Display ipynb in a better format',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lydian/reviewboard-ipynb',
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
    install_requires = [
        'beautifulsoup4',
        'nbconvert',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Review Board',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
