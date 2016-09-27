宏
===

.. highlight:: jinja

Flask-Bootstrap和macros（宏）一起让你的生活更简单。它们需要像下面的例子里这样导入::

  {% extends "bootstrap/base.html" %}
  {% import "bootstrap/wtf.html" as wtf %}

这会以前缀 ``wtf`` 导入宏 ``wtf.html`` 。
（这些在 :doc:`forms` 有一些讨论。）。

In addition to the small macros on this page, broad support for other libraries
is also available; see :doc:`forms` and :doc:`sqlalchemy` for details.


跨浏览器支持
-----------

跨浏览器支持（特别对Internet Explorer < 9的版本来说）通常是
必要的，但是Flask-Bootstrap没有附加这个功能。你可以下载 `html5shiv
<https://raw.github.com/aFarkas/html5shiv/master/dist/html5shiv.min.js>`_ 和
`Respond.js <https://raw.githubusercontent.com/scottjehl/Respond/master/dest/
respond.min.js>`_ ，把它们放在你程序的静态文件夹，然后像下面的例子那样包含它们 ::

  {% import "bootstrap/fixes.html" as fixes %}
  {% block head %}
    {{super()}}
    {{fixes.ie8()}}
  {% endblock %}


当这些脚本文件没有被包含的时候，会使用CDN链接。所以如果你没有使用
 ``BOOTSTRAP_SERVE_LOCAL`` ，它们会自动生效。具体见 :doc:`cdn`
这里有关于Flask-Bootstrap如何实现CDN设置的细节。


Google Analytics
----------------

`Google Analytics <http://www.google.com/analytics/>`_  的API最近变化的相当快，目前
`analytics.js <https://developers.google.com/analytics/devguides/collection/analyticsjs/>`_
是受支持最好的，使用 ``uanalytics(id, options='auto')`` 宏 ::

  {% import "bootstrap/google.html" as google %}

  {% block scripts %}
    {{super()}}
    {{google.uanalytics('U-XXXX-YY')}}
  {% endblock %}

可以传入选项给js函数 ``ga()`` 调用, 比如说利用
`User ID <https://developers.google.com/analytics/
devguides/collection/analyticsjs/user-id>`_ 特性 ::

  {{google.uanalytics('U-XXXX-YY', {'userId': 'myUser'})}}

如果你想从外部配置Google Analytics的账户，你可以这样 ::

  {{google.uanalytics(config['GOOGLE_ANALYTICS_ID'])}}


.. note:: 请确保你至少pseudomize user ids properly.

The officially deprecated `ga.js
<https://developers.google.com/analytics/devguides/collection/gajs/>`_ API
support is also available supported through a similarly named macro
``analytics(account)``::

  {{google.analytics(account=config['GOOGLE_ANALYTICS_ID'])}}


Utilities
---------

A few extra template macros are available in the ``bootstrap/utils.html``
file. Like the form macros, these are intended to aid rapid application
development, until they are replaced with custom solutions in more mature
applications.

.. py:function:: flashed_messages(messages=None, container=True, transform=..., default_category=None, dismissible=False)

   Renders Flask's :func:`~flask.flash` messages. Maps commonly used categories
   to the slightly uncommon bootstrap css classes (i.e. ``error -> danger``).

   :param messages: A list of messages. If not given, will use
                    :func:`~flask.get_flashed_messages` to retrieve them.
   :param container: If true, will output a complete
                     ``<div class="container">`` element, otherwise just the
                     messages each wrapped in a ``<div>``.
   :param transform: A dictionary of mappings for categories. Will be looked up
                     case-insensitively. Default maps all Python loglevel
                     *names* to bootstrap CSS classes.
   :param default_category: If a category does not has a mapping in transform,
                            it is passed through unchanged. If
                            ``default_category`` is set, it is replaced with
                            this instead.
   :param dismissible: If true, will output a button to close an alert.
                       For fully functioning, dismissible alerts,
                       you must use the alerts JavaScript plugin.

Note that for this functionality to work properly, flashing messages must be
categorized with a valid bootstrap alert category (one of ``success``,
``info``, ``warning``, ``danger``).

Example:

.. code-block:: python

    flash('Operation failed', 'danger')

Versions of Flask-Bootstrap pre-3.3.5.7 did not escape the content of
``flashed_messages`` to allow HTML to be used. This behaviour has changed, the
preferred way to utilize HTML inside messages now is by using the
``Markup``-wrapper:


.. code-block:: python

    from flask import flash
    from markupsafe import Markup

    # ...

    flash(Markup('Flashed message with <b>bold</b> statements'), 'success')

    user_name = '<b>ad username'
    flash(Markup('<u>You</u> are our favorite user, <i>'
                 + user_name
                 + Markup('</i>!'),
         'danger')

.. py:function:: icon(type, extra_classes, **kwargs)

   Renders a Glyphicon in a ``<span>`` element.

   :param messages: The short name for the icon, e.g. ``remove``.
   :param extra_classes: A list of additional classes to add to the class
                         attribute.
   :param kwargs: Additional html attributes.


.. py:function:: form_button(url, content, method='post', class='btn-link',\
                 **kwargs)

   Renders a button/link wrapped in a form.

   :param url: The endpoint to submit to.
   :param content: The inner contents of the button element.
   :param method: ``method``-attribute of the surrounding form.
   :param class: ``class``-attribute of the button element.
   :param kwargs: Extra html attributes for the button element.


A handy little method to create things like delete-buttons without using
``GET`` requests. An example::

  {{form_button(url_for('remove_entry', id=entry_id),
                icon('remove') + ' Remove entry')}}
