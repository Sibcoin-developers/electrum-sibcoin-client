# Electrum-SIB - lightweight Sibcoin client

## Install

Electrum-SIB is a pure python application. However, if you want to use the
Qt interface, then you need to install the Qt dependencies

`sudo apt-get install python-qt4`

If you downloaded the official package (tar.gz), then you can run
Electrum-SIB from its root directory, without installing it on your
system; all the python dependencies are included in the 'packages'
directory. To run Electrum-SIB from its root directory, just do::

    ./electrum-sib

If you cloned the git repository, then you need to compile extra files
before you can run Electrum-SIB. Read the next section, "Development
Version".