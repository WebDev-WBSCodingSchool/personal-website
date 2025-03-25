from flask import Blueprint, render_template
from ..routes.auth import login_required
from ..db import get_connection

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.get('/')
@login_required
def admin():
   return render_template('admin/admin.html')