from logging import config

import yaml
from dotenv import load_dotenv

# Load environmental variables
load_dotenv()

# Configure logging
with open("log_spec.yaml", "r") as log_spec_file:
    config.dictConfig(yaml.load(log_spec_file))
