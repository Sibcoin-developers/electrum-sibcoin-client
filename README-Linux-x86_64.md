### Electrum-SIB - lightweight multi-coin client
Electrum-SIB provides a basic SPV wallet for Sibcoinpay. It is a BIP-0044-compliant wallet based on the original Electrum for Bitcoin. This Electrum-SIB client uses Electrum servers to retrieve necessary blockchain headaer & transaction data, so no "Electrum-SIB server" is necessary.

Because of the Simplified Payment Verification nature of the wallet, services requiring Masternode communications, such as DarkSend and InstantX are not available.

Homepage: https://sibcoin.money




1. ELECTRUM_SIB ON LINUX
----------------------

 - Installer package is provided at https://sibcoin.money
 - To download and use:
    ```
    cd ~
    wget https://sibcoin.money/releases/v2.4.1/Electrum-SIB-2.4.1-Linux_x86_64.tgz
    tar -xpzvf Electrum-SIB-2.4.1-Linux_x86_64.tgz
    cd Electrum-SIB-2.4.1
    ./electrum-sibcoin_x86_64.bin
    ```


Once successfully installed simply type
   ```
   electrum-sibcoin
   ```
   Your wallets will be located in /home/YOUR_LOGIN_NAME/.electrum-sibcoin/wallets

Installation on 32bit machines is best achieved via github master or TAGGED branches

2. HOW OFFICIAL PACKAGES ARE CREATED
------------------------------------

See contrib/electrum-sibcoin-release/README.md for complete details on mazaclub release process

