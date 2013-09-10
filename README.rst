nodevers
========

nodevers is a **Node**.js **vers**\ ion manager.

Prerequisites
-------------
To run nodevers you'll need:

* `Python`_ (2.6 or 2.7)

And to build Node you'll need:

* `GNU make`_ (3.81 or newer)

* A C(++) compiler

* Python (2.6 or 2.7)

* libssl-dev **(only if you want to build Node v0.6.x)**

* libexecinfo **(only if you are using FreeBSD or OpenBSD)**

Installation
------------
To install nodevers, simply run:

::

    $ pip install nodevers

Or if you have downloaded the zip/cloned from GitHub:

::

    $ python setup.py install

You'll also need to add either:

* ``~/.nodevers/bin``

or

* ``$NODEVERS_PREFIX/bin`` if you have set the environment variable ``NODEVERS_PREFIX``

or

* ``/opt/nodevers/bin`` if you run nodevers and install Nodes as root

to the ``PATH``.

Usage
-----
Listing all the Nodes available for installation:

::

    $ nodevers install -l

Installing a Node:

::

    $ nodevers install 0.10.18

Setting the default Node version:

::

    $ nodevers use 0.10.18

You can also pass arguments to Node's configure script during building:

::

    $ nodevers install 0.10.18 --buildargs="--gdb"

License
-------
nodevers is licensed under BSD (3-Clause) License.
See the LICENSE file for the full license text.

.. _`Python`: http://python.org/
.. _`GNU make`: http://www.gnu.org/software/make/