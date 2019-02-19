from distutils.core import setup

setup(
  name = 'aws-mfa-gen',
  packages = ['aws-mfa-gen'],
  version = '0.1',
  license='MIT',
  description = 'Provides aws-mfa-gen command that uses AWS STS to assume role and place result into aws cli credentials file.',
  author = 'Marcin Byrdziak',
  author_email = 'mbyrdziak@gmail.com',
  url = 'https://github.com/mbyrdziak/aws-mfa-gen',
  download_url = 'https://github.com/mbyrdziak/aws-mfa-gen/tarball/0.1',
  keywords = ['aws', 'mfa', 'login'],
  install_requires=[
    'boto',
    'configparser',
  ],
  scripts=['aws-mfa-gen/aws-mfa-gen'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
  ],
)
