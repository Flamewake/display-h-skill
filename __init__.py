from mycroft import MycroftSkill, intent_handler, intent_file_handler
from adapt.intent import IntentBuilder


class DisplayH(MycroftSkill):
    def __init__(self):
        super(DisplayH, self).__init__(name="DisplayH")

    @intent_handler(IntentBuilder("HIntent").require("HKeyword.voc"))
    def handle_h_display(self, message):
        self.speak_dialog('h.display')
        self.enclosure.mouth_text('H')

    def stop(self):
    	pass

def create_skill():
    return DisplayH()

