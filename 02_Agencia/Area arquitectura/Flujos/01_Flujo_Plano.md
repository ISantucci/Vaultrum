## Propósito

Convertir lo que otra área va a hacer en un procedimiento en cascada que se pueda ejecutar sin romper ninguna ley del grafo.

Es el flujo por el que el área entra el 80% de las veces. Los otros cuatro existen para cuando esto no se hizo a tiempo.

---

## Entrada del flujo

- Un área declara **qué va a hacer** y qué parte de eso toca la forma: crear notas, abrir un índice, purgar links, mover contenido, integrar material de afuera.
- No hace falta que sepa qué leyes aplican. Eso es lo que viene a buscar.

Si lo que el área va a hacer no toca la forma —editar el cuerpo de una nota que ya existe, cambiar un número, corregir una redacción— el flujo lo dice y no arranca. El área no necesita un plano para eso.

---

## Transformación que realiza

- Separa la acción en la parte que toca la forma y la parte que no.
- Identifica qué leyes aplican y, explícitamente, **cuáles no**: un plano que cita las seis siempre no informa nada.
- Ordena los pasos de menor a mayor riesgo, y declara qué medición corre entre cada uno.
- Marca los puntos que necesitan decisión del owner antes de que el área se choque con ellos: índices nuevos, renombres, cualquier cosa del Core.

---

## Salida esperada / formato

```txt
## Qué se va a hacer
   la acción en una línea, y qué parte toca la forma
## Leyes que aplican
   cuáles sí, cuáles no, y por qué
## Procedimiento en cascada
   paso — qué se hace — qué ley cubre — qué se mide después
## Gates
   qué cierra cada etapa y qué la hace rebotar
## Lo que hay que preguntarle al owner
```

Se registra como `ARQ-XXX` en modo **Plano**.

---

## Criterios de aceptación

- El área que consultó puede ejecutar el plano sola, sin volver a preguntar.
- Cada paso dice qué ley cubre. Un paso sin ley es una preferencia, no una regla.
- Cada gate se puede verificar mecánicamente, o se declara que no se puede.
- Las decisiones del owner están marcadas **antes** del paso que las necesita, no después.

---

## Condiciones para avanzar

El área ejecuta el plano y cierra con el gate de cierre. Si al medir el resultado el grafo quedó fuera de ley, entra el `03_Flujo_Auditoria_Grafo`: el plano falló o la ejecución se desvió, y hay que saber cuál de las dos.

---

## Qué debe evitar

No ejecuta el plano. No define qué debe producir el área. No entrega una lista de leyes sin orden: el orden es la mitad del plano.

---

## Resultado final

Un procedimiento que otra área puede correr sin romper nada, y sin tener que aprenderse las seis leyes.
