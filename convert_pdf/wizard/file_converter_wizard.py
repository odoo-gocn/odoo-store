# -*- coding: utf-8 -*-
# Copyright 2025 Go On Associated
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import models, fields, _
from odoo.exceptions import UserError
from ..services.registry import ConverterRegistry

class FileConverterWizard(models.TransientModel):
    _name = "documents.file.converter.wizard"
    _description = "Documents File Converter Wizard"

    document_id = fields.Many2one(
        comodel_name="documents.document",
        string="Document",
        readonly=True,
        required=True,
    )
    attachment_id = fields.Many2one(
        related="document_id.attachment_id",
        readonly=True,
    )
    filename = fields.Char(
        related="attachment_id.name",
        string="File Name",
        readonly=True,
    )
    mimetype = fields.Char(
        related="attachment_id.mimetype",
        string="File Type",
        readonly=True,
    )
    conversion_type = fields.Selection(
        selection=[
            ("png_to_pdf", "PNG → PDF"),
            ("jpeg_to_pdf", "JPEG → PDF"),
        ],
        string="Conversion Type",
        required=True,
    )
    replace_original = fields.Boolean(
    string="Replace original file",
    default=False,
    help="If checked, the original file will be replaced by the converted one.",
    )

    def action_convert(self):
        self.ensure_one()

        if not self.attachment_id:
            raise UserError(_("The selected document does not have an attached file."))

        if not self._is_conversion_allowed():
            raise UserError(_(
                "The selected conversion is not compatible with the file type (%s)."
            ) % (self.mimetype or "unknown"))

        converter = self._get_converter()
        result = converter.convert()

        if self.replace_original:

            self.document_id.attachment_id.write({
                "name": result["filename"],
                "datas": result["datas"],
                "mimetype": result["mimetype"],
            })
        else:
            attachment = self.env["ir.attachment"].create({
                "name": result["filename"],
                "datas": result["datas"],
                "mimetype": result["mimetype"],
            })

            self.env["documents.document"].create({
                "name": result["filename"],
                "attachment_id": attachment.id,
                "folder_id": self.document_id.folder_id.id,
                "owner_id": self.env.user.id,
            })

        return {"type": "ir.actions.act_window_close"}

    
    def _is_conversion_allowed(self):
        self.ensure_one()

        rules = {
            "png_to_pdf": ["image/png"],
            "jpeg_to_pdf": ["image/jpeg"],
        }

        allowed_mimetypes = rules.get(self.conversion_type)
        if not allowed_mimetypes:
            return False

        return self.mimetype in allowed_mimetypes
    
    def _get_converter(self):
        self.ensure_one()

        converter = ConverterRegistry.get_converter(
            self.conversion_type,
            self.attachment_id,
        )

        if not converter:
            raise UserError(_("No strategy found for this conversion."))

        return converter
