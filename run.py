#!/usr/bin/env python

import logging
from engine.routes import app

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

for handler in app.logger.handlers:
    handler.setFormatter(formatter)

app.run(debug=True)