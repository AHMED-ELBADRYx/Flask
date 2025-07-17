from flask import Flask, render_template

skills = Flask(__name__, template_folder='Templates', static_folder="Static")

my_skills = [('Html', 80), ('Css', 70), ('JavaScript', 60), ('Python', 90), ('Flask', 75), ('Django', 50), ('Java', 40), ('C++', 30)]

@skills.route('/')
def home():
    return render_template('home.html',
                           title='Home Page',
                           text='Welcome to the Home Page from main!',
                           custom_css='sty_home')

@skills.route('/about')
def about():
    return render_template('about.html',
                           title='About Page',
                           text='Welcome to the About Page from main!',
                           custom_css='sty_about')

@skills.route('/skills')
def contact():
    return render_template('skills.html',
                           title='Skills Page',
                           custom_css='sty_skills',
                           page_head='Skills',
                           page_text='This is the Skills page.',
                           skills=my_skills)

if __name__ == '__main__':
    skills.run(debug=True, port=5000)

    