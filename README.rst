Installation
------------

Firstly, install postgreSQL and create a DB. Then, write in your terminal:

.. code-block :: pycon

    >>> pip install -r requirements.txt
    >>> DATABASE_URL="postgresql://localhost/[name]"
    >>> export APP_SETTINGS="config.Congig"

Then run ``python app.py``. Voila!

