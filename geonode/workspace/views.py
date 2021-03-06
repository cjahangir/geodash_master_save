from actstream.models import Action
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required, user_passes_test

from geonode.layers.models import Layer
from geonode.documents.models import Document
from geonode.maps.models import Map
from geonode.groups.models import GroupProfile
from geonode.layers.models import LayerSubmissionActivity, LayerAuditActivity


class MemberWorkspaceLayer(ListView):

    """
    This view returns members resources for different stages.
    """

    model = Layer
    template_name = 'member/layer.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(*args, **kwargs)

        context['draft_list'] = Layer.objects.filter(owner=self.request.user, status='DRAFT')
        context['pending_list'] = Layer.objects.filter(owner=self.request.user, status='PENDING')[:15]
        context['denied_list'] = Layer.objects.filter(owner=self.request.user, status='DENIED')
        context['active_list'] = Layer.objects.filter(owner=self.request.user, status='ACTIVE')
        return context


class MemberWorkspaceDocument(ListView):
    """
    This view returns members resources for different stages.
    """

    model = Document
    template_name = 'member/document.html'


    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(*args, **kwargs)
        context['draft_list'] = Document.objects.filter(owner=self.request.user, status='DRAFT')
        context['pending_list'] = Document.objects.filter(owner=self.request.user, status='PENDING')[:15]
        context['denied_list'] = Document.objects.filter(owner=self.request.user, status='DENIED')
        context['active_list'] = Document.objects.filter(owner=self.request.user, status='ACTIVE')
        return context


class MemberWorkspaceMap(ListView):

    """
    This view returns members resources for different stages.
    """

    model = Map
    template_name = 'member/map.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(*args, **kwargs)
        context['draft_list'] = Map.objects.filter(owner=self.request.user, status='DRAFT')
        context['pending_list'] = Map.objects.filter(owner=self.request.user, status='PENDING')[:15]
        context['denied_list'] = Map.objects.filter(owner=self.request.user, status='DENIED')
        context['active_list'] = Map.objects.filter(owner=self.request.user, status='ACTIVE')
        return context


class AdminWorkspaceLayer(ListView):
    """
    This view returns members resources for different stages.
    """

    model = Layer
    template_name = 'admin/layer.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(*args, **kwargs)
        groups = GroupProfile.objects.filter(groupmember__user=self.request.user, groupmember__role='manager')
        context['user_approval_request_list'] = Layer.objects.filter(status='PENDING', group__in=groups)
        context['approved_list'] = Layer.objects.filter(status='ACTIVE', group__in=groups)[:15]
        context['user_draft_list'] = Layer.objects.filter(status='DRAFT', group__in=groups)
        context['denied_list'] = Layer.objects.filter(status='DENIED', group__in=groups)[:15]
        return context


class AdminWorkspaceDocument(ListView):
    """
    This view returns members resources for different stages.
    """

    model = Document
    template_name = 'admin/document.html'


    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(*args, **kwargs)
        groups = GroupProfile.objects.filter(groupmember__user=self.request.user, groupmember__role='manager')
        context['user_approval_request_list'] = Document.objects.filter(status='PENDING', group__in=groups)
        context['approved_list'] = Document.objects.filter(status='ACTIVE', group__in=groups)[:15]
        context['user_draft_list'] = Document.objects.filter(status='DRAFT', group__in=groups)
        context['denied_list'] = Document.objects.filter(status='DENIED', group__in=groups)[:15]
        return context


class AdminWorkspaceMap(ListView):

    """
    This view returns members resources for different stages.
    """

    model = Map
    template_name = 'admin/map.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(*args, **kwargs)
        groups = GroupProfile.objects.filter(groupmember__user=self.request.user, groupmember__role='manager')
        context['user_approval_request_list'] = Map.objects.filter(status='PENDING', group__in=groups)
        context['approved_list'] = Map.objects.filter(status='ACTIVE', group__in=groups)[:15]
        context['user_draft_list'] = Map.objects.filter(status='DRAFT', group__in=groups)
        context['denied_list'] = Map.objects.filter(status='DENIED', group__in=groups)[:15]
        return context