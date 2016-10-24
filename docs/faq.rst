FAQ
===


为什么在我的模板输出里有我不想出现的自动转义？
-------------------------------------------

确保你的模板文件后缀为 ``.htm`` ， ``.html`` ， ``.xml`` 或是 ``.xhtml`` 。
Flask依据模板文件扩展名来设置Jinja2自动转义模式（更多信息见 `这个StackOverflow问题
<http://stackoverflow.com/questions/13222925/how-do-i-enable-autoescaping-in-templates-with-a-jhtml-extension-in-flask>`_ ）。

尽管如此，一般的约定是在你的Flask应用里使用 ``.html`` 后缀来命名你的HTML模板。


我怎么向模板添加自定义的jacascript？
-----------------------------------
.. highlight:: jinja

使用Jinjia2的 super_ 连同 ``scripts`` 块。这个super函数从父模板
添加块的内容，这种方式甚至可以让你决定是否想要在jQuery/bootstrap之前或之后加载。举例来说::

  {% block bootstrap_js_bottom %}
    {{super()}}
    <script src="my_app_code.js">
  {% endblock %}


为什么Bootstrap的javascript不加载？
----------------------------------

一个容易忽视的小错误是块名：尽管有一个块叫 ``body`` ，但它通常不是你想替换的那个，
你应该使用 ``content`` 。 一般地，javascript默认在 ``<body>`` 标签的 `最后
<https://stackoverflow.com/questions/436411/where-is-the-best-place-to-put-
script-tags-in-html-markup>`_ 加载 ）。

:ref:`block-names` 有更多具体内容。


我如何向头部（header）添加自定义内容？
-------------------------------------

一个经常冒出来的问题是如何添加自定义的内容到 ``<head>`` 元素，像 ``<link>`` 标签或是网站头像（favicon）。
通过使用 super_ 函数，这也很容易实现::

  {% block head %}
  {{super()}}
  <link rel="icon" type="image/png" href="http://example.com/myicon.png">
  {% endblock %}

这会刚好在关闭的 ``</head>`` 上面添加你想要的内容。
另一个用于大型项目的方法是创建一个新的基模板，然后自己添加需要的块::


  {% block head %}
  {{super()}}
  {% block favicon %}<!-- 默认的网站头像（favicon）可以放到这里 -->{% endblock %}
  {% block feeds %}{% endblock %}
  {% endblock %}

然后，这个基模板的子模板可以使用这些块去指定一个自定义的feed或网站头像（favicon）。


我如何添加一个尾部（footer）？
--------------------------------

``super()`` 函数也可以被用来扩展任何已经被定义的块。
为确定的样式创建另一个衍生的基模板通常是一个好主意。
一个例子 ``with-footer.html``::


    {% extends "bootstrap/base.html" %}

    {%- block content %}
    {{super()}}
    {%- block footer %}
    <footer>&copy; 2016 Awesome, Inc.</footer>
    {%- endblock footer %}
    {%- endblock content %}

所有扩展自 ``with-footer.html`` 的模板的 ``footer`` 块都将被覆盖。


我在部署时如何加载静态文件？
--------------------------

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


我如何使用Bootstrap2/3？
-----------------------
.. highlight:: python

目前Bootstrap主要的稳定版本是3，很不幸，它不向后兼容Bootstrap2。除了版本3，Flask-Bootstrap
继续支持Bootstrap2的最新版本，（不过你不要期待有新特性，只是修正了漏洞而已。）当然，还有Bootstrap3。

通过安装Flask-Bootstrap，你将总是得到最新版本，即Boostrap3。要安装（或是保持）Flask-Bootstrap 2，
你必须在你的 ``setup.py`` 或 ``requirements.txt`` 里指定版本，类似这样::

  # other stuff in setup.py
  # ...
  install_requires=['flask-bootstrap<3', 'another_package']
  # ...

把Flask-Bootstrap固定为一个明确的版本是个好主意（例如 ``'flask-bootstrap==2.3.2.2'`` ，以此来避免生产环境中的意外）。

更多细节见 :doc:`bootstrap2` 文档。


FontAwesome在哪里？
------------------
.. highlight:: jinja

使用Bootstrap2的Flask-Bootstrap版本包含了 FontAwesome_ ，这对Flask-Bootstrap3和更高版本不再是一个问题。

起初，Bootstrap确实自带了基于图片的图标，不过它缩放的不好，
FontAwesome通过提供一个基于矢量图的替代品和附加的图标修正了这个问题。
然而，从Bootstrap3开始，图标被作为字体再次包含了进来，基于这个原因FontAwesome被从扩展里去掉了，以便简化内容。

今天， FontAwesome_ 不再是唯一的选择，网上有一个对可选替代品的 `比较
<http://tagliala.github.io/vectoriconsroundup/>`_ 。

如果你仍然想要使用FontAwesome，通过在你的继承自基模板的模板里增加style块，你可以很容易的包含它::

  {% block styles -%}
  {{super()}}
  <link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet">
  {% endblock styles %}

..  _FontAwesome: http://fontawesome.io
.. _super: http://jinja.pocoo.org/docs/templates/#super-blocks


.. _jquery-faq:

为什么你附带了jQuery1而不是jQuery2？
-----------------------------------

在我写这篇文档的时候（2014年七月），在jQuery1和2之间有两个主要的区别：版本1支持IE6-8，
然而版本2放弃了这些对支持旧版本的支持，换来了一个更小的内存占用和一下性能提升。市面上至少有20%
的浏览器（来源 `NetMarketShare
<http://www.netmarketshare.com /browser- market-
share.aspx?qprid=2&qpcustomd=0>`_ ）仍然含有不被jQuery2支持的版本。


除非你有特别需要，jQuery2的优点仍然不会大过它对市面上五分之一浏览器的不支持。
最后，Bootstrap和jQuery都是为了简化建站时处理问题的难度，而且这个目标能更好的达到，
离不开对jQuery1的广泛支持。


我如何使用jQuery2而不是jQuery1？
---------------------------------

.. highlight:: python

你可以使用Flask-Bootstrap的CDN支持来从不同的来源加载这些资源::

  from flask_bootstrap import WebCDN
  app.extensions['bootstrap']['cdns']['jquery'] = WebCDN(
      '//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/'
  )

这会加载 ``jquery.js`` 或任何指定的CDN上需要的文件。
如果你更想要传送你自己本地的jQuery版本，你可以使用类似于下面的代码片段::

    from flask_bootstrap import StaticCDN
    app.extensions['bootstrap']['cdns']['jquery'] = StaticCDN()

注意在这个情况下你需要下载一个合适的 ``jquery.js`` 和/或 ``jquery.min.js`` ，然后把它放到你的应用的 ``static`` 文件夹。

上面的所有配置也会导致jQuery的 ``BOOTSTRAP_SERVE_LOCAL`` 选项被忽略。
如果你需要一个更加复杂的配置来支持这个选项，看一下 ``init_app`` 的源码和 :doc:`cdn` 的文档。