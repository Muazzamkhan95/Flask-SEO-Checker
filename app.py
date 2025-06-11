from flask import Flask,request, render_template, redirect, url_for
import requests
from config import DevConfig
from models import db, User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from bs4 import BeautifulSoup
from models import SEORequest

app = Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'  # redirect to this if user not logged in
login_manager.init_app(app)

# Create tables on startup (you can move this to a separate CLI or setup file later)
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
     return render_template("home.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("dashboard"))  # redirect to a protected page
        else:
            error = "Invalid email or password."

    return render_template("login.html", error=error)


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    message = None

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            error = "User already exists."
        else:
            hashed_password = generate_password_hash(password)
            new_user = User(email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            message = "✅ Registration successful!"
            return redirect(url_for("login"))
    
    return render_template("register.html", error=error, message=message)   



@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/SEOChecker", methods=["GET", "POST"])
@login_required
def SEOChecker():
    info = {}
    error = None
    seo_score = 0
    total_checks = 0

    if request.method == "POST":
        url = request.form.get("url")
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Title
            title = soup.title.string.strip() if soup.title else ""
            info["title"] = title
            total_checks += 1
            if title and len(title) <= 60:
                seo_score += 1

            # Meta Description
            desc_tag = soup.find("meta", attrs={"name": "description"})
            description = desc_tag["content"].strip() if desc_tag and "content" in desc_tag.attrs else ""
            info["description"] = description
            total_checks += 1
            if description and len(description) <= 160:
                seo_score += 1

            # H1
            h1_tags = soup.find_all("h1")
            info["h1_count"] = len(h1_tags)
            info["h1"] = h1_tags[0].get_text(strip=True) if h1_tags else ""
            total_checks += 1
            if len(h1_tags) == 1:
                seo_score += 1

            # H2
            h2_tags = soup.find_all("h2")
            info["h2"] = [h.get_text(strip=True) for h in h2_tags]

            # Image alt text
            images = soup.find_all("img")
            images_with_alt = [img for img in images if img.get("alt")]
            info["image_alt_ratio"] = f"{len(images_with_alt)}/{len(images)}"
            total_checks += 1
            if len(images) == 0 or (len(images_with_alt) / len(images) >= 0.8):
                seo_score += 1

            # Robots meta
            robots = soup.find("meta", attrs={"name": "robots"})
            robots_content = robots["content"].lower() if robots and "content" in robots.attrs else "none"
            info["robots"] = robots_content
            total_checks += 1
            if "noindex" not in robots_content and "nofollow" not in robots_content:
                seo_score += 1

            # Canonical
            canonical = soup.find("link", rel="canonical")
            info["canonical"] = canonical["href"] if canonical and "href" in canonical.attrs else ""
            total_checks += 1
            if info["canonical"]:
                seo_score += 1

            info["seo_score"] = f"{seo_score}/{total_checks}"
            info["score_percentage"] = int((seo_score / total_checks) * 100)


            seo_entry = SEORequest(
                url=url,
                score=seo_score,
                score_out_of=total_checks,
                title=info["title"],
                description=info["description"],
                h1=info["h1"],
                h1_count=info["h1_count"],
                image_alt_ratio=info["image_alt_ratio"],
                robots=info["robots"],
                canonical=info["canonical"],
                user=current_user
            )

            db.session.add(seo_entry)
            db.session.commit()

        except Exception as e:
            error = f"Error scraping {url}: {e}"

    history = SEORequest.query.filter_by(user_id=current_user.id).order_by(SEORequest.timestamp.desc()).all()
    return render_template("scrape.html", info=info, error=error,history=history)


if __name__ == "__main__":
    app.run(debug=True)



