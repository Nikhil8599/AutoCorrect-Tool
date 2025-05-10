from flask import Flask, request, render_template
from model import SpellCheckerModule

app = Flask(__name__)
spell_checker_module = SpellCheckerModule()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spell', methods=['POST'])
def spell():
    if request.method == 'POST':
        text = request.form['text']
        spelling_corrected = spell_checker_module.correct_spell(text)
        grammar_corrected, grammar_issues = spell_checker_module.correct_grammar(spelling_corrected)

        return render_template('index.html',
                               corrected_text=grammar_corrected,
                               corrected_grammar=grammar_issues)

@app.route('/grammar', methods=['POST'])
def grammar():
    # Not implemented
    return "Grammar correction endpoint"

if __name__ == '__main__':
    app.run(debug=True)
