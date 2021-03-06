from flask import Flask,render_template,request
from stories import story,my_story

app = Flask(__name__)

@app.route("/")
def hello():
    story1 = story.prompts
    story2 = my_story.prompts
    story_type = request.args.get("story_form")
    if story_type == "story1":
        return render_template("form.html",story=story1,story_type="story1")
    return render_template("form.html",story=story2,story_type="story2")

@app.route("/my_story/<story_type>")
def the_story(story_type):
    story_dict = request.args.to_dict()
    _my_story = story.generate(story_dict)
    my_story2 = my_story.generate(story_dict)
    if story_type == "story1":
        return render_template("story.html",story=_my_story)
    return render_template("story.html",story=my_story2)