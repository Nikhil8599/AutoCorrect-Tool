from textblob import TextBlob
from language_tool_python import LanguageTool

class SpellCheckerModule:
    def __init__(self):
        self.grammar_check = LanguageTool('en-US')

    def correct_spell(self, text):
        # Apply spelling correction using TextBlob
        corrected = TextBlob(text).correct()
        return str(corrected)

    def correct_grammar(self, text):
        # Apply grammar corrections using LanguageTool
        corrected_text = self.grammar_check.correct(text)
        matches = self.grammar_check.check(text)
        grammar_issues = [match.message for match in matches]
        return corrected_text, grammar_issues
