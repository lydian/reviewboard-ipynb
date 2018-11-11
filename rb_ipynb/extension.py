import logging

from bs4 import BeautifulSoup
from django.utils.safestring import mark_safe
from reviewboard.extensions.base import Extension
from reviewboard.extensions.base import JSExtension
from reviewboard.extensions.hooks import ReviewUIHook
from reviewboard.reviews.ui.text import TextBasedReviewUI
from nbconvert.exporters.html import HTMLExporter
from reviewboard.reviews.ui.base import FileAttachmentReviewUI


class IpynbReviewUIExtension(Extension):

    css_bundles = {
        'default': {
            'source_filenames': (
                'css/vendor/notebook.css',
            )
        }

    }

    def initialize(self):
        logging.debug('Initialize My Plugin')
        ReviewUIHook(self, [IpynbReviewUI])


class IpynbReviewUI(TextBasedReviewUI):

    supported_mimetypes = ['text/plain']
    template_name = 'rb_ipynb/ipynb.html'
    can_render_text = True
    supports_diffing = True
    _soup = None

    def __init__(self, *args, **kwargs):
        super(IpynbReviewUI, self).__init__(*args, **kwargs)
        self.init_args = args
        self.init_kwargs = kwargs

    def render_to_response(self, request):
        file_type = self.obj.filename.rsplit('.', 1)
        if len(file_type) < 2 or file_type[1].lower() != 'ipynb':
            logging.debug('Use TextBasedReviewUI')
            return TextBasedReviewUI(
                *self.init_args, **self.init_kwargs
            ).render_to_response(request)
        else:
            logging.debug('Use IpynbReviewUI')
            return super(IpynbReviewUI, self).render_to_response(request)

    @property
    def soup(self):
        if self._soup is None:
            self.obj.file.open()
            output, resource = HTMLExporter().from_file(self.obj.file)
            self._soup = BeautifulSoup(output, 'html.parser')
        return self._soup

    def get_extra_context(self, request):
        context = super(IpynbReviewUI, self).get_extra_context(request)
        excludes = ['require.min.js', 'jquery.min.js']
        js = [
            str(row) for row in self.soup.find_all('script')
            if all(exclude not in str(row) for exclude in excludes)
        ]
        context['append']  = mark_safe(''.join(js))
        return context

    def generate_render(self):
        result = [
            mark_safe(row)
            for row in self.soup.find_all(class_='cell')]
        return result
