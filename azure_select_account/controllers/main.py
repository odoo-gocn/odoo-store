# -*- coding: utf-8 -*-
# Copyright 2025 Go On Associated
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.auth_oauth.controllers.main import OAuthLogin
from odoo.http import request
import json
import werkzeug.urls

class CustomOAuthLogin(OAuthLogin):

    def list_providers(self):
        # First, we fetch all enabled providers
        try:
            providers = request.env['auth.oauth.provider'].sudo().search_read([('enabled', '=', True)])
        except Exception:
            providers = []

        # Now, we iterate over each one to build the authentication link
        for provider in providers:
            return_url = request.httprequest.url_root + 'auth_oauth/signin'
            state = self.get_state(provider)

            # Default parameters for all providers
            params = dict(
                response_type='token',
                client_id=provider['client_id'],
                redirect_uri=return_url,
                scope=provider['scope'],
                state=json.dumps(state),
            )

            # ===================================================================
            # HERE IS THE MAIN LOGIC:
            # We check if the provider is Azure.
            # The safest way is to check the authorization endpoint.
            # ===================================================================
            if provider.get('auth_endpoint') and 'login.microsoftonline.com' in provider['auth_endpoint']:
                # If it is Azure, we add the 'prompt' parameter
                params['prompt'] = 'select_account'

            # We build the authentication link for the provider
            auth_endpoint = provider['auth_endpoint'].rstrip('?') if provider.get('auth_endpoint') else ''
            sep = '&' if '?' in auth_endpoint else '?'
            provider['auth_link'] = "%s%s%s" % (
                auth_endpoint,
                sep,
                werkzeug.urls.url_encode(params)
            )

        # The return remains outside the loop to return the complete and modified list
        return providers