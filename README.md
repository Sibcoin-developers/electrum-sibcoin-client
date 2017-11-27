# Electrum-Sibcoin - lightweight Sibcoin client

[Homepage](https://sibcoin.money/)

![example sibcoin wallet](https://github.com/Sibcoin-developers/electrum-sibcoin-client/blob/master/sib-wallet-example.jpg)

## Getting started


Electrum-Sibcoin is a pure python application. However, if you want to use the
Qt interface, then you need to install the Qt dependencies:

    sudo apt-get install python-qt4

If you downloaded the official package (tar.gz), then you can run
Electrum-Sibcoin from its root directory, without installing it on your
system; all the python dependencies are included in the 'packages'
directory. To run Electrum-Sibcoin from its root directory, just do::

    ./electrum-sibcoin

If you cloned the git repository, then you need to compile extra files
before you can run Electrum-Sibcoin. Read the next section, "Development
Version".



## Development version


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
