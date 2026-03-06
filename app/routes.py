from flask import Blueprint, flash, redirect, render_template, request, url_for

from .extensions import db
from .models import Fragrance

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    total = Fragrance.query.count()
    latest = Fragrance.query.order_by(Fragrance.created_at.desc()).limit(5).all()
    return render_template("index.html", total=total, latest=latest)


@bp.route("/fragrances")
def fragrances():
    records = Fragrance.query.order_by(Fragrance.brand.asc(), Fragrance.name.asc()).all()
    return render_template("fragrances.html", fragrances=records)


@bp.route("/fragrances/new", methods=["GET", "POST"])
def add_fragrance():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        brand = request.form.get("brand", "").strip()
        notes = request.form.get("notes", "").strip()
        season = request.form.get("season", "").strip()

        if not name or not brand:
            flash("Name and brand are required.", "error")
            return render_template("add_fragrance.html")

        fragrance = Fragrance(name=name, brand=brand, notes=notes or None, season=season or None)
        db.session.add(fragrance)
        db.session.commit()
        flash("Fragrance added successfully.", "success")
        return redirect(url_for("main.fragrances"))

    return render_template("add_fragrance.html")
