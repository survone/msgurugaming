from setuptools import setup

setup(name='twitchlivenotifier',
      version='1.0',
      description='Python script to notify a Discord server when MsGuruGaming goes live, with the current game and box art.',
      url='https://github.com/survone/msgurugaming/',
      author='StankToe',
      author_email='phone.william@gmail.com',
      license='GPLv3',
      packages=['twitchlivenotifier'],
	  install_requires=[
          'requests', 'zc.lockfile',
      ],
      entry_points = {
        'console_scripts': ['twitchlivenotifier=twitchlivenotifier.command_line:main'],
      },
      zip_safe=False)
