## Propósito

Convertir lo que otra área va a cerrar en un presupuesto de comunicación que condicione el diseño **antes** de que sea caro cambiarlo.

Es el flujo por el que el área debería entrar primero. Los otros cuatro existen para lo que viene después, o para cuando esto no se hizo a tiempo.

---

## Entrada del flujo

- Un `RQ` con interfaz, y la intención de Game Design de cerrar un sistema sobre él.
- No hace falta que el `GDS` esté escrito. Ese es el punto: el presupuesto llega antes.

Si el requerimiento no tiene nada que alguien tenga que leer, el flujo lo dice y no arranca. Un `RQ` de registro interno o de estructura de carpetas no necesita presupuesto.

---

## Transformación que realiza

- Cuenta las señales que van a competir por la misma pantalla al mismo tiempo.
- Reparte los canales disponibles —color, posición, forma, tamaño, movimiento, sonido— y declara cuáles ya están ocupados.
- Fija el techo: densidad por pantalla, franjas reservadas, información permanente.
- Declara **qué no entra**, y qué habría que cambiar en el sistema para que entre.

---

## Salida esperada / formato

```txt
## Qué se va a cerrar
## Señales que compiten
## Canales disponibles
## Techo declarado
## Lo que no entra
```

Se escribe como la **mitad A** del `UXS-XXX.n`, declarando el `RQ` como insumo.

---

## Criterios de aceptación

- Hay un número: cuántas señales, cuántos bloques por pantalla, qué porcentaje de la altura ocupan las franjas.
- Cada canal ocupado dice **por qué** está ocupado.
- Lo que no entra está escrito, no omitido.
- Game Design puede cerrar el `GDS` contra el presupuesto sin volver a preguntar.

---

## Condiciones para avanzar

Game Design cierra el `GDS` citando el presupuesto. Con el `GDS` cerrado se entra al `02_Flujo_Analisis_UX`.

Si el `GDS` cierra **ignorando** el presupuesto, no es un rebote automático: es un hallazgo que el Validador declara al cerrar la mitad B, y la deuda queda escrita.

---

## Qué debe evitar

No diseña la interfaz. No decide qué estados debe tener el sistema. No entrega una lista de buenas prácticas: un presupuesto sin números es una preferencia.

---

## Resultado final

Un presupuesto contra el cual otra área puede cerrar su sistema sabiendo qué va a poder comunicar.
