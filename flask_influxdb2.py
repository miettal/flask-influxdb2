from flask import current_app
from flask import _app_ctx_stack

from influxdb_client import InfluxDBClient


class InfluxDB2(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('INFLUXDB_V2_URL', 'http://localhost:8086')
        app.config.setdefault('INFLUXDB_V2_TOKEN', 'my-token')
        app.config.setdefault('INFLUXDB_V2_DEBUG', None)
        app.config.setdefault('INFLUXDB_V2_TIMEOUT', 10000)
        app.config.setdefault('INFLUXDB_V2_ORG', 'my-org')
        app.config.setdefault('INFLUXDB_V2_ENABLE_GZIP', False)
        app.config.setdefault('INFLUXDB_V2_DEFAULT_DICT', None)
        app.teardown_appcontext(self.teardown)

    def connect(self):
        return InfluxDBClient(
            url=current_app.config['INFLUXDB_V2_URL'],
            token=current_app.config['INFLUXDB_V2_TOKEN'],
            debug=current_app.config['INFLUXDB_V2_DEBUG'],
            timeout=current_app.config['INFLUXDB_V2_TIMEOUT'],
            enable_gzip=current_app.config['INFLUXDB_V2_ENABLE_GZIP'],
            org=current_app.config['INFLUXDB_V2_ORG'],
            default_tags=current_app.config['INFLUXDB_V2_DEFAULT_DICT'],
        )

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'influxdb'):
            ctx.influxdb.close()

    @property
    def connection(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'influxdb'):
                ctx.influxdb = self.connect()
            return ctx.influxdb

    @property
    def query_api(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'query_api'):
                ctx.query_api = self.connection.query_api()
            return ctx.query_api
