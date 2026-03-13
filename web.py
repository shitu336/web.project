from flask import Flask, render_template_string, request, redirect, session

app = Flask(_name_)
app.secret_key = "secret"

# Dummy data (admin can change)
slider_text = "Welcome to Our NGO"
mission = "Helping children with education and better future."
vision = "Create a society where every child gets opportunity."

# ---------------- HOME PAGE ----------------
home_page = """
<html>
<head>
<title>NGO Home</title>
<style>

body{font-family:Arial;margin:0}

header{
background:#2c3e50;
color:white;
padding:15px;
display:flex;
justify-content:space-between;
}

nav a{
color:white;
margin:10px;
text-decoration:none;
}

.slider{
background:#eee;
padding:60px;
text-align:center;
font-size:30px;
}

.section{
padding:40px;
text-align:center;
}

.stats{
background:#f4f4f4;
padding:30px;
display:flex;
justify-content:center;
gap:40px;
}

.card{
border:1px solid #ccc;
padding:20px;
margin:10px;
width:220px;
display:inline-block;
}

footer{
background:#222;
color:white;
padding:20px;
display:flex;
justify-content:space-around;
}

button{
background:#3498db;
color:white;
border:none;
padding:8px;
}

</style>
</head>

<body>

<header>
<h2>NGO Logo</h2>
<nav>
<a href="/">Home</a>
<a href="/login">Admin</a>
</nav>
</header>

<div class="slider">
{{slider}}
</div>

<div class="section">

<h2>Vision & Mission</h2>

<div class="card">
<h3>Mission</h3>
<p>{{mission}}</p>
</div>

<div class="card">
<h3>Vision</h3>
<p>{{vision}}</p>
</div>

</div>

<div class="stats">
<div>3067<br>Campaign Hosted</div>
<div>10000+<br>Students</div>
<div>50000+<br>People Helped</div>
<div>2000+<br>Volunteers</div>
</div>

<div class="section">

<h2>Our Campaigns</h2>

<div class="card">
<h3>Girls Education</h3>
<p>Empowering girls with education.</p>
<button>See Details</button>
</div>

<div class="card">
<h3>Child Nutrition</h3>
<p>Helping children get proper nutrition.</p>
<button>See Details</button>
</div>

<div class="card">
<h3>Elderly Care</h3>
<p>Support for senior citizens.</p>
<button>See Details</button>
</div>

</div>

<footer>

<div>
<h3>Contact</h3>
<p>Email: ngo@gmail.com</p>
</div>

<div>
<h3>Quick Links</h3>
<p>Home</p>
<p>About</p>
</div>

<div>
<h3>Social</h3>
<p>Facebook</p>
<p>Instagram</p>
</div>

</footer>

</body>
</html>
"""

# ---------------- ADMIN LOGIN ----------------
login_page = """
<h2>Admin Login</h2>

<form method="post">
Username:<br>
<input type="text" name="user"><br><br>

Password:<br>
<input type="password" name="pass"><br><br>

<button type="submit">Login</button>
</form>
"""

# ---------------- DASHBOARD ----------------
dashboard_page = """
<h2>Admin Dashboard</h2>

<a href="/manage">Manage Home Page</a><br><br>

<a href="/logout">Logout</a>
"""

# ---------------- MANAGE CONTENT ----------------
manage_page = """
<h2>Manage Home Page Content</h2>

<form method="post">

Slider Text:<br>
<input type="text" name="slider" value="{{slider}}"><br><br>

Mission:<br>
<textarea name="mission">{{mission}}</textarea><br><br>

Vision:<br>
<textarea name="vision">{{vision}}</textarea><br><br>

<button type="submit">Update</button>

</form>
"""

# Routes

@app.route("/")
def home():
    return render_template_string(home_page, slider=slider_text, mission=mission, vision=vision)


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        if request.form["user"] == "admin" and request.form["pass"] == "admin":
            session["admin"] = True
            return redirect("/dashboard")
    return render_template_string(login_page)


@app.route("/dashboard")
def dashboard():
    if "admin" not in session:
        return redirect("/login")
    return render_template_string(dashboard_page)


@app.route("/manage", methods=["GET","POST"])
def manage():
    global slider_text, mission, vision

    if "admin" not in session:
        return redirect("/login")

    if request.method == "POST":
        slider_text = request.form["slider"]
        mission = request.form["mission"]
        vision = request.form["vision"]

    return render_template_string(manage_page, slider=slider_text, mission=mission, vision=vision)


@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/")

# Run server
if _name_ == "_main_":
    app.run(debug=True)