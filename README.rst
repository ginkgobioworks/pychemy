PyChemy
=======

.. image:: https://travis-ci.org/ginkgobioworks/pychemy.svg?branch=master
    :target: https://travis-ci.org/ginkgobioworks/pychemy

Helpers for handling chemical formulas in Python. Mostly adopted from work of
`Christoph Gohlke <http://www.lfd.uci.edu/~gohlke/>`_. Added methods that are useful for mass spec
data analysis.

Depends on `Open Babel <http://openbabel.org/>`_ and its Python bindings for handling InChI strings.


Development
-----------

Development requires Docker and Make on your host system. Everything else, including Open Babel, is
taken care of inside the Docker containers.

Spin up your container using the provided ``docker-compose.yml`` file and ``Makefile`` by running
``make image``. This creates an image with a correct git configuration for your user, which makes it
easy to release. All of the commands you should need to run are defined the ``Makefile`` as targets.
All of the targets except for ``image``, are meant to be run inside the Docker container, but can be
run from the host machine by having ``-ext`` appended to them. For example, to run tests, you could
either call ``make test`` from a shell inside the container, or ``make test-ext`` from the host.

This project supports both Python 2 and Python 3. To test Python 3, make run the ``make
test`` and ``make test-ext`` with the ``TOXENV`` environment set to ``py3``, e.g.:

::

    TOXENV=py3 ./make test-ext


All pull requests are run through the Travis CI process specified in ``.travis.yml`` and must pass
all unit and doc tests in Python 2 and Python 3 before being accepted.

Deployment
----------

Deployment of tagged commits happens to PyPI automatically via Travis CI. To bump and deploy a new
version directly, you must have access to write to the master branch. Run ``make bump/[foo]-ext``,
where ``[foo]`` is ``major``, ``minor``, or ``patch``. Then ``git push origin --tags master``. If
you do not have access to the master branch, do the same thing, but in a separate branch, and make
a pull request.
