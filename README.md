Oxyhydrogen
===========

Which ciphers are handled by this secure connection?

Install
-------

Install the _python-openssl_ package on Debian like Linux.

Install the _pyOpenSSL_ package on other OS. Be careful, on MacOS X, use openssl from brew, it's fresher but painful to install.

Use
---

It works with any ssl server, not only HTTPS.

    ./cipher.py duckduckgo.com 443


More
----

 * http://www.openssl.org/docs/apps/ciphers.html
 * https://briansmith.org/browser-ciphersuites-01.html
 * https://blog.thijsalkema.de/blog/2013/09/02/the-state-of-tls-on-xmpp-3/


Todo
----

The code is ugly.

Licence
-------

3 terms BSD Licence © 2013 Mathieu Lecarme
