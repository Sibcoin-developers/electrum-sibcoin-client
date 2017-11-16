Electrum-SIB - lightweight Sibcoin client
==========================================

::

  Licence: MIT Licence
  Original Author: Thomas Voegtlin
  Port Maintainer: Tyler Willis, Holger Schinzel
  Language: Python
  Homepage: https://sibcoin.money/


.. image:: https://travis-ci.org/sibpay/electrum-sib.svg?branch=master
    :target: https://travis-ci.org/sibpay/electrum-sib
    :alt: Build Status





Getting started
===============

![alt text](http://url/to/img.png)

Electrum-SIB is a pure python application. However, if you want to use the
Qt interface, then you need to install the Qt dependencies::

    sudo apt-get install python-qt4

If you downloaded the official package (tar.gz), then you can run
Electrum-SIB from its root directory, without installing it on your
system; all the python dependencies are included in the 'packages'
directory. To run Electrum-SIB from its root directory, just do::

    ./electrum-sibcoin

If you cloned the git repository, then you need to compile extra files
before you can run Electrum-SIB. Read the next section, "Development
Version".



Development version
===================

Check out the code from Github::

    git clone git://github.com/sibpay/electrum-sib.git
    cd electrum-sib

Run install (this should install dependencies)::

    python setup.py install

Compile the icons file for Qt::

    sudo apt-get install pyqt4-dev-tools
    pyrcc4 icons.qrc -o gui/qt/icons_rc.py

Compile the protobuf description file::

    sudo apt-get install protobuf-compiler
    protoc --proto_path=lib/ --python_out=lib/ lib/paymentrequest.proto

Create translations::

    sudo apt-get install python-pycurl gettext
    ./contrib/make_locale



Install on Linux systems
========================

If you install Electrum-SIB on your system, you can run it from any
directory.

If you have pip, you can do::

    python setup.py sdist
    sudo pip install --pre dist/Electrum-SIB-2.0.tar.gz


If you don't have pip, install with::

    python setup.py sdist
    sudo python setup.py install



Creating Binaries
=================


In oder to creating binaries, you must create the 'packages' directory::

    ./contrib/make_packages

This directory contains the python dependencies used by Electrum-SIB.

Mac OS X
--------

    # On port based installs
    sudo python setup-release.py py2app

    # On brew installs
    ARCHFLAGS="-arch i386 -arch x86_64" sudo python setup-release.py py2app --includes sip

    sudo hdiutil create -fs HFS+ -volname "Electrum-SIB" -srcfolder dist/Electrum-SIB.app dist/electrum-sib-VERSION-macosx.dmg


Windows
-------

see contrib/build-wine/README


Android
-------

see gui/kivy/Readme.txt
