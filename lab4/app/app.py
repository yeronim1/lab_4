import os
import sys
import yaml
import boto3
import botocore
from waitress import serve
from sqlalchemy import text, inspect

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from lab4.app.my_project import create_app

DEVELOPMENT_PORT = 5000
PRODUCTION_PORT = int(os.getenv("PORT", "8080"))
HOST = "0.0.0.0"

DEVELOPMENT = "development"
PRODUCTION = "production"
FLASK_ENV = "FLASK_ENV"
ADDITIONAL_CONFIG = "ADDITIONAL_CONFIG"

def get_parameter_from_ssm(parameter_name):
    ssm = boto3.client('ssm', region_name="eu-north-1")
    try:
        param = ssm.get_parameter(Name=parameter_name, WithDecryption=True)
        return param["Parameter"]["Value"]
    except botocore.exceptions.ClientError as e:
        print(f"Error fetching parameter {parameter_name} from SSM: {e}")
        return None

def _normalize_mysql_uri(uri: str) -> str:
    if uri and uri.startswith("mysql://"):
        return "mysql+pymysql://" + uri[len("mysql://"):]
    return uri

if __name__ == "__main__":
    flask_env = os.environ.get(FLASK_ENV, DEVELOPMENT).lower()

    config_yaml_path = os.path.join(os.path.dirname(__file__), 'config', 'app.yml')
    with open(config_yaml_path, "r", encoding="utf-8") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)

    additional_cfg = cfg.get(ADDITIONAL_CONFIG, {})
    additional_cfg["MYSQL_ROOT_USER"] = get_parameter_from_ssm("database_user")
    additional_cfg["MYSQL_ROOT_PASSWORD"] = get_parameter_from_ssm("database_password")

    if flask_env == DEVELOPMENT:
        config_data = dict(cfg.get(DEVELOPMENT, {}))
        config_data["SQLALCHEMY_DATABASE_URI"] = get_parameter_from_ssm("database_uri")
        debug = True
        port = DEVELOPMENT_PORT
    elif flask_env == PRODUCTION:
        config_data = dict(cfg.get(PRODUCTION, {}))
        config_data["SQLALCHEMY_DATABASE_URI"] = get_parameter_from_ssm("database_uri")
        debug = False
        port = PRODUCTION_PORT
    else:
        raise ValueError(f"Unknown {FLASK_ENV}='{flask_env}'. Use '{DEVELOPMENT}' or '{PRODUCTION}'.")

    env_db_url = os.getenv("DATABASE_URL", "").strip()
    if env_db_url:
        env_db_url = _normalize_mysql_uri(env_db_url)
        config_data["SQLALCHEMY_DATABASE_URI"] = env_db_url
    else:
        yaml_db_url = config_data.get("SQLALCHEMY_DATABASE_URI", "")
        config_data["SQLALCHEMY_DATABASE_URI"] = _normalize_mysql_uri(yaml_db_url)

    app = create_app(config_data, additional_cfg)

    if flask_env == DEVELOPMENT:
        app.run(host=HOST, port=port, debug=debug)
    else:
        serve(app, host=HOST, port=port)