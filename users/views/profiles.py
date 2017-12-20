# -*- coding: utf-8 -*-
# Create your views here.

from users.models import Profile
from users.serializers.profiles import ProfileSerializer
from .abstract_view import AbstractList, AbstractDetail


class ProfileList(AbstractList):

    def __init__(self):
        super().__init__(Profile, ProfileSerializer)


class ProfileDetail(AbstractDetail):

    def __init__(self):
        super().__init__(Profile, ProfileSerializer)