import datetime
import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")

class AppendCurrentTimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command(
            "insert_snippet",
            {
                "contents": "%s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        )
