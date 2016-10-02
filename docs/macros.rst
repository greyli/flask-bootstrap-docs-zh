宏
===

.. highlight:: jinja

Flask-Bootstrap和macros（宏）一起让你的生活更简单。它们需要像下面的例子里这样导入::

  {% extends "bootstrap/base.html" %}
  {% import "bootstrap/wtf.html" as wtf %}

 这会以前缀 ``wtf`` 导入宏 ``wtf.html`` （这些在 :doc:`forms` 有一些讨论）。

除了这个页面上的较小的宏，对其他库也广泛支持。具体参见 :doc:`forms` 和 :doc:`sqlalchemy` 。


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

如果你想从外部配置Google Analytics的账户，可以这样 ::

  {{google.uanalytics(config['GOOGLE_ANALYTICS_ID'])}}


.. note:: 请确保你至少正确验证（pseudomize）你的用户ID。

官方不赞成使用的 `ga.js
<https://developers.google.com/analytics/devguides/collection/gajs/>`_ API
通过一个类似的叫做 ``analytics(account)`` 的宏被支持 ::

  {{google.analytics(account=config['GOOGLE_ANALYTICS_ID'])}}


Utilities
---------

一些额外的模板宏可以在 ``bootstrap/utils.html``
文件里获取。 和表单宏一样，这些是打算用来帮助快速开发应用的，在实际成熟的应用里，它们应该被合适的解决方案替换掉。

.. py:function:: flashed_messages(messages=None, container=True, transform=..., default_category=None, dismissible=False)

   渲染Flask的 :func:`~flask.flash` 消息。用常用的消息类别名称匹配稍不常用的Bootstrap CSS类名。
   （即： ``error -> danger`` ）

   :param messages: 一个消息的列表，如果没有给出，会使用
                    :func:`~flask.get_flashed_messages` 重新获取它们。
   :param container: 如果设为True，会输出一个完整的     。
                     ``<div class="container">`` 元素，否则只是每条消息被包裹进一个 ``<div>`` 里。
   :param transform: 一个匹配消息类别的字典。查询时对大小写敏感。
                     默认匹配所有Python loglevel级别的 *names*
                     到Bootdtrap CSS类。
   :param default_category: 如果一个类别在transform里没有匹配，那么它会被直接传入，不作改变。
                            而如果设置了 ``default_category`` ，那么将会被替换为这个值。
   :param dismissible: 如果设为True， 将会输出一个关闭按钮到消息上
                       如果想要完整功能的可关闭的消息提示，
                       你需要使用JavaScript消息提示（alert）插件。

需要注意的是，要想让这些工作正常，显示的消息必须匹配一个有效的bootstrap消息类别。（也就是 ``success`` ，
``info`` ， ``warning`` ， ``danger`` 之一。）

举例来说：

.. code-block:: python

    flash('Operation failed', 'danger')

3.3.5.7之前的Flask-Bootstrap的版本不对 ``flashed_messages`` 的内容进行转义，所以没法使用HTML。
这个规则已经改变了，现在推荐使用 ``Markup`` 包裹器，可以让消息里的HTML生效：

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

   在一个 ``<span>`` 元素里渲染Glyphicon。

   :param messages: 图片的短名字，比如 ``remove`` 。
   :param extra_classes: 添加到类属性的附加类的列表
   :param kwargs: 附加的HTML属性


.. py:function:: form_button(url, content, method='post', class='btn-link',\
                 **kwargs)

   渲染一个被表单包裹的按钮/链接。

   :param url: 要提交到的端点（endpoint）。
   :param content: 按钮元素的内容。
   :param method: 周围表单的 ``method`` 属性。
   :param class: 按钮元素的 ``class`` 属性。
   :param kwargs: 按钮元素的额外HTML属性。


一个方便的小方法，可以用来创建像删除按钮这样的东西，而不用使用 ``GET`` 请求。
一个例子 ::

  {{form_button(url_for('remove_entry', id=entry_id),
                icon('remove') + ' Remove entry')}}
