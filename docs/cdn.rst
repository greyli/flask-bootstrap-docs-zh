CDN 支持
========

Flask-Bootstrap 支持CDN和本地两种方式来调用资源文件，在运行时是可配置的。
一旦初始化，Flask-Bootstrap会存储一个叫 ``yourapp.extensions['bootstrap']['cdns']`` 的字典到你的程序实例里。
这个字典会匹配名字到 :py:class:`~flask_bootstrap.CDN` 实例。

当使用其他提供CDN的资源，你也可以在你的模板使用 :py:func:`~flask_bootstrap.bootstrap_find_resource` 。
CDN会通过增加新的条目到上面提到的字典里面的方式被添加。

.. autoclass:: flask_bootstrap.CDN
   :members:

.. autoclass:: flask_bootstrap.StaticCDN
   :members:

.. autoclass:: flask_bootstrap.WebCDN
   :members:

.. autofunction:: flask_bootstrap.bootstrap_find_resource
