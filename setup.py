import setuptools

__version__ = str('0.1.0')

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

packages = [
    'mastadonlib'
]


setuptools.setup(
    name='mastadon.py',
    version=__version__,
    packages=packages,
    url='https://github.com/mastadonapp/mastadon.py',
    license='MIT',
    author='Mastadon',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=requirements,
    description='Asynchronous Discord API Wrapper For Python',
    python_requires='>=3.9',
)