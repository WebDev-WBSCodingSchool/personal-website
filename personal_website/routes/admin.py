from flask import Blueprint, flash, redirect, render_template, request, url_for
from ..routes.auth import login_required
from ..db import get_connection
import base64

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.get('/')
@login_required
def admin():
   return render_template('admin/admin.html')

@admin_bp.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
   if request.method == 'POST':
      error = None
      data_uri = None
      full_name = request.form['full_name']
      bio = request.form['bio']
      location = request.form['location']
      email = request.form['email']
      picture = request.files['picture']
      
      if(not full_name):
         error = 'Full name is required'
      elif(not bio):
         error = 'Bio is required'
      elif(not location):
         error = 'Location is required'
      elif(not email):
         error = 'Email is required'

      if picture:
         allowed_extensions = ['image/jpeg', 'image/png', 'image/jpg']
         media_type = picture.mimetype
         if(media_type not in allowed_extensions):
            error = 'Invalid file type. Please upload an image file'
         else:
            image_bytes = picture.read()
            if(len(image_bytes) > 5000000):
               error = 'Image file is too large. Max size is 5MB'
            else:
               base64_data = base64.b64encode(image_bytes).decode('utf-8')
               data_uri = f"data:image/{media_type};base64,{base64_data}"
               
      if(error is None):
         conn = get_connection()
         cur = conn.cursor()
         if(data_uri is None):
            cur.execute(
               '''
               INSERT INTO personal_info (info_id, full_name, bio, location, email)
               VALUES (1, %s, %s, %s, %s)
               ON CONFLICT (info_id)
               DO UPDATE SET
                  full_name = EXCLUDED.full_name,
                  bio = EXCLUDED.bio,
                  location = EXCLUDED.location,
                  email = EXCLUDED.email
               ''',
               (full_name, bio, location, email)
            )
         else:
            cur.execute(
               '''
               INSERT INTO personal_info (info_id,full_name, bio, location, email, picture)
               VALUES (1, %s, %s, %s, %s, %s)
               ON CONFLICT (info_id)
               DO UPDATE SET
                  full_name = EXCLUDED.full_name,
                  bio = EXCLUDED.bio,
                  location = EXCLUDED.location,
                  email = EXCLUDED.email,
                  picture = EXCLUDED.picture
               ''',
               (full_name, bio, location, email, data_uri)
            )
         conn.commit()
         cur.close()
         conn.close()
      else:  
         flash(error)
      return redirect(url_for('admin.edit_profile'))
   conn = get_connection()
   cur = conn.cursor()
   cur.execute("SELECT * FROM personal_info")
   personal_info = cur.fetchone()
   cur.close()
   conn.close()
   data = {
    'full_name': personal_info[1] if personal_info else '',
    'bio': personal_info[2] if personal_info else '',
    'location': personal_info[3] if personal_info else '',
    'email': personal_info[4] if personal_info else '',
    'picture': personal_info[5] if personal_info else ''
   }
   return render_template('admin/edit-profile.html', data=data)

@admin_bp.route('/edit-projects')
@login_required
def edit_projects():
   return render_template('admin/edit-projects.html')