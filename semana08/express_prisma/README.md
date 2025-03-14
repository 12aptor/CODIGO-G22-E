# Crear API con Express, Prisma y TypeScript

## Creación del proyecto

```bash
npm init -y
```

## Instalación de dependencias

```bash
npm install express
npm install @prisma/client
npm install -D @types/express
npm install -D typescript
npm install -D ts-node-dev # (Incluye hot reload)
npm install -D prisma
```

## Configuración de TypeScript

```bash
npx tsc --init
```

```json
{
  "compilerOptions": {
    "target": "ES6",
    "module": "commonjs",
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "resolveJsonModule": true,
    "strict": true,
    "outDir": "./build"
  },
  "include": ["**/*.ts"],
  "exclude": ["node_modules", "build"]
}
```

## Package.json

```json
{
  "name": "express_prisma",
  "version": "1.0.0",
  "description": "```bash\r npm init -y\r ```",
  "main": "src/app.ts",
  "scripts": {
    "dev": "ts-node-dev src/app.ts",
    "build": "tsc",
    "start": "node build/app.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "type": "commonjs",
  "dependencies": {
    "express": "^4.21.2"
  },
  "devDependencies": {
    "@types/express": "^5.0.0",
    "ts-node-dev": "^2.0.0",
    "typescript": "^5.8.2"
  }
}
```

## Configuración de Prisma

```bash
npx prisma init # (Crear el archivo schema.prisma)
```

## Configuración de .env

```bash
DATABASE_URL=''
```

## Ejecutar las migraciones

```bash
npx prisma migrate dev --name "nombre_migracion"
```