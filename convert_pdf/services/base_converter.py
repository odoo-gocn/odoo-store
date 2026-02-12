# -*- coding: utf-8 -*-
# Copyright 2025 Go On Associated
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from abc import ABC, abstractmethod

class BaseConverter(ABC):
    """
    Classe base para todas as estratégias de conversão.
    """

    def __init__(self, attachment):
        self.attachment = attachment

    @abstractmethod
    def convert(self):
        """
        Deve retornar:
        - filename
        - mimetype
        - datas (base64)
        """
        raise NotImplementedError
