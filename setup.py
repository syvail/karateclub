from distutils.core import setup
setup(
  name = "KarateClub",
  packages = ["KarateClub"],
  version = "0.1",
  license = "MIT",
  description = "A general purpose library for community detection research.",
  author = "Benedek Rozemberczki",
  author_email = "benedek.rozemberczki@gmail.com",
  url = "https://github.com/benedekrozemberczki/KarateClub",
  download_url = "https://github.com/benedekrozemberczki/KarateClub/archive/v_01.tar.gz",
  keywords = ["community", "detection", "networkx", "graph", "clustering"],
  install_requires=[
          "numpy",
      ],
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.5",
  ],
)