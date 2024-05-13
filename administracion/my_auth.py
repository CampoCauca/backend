from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class BaseAuthPerm(LoginRequiredMixin, UserPassesTestMixin):
    _PERMISSIONS = []
   
    
    def get_login_url(self):
        if not self.request.user.is_authenticated:
            # el usuario no está logueado, ir a la página de login
            return super(BaseAuthPerm, self).get_login_url()
        # El usuario está logueado pero no está autorizado
        return '/no_autorizado/'
    
    def test_func(self):
        # obtenemos todos los grupos del usuario logueado
        grupos = self.request.user.groups.all()
        # comparamos los grupos del usuario con la lista de permisos
        for grupo in self._PERMISSIONS:
            if grupo in []:
                return True

        return False 