<p align="center">
  <a href="https://github.com/morelo-network/Morelo-GUI">
    <img src="https://i.imgur.com/QUho6b1.jpg" alt="Logo" align="center" width="100%">
  </a>
</p>




### Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Pre Requirementss](#pre-requirements)
* [Usage](#script-usage)
* [Contact](#contact)




### About The Project

Standard Morelo wallet application is console-based application, and this is reason why it's sometimes hard to use it. Our team created this easy to use, user friendly and nice looking GUI wallet for Morelo cryptocurrency. Wallet is providing basic functionallity to receieve and send your founds. For advanced users it's recommended to use wallet CLI instead. 

Why you should use it?
* Is user friendly. Everyone can setup wallet in secs!
* Easy to setup, just download the binary and launch It.
* Nice looking UI is porn for your eyes.
* Provide basic functionallit, which is enough for most users.

Of course that wallet doesn't giving you full control of Morelo wallet, but giving you enough features for basic usage. If you have any suggestions you can pull a request and i will review that.

### Built With
* [Python 3.7](https://www.python.org/downloads/)
* [PyQt 5](https://pypi.org/project/PyQt5/)
* [QrCode](https://pypi.org/project/qrcode/)


### Getting Started

1) Download latest Morelo-GUI release.
2) Download latest Morelo binaries.
3) Unpack both with any archive unpacker in same folder.
4) Run Morelo-GUI.
5) Follow steps in application to create or open existing wallet.

### Pre Requirements

If you want run Morelo GUI script by self or you using other OS than windows you need that things:

* [Python 3.x](https://www.python.org/downloads/)

Download, run installator and follow installation steps.

* [Latest Morelo binaries](https://github.com/MoreloNetwork/morelo/releases)

Download and unpack binaries (morelod, morelo-wallet-rpc) in same folder as script.

* PyQt 5
* QrCode
* Requests
* Psutil

Open your terminal and type commands above to install required packages:
```sh
python -m pip install PyQt5
python -m pip install qrcode[pil]
python -m pip install requests
python -m pip install psutil
```
If some another package is missed, script will tell you during execution.


### Script usage
```sh
python Morelo-GUI.py [--offline]

Arguments:

--offline     Optional, runs wallet in offline mode. Generally for debuging purposes
```


## Contact

MrKris7100 (Dev) - E-mail: mrkris7100@gmail.com - [Discord](https://discordapp.com/): Mrkris7100#0810

Project Link: [https://github.com/MoreloNetwork/Morelo-GUI](https://github.com/MoreloNetwork/Morelo-GUI)
