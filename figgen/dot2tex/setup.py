from distutils.core import setup

setup(name='dot2tex',
      version='2.7.0',
      description = 'A Graphviz to LaTeX converter',
      long_description="""\
The purpose of dot2tex is to give graphs generated by the graph layout tool
Graphviz_, a more LaTeX friendly look and feel. This is accomplished by:

- Using native PSTricks_ and `PGF/TikZ`_ commands for drawing arrows,
  edges and nodes.
- Typesetting labels with LaTeX, allowing mathematical notation.
- Using backend specific styles to customize the output.

.. _Graphviz: http://www.graphviz.org/
.. _PSTricks: http://tug.org/PSTricks/main.cgi/
.. _PGF/TikZ: http://www.ctan.org/tex-archive/help/Catalogue/entries/pgf.html
""",
      author = 'Kjell Magne Fauske',
      author_email = 'kjellmf@gmail.com',
      url = "http://www.fauskes.net/code/dot2tex/",
      download_url = "http://www.fauskes.net/code/dot2tex/download/",
      py_modules = ['dot2tex.dot2tex'],
      scripts=['dot2tex/dot2tex'],
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Text Processing :: Markup :: LaTeX',
        'Topic :: Utilities',
       ],
      install_requires = ['pyparsing','pydot'],
      # easy_install does not manage to install pyparsing from pypi,
      # so we have to provide the correct download link.
      dependency_links = [
          "http://sourceforge.net/project/showfiles.php?group_id=97203",
          "http://code.google.com/p/pydot/downloads/list"
      ],
      entry_points = {
          'console_scripts': [
              'dot2tex = dot2tex.dot2tex:main',
        ]
    
    }
)