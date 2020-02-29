from .base import Base
import glob
import os
import re

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
                candidates.extend(self._extract(file))

        return candidates

    def _extract(self,filename):
        entries = []
        extracted = []
        with open(filename) as f:
            lines = f.readlines()
            line_count = 1

            for line in lines:
                match = re.search(r'<denite-clipy>(.*)</denite-clipy>',line)

                if match:
                    entries.append({'body':match.groups()[0],'line':line_count})
                line_count = line_count + 1
        
            for i,entry in enumerate(entries):
                if i != len(entries) - 1:
                    body = entry['body']
                    line_start = entries[i]['line']
                    line_end = entries[i+1]['line'] -2
                    extracted.append({'word':body,'__line':"{}:{}".format(line_start,line_end),'action__path':filename})
                else:
                    body = entry['body']
                    line_start = entries[i]['line']
                    extracted.append({'word':body,'__line':"{}:{}".format(line_start,len(lines)),'action__path':filename})

        return extracted
        
