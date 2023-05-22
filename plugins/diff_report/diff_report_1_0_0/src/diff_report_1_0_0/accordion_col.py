class AccordionCol:
    def __init__(self, name):
        self.name = name
        self.p_tags = []

    def add_tag(self, tag):
        self.p_tags.append(tag)