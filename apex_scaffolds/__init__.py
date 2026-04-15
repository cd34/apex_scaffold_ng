from pyramid.scaffolds import PyramidTemplate


class JinjaPyramidTemplate(PyramidTemplate):
    def pre(self, command, output_dir, vars):
        vars['jinja_start'] = '{{'
        vars['jinja_end'] = '}}'

        super().pre(command, output_dir, vars)


class RajaTemplate(JinjaPyramidTemplate):
    _template_dir = 'ng_template'
    summary = 'Routes, Alchemy, Jinja2, Apex'
