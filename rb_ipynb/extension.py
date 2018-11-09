import logging

from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import ReviewUIHook
from reviewboard.extensions.hooks import FileAttachmentThumbnailHook
from reviewboard.attachments.mimetypes import TextMimetype
from reviewboard.reviews.ui.text import TextBasedReviewUI


class IpynbReviewUIExtension(Extension):

    css_bundles = {
        'default': {
            'source_filenames': (
                'css/vendor/notebook.css',
                'css/vendor/prism.css'
            )
            }
    }
    js_bundles = {
        'default': {
            'source_filenames': (
                'js/vendor/ansi_up.min.js',
                'js/vendor/es5-shim.min.js',
                'js/vendor/marked.min.js',
                'js/vendor/notebook.min.js',
                'js/vendor/prism.min.js'
            )
        }
    }


    def initialize(self):
        logging.debug('Initialize My Plugin')
        ReviewUIHook(self, [IpynbReviewUI])


class IpynbReviewUI(TextBasedReviewUI):

    supported_mimetypes = ['text/plain']

    def get_extra_context(self, request):
        logging.debug('Ipynb Viewer')
        context = super(IpynbReviewUI, self).get_extra_context(request)

        if self.obj.filename.rsplit('.', 1)[1] != 'ipynb':
            return context


        self.template_name = 'rb_ipynb/ipynb.html'
        context['raw_file'] = self.get_text()
        return context
