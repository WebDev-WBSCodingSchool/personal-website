from flask import Blueprint, render_template
from ..db import get_connection

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.get('/')
def admin():
   return render_template('admin/admin.html')