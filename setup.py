#!/usr/bin/env python2

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp
import argparse

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum-SIB requires Python version >= 2.7.0...")

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root=', dest='root_path', metavar='dir', default='/')
    opts, _ = parser.parse_known_args(sys.argv[1:])
    usr_share = os.path.join(sys.prefix, "share")
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
            not os.access(opts.root_path, os.W_OK):
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['$XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-sib.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-dash.png'])
    ]

setup(
    name="Electrum-SIB",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes',
        'ecdsa',
        'pbkdf2',
        'requests',
        'qrcode',
        'dnspython',
        'jsonrpclib',
        'trezor',
    ],
    dependency_links=[
        'git+https://github.com/ivansib/x11_gost_hash',
        'git+https://github.com/trezor/python-trezor@v0.6.13#egg=trezor',
        'git+https://github.com/keepkey/python-keepkey@v0.7.2#egg=keepkey',
        'git+https://github.com/LedgerHQ/btchip-python.git@v0.1.17#egg=btchip',
    ],
    packages=[
        'electrum_sib',
        'electrum_sib_gui',
        'electrum_sib_gui.qt',
        'electrum_sib_plugins',
        'electrum_sib_plugins.audio_modem',
        'electrum_sib_plugins.cosigner_pool',
        'electrum_sib_plugins.email_requests',
        'electrum_sib_plugins.exchange_rate',
        'electrum_sib_plugins.hw_wallet',
        'electrum_sib_plugins.keepkey',
        'electrum_sib_plugins.labels',
        'electrum_sib_plugins.ledger',
        'electrum_sib_plugins.plot',
        'electrum_sib_plugins.trezor',
        'electrum_sib_plugins.virtualkeyboard',
    ],
    package_dir={
        'electrum_sib': 'lib',
        'electrum_sib_gui': 'gui',
        'electrum_sib_plugins': 'plugins',
    },
    package_data={
        'electrum_sib': [
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ]
    },
    scripts=['electrum-sibcoin'],
    data_files=data_files,
    description="Lightweight Sibcoinpay Wallet",
    author="serbernar",
    license="MIT License",
    url="https://sibcoin.money",
    long_description="""Lightweight Sibcoin Wallet"""
)
