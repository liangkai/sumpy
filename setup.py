from setuptools import setup
import os

setup(
    name = 'sumpy',
    packages = ['sumpy'],
    version = '0.0.1',
    description = 'SUMPY: an automatic text summarization library',
    author='Chris Kedzie',
    author_email='kedzie@cs.columbia.edu',
    url='https://github.com/kedz/sumpy',
    install_requires=[
        'nltk', 'numpy', 'scipy', 'scikit-learn', 'pandas',
        'networkx',
    ],
    include_package_data=True,
    package_data={
        'sumpy': [os.path.join('data', 'smart_common_words.txt.gz'),
                  os.path.join('data', 'mead_example_docs', '41.docsent'),   
                  os.path.join('data', 'mead_example_docs', '81.docsent'),
                  os.path.join('data', 'mead_example_docs', '87.docsent'),
                 ]},

)
                    
