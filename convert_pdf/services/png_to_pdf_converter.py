# -*- coding: utf-8 -*-
# Copyright 2025 Go On Associated
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
import base64
import io
from PIL import Image
from .base_converter import BaseConverter

class PngToPdfConverter(BaseConverter):
    """
    Converte PNG para PDF.
    """
    def convert(self):
        # Decodifica o arquivo original
        image_data = base64.b64decode(self.attachment.datas)
        image_stream = io.BytesIO(image_data)

        image = Image.open(image_stream)

        # Garante compatibilidade com PDF
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        output_stream = io.BytesIO()
        image.save(output_stream, format="PDF")

        pdf_data = base64.b64encode(output_stream.getvalue())

        filename = self._build_filename()

        return {
            "filename": filename,
            "mimetype": "application/pdf",
            "datas": pdf_data,
        }

    def _build_filename(self):
        original_name = self.attachment.name or "arquivo"
        if original_name.lower().endswith(".png"):
            return original_name[:-4] + ".pdf"
        return original_name + ".pdf"
