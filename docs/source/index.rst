Myservice
=========


**myservice** is a simple JSON Flask application.

The application is created with :class:`Flask`:

.. literalinclude:: ../../myservice/app.py


The :file:`settings.ini` file which is passed to :class:`Config`
contains options for running the Flask app:

.. literalinclude:: ../../myservice/settings.ini
   :language: ini


The :file:`.env` file which is passed to :func:`run`
contains options for running the Flask app that are environment specific:

.. literalinclude:: ../../myservice/.env
   :language: ini

Blueprint are imported from :mod:`myservice.views` and one
Blueprint and view example was provided in :file:`myservice/views/home.py` and :file:`myservice/views/hello.py`:

.. literalinclude:: ../../myservice/views/home.py
   :name: home.py
   :emphasize-lines: 14


Views can return simple mappings (as highlighted in the example above),
in that case they will be converted into a JSON response.

.. toctree::
   :maxdepth: 2

   api
