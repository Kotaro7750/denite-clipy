from .base import Base
import glob
import os

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'clipy'
        self.kind = 'clipy'

    def on_init(self,context):
        context['__bufnr'] = str(self.vim.call('bufnr','%'))

    def gather_candidates(self,context):
        candidates = []

        clipy_root = self.vim.vars['clipy_root']
        clipy_filetype = self.vim.vars['clipy_filetype']

        for filetype in clipy_filetype:
            files = glob.glob("{}/**/*.{}".format(clipy_root,filetype),recursive = True)
            for file in files:
                candidates.append(self._converter(file))

        return candidates

    def _converter(self,filename):
        return {
                'word':os.path.basename(filename),
                'action__path':filename,
                }

