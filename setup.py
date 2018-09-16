from setuptools import setup, find_packages

    
setup(name='pytimer_enhanced',
      version='1.0',
      description='An enhanced timer for Python',
      long_description='',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
      ],
      install_requires=['docutils>=0.3'],
      keywords='timer enhanced repeated events utils module python',
      url='http://github.com/themelon-boy/pytimer_enhanced',
      author='Marco Espinosa',
      author_email='marcoantonio.espinosa@gmx.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      package_data={'pytimer_enhanced': ['*.txt'],},
      zip_safe=False)