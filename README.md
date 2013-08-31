irccrypt
========

This is a library containing implementations of various cryptographic systems as used over IRC

This project was authored by Björn Edström and is documented [here](http://blog.bjrn.se/2009/01/proposal-for-better-irc-encryption.html)

This github repository exists solely to have somewhere to point pip at to provide automatic dependency management, and should not be added to the Cheese Shop.

Usage:

    setup(
        ...,
        install_requires=['irccrypt', ...],
        dependency_links=['https://github.com/predakanga/irccrypt/tarball/master#egg=irccrypt-0.1.1'],
    )