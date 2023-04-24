from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    'Operating System :: OS Independent'
]

with open("README.md", "r") as fh:
    long_description = fh.read()

description = "HTML Template"

setup(
    name='hempl',
    version='0.1.1',
    packages=find_packages(),
    package_data={
        "hempl": ['*', '*/*', '*/*/*', '*/*/*/*'],
    },
    url='https://github.com/ShadowCodeCz/hempl',
    project_urls={
        'Source': 'https://github.com/ShadowCodeCz/hempl',
        'Tracker': 'https://github.com/ShadowCodeCz/hempl/issues',
    },
    author='ShadowCodeCz',
    author_email='shadow.code.cz@gmail.com',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=classifiers,
    keywords='html template',
    install_requires=["Pillow"],
)
