# Mixin para que las views puedan mostrar el usuario en la barra de navegación
class UsuarioMixin():
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['usuario'] = self.request.user
        return contexto
