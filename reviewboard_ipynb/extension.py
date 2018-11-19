import logging

from bs4 import BeautifulSoup
from django.utils.safestring import mark_safe
from nbconvert.exporters.html import HTMLExporter
from reviewboard.extensions.base import Extension
from reviewboard.extensions.base import JSExtension
from reviewboard.extensions.hooks import ReviewUIHook
from reviewboard.reviews.ui.text import TextBasedReviewUI
from reviewboard.reviews.ui.base import FileAttachmentReviewUI


class IpynbReviewUIExtension(Extension):

    css_bundles = {
        'default': {
            'source_filenames': (
                'css/notebook.css',
            )
        }

    }

    def initialize(self):
        logging.debug('Initialize Ipynb Plugin')
        ReviewUIHook(self, [IpynbReviewUI])


class IpynbReviewUI(TextBasedReviewUI):

    supported_mimetypes = ['text/plain']
    can_render_text = True
    supports_diffing = True

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

    def generate_render(self):
        self.obj.file.open()
        output, resource = HTMLExporter().from_file(self.obj.file)
        soup = BeautifulSoup(output, 'html.parser')
        excludes = ['require.min.js', 'jquery.min.js']
        js = ' '.join([
            str(row) for row in soup.find_all('script')
            if all(exclude not in str(row) for exclude in excludes)
        ])

        result = [
            mark_safe(
                '<div class="review-ipynb">' +
                js + str(row) +
                '</div>'
            ) for row in soup.find_all(class_='cell')]
        return result
