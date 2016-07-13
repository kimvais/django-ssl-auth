from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.core.urlresolvers import reverse

class Tests(TestCase):
    """Automated tests to ensure everything is working as designed."""
    
    def test_login_new_user(self):
        """Ensure users are automatically created."""
        
        # Make sure the user doesn't already exist.
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='1')
        
        # Simulate an SSL connection (of a new user)
        response = self.client.get('/login',
                                    HTTP_X_SSL_AUTHENTICATED='SUCCESS',
                                    HTTP_X_SSL_USER_DN='C=FI/serialNumber=1/GN=John/SN=Smith/CN=John Smith',
                                    HTTP_X_FORWARDED_PROTOCOL='https')
        
        # Ensure the new user was created
        try:
            user = User.objects.get(username='1')
        except:
            self.fail("New user wasn't created.")
        
        self.assertEqual(user.first_name, 'John', str('First name was incorrect.'))
        self.assertEqual(user.last_name, 'Smith', str('Last name was incorrect.'))
