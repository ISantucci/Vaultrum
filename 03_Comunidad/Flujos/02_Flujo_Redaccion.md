## Propósito

Convertir el informe de avance en el texto publicable, en español e inglés, con el formato fijo de la cuenta.

---

## Entrada del flujo

- El informe del `01_Flujo_Lectura_De_Avance` con veredicto **hay post**.
- El mensaje central declarado.
- Las fichas del Archivo de las últimas publicaciones, para no repetir estructura ni apertura.

No arranca sin informe. Escribir primero y buscar el respaldo después es exactamente el orden que produce humo.

---

## Transformación que realiza

- Declara **los tres tiempos** —problema, implementación, caso de uso— antes de escribir una línea.
- Elige la forma del post: actualización de sistema, entrega de proyecto, o reaparición.
- Escribe la versión en español, que es la que fija el contenido.
- Escribe la versión en inglés con el mismo contenido y lectura natural.
- Escribe la versión corta de 280 caracteres con el mismo mensaje central.
- Arma **un solo bloque** con los dos idiomas adentro, en el formato de salida de la cuenta.

---

## Salida esperada / formato

Un solo bloque bajo el título `## Post`, con los dos idiomas adentro separados por una línea de **exactamente cinco guiones**:

```txt
[post en español]

-----

[post en inglés]

---

Actualización en la red Vaultrumita / Vaultrumite red update:
[imagen del árbol de nodos]
```

Y la versión corta con la misma forma: un bloque bajo `## Versión corta`, los dos idiomas, el mismo separador, cada mitad dentro de los 280 caracteres.

El texto se parte en dos secciones solo en un borrador. Lo que se registra es lo que se copia y se publica de una sola vez.

---

## Criterios de aceptación

- Ninguna afirmación del texto está fuera del informe.
- Todo número del texto aparece igual en el informe.
- Las dos versiones dicen lo mismo; ninguna tiene una afirmación que la otra no tenga.
- Lo no construido, si se menciona, está declarado como no construido.
- El texto está en **un solo bloque** por título, con el separador de cinco guiones exacto.
- Los tres tiempos están declarados y se leen en el post, en ese orden.
- El caso de uso es real y con resultado, o su ausencia está declarada.
- `Herramientas/post.py --verificar` devuelve 0 sobre la `PUB`.

---

## Condiciones para avanzar

Avanza al `03_Flujo_Pedido_De_Capturas` cuando el texto está cerrado en los dos idiomas **y el formato pasó la herramienta**. Un texto correcto en un formato que la herramienta no puede leer no está cerrado: está escrito.

No avanza con el español listo y el inglés pendiente: son un solo entregable.

---

## Qué debe evitar

No agrega datos. No suaviza un pendiente para que suene mejor. No promete lo que no existe. No usa la palabra "automático" para describir algo que alguien tiene que apretar.

---

## Resultado final

El texto del post, cerrado, en los dos idiomas, sin una sola afirmación que no venga del informe.
