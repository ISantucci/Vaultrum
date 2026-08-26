---
plantilla: Modelo de prueba reusable
alcance: un sistema
---

# Modelo de prueba — <Sistema>

El conocimiento acumulado sobre cómo falla este sistema. No es un plan de prueba: es la materia prima con la que se escribe cualquier plan futuro sobre él.

## Propósito del sistema

## Valor crítico para el jugador

Qué pierde si esto falla. De acá sale la severidad por defecto.

## Componentes

Los ejes que se combinan. Ejemplo para un inventario:

```txt
entrada          click · arrastre · atajo de teclado · mando
estado del inventario   vacío · parcial · lleno · abierto · cerrado
estado del item  apilable · único · equipado · de misión · descartable
estado del mundo juego normal · transición · combate · pausa
```

## Estados y transiciones

## Integraciones

Qué sistemas tocan a este y cuáles toca él.

## Modos de falla

## Defectos históricos

Qué se rompió antes, en qué versión y por qué. Es el mejor mapa de dónde buscar.

## Límites

Valores frontera y qué pasa en cada uno.

## Combinaciones de alto valor

Las que ya encontraron algo, o las que cruzan dos ejes que nadie diseñó juntos.

## Charters estándar

## Candidatos a regresión

## Candidatos a automatización

## Instrumentación útil

Comandos, atajos de estado, semillas, logs que hacen barato probar esto.

## Anti-patrones conocidos

Formas de probar este sistema que ya se demostraron inútiles.
