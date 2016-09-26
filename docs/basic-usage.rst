基本用法
====

开始前第一步是导入和加载扩展::

    from flask import Flask
    from flask_bootstrap import Bootstrap

    def create_app():
      app = Flask(__name__)
      Bootstrap(app)

      return app

    # do something with app...

加载后，新的模板可以从你的模板库里获取。

示例程序
----

如果你想看一个小的程序示例，可以 `到github上浏览
<https://github.com/mbr/flask-bootstrap/tree/master/sample_app>`_ 。


模板
----
.. highlight:: jinja

创建一个基于Bootstrap的模板很简单::

    {% extends "bootstrap/base.html" %}
    {% block title %}This is an example page{% endblock %}

    {% block navbar %}
    <div class="navbar navbar-fixed-top">
      <!-- ... -->
    </div>
    {% endblock %}

    {% block content %}
      <h1>Hello, Bootstrap</h1>
    {% endblock %}

所有你要在子模板里做的事情都是基于块（block）的。一些块（像 ``title`` ， ``navbar`` 或 ``content`` ）
是“convenience blocks”。严格来说，它们不是必须的，但是被增加用来优化文档结构（？）。

一个非常有用的特性是 `Jinja2的super()
<http://jinja.pocoo.org/docs/templates/#super-blocks>`_ 函数。它可以让你修改块，而不是替换它们。

.. _block-names:


~~~~~~~~~~~~~~~~

============ =========== =======
块名         外部块的目的
============ =========== =======
doc                      最外部的块。
html         doc         包含 ``<html>`` 标签的所有内容。
html_attribs doc         HTML标签的属性。
head         doc         包含 ``<head>`` 标签的所有内容。
body         doc         包含 ``<body>`` 标签的所有内容。
body_attribs body        主体标签的属性。
**title**    head        包含 ``<title>`` 标签的所有内容。
**styles**   head        包含所有头部的CSS文件 ``<link>`` 标签。
metas        head        包含所有头部的 ``<meta>`` 标签。
**navbar**   body        直接放在*content*上面的空块。
**content**  body        HTML主体（body）的便利块，把东西放在这里。
**scripts**  body        包含所有在HTML文件尾部的 ``<script>`` 标签。
============ =========== =======

示例
~~~~

* 增加一个自定义的CSS文件::

    {% block styles %}
    {{super()}}
    <link rel="stylesheet"
          href="{{url_for('.static', filename='mystyle.css')}}">
    {% endblock %}

* 自定义在Bootstrap的javascript代码*之前*加载的Javascript::

    {% block scripts %}
    <script src="{{url_for('.static', filename='myscripts.js')}}"></script>
    {{super()}}
    {% endblock %}

* 增加 ``lang="zh"`` 属性到 ``<html>``-标签::

    {% block html_attribs %} lang="zh"{% endblock %}

静态文件
----

路径的末节点（url-endpoint） ``bootstrap.static`` 可以让你引用Bootstrap文件，但通常不需要这样。
更好的做法是使用 ``bootstrap_find_resource`` 模板过滤器，它会负责设置CDN。

对当前的资源系统的详细描述在 :doc:`cdn` 。

