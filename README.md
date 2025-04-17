# 🌐 Personal Website – Flask SSR Project – WBS CODING SCHOOL

A simple **server-side rendered (SSR)** personal website built with Flask for educational purposes at **WBS CODING SCHOOL**.  
It lets you set up a basic profile, upload and manage projects, and handle simple user authentication.

Ideal for educational purposes or as a boilerplate for your own portfolio.

![Screenshot From 2025-03-31 13-35-50](https://github.com/user-attachments/assets/ab8c095a-4abb-4d63-8104-b479eb27bd60)

## 🔧 Installation

1. **Clone the repository**

```bash
git clone git@github.com:WebDev-WBSCodingSchool/personal-website.git
cd personal-website
```

2. **Create and activate a virtual environment**

macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows

```bash
py -3 -m venv .venv
.venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set your environment variables**

```bash
export PG_URI=your_postgres_connection_string
export SECRET_KEY=your_flask_secret_key
```

5. **Run the application**

```bash
flask --app personal_website run --debug --port 8080
```

## 🧩 Blueprints & Routes

### 🏠 Home Blueprint – /

Public-facing routes to display your personal profile and projects.

`GET /`

Renders the homepage with data from `personal_info` and `projects` tables.

### 🔐 Auth Blueprint – /auth

Handles login/logout and access control for the admin section.

`GET /auth/login`
Renders the login form.
`POST /auth/login`
Processes login credentials.

`GET /auth/logout`
Logs the user out and redirects to `/`.

`@login_required`
Decorator used to protect admin routes.

### ⚙️ Admin Blueprint – /admin

Admin dashboard for managing your profile and projects. Requires login.

`GET /admin`
Renders the dashboard with the options to edit profile or manage projects.

`GET /admin/edit_profile`
Renders edit profile form

`POST /admin/edit_profile`
Saves changes to your personal information.

`GET /admin/add_project`
Form to add a new project.

`POST /admin/add_project`
Saves a new project

`GET /admin/edit_projects`
Lists all projects with edit/delete options.

`GET /admin/edit_project/<id>`
Edit a specific project by ID.

`POST /admin/edit_project/<id>`
Save changes to the selected project.

`POST /admin/delete_project/<id>`
Deletes the project by ID.

### 📌 Notes

This projects uses [Jinja](https://jinja.palletsprojects.com/en/stable/) templates. DJLint is used for formatting, if you are using VSCode, install the [DJLint](https://marketplace.visualstudio.com/items?itemName=monosans.djlint) extension, some options for VSCode are included in `.vscode/`

Regarding styles, [TailwindCSS](https://tailwindcss.com/) is used with [DaisyUI](https://daisyui.com/) on top.

A `create-database.sql` file is provided to create the relations and seed some sample data.
