from setuptools import setup

setup(
    name='galgal',
    version='0.0.1',
    author='Magine Lee',
    author_email='con@loli.lu',
    description='Text Adventure Game Maker',
    url='https://github.com/Ma233/galgal',
    license='GNU GPL 3.0',
    packages=['galgal'],
    entry_points={'console_scripts': [
        "galgal = galgal.command:main",
    ]}
)
