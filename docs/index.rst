===============
Flask-Bootstrap
===============

.. tip:: 这个项目目前已经很久没有更新，而且不支持Bootstrap 4，你可以尝试使用一个更轻量的的替代品：`Bootstrap-Flask <https://github.com/greyli/bootstrap-flask>`_。

Flask-Bootstrap 把 `Bootstrap <http://getbootstrap.com>`_ 打包进一个
扩展，这个扩展主要由一个叫“bootstrap”的蓝本（blueprint）组成。它也可以创建链接从一个CDN上引用Bootstrap资源。

.. toctree::
   :maxdepth: 3

   basic-usage
   configuration
   macros
   forms
   sqlalchemy
   nav
   cdn
   faq
   bootstrap2
   changelog
   translate


安装
----

Flask-Bootstrap 可以使用 ``pip`` 从 `PyPI
<http://pypi.python.org/pypi/Flask-Bootstrap>`_ 上获取安装。建议使用 `virtualenv <http://www.virtualenv.org/en/latest/>`_ ——没有特别的原因，只是为了最佳实践。安装很简单::

   pip install flask-bootstrap

开发用途可以克隆 `官方GitHub仓库 <https://github.com/mbr/flask-bootstrap>`_ 然后使用下面的命令安装::

   python setup.py develop


起步
----

直接去读 :doc:`基本用法 <basic-usage>` 吧。同时还有一份 :doc:`faq` 清单可供参阅。

在写这份文档时，最新的Bootstrap版本已经到了Bootstrap 3（现在已经是4了！）。
一个Flask-Bootstrap分支仍然支持Bootstrap2，具体细节在这里
:doc:`bootstrap2` 。


版本笔记
----

Flask-Bootstrap 尝试跟随Bootstrap更新的脚步。版本变化的形式通常为
 ``<Bootstrap 版本>.<Flask-Bootstrap 版本>`` 。举例来说，
版本 ``2.0.3.2`` 集成了Bootstrap ``2.0.3`` 版本，并且是Flask-Bootstrap集成这个版本的第二次更新。

如果你需要让你的模板不改变，那么在你的setup.py里固定版本就可以了。
