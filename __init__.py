from mycroft import MycroftSkill, intent_file_handler


class DisplayH(MycroftSkill):
    SEC_PER_LETTER = 0.9         # based on the Mark 1 scrolling speed
    LETTERS_PER_SCREEN = 7.0     # based on the Mark 1 screen size

    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('h.display.intent')
    def handle_h_display(self, message):
        self.speak_dialog('h.display')
        self.enclosure.mouth_text('The meaning of life, the universe and everything is 42')


def create_skill():
    return DisplayH()

