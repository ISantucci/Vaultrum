---
plantilla: Gate de calidad
alcance: el artefacto QA
---

# QA-<XXX[.n]> — <Épica>

## Insumo

`EJ-XXX.n` (gate de hilo) o `TL-XXX` (gate de entrega). Una línea rotulada, no una mención suelta.

## Alcance y perfil

```qa-alcance
tipo     hilo
insumo   EJ-XXX.n
perfil   estandar
```

Qué entra, qué no entra, y por qué se eligió este perfil.

## Versión

```qa-build
build       <identificador>
commit      <commit o rama>
plataforma  <plataforma>
entorno     <editor | build de destino>
congelada   si
```

## Verificación de build

```qa-humo
instalacion ok | arranque ok | pantalla principal ok | entrada ok
bucle ok | camino critico ok | caidas ok | logs ok | guardado ok
resultado   aceptada
```

## Riesgos

```qa-riesgo
<sistema> | <prob 1-5> | <impacto 1-5> | <deteccion 1-5> | <exposicion 1-5> | <modo de falla concreto>
```

## Ejecutado y no ejecutado

Qué corrió y qué no, con la razón de lo segundo.

## Defectos

```qa-defectos
BUG-XXX | mayor | cerrado | reverificado en <build>
BUG-XXX | menor | diferido | <alternativa o razón>
```

Severidades: `bloqueante` `critico` `mayor` `menor` `trivial`. Estados: `abierto` `diferido` `cerrado`, y el cuarto campo es obligatorio cuando el estado es `cerrado`. Un bloqueante abierto es NO-GO: no se acepta.

## Regresión

```qa-regresion
suite bloqueante | <build> | ok
suite esencial   | <build> | ok
```

## Cobertura

```qa-cobertura
sistema | feliz | negativo | limite | estados | guardado | rendimiento | accesibilidad | idioma | plataforma
<sistema> | si | si | si | si | na:<razon> | na:<razon> | si | si | <plataforma>
```

## Riesgo residual y aceptación

```qa-aceptado
BUG-XXX | menor | <quién acepta> | <razón y qué pasa después>
```

## Medición

Salida de `calidad.py --verificar`. Si no se pudo correr, se dice con esas palabras: *medición no disponible — estimación*.

## Veredicto

```qa-decision
CONDITIONAL GO
```

## Fundamento

Por qué este veredicto y no otro. Un CONDITIONAL GO enumera sus excepciones una por una.

## Captura

- Qué entra a la suite de regresión:
- Qué modelo de prueba reusable se crea o actualiza:
- Qué se deriva al Área de Conocimiento:
- ¿Justifica análisis de causa raíz?:

## Estado

En intake / En análisis / En pase / En reverificación / **Cerrado** / Devuelto.
