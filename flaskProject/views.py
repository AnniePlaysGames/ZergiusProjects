from flask import request, jsonify

from flask_classy import FlaskView, route


class MainView(FlaskView):
    route_base = "/"
    languages = [{"name": "JavaScript"}, {"name": "CSharp"}, {"name": "Python"}]

    @route("/lang")
    def get_all_languages(self):
        return jsonify({'languages': self.languages})

    @route("/lang<string:name>", methods=["GET"])
    def search_language(self, name: str):
        langs = [language for language in self.languages if language["name"] == name]
        return jsonify({"language": langs[0]})

    @route("/lang<string:name>", methods=["POST"])
    def add_new(self):
        new_language = {"name": request.json["name"]}
        self.languages.append(new_language)
        return jsonify({"languages": self.languages})

    @route("/lang<string:name>", methods=["PUT"])
    def update_language_name(self, name: str):
        langs = [language for language in self.languages if language["name"] == name]
        langs[0]["name"] = request.json["name"]
        return jsonify({"language": langs[0]})
