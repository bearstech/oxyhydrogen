Oxyhydrogen
===========

Which ciphers are handled by this secure connection?

Install
-------

Install the _python-openssl_ package on Debian like Linux.

Install the _pyOpenSSL_ package on other OS. Be careful, on MacOS X, use openssl from brew, it's fresher.

Use
---

It works with any ssl server, not only HTTPS.

    ./cipher.py duckduckgo.com 443


More
----

https://briansmith.org/browser-ciphersuites-01.html

Todo
----

The code is ugly, some TLS test can be nice, too.

Licence
-------

3 terms BSD Licence © 2013 Mathieu Lecarme
