type UsuarioBase = {
    readonly id: number;
    nombre: string;
    edad: number;
}

type UsuarioPropiedades = {
    dni?: string;
    direccion?: string;
}

type Usuario = UsuarioBase & UsuarioPropiedades;

const usuario: Usuario = {
    id: 1,
    nombre: "Juan",
    edad: 20,
    dni: "87654321",
}

usuario.nombre = "Juan Perez";