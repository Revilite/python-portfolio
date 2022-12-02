from flask import Blueprint as bp
from flask import render_template as rt

views = bp("views", __name__)

@views.route("/", methods=["GET"])
def home():
  return rt("base.html")

@views.route("/contact", methods=["GET"])
def contact():
  return rt("contact.html")

@views.route("/projects", methods=["GET"])
def projects():
  return rt("projects.html")

@views.route("/resume", methods=["GET"])
def resume():
  return rt("resume.html")