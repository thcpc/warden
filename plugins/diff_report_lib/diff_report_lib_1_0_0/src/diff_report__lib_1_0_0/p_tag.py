class PTag:
    def __init__(self, content, mark):
        self.content = content
        self.mark = mark

    def html(self):
        if self.mark != "equal": return f'<code>{self.content}</code>'
        return self.content
