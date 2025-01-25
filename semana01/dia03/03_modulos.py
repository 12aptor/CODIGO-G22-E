""" Módulos """

""" Módulos preinstalados """
import os
import random
import sys
import platform
import datetime
import typing

print(os.environ)
print(platform.system())

""" Módulos personalizados """
from modulos import modulo_usuario
from modulos.modulo_usuario import saludar

print(modulo_usuario.usuarios)
modulo_usuario.saludar('admin')
saludar('user')