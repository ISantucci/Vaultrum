## Propósito

Verificar la ley 6: lo que se entrega se parsea. El instrumento lee el archivo entregado, no el fuente.

---

## Entrada del flujo

- Un `ART-XXX.n` con `06_Flujo_Verificacion_Malla` cerrado en verde.
- Un pedido de entrega en formato externo: `.glb`, `.fbx`.
- El contrato del cliente: nomenclatura, ejes, unidades, qué puede venir adentro del archivo.

Es condicional. Sin entrega externa, no corre.

---

## Transformación que realiza

- Corre `arte.entrega()` con `07_Integrador_Entrega` sobre el archivo exportado.
- Nombres de malla, comparados contra el contrato del cliente.
- Ejes y unidades tal como quedaron escritos en el archivo.
- Basura colada: todo objeto que está adentro y no fue declarado.
- Cada especificación medible se ajusta hasta dar el valor, y recién entonces se afirma.

---

## Salida esperada / formato

```txt
## Archivo parseado
   ruta y formato
## Nombres
   declarado contra encontrado
## Ejes y unidades
## Objetos no declarados
## Especificaciones ajustadas
   valor pedido y valor medido
```

---

## Es otro dominio de falla

Los tres defectos de exportación ocurrieron con la malla en ley: nombres de malla huérfanos, un `Cube` colado desde el view layer de otra escena, y el contrato de nomenclatura del cliente sin cumplir. Ninguno lo podía ver `arte.malla()`, porque ninguno estaba en la malla. El fuente puede estar impecable y el archivo entregado estar mal.

De ahí la regla del flujo: el contrato del cliente le gana a la convención interna. Cuando los dos no coinciden, manda el contrato y la diferencia se escribe.

---

## Ajustar, no afirmar

Regla de `RA-007`: una especificación medible se ajusta, no se afirma. La Figura_Humana cerró en 75.00 kg y 1.750 m porque se ajustó hasta dar, no porque alguien escribiera que los daba.

---

## Criterios de aceptación

- La medición salió del archivo entregado, no del fuente.
- Cada nombre está comparado contra el contrato, línea a línea.
- Cero objetos no declarados adentro del archivo.
- Toda especificación medible tiene valor pedido y valor medido, y coinciden.

---

## Condiciones para avanzar

No avanza a ningún flujo: cierra el `ART-XXX.n`.

No cierra si el archivo no se pudo parsear, si aparece un objeto no declarado o si un nombre no cumple el contrato. Eso vuelve a exportación con el hallazgo concreto, y se parsea de nuevo.

Cuando el flujo no corre por no haber entrega externa, la omisión se declara con su razón y el `ART-XXX.n` cierra en `06_Flujo_Verificacion_Malla`.

---

## Qué debe evitar

No mide el fuente y llama a eso entrega. No afirma un peso ni una altura sin haberlos ajustado. No impone la convención interna por encima del contrato. No borra un objeto colado sin escribir de dónde vino.

---

## Resultado final

Un archivo entregado leído como lo va a leer el cliente, con sus nombres, sus ejes, sus unidades y su contenido verificados contra el contrato.
