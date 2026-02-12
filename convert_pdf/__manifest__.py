# -*- coding: utf-8 -*-
# Copyright 2025 Go On Associated
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Convert Image to PDF",
    "version": "18.0.1.0.0",
    "category": "Productivity/Documents",
    "summary": "Convert JPEG/PNG images to PDF directly inside Odoo Documents",
    "description": """
    Simple and efficient tool to convert image files to PDF within the Documents app.
    Supports PNG and JPEG. Allows replacing the original file or creating a new one.
    """,
    "author": "Go On Associated",
    "website": "https://www.gocn.com.br",
    "license": "LGPL-3",
    "depends": ["documents"],
    "external_dependencies": {
        "python": ["Pillow"],
    },
    "data": [
        "security/ir.model.access.csv",
        "data/documents_server_action.xml",
        "wizard/file_converter_wizard_view.xml",
    ],
    "images": ['static/description/main_screenshot.png'], 
    "installable": True,
    "application": False,
}