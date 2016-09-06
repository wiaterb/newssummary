#!/usr/bin/env python
# -*- coding: utf-8 -*-
from api.generic_list import GenericList
from core.models import Word


class WordsList(GenericList):
    list_class = Word
