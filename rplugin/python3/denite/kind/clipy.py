from denite.base.kind import Base

class Kind(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'clipy'
        self.default_action = 'paste'

    def action_paste(self,context):
        targets = context['targets']
        self.vim.command('r {}'.format(targets[0]['action__path']))
