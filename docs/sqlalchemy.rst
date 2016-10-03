Flask-SQLAlchemy 支持
=====================

`Flask-SQLAlchemy <https://pythonhosted.org/Flask-SQLAlchemy/>`_ 通过
它的 :meth:`~flask_sqlalchemy.BaseQuery.paginate` 对象支持分页。这些可以通过 ``render_pagination`` 宏自动渲染。
supports

.. code-block:: jinja

  {% from "bootstrap/pagination.html" import render_pagination %}

  {# ... #}

  {{render_pagination(query_results)}}

.. py:function:: render_pagination(pagination,\
                     endpoint=None,\
                     prev='«',\
                     next='»',\
                     ellipses='…',\
                     size=None,\
                     args={},\
                     **kwargs)

   为分页查询渲染一个分页导航。

   :param pagination: :class:`~flask_sqlalchemy.Pagination` 的实例。
   :param endpoint: 指定当一个页数被点击时要调用的端点。
                    将会用给定的端点和一个 ``page`` 参数调用 :func:`~flask.url_for` 。
                    如果设为 ``None`` 使用当前的请求端点。
   :param prev: “上一页”按钮使用的符号或文本。如果设为 ``None`` ，按钮将被隐藏。
   :param next: “下一页”按钮使用的符号或文本。如果设为 ``None`` ，按钮将被隐藏。
   :param ellipses: 指明跳过的页数使用的符号或文本，
                    如果设为 ``None`` ，则不显示指示符号。
   :param size: 可以是‘sm’或‘lg’，分别表示小的和大的分页导航。
   :param args: 传给 :func:`~flask.url_for` 的附加的变量。如果``endpoint`` 是 ``None`` ，使用 :attr:`~flask.Request.args` 和
                :attr:`~flask.Request.view_args` 。
   :param kwargs: ``<ul>`` 元素的额外属性。
