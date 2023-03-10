from livemark import Plugin


class CustomPlugin(Plugin):
    identity = "custom"

    # Process

    def process_markup(self, markup):
        pass
