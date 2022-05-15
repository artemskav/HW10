from utils import *
from flask import Flask

app = Flask(__name__)

@app.route('/')
def page_index():
    code_html = code_html_main_page()
    return code_html

@app.route('/candidate/<int:pk>')
def page_candidate(pk):
    code_html = code_html_one_candidate(pk)
    return code_html

@app.route('/skills/<skill>')
def page_candidate_skills(skill):
    code_html = code_html_skills(skill.lower())
    return code_html

app.run()
