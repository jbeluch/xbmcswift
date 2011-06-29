class Module(object):
    # All modules will keep their method names local, so without their module name prefixed
    # the show_videos module in mit will be called show_videos, not mit.show_videos

    def __init__(self, namespace):
        self._namespace = namespace.split('.')[-1] # Get rid of package prefixes
        self._view_functions = {}
        self._routes = []
        self._register_funcs = []

    def route(self, url_rule, default=False, name=None, **options):
        def decorator(f):
            view_name = name or f.__name__
            self.add_url_rule(url_rule, f, name=view_name, default=default, **options)
            return f
        return decorator

    def url_for(self, endpoint, **items):
        full_endpoint = '%s.%s' % (self._namespace, endpoint)

        try:
            return self._plugin.url_for(full_endpoint, **items)
        except AttributeError:
            raise Exception, 'Must register_module with an application.'

    def add_url_rule(self, url_rule, view_func, name, default=False, **options):
        name = '%s.%s' % (self._namespace, name)

        def register_rule(plugin, url_prefix):
            full_url_rule = url_prefix + url_rule
            plugin.add_url_rule(full_url_rule, view_func, name, default, **options)
            self._plugin = plugin

        self._register_funcs.append(register_rule)

    @property
    def parent_plugin(self):
        return self._plugin

    #@parent_plugin.setter
    #def plugin(self, plugin):
        #self._plugin = plugin
    @property
    def qs_args(self):
        if not self._plugin:
            raise Exception, 'Not registered with any app.'
        return self._plugin.qs_args

    @property
    def routes(self):
        return self._routes

    @property
    def view_functions(self):
        return self._view_functions

    @property
    def namespace(self):
        return self._namespace

    @property
    def url_prefix(self):
        return self._url_prefix
