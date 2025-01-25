# Entornos Virtuales 😀

## ¿Qué es un entorno virtual?

Un entorno virtual es una herramienta que nos permite crear un entorno de desarrollo aislado del sistema principal. Esto permite instalar las dependencias necesarias para nuestro proyecto sin afectar a otros proyectos.

## Crear un entorno virtual

```bash
python -m venv "nombre-del-entorno"
```

## Activar un entorno virtual

```bash
# Windows cmd
nombre-de-entorno\Scripts\activate
# Windows GitBash
source nombre-de-entorno/Scripts/activate

# Linux/MacOs
source nombre-de-entorno/bin/activate
```

## Desactivar un entorno virtual

```bash
deactivate
```

## Instalar dependencias

```bash
pip install "nombre-de-la-dependencia"
```

## Listar dependencias

```bash
pip freeze
```

## Exportar dependencias

```bash
pip freeze > requirements.txt
```

## Instalar dependencias desde un archivo

```bash
pip install -r requirements.txt
```