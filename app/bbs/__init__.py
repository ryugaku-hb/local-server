from flask import Blueprint

bbs_bp = Blueprint("bbs", __name__)

from . import routes  # noqa
