使用 Bootstrap 2
================

目前Bootstrap主要的稳定版本是3，它不向后兼容Bootstrap2。除了版本3，Flask-Bootstrap
继续支持Bootstrap2的最新版本。（不过你不要期待有新特性，只是修正了漏洞而已。）

安装
-----

通过安装Flask-Bootstrap，你将总是得到最新版本，即Boostrap3。要安装（或是保持）Flask-Bootstrap 2，
你必须在你的 ``setup.py`` 或 ``requirements.txt`` 里指定版本，类似这样::

    # other stuff in setup.py...
    install_requires=['flask-bootstrap<3', 'another_package']

把Flask-Bootstrap固定为一个明确的版本是个好主意（例如 ``'flask-bootstrap==2.3.2.2'`` ，以此来避免生产环境中的意外）。

文档
-----

在版本3之前，Flask-Bootstrap只有一个README文件来作为文档。你可以在下面找到整个文件。


你也可以在 `github <https://github.com>`_ 上查找之前的版本标签。
要看主要的版本2的代码或样例程序，在这里 `2.3.2.2 <https://github.com/mbr/flask-bootstrap/tree/2.3.2.2>`_ 。

Flask-Bootstrap
^^^^^^^^^^^^^^^

Flask-Bootstrap 把 `Bootstrap <http://getbootstrap.com>`_ 打包进一个
扩展，这个扩展主要由一个叫“bootstrap”的蓝本（blueprint）组成。它也可以创建链接从一个CDN上引用Bootstrap。


用法
****

这儿是一个例子::
Here is an example::

  from flask_bootstrap import Bootstrap

  [...]

  Bootstrap(app)

这让一些新的模板可供使用，主要是 ``bootstrap_base.html`` 和 ``bootstrap_responsive.html`` 。
这些是包含所有bootstrap资源文件和预定义块（你可以在块里放你的内容）的空白页。要修改的核心块是 ``body_content`` ，
另外查看模板的源码寻找更多可能性。

url端点（url-endpoint） ``bootstrap.static`` 可以让你引用Bootstrap资源文件，但通常不需要这样。
更好的做法是使用 ``bootstrap_find_resource`` 模板过滤器，它会负责设置CDN。

宏
****

.. highlight:: jinja

一些可供使用的宏可以让你的生活更加简单。这些需要被导入（我建议创建你自己的“base.html”模板，
首先扩展bootstrap的基模板，然后在那里包含这个宏）。

一个“base.html”的例子::

  {% extends "bootstrap_responsive.html" %}
  {% import "bootstrap_wtf.html" as wtf %}

表单
~~~~

``bootstrap/wtf.html`` 模板包含了帮助你快速输出表单的宏。
最基本的方式是把它们作为手动创建表单的助手::

  <form class="form form-horizontal" method="post">
    {{ form.hidden_tag() }}
    {{ wtf.form_errors(form, "only") }}

    {{ wtf.horizontal_field(form.field1) }}
    {{ wtf.horizontal_field(form.field2) }}

    <div class="form-actions">
       <button name="action_save" type="submit" class="btn btn-primary">Save changes</button>
    </div>
  </form>

然而，你经常只是想快速生成一个表单，而且不需要过度的微调::


::

  {{ wtf.quick_form(form) }}

配置选项
*********

这里有一些模板使用的配置选项:

