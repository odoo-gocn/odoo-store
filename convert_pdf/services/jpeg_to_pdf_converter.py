# -*- coding: utf-8 -*-
# Copyright 2025 Go On Associated
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
import base64
import io
from PIL import Image
from .base_converter import BaseConverter

class JpegToPdfConverter(BaseConverter):
    """
    Converte JPEG para PDF.
    """
    def convert(self):
        image_data = base64.b64decode(self.attachment.datas)
        image_stream = io.BytesIO(image_data)

        image = Image.open(image_stream)

        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        output_stream = io.BytesIO()
        image.save(output_stream, format="PDF")

        pdf_data = base64.b64encode(output_stream.getvalue())

        return {
            "filename": self._build_filename(),
            "mimetype": "application/pdf",
            "datas": pdf_data,
        }

    def _build_filename(self):
        name = self.attachment.name or "imagem"
        if name.lower().endswith(".jpg") or name.lower().endswith(".jpeg"):
            return name.rsplit(".", 1)[0] + ".pdf"
        return name + ".pdf"
