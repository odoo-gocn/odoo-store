# Documents to PDF Converter

![Odoo Version](https://img.shields.io/badge/Odoo-19.0-purple) ![License](https://img.shields.io/badge/License-LGPL--3-blue) ![Enterprise](https://img.shields.io/badge/Requires-Odoo%20Enterprise-orange)

**Turn Images into Professional PDFs Instantly inside Odoo Documents.**

## 📌 Overview
Storing scattered images (Receipts, ID Cards, Contracts) in JPG or PNG format creates clutter in the workspace. 

This module adds a native conversion tool directly inside the **Odoo Documents** app (Enterprise), allowing you to transform images into standard PDFs with just a few clicks, without needing to download files or use external tools.

## ✨ Key Features
* **Smart Conversion:** Supports **PNG** and **JPEG**. Automatically handles transparency (RGBA) to ensure perfect PDF rendering.
* **Flexible Management:** Choose between **replacing the original file** (ideal for receipts) or **creating a new PDF copy** (keeping the raw asset).
* **Privacy First:** Conversion happens 100% locally on your server. No image data is sent to external APIs.

## ⚙️ Requirements
* **Odoo Edition:** Enterprise (Depends on the `documents` module).
* **Python Dependencies:** `Pillow` (Standard in Odoo environments).

## 🚀 How to Use
1.  **Select:** Click on any **PNG** or **JPEG** file inside your Documents workspace.
2.  **Action:** Click the **"Convert to PDF"** button located in the top toolbar (Control Panel).
3.  **Confirm:** A wizard will appear. Choose if you want to replace the original file or create a copy, then click **Convert**.

## ⚠️ Known Limitations
* **Bulk Action:** Currently, the tool converts **one file at a time** to ensure naming accuracy.
* **Formats:** Specialized in Image-to-PDF. Does not support Word/Excel to PDF conversion.

## 📜 License
This module is licensed under the **GNU Lesser General Public License v3 (LGPL-3)**.

---
Developed with 💚 by **Go On Associated**.