====================================== ======================================================== ===
选项                                    默认值
====================================== ======================================================== ===
``BOOTSTRAP_USE_MINIFIED``             ``True``                                                 是否使用压缩过的css/js文件。
``BOOTSTRAP_JQUERY_VERSION``           ``'1'``                                                  This version of jQuery is included in the template via Google CDN. Also honors ``BOOTSTRAP_USE_MINIFIED``. Set this to ``None`` to not include jQuery at all. Note that non-minified Bootstrap resources are sometimes missing on bootstrapcdn, so it is best not to use it without turning on ``BOOTSTRAP_USE_MINIFIED``.
``BOOTSTRAP_HTML5_SHIM``               ``True``                                                 Include the default IE-fixes that are usually included when using bootstrap.
``BOOTSTRAP_GOOGLE_ANALYTICS_ACCOUNT`` ``None``                                                 If set, include `Google Analytics <http://www.google.com/analytics>`_ boilerplate using this account.
``BOOTSTRAP_USE_CDN``                  ``False``                                                If ``True``, Bootstrap resources will no be served from the local app instance, but will use a Content Delivery Network instead (configured by ``BOOTSTRAP_CDN_BASEURL``).
``BOOTSTRAP_CDN_BASEURL``              A dictionary set up with URLs to ``cdnjs.com``.          The URLs to which Bootstrap and other filenames are appended when using a CDN.
``BOOTSTRAP_CDN_PREFER_SSL``           ``True``                                                 如果 ``BOOTSTRAP_CDN_BASEURL`` 以 ``//`` 开头，会在之前添加 ``'https:'`` 。
``BOOTSTRAP_CUSTOM_CSS``               ``False``                                                If ``True``, no Bootstrap CSS files will be loaded. Use this if you compile a custom css file that already includes bootstrap.
``BOOTSTRAP_QUERYSTRING_REVVING``      ``True``                                                 If ``True``, will apppend a querystring with the current version to all static resources served locally. This ensures that upon upgrading Flask-Bootstrap, these resources are refreshed.
====================================== ======================================================== ===

.. _FontAwesome: http://fortawesome.github.com/Font-Awesome/

安装
****

你可以使用 ``pip`` 从github或是从 `PyPI
<http://pypi.python.org/pypi/Flask-Bootstrap>`_ 安装。

版本笔记
*********

Flask-Bootstrap 尝试跟随Bootstrap更新的脚步。版本变化通常
在 ``Bootstrap version`` 和 ``Flask-Bootstrap iteration`` 里。举例来说，
版本 ``2.0.3.2`` 集成了Bootstrap ``2.0.3`` 版本，并且是Flask-Bootstrap集成这个 版本的第二次更新。

如果你需要让你的模板不改变，那么在你的setup.py里固定版本就可以了。

FAQ
***

1. 为什么在我的模板输出里有我不想出现的自动转义？
   确保你的模板文件后缀为 ``.htm`` ， ``.html`` ， ``.xml`` 或是 ``.xhtml`` 。
   Flask依据模板文件扩展名来设置Jinja2自动转义模式（更多信息见： `this StackOverflow question
   <http://stackoverflow.com/questions/13222925/how-do-i-enable-autoescaping-in-templates-with-a-jhtml-extension-in-flask>`_
   ）。

   尽管一般的约定是在你的Flask应用里使用 ``.html`` 后缀来命名你的HTML模板。

2. 我怎么向模板添加自定义的jacascript？

   使用Jinjia2的 ``super()`` 连同 ``bootstrap_js_bottom`` 块。这个super函数从父模板
   添加块的内容，这种方式甚至可以让你决定是否想要在jQuery/bootstrap之前或之后加载。举例来说::

     {% block bootstrap_js_bottom %}
       {{super()}}
       <script src="my_app_code.js">
     {% endblock %}


3. 我如何在部署时服务静态文件？
How do I serve the static files in deployment?

   Flask-Bootstrap只是简单的添加一个叫 ``bootstrap`` 的蓝本，从这个意义上来说，它并不特别。
   静态文件被匹配到一个特殊的URL前缀（）
   Flask-Bootstrap is not special in the sense that it simply adds a blueprint
   named ``bootstrap``. The static files map to a specific URL-prefix (per
   default ``static/bootstrap`` and are served from a specific directory
   found in your virtualenv installation (e.g.
   ``lib/python2.7/site-packages/flask_bootstrap/static``), so a traditional
   setup would be setting up your webserver to serve this address from the
   mentioned directory.

   A more elegant approach is having a cache in front of the WSGI server that
   respects ``Cache-Control`` headers. Per default, Flask will serve static
   files with an expiration time of 12 hours (you can change this value using
   the ``SEND_FILE_MAX_AGE_DEFAULT``), which should be sufficient.

   For this approach `nginx <http://nginx.org>`_ (or, if you prefer,
   `Varnish <http://varnish-cache.org>`_) or their cloud-service based
   equivalents should suffice. Flask-Bootstrap 2.3.2.2 supports this by
   offering querystring revving (see ``BOOTSTRAP_QUERYSTRING_REVVING``) to
   ensure newer Bootstrap versions are served when you upgrade Flask-Bootstrap.


变更记录
~~~~~~~~~


参见 :doc:`changelog` ，那里有包括版本2的变更记录。
