from flask import Blueprint, render_template, request
from ..routes.auth import login_required
from ..db import get_connection

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.get('/')
@login_required
def admin():
   return render_template('admin/admin.html')

@admin_bp.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
   if request.method == 'POST':
      print("Updating profile")  
   return render_template('admin/edit-profile.html')

@admin_bp.route('/edit-projects')
@login_required
def edit_projects():
   return render_template('admin/edit-projects.html')