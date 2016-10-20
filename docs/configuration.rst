配置
====

这儿有一些Flask-Bootstrap使用的配置选项，这些是普通的Flask配置变量（关于Flask配置变量， `这里 <http://flask.pocoo.org/docs/config/>`_ 有一个指南）。

.. note:: 有一个Flask扩展可以用来以
          `Flask-Appconfig <https://github.com/mbr/flask-appconfig>`_ 的形式协助编写
          `Twelve-Factor <http://12factor.net/>`_ 范式的应用程序。它也可以处理其他类型的配置安装
          而且和Flask-Bootstrap兼容很好。

====================================== ======================================================== ===
选项                                    默认值
====================================== ======================================================== ===
``BOOTSTRAP_USE_MINIFIED``             ``True``                                                 是否使用压缩过的css/js文件。
``BOOTSTRAP_SERVE_LOCAL``              ``False``                                                如果设为 ``True``，每次都将加载本地的Bootstrap资源文件。具体见：:doc:`cdn` 。
``BOOTSTRAP_LOCAL_SUBDOMAIN``          ``None``                                                 传递一个 ``subdomain`` 变量给已经生成的 :class:`~flask.Blueprint` 。当需要加载不同子域的本地文件时会很有用。
``BOOTSTRAP_CDN_FORCE_SSL``            ``True``                                                 如果一个CDN资源地址以 ``//`` 开头，会在地址前添加 ``'https:'`` 。
``BOOTSTRAP_QUERYSTRING_REVVING``      ``True``                                                 如果设为 ``True`` ，会添加一个包含当前所有本地静态文件版本的查询字符串。这会确保一旦升级Flask-Bootstrap，这些文件就会被更新。
====================================== ======================================================== ===
