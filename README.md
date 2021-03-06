nodervers
=========

nodevers is a [**Node**.js][nodejs] **vers**ion manager.

### Prerequisites

To run nodevers you'll need:

* [Python][py]

And to build Node.js you'll need:

   * [GNU make][gmake] (3.81 or newer)

   * A C(++) compiler

   * Python (2.6 or 2.7)

   * libssl-dev (only if you want to build Node v0.6.x)

   * libexecinfo (only if you are using FreeBSD or OpenBSD)

### Installation

To install nodevers, simply run:

    $ pip install nodevers

Or if you have downloaded a zip/cloned from GitHub:

    $ python setup.py install

You'll also need to add either:


* `~/.nodevers/bin`

or

* `$NODEVERS_PREFIX/bin` if you have set the environment variable `NODEVERS_PREFIX`

or

* `/opt/nodevers/bin` if you run nodevers and install Nodes as root

to the `PATH`.

### Usage

Installing a Node:

    $ nodevers install 0.10.17

Switching to a Node:

    $ nodevers use 0.10.17

You can also pass arguments to Node's configure script during building:

    $ nodevers install 0.10.17 --buildargs="--gdb"

### License

nodevers is licensed under BSD (3-Clause) License.  
See the LICENSE file for the full license text.

[nodejs]: http://nodejs.org/
[py]: http://python.org/
[gmake]: http://www.gnu.org/software/make/
