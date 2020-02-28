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
        files = glob.glob("/home/denjo/Develope/algorithm/**/*.hpp",recursive = True)
        return [self._converter(file) for file in files]

    def _converter(self,filename):
        return {
                'word':os.path.basename(filename),
                'action__path':filename,
                }
