# This file is part of JuliaBase-Institute

"""View for showing an informal layer stack as a PDF file.
"""

import subprocess, uuid, os, io
from functools import partial
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import django.utils.text
from django.utils.translation import ugettext as _
import jb_common.utils.base
from samples import permissions
import samples.utils.views as utils
from institute import models, informal_stacks


def generate_stack(thumbnail, locations, sample, sample_details):
    # FixMe: This should be implemented without writing to the disk.
    pdf_filename = "/tmp/stack_{}.pdf".format(uuid.uuid4())
    informal_stacks.generate_diagram(
        pdf_filename, [informal_stacks.Layer(layer) for layer in sample_details.informal_layers.all()],
        str(sample), _("Layer stack of {0}").format(sample))
    if thumbnail:
        stream = io.BytesIO(subprocess.check_output(
            ["gs", "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=pngalpha", "-r100", "-dEPSCrop",
             "-sOutputFile=-", pdf_filename]))
        os.remove(pdf_filename)
    else:
        stream = jb_common.utils.base.open_and_unlink(pdf_filename)
    return stream


@login_required
def show_stack(request, sample_id, thumbnail):
    """Shows a particular informal layer stack.  Although its response is a bitmap
    rather than an HTML file, it is served by Django in order to enforce user
    permissions.

    :param request: the current HTTP Request object
    :param sample_id: the database ID of the sample
    :param thumbnail: whether we should deliver a thumbnail version

    :type request: HttpRequest
    :type process_id: str
    :type thumbnail: bool

    :return:
      the HTTP response object with the image

    :rtype: HttpResponse
    """
    sample_details = get_object_or_404(models.SampleDetails, pk=utils.convert_id_to_int(sample_id))
    sample = sample_details.sample
    permissions.get_sample_clearance(request.user, sample)
    if not sample_details.has_producible_stack_diagram():
        raise Http404("No stack diagram available.")
    locations = sample_details.get_stack_diagram_locations()
    filepath = locations["thumbnail_file" if thumbnail else "diagram_file"]
    stream = jb_common.utils.base.get_cached_bytes_stream(
        filepath, partial(generate_stack, thumbnail, locations, sample, sample_details), timestamps=[sample.last_modified])
    return jb_common.utils.base.static_response(
        stream, None if thumbnail else "{0}_stack.pdf".format(django.utils.text.slugify(str(sample))),
        "image/png" if thumbnail else "application/pdf")
