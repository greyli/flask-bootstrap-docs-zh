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


你也可以在 `GitHub <https://github.com>`_ 上查找之前的版本标签。
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

URL端点（url-endpoint） ``bootstrap.static`` 可以让你引用Bootstrap资源文件，但通常不需要这样。
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

然而，你经常只是想快速生成一个表单，而且不需要过度的微调，这时可以直接使用 ``quick_form`` 宏::

  {{ wtf.quick_form(form) }}

配置选项
*********

这里有一些模板使用的配置选项:

====================================== ======================================================== ===
选项                                    默认值
====================================== ======================================================== ===
``BOOTSTRAP_USE_MINIFIED``             ``True``                                                 是否使用压缩过的css/js文件。
``BOOTSTRAP_JQUERY_VERSION``           ``'1'``                                                  模板里这个版本的jQuery通过Google的CDN加载。另外提一下 ``BOOTSTRAP_USE_MINIFIED`` ，把这个值设为None会不加载jQuery。要注意的是未压缩的Bootstrap资源在Boostrap的CDN上有时会丢失，所以在没有打开 ``BOOTSTRAP_USE_MINIFIED`` 时最好不要用它。
``BOOTSTRAP_HTML5_SHIM``               ``True``                                                 加载默认的IE兼容性修复文件，这些文件通常在使用bootstrap时被加载。
``BOOTSTRAP_GOOGLE_ANALYTICS_ACCOUNT`` ``None``                                                 如果设置，使用这个账号加载 `Google Analytics <http://www.google.com/analytics>`_ 模板文件（boilerplate）。
``BOOTSTRAP_USE_CDN``                  ``False``                                                如果设为 ``True`` ，Bootstrap资源将不会从本地应用实例加载，而是使用CDN（使用 ``BOOTSTRAP_CDN_BASEURL`` 配置）。
``BOOTSTRAP_CDN_BASEURL``              用匹配到 ``cdnjs.com`` 的CDN地址建立的字典。                当使用CDN时要添加的Bootstrap和其他文件名的CDN地址。
``BOOTSTRAP_CDN_PREFER_SSL``           ``True``                                                 如果 ``BOOTSTRAP_CDN_BASEURL`` 以 ``//`` 开头，会在之前添加 ``'https:'`` 。
``BOOTSTRAP_CUSTOM_CSS``               ``False``                                                如果设为 ``True`` ，将不会加载Bootstrap的CSS文件。如果你编写了一个自定义的css文件，其中已经包含了bootstrap，可以使用这个选项。
``BOOTSTRAP_QUERYSTRING_REVVING``      ``True``                                                 如果设为 ``True`` ，会添加一个包含当前所有本地静态文件版本的查询字符串。这会确保一旦升级Flask-Bootstrap，这些文件就会被更新。
====================================== ======================================================== ===

.. _FontAwesome: http://fortawesome.github.com/Font-Awesome/

安装
****

你可以使用 ``pip`` 从GitHub或是从 `PyPI
<http://pypi.python.org/pypi/Flask-Bootstrap>`_ 安装。

版本笔记
*********

Flask-Bootstrap 尝试跟随Bootstrap更新的脚步。版本变化通常
在 ``Bootstrap version`` 和 ``Flask-Bootstrap iteration`` 里。举例来说，
版本 ``2.0.3.2`` 集成了Bootstrap ``2.0.3`` 版本，并且是Flask-Bootstrap集成这个版本的第二次更新。

如果你需要让你的模板不改变，那么在你的setup.py里固定版本就可以了。

FAQ
***

1. 为什么在我的模板输出里有我不想出现的自动转义？
   确保你的模板文件后缀为 ``.htm`` ， ``.html`` ， ``.xml`` 或是 ``.xhtml`` 。
   Flask依据模板文件扩展名来设置Jinja2自动转义模式（更多信息见 `这个StackOverflow问题
   <http://stackoverflow.com/questions/13222925/how-do-i-enable-autoescaping-in-templates-with-a-jhtml-extension-in-flask>`_
   ）。

   尽管如此，一般的约定是在你的Flask应用里使用 ``.html`` 后缀来命名你的HTML模板。

2. 我怎么向模板添加自定义的JavaScript？

   使用Jinjia2的 ``super()`` 连同 ``bootstrap_js_bottom`` 块。这个super函数从父模板
   添加块的内容，这种方式甚至可以让你决定是否想要在jQuery/bootstrap之前或之后加载。举例来说::

     {% block bootstrap_js_bottom %}
       {{super()}}
       <script src="my_app_code.js">
     {% endblock %}


3. 我在部署时如何加载静态文件？

   Flask-Bootstrap只是简单的添加一个叫 ``bootstrap`` 的蓝本，在这个意义上来说，它并不特别。
   静态文件被匹配到一个特殊的URL前缀（默认为 ``static/bootstrap`` ）而且通过一个特定的文件夹提供，
   这个文件夹可以在你的virtualenv安装包里找到（比如 ``lib/python2.7/site-packages/flask_bootstrap/static`` ），
   所以一个典型的安装将会是设定你的web服务器服务上面提到的文件夹的地址。

   一个更优雅的解决方案是在WSGI服务器前放置一个缓存来处理 ``Cache-Control`` 报头。
   默认情况下，Flask会在加载静态文件时附带一个12小时的过期时间
   （你可以使用 ``SEND_FILE_MAX_AGE_DEFAULT`` 改变这个值），这应该足够了。

   这个方案可以使用 `nginx <http://nginx.org>`_
   （或者，也许你更喜欢 `Varnish <http://varnish-cache.org>`_ ）或者他们的基于
   相同工具的云服务应该也足够了。Flask-Bootstrap2.3.2.2通过提供查询字符串加速支持这些，
   这确保当你更新Flask-Bootstrap时，更新版本的Bootstrap会被加载。
   （查看 ``BOOTSTRAP_QUERYSTRING_REVVING`` ）


变更记录
~~~~~~~~~


参见 :doc:`changelog` ，那里有包括版本2的变更记录。
