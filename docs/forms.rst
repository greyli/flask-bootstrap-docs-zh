WTFForms 支持
=============

``bootstrap/wtf.html`` 模板包含了帮助你快速输出表单的宏。
Flask-WTF_ 不是Flask-Bootstrap的依赖，但是必须被正确的安装。
在最近的几个版本中， Flask-WTF_ 的API变化很大，Flask-Bootstrap目前为 Flask-WTF_ 的0.9.2版本开发。

最基本的方式是把它们作为手动创建表单的助手。

.. code-block:: jinja

  <form class="form form-horizontal" method="post" role="form">
    {{ form.hidden_tag() }}
    {{ wtf.form_errors(form, hiddens="only") }}

    {{ wtf.form_field(form.field1) }}
    {{ wtf.form_field(form.field2) }}
  </form>

然而，你经常只是想快速生成一个表单，而且不需要过度的微调::

  {{ wtf.quick_form(form) }}


表单宏参考
----------

.. py:function:: quick_form(form,\
                    action=".",\
                    method="post",\
                    extra_classes=None,\
                    role="form",\
                    form_type="basic",\
                    horizontal_columns=('lg', 2, 10),\
                    enctype=None,\
                    button_map={},\
                    id="")


   为一个完整的 Flask-WTF_ 表单输出Bootstrap-markup。

   :param form: 要输出的表单。
   :param method: ``<form>`` 的method属性。
   :param extra_classes: 添加到 ``<form>`` 的类。
   :param role: ``<form>`` 的role属性.
   :param form_type: ``basic`` ， ``inline`` 或是 ``horizontal`` 之一。
                     关于不同表单样式的具体内容，见 Bootstrap_ 文档。
   :param horizontal_columns: 当使用水平定位的时候，像这样定位表单。必须是一个三元组：
                               ``(column-type, left-column-size, right-colum-size)``.
   :param enctype: ``<form>`` 的enctype属性。如果设为 ``None``
                   而且一个 :class:`~wtforms.fields.FileField` 出现在表单里，
                   这个值会被自动设置为 ``multipart/form-data`` 。
   :param button_map: 一个字典，匹配按钮字段名称到  ``primary`` ， ``danger`` 或是 ``success`` 。
                      在 ``button_map`` 里没有找到的按钮会使用 ``default`` 类型。
   :param id: ``<form>`` 的id属性。

.. py:function:: form_errors(form, hiddens=True)

   渲染包含表单错误消息的段落。这通常只用来输出隐藏字段表单的错误，因为其他的被附加到表单字段上了。

   :param form: 应该被渲染错误信息的表单。
   :param hiddens: If 如果设为 ``True`` ，也渲染隐藏字段的错误。
                   如果设为 ``'only'`` ， *only* 渲染这些。


.. py:function:: form_field(field,\
                            form_type="basic",\
                            horizontal_columns=('lg', 2, 10),\
                            button_map={})

    渲染单个表单字段及周围的元素。主要通过 ``quick_form`` 使用。

.. _Flask-WTF: https://flask-wtf.readthedocs.org/en/latest/
.. _Bootstrap: http://getbootstrap.com/

