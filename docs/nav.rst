Flask-Nav 支持
==============

Flask-Nav_ 扩展可以让你很容易的创建导航构件，而且Flask-Bootstrap为此附带了一个与Bootstrap相
兼容的渲染器。一旦你初始化一个程序，Flask-Bootstrap默认会注册这个Bootstrap渲染器。

渲染一个简易的（"just works"）导航栏，举例来说

.. code-block:: jinja

    {% block navbar %}
    {{nav.mynavbar.render()}}
    {% endblock %}

这会自动生成与Bootstrap相兼容的HTML代码。
一个生成能工作的导航栏的最小化的例子是这样的：

.. code-block:: python

    from flask_nav import Nav
    from flask_nav.elements import Navbar, View

    nav = Nav()

    @nav.navigation()
    def mynavbar():
        return Navbar(
            'mysite',
            View('Home', 'index'),
        )

    # ...

    nav.init_app(app)

你可以看看示例程序，它有关于导航的更加详细的例子。

The BootstrapRenderer
---------------------

这个用来渲染Bootstrap式HTML的渲染器（通过 ``flask_bootstrap.nav.BootstrapRenderer`` 提供）有一些明确的特性。
换句话说，任何 :class:`~flask_nav.elements.Navbar` 的 ``title`` 属性也可以是一个 :class:`~flask_nav.elements.Link` 或 :class:`~flask_nav.elements.View` 。

如果 ``title`` 不是 ``None`` ，它会被使用 ``brand`` 类来渲染。（具体见 `Bootstrap docs
<http://getbootstrap.com/components/#navbar-brand-image>`_ ）
而且如果它有一个 ``get_url`` 方法，那么它的返回值将会是 ``brand`` 文本的链接。



定制导航栏（navbar）
~~~~~~~~~~~~~~~~~~~

如果想要修改 ``BootstrapRenderer`` 的输出，你可以创建子类，然后注册这个子类作为另一个渲染器。
你可以看看 Flask-Nav_ 的文档，那儿有 `关于这个话题的更多信息 <http://pythonhosted.org/flask-nav/advanced-topics.html#implementing-custom-renderers>`_ 。

.. _Flask-Nav: http://pythonhosted.org/flask-nav
