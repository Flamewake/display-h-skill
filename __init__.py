from mycroft import MycroftSkill, intent_file_handler


class DisplayH(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('h.display.intent')
    def handle_h_display(self, message):
        self.speak_dialog('h.display')


def create_skill():
    return DisplayH()

