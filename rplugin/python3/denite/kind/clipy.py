from denite.base.kind import Base

class Kind(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'clipy'
        self.default_action = 'paste'

    def action_paste(self,context):
        targets = context['targets']
        filename = targets[0]['action__path']
        line = targets[0]['__line']

        self.vim.feedkeys(":put =readfile('{}')[{}]\n".format(filename,line))
