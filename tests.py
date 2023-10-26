from django.test import TestCase
from django.core.exceptions import ValidationError
from Smodal.social_media_bot import SocialMediaBot
from Smodal.sale_items import SaleItem, ChatBot
from Smodal.lambda_functions import register_affiliate_manager, monitor_affiliated_models, give_credit
import uuid
import os
from .models import OIDCConfiguration, Credentials, EncryptedSensitiveData, AffiliateUploads, OpenAIAPICalls, UserProfile, FileUpload, Banking
from .views import load_dashboard, login_user, logout_user, form_submit, file_upload, user_activity, banking, serve
import json
from subprocess import Popen, PIPE
from Smodal.logging import logger 

class LambdaFunctionsTest(TestCase):
    # ... Existing tests ...
    pass

class SmodalTest(TestCase):
    def setUp(self) -> None:
        # ... Existing setUp ...

    # ... Existing tests ...

    def test_login_ninjaai_user(self):
        """
        Test to ensure that ninjaai user can login with given password
        """
        response = self.client.post('/login', {'username':'ninjaai', 'password':'Sober323'} )
        self.assertEqual(response.status_code, 200)
    
    def test_ninjaai_user_normal_privileges(self):
        """
        Test to ensure that ninjaai user has normal user rights
        """
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)

    # ... Existing tests ...

    def test_handle_errors(self):
        # ... Existing test_handle_errors ...
        pass
