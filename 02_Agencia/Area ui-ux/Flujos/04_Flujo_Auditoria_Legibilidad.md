## Propósito

Medir el estado real de las seis leyes sobre un `UXS`, y entregar el informe sin proponer ni tocar nada todavía.

---

## Entrada del flujo

- Un `UXS` instrumentado, o la carpeta de salidas completa.
- O una entrega que falló el gate de cierre, para saber qué la dejó fuera de ley.
- Ninguna otra condición: la auditoría se puede correr siempre.

---

## Transformación que realiza

- Corre `Herramientas/legibilidad.py` sobre la ruta.
- Lista lo que está fuera de ley por ley y por archivo, con su número.
- Separa lo que tiene excepción declarada en `Herramientas/excepciones.txt` de lo que no la tiene.
- Separa lo que la herramienta **no puede probar**, y lo dice como juicio.

---

## Salida esperada / formato

```txt
## Medición
## Fuera de ley
## Excepciones declaradas
## Fuera del alcance de la herramienta
```

---

## Criterios de aceptación

- Los números salen de la herramienta, no de una lectura a ojo.
- Cada falla dice qué ley infringe y con qué valor.
- Lo que sigue siendo juicio está separado y rotulado como juicio.

---

## Condiciones para avanzar

Avanza al `05_Flujo_Validacion_UX` con el informe completo.

No avanza si la medición no se pudo correr: en ese caso se declara *medición no disponible* y se detiene. Un `UXS` sin instrumentar se reporta como **spec sin instrumentar** y vuelve al diseño.

---

## Qué debe evitar

No repara nada. No propone cambios. No estima un contraste ni una distinción sin haber corrido la herramienta.

---

## Resultado final

Un informe que dice exactamente qué ley está en rojo, dónde y con qué número.
