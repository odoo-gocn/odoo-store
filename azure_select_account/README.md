# Azure SSO: Force Account Selection
## Stop the Auto-Login Loop on Odoo 18+

> ℹ️ **Compatibility:** Odoo Community & Enterprise (v18.0 / v19.0)

---

### The Problem
By default, Odoo's Azure OAuth implementation remembers the last logged-in Microsoft account. While this is convenient for single users, it creates a **frustrating loop** for users who manage multiple accounts (e.g., Consultants, Developers, or users with both Personal and Work accounts).

Once logged in, it becomes difficult to switch accounts without clearing browser cookies or opening an Incognito window.

### The Solution
This module injects the standard OAuth2 parameter `prompt='select_account'` into the Azure authentication request.

**Result:** Microsoft will *always* present the account selection screen, giving the user full control over which identity to use for that session.

---

## Key Features

* **🖱️ Total Control:** Never get stuck in the wrong account again. Forces the chooser UI every time.
* **⚙️ Zero Configuration:** Plug & Play. Install the module, and it works instantly for all Azure OAuth providers.
* **🛡️ Standard Compliant:** Uses official Microsoft Entra ID (Azure AD) URL parameters. Safe and secure.

---

## FAQ

**Does this affect Google or other providers?**
No. The code specifically checks for `login.microsoftonline.com` endpoints before applying the parameter.

**Will users have to type their password every time?**
Not necessarily. If their session is active with Microsoft, they just click their name. They only need to type the password if the Microsoft session itself has expired.

---

Developed with by **Go On Associated**