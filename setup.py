
from distutils.core import setup
setup(
  name = 'pyAWM',         # How you named your package folder (MyLib)
  packages = ['pyAWM'],   # Chose the same as "name"
  # package_dir={'': 'C:/Users/aswanth kumar/Desktop'},
  version = '0.2.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This library automates your whatsapp messages, files, media. It Schedules your messages at given time',   # Give a short description about your library
  author = 'Kalyan Pavan Latchipatruni',                   # Type in your name
  author_email = 'kaluyanpavan1179@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/kalyan1179/Automate-WhatsApp-Messages-with-Python',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/kalyan1179/Automate-WhatsApp-Messages-with-Python/archive/0.2.1.tar.gz',    # I explain this later on
  keywords = ['WHATSAPP', 'AUTOMATE', 'MESSAGE', 'AUTOMATION', 'SEND'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'selenium',
        
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
