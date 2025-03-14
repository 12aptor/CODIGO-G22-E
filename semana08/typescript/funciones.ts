function saludar(nombre: string) {
  console.log(`Hola ${nombre}`);
}
saludar("Juan");

function sumar(a: number, b: number): void {
  if (a + b > 10) {
    throw new Error("El resultado es mayor a 10");
  }
}
const result = sumar(2, 3);

const esMayorDeEdad = (edad: number): boolean => {
  return edad > 18;
};

const mostrarEdad = (edad: number, fn: (edad: number) => boolean): number => {
  const result = fn(20);
  if (result) {
    console.log("Soy mayor de edad");
    return edad;
  }
  console.log("No soy mayor de edad");
  return edad;
};

mostrarEdad(20, esMayorDeEdad);
