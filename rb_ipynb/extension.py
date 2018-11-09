import logging

from django.utils.safestring import mark_safe
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import ReviewUIHook
from reviewboard.reviews.ui.text import TextBasedReviewUI
from nbconvert.exporters.html import HTMLExporter

class IpynbReviewUIExtension(Extension):

    def initialize(self):
        logging.debug('Initialize My Plugin')
        ReviewUIHook(self, [IpynbReviewUI])


class IpynbReviewUI(TextBasedReviewUI):

    supported_mimetypes = ['text/plain']


    def get_extra_context(self, request):
        logging.debug('Ipynb Viewer')
        context = super(IpynbReviewUI, self).get_extra_context(request)

        #  ipynb mime types is no difference with plain text, the work around
        # is by default mapping to the review ui, and if the file type is
        # not ipynb, fall back to TextBasedReviewUI.
        if self.obj.filename.rsplit('.', 1)[1] != 'ipynb':
            return context

        self.template_name = 'rb_ipynb/ipynb.html'
        self.obj.file.open()
        output, resource = HTMLExporter().from_file(self.obj.file)
        context['raw_file'] = mark_safe(output)
        return context
