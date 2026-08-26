## Propósito

El Flujo de Validación de Entrega cierra el trabajo de un timeline.

Su función es verificar que lo construido **entregue la experiencia prometida**, no solo que compile y respete el alcance. Es el último gate antes de dar una iteración por entregada.

Existe porque la revisión técnica del Área de Programación valida **cómo está construido** cada hilo, y hasta acá nadie validaba **qué se entregó** como conjunto.

---

## Entrada del flujo

- un `TL-XXX` con todos sus hilos `.n` en revisión técnica OK (cada uno con su `EJ-XXX.n` cerrado por el Revisor Técnico),
- su `QA-XXX` de entrega cerrado, en GO o CONDITIONAL GO, con su riesgo residual declarado,
- los `RQ` del timeline, como contrato de lo prometido,
- los `GDS` (y `LDS`/`UXS` si existieron), como contrato de cómo debía sentirse,
- lo construido, ejecutándose.

Si algún hilo del timeline todavía no cerró su revisión técnica, el flujo no arranca: se marca el faltante.

---

## Transformación que realiza

- Parte del Core: identidad, principios y criterios aplicables (principio 1).
- Jala **on-demand** `05_Fundamentos_de_experiencia_ludica` de la Biblioteca de la Escuela y lee la entrega contra los pilares que aplican.
- Verifica la trazabilidad del timeline: `TL → RQ → GDS → (LDS / UXS) → SOL → EJ → QA`, más el `QA-XXX` de entrega.
- Corre el checklist de **definición de terminado** contra lo que se puede jugar, no contra el papel.
- Decide el estado de la entrega y, si corresponde, a qué área rebota cada hallazgo.
- Marca el aprendizaje reutilizable para derivarlo al Área de Conocimiento.

El checklist operativo y la tabla de rebote de este paso viven en la skill del área (`vaultrum-produccion`, Paso 4). Este flujo no los repite: define cuándo el paso puede darse por cerrado.

---

## Salida esperada / formato

```txt
## Entrega validada (TL-XXX)
## Trazabilidad          → eslabones presentes y faltantes
## Contra los RQ         → ¿resuelve lo prometido?
## Contra los GDS        → ¿se juega como se diseñó?
## Definición de terminado → checklist, con lo que falta explícito
## Experiencia           → lectura contra los pilares que aplican
## Hallazgos             → qué rebota y a qué área
## Aprendizaje para el Core (si hay)
## Estado de la entrega  → Cerrado / Ajustar / Pausado
```

Se registra como `VE-XXX` en `Salidas/Validaciones/` y se indexa en `00_Indice_ve`.

---

## Criterios de aceptación

El flujo puede darse por cerrado cuando:

- la entrega fue verificada **corriendo**, no leyendo specs,
- cada `RQ` del timeline tiene una respuesta explícita: cumplido, incompleto o descartado con motivo,
- el `QA` de entrega está citado, con su veredicto y su riesgo residual,
- la definición de terminado está tildada o tiene lo faltante escrito,
- cada hallazgo tiene un área destino concreta, no una queja general,
- el estado de la entrega está declarado.

---

## Condiciones para cerrar la entrega

Se cierra en **Cerrado** cuando la entrega responde a los `RQ`, se juega como el `GDS` la diseñó y cumple la definición de terminado.

Vuelve como **Ajustar** cuando hay hallazgos concretos, cada uno con su destino concreto (un área, o el sub-agente de Producción que corresponda). La tabla de rebote vive en la skill del área (`vaultrum-produccion`, Paso 4), junto al checklist: este flujo no la repite.

Queda **Pausado** cuando falta información o una decisión del owner para poder validar. Se declara qué falta (principio 9) y no se fuerza el cierre.

No debe cerrarse en **Cerrado** si:

- el `QA` de entrega está en NO-GO, o no existe,
- el resultado "funciona pero no es bueno" — ese estado es *Ajustar*,
- falta un eslabón de trazabilidad que correspondía existir,
- la definición de terminado tiene ítems sin tildar y sin justificar,
- se validó leyendo el código en vez de usando lo construido.

---

## Qué debe evitar este flujo

No revisa código ni arquitectura: eso es el Revisor Técnico del Área de Programación.

No rediseña reglas ni balance: rebota a Game Design con el hallazgo concreto.

No amplía el alcance: una mejora detectada fuera de lo acordado se registra como `RQ` nuevo, no se mete en esta entrega.

No cierra por cansancio ni por avanzar.

---

## Pendiente declarado

La fuente canónica de la *definición de terminado* debería ser el libro `03_Definicion_de_terminado` de la Biblioteca, hoy en estado **Reservado**. Mientras ese libro no esté escrito, el checklist operativo vive en la skill del área. Cuando la Escuela lo complete, la skill debe pasar a referenciarlo en vez de sostenerlo (principios 2 y 9).

---

## Resultado final

Una iteración que se sostiene sola frente a un jugador — o una lista de hallazgos concretos para que vuelva a sostenerse.

Eficacia sobre inmediatez: vale más una entrega en *Ajustar* con hallazgos claros que una cerrada que nadie quiere jugar.
