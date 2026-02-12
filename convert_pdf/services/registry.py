# -*- coding: utf-8 -*-
# Copyright 2025 Go On Associated
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from .png_to_pdf_converter import PngToPdfConverter
from .jpeg_to_pdf_converter import JpegToPdfConverter

class ConverterRegistry:
    """
    Registry responsável por mapear o tipo de conversão
    para a Strategy correta.
    """

    _registry = {}

    @classmethod
    def register(cls, conversion_type, converter_class):
        cls._registry[conversion_type] = converter_class

    @classmethod
    def get_converter(cls, conversion_type, attachment):
        converter_class = cls._registry.get(conversion_type)
        if not converter_class:
            return None
        return converter_class(attachment)

ConverterRegistry.register(
    "png_to_pdf",
    PngToPdfConverter,
)    
ConverterRegistry.register(
    "jpeg_to_pdf",
    JpegToPdfConverter,
)