---
plantilla: Verificación de build
alcance: una build candidata
---

# Verificación de build — <Identificador>

Responde una sola pregunta: **¿vale la pena gastar horas probando esta build?**

## Identidad

- Build:
- Rama / commit:
- Fecha:
- Plataforma:
- Quién ejecuta:
- Perfil del pase que habilita:

## Checks

| Check | Criterio de falla | Resultado | Evidencia |
|---|---|---|---|
| Instala o actualiza | no completa, o pide algo que no está | | |
| Abre | no llega a la pantalla principal | | |
| Pantalla principal | no responde o falta un elemento crítico | | |
| Entrada principal | el control no responde | | |
| Bucle principal | no se puede iniciar | | |
| Camino crítico del alcance | está bloqueado | | |
| Caída o congelamiento | ocurre en los primeros minutos | | |
| Logs | muestran una falla bloqueante evidente | | |
| Guardar y cargar básico | falla, si aplica | | |
| Suite de humo automática | falla, si existe | | |

En perfil Ligero, los checks se acotan al camino afectado y se declara cuáles se omitieron.

## Bloqueantes encontrados

| Defecto | Qué impide probar | Evidencia |
|---|---|---|

## Decisión

- [ ] Aceptada — el pase profundo empieza
- [ ] Condicional — se declara qué área queda sin poder probarse
- [ ] Rechazada — el pase no empieza

## Fundamento

Por qué, con evidencia. Una build rechazada dice exactamente qué falló.
