# flask-influxdb2

## Installation

    $ pip install flask-influxdb2

## How to Use


    from flask import Flask
    from flask_influxdb2 import InfluxDB2
    
    app = Flask(__name__)
    app.config['INFLUXDB_V2_URL'] = 'http://...'
    app.config['INFLUXDB_V2_TOKEN'] = 'http://...'
    
    influxdb2 = InfluxDB2()
    influxdb2.init_app(app)
    
    @app.route('/')
    def index():
        query = '...'
        result = influxdb2.query_api(query)
        ...
        
        return ...
   


# Configuration Keys

keyname (default value)

    INFLUXDB_V2_URL ('http://localhost:8086')
    INFLUXDB_V2_TOKEN ('my-token')
    INFLUXDB_V2_DEBUG (None)
    INFLUXDB_V2_TIMEOUT (10000)
    INFLUXDB_V2_ORG ('my-org')
    INFLUXDB_V2_ENABLE_GZIP (False)
    INFLUXDB_V2_DEFAULT_DICT (None)
