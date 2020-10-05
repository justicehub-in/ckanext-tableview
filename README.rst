======================
ckanext-datatablesview
======================

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!

Source code for datatables implementation was forked from an official `CKAN Repository <https://github.com/ckan/ckan/tree/ckan-2.8.1/ckanext/datatablesview>`_

------------
Requirements
------------

Tested with CKAN Version 2.6 and 2.8


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-datatablesview:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Clone repository and install the ckanext-datatablesview Python package into your virtual environment::

     python setup.py install

3. Add ``table_view`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


------------------------
Development Installation
------------------------

To install ckanext-datatablesview for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/justicehub-in/ckanext-datatablesview.git
    cd ckanext-datatablesview
    python setup.py develop
