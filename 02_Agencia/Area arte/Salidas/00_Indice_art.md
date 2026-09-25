## Propósito

Registro del contrato de salida del Área de Arte.

Cada `ART` declara **qué se construyó, con qué se midió y qué quedó sin medir**. No es una galería: es el documento contra el cual otra área puede consumir un asset sin abrir el archivo fuente.

---

## Los dos cortes

| Artefacto | Cierra | Cuelga de | Cuándo |
|---|---|---|---|
| `ART-XXX.n` | un hilo: el asset o el set de assets de un requerimiento | `RQ-XXX.n` | el hilo terminó su verificación de malla |
| `ART-XXX` | la entrega: la pasada sobre el set completo | `TL-XXX` | todos los hilos cerraron y la épica va a cerrarse |

Es el mismo corte que Control de Calidad, y por una razón estructural y no por copiar: **la coherencia visual y el costo en pantalla son propiedades del conjunto.** No se pueden medir asset por asset. Doce assets que pasan individualmente pueden ser un set incoherente y un presupuesto reventado.

La mitad A del `ART-XXX.n` —dimensión maestra, presupuesto por familia y paleta— cuelga además del `LDS-XXX.n`, porque la escala del arte sale de la escala del espacio.

---

## Numeración

La subnumeración `.n` se hereda del hilo, igual que el resto de la cadena:

```txt
RQ-001.2  ->  GDS-001.2  ->  LDS-001.2  ->  ART-001.2
```

`ART-XXX` **no lleva `.n`**, igual que `QA-XXX` y `VE-XXX`: la decisión sobre el conjunto es del entregable y no de la pieza.

---

## Las cuatro secciones segregadas

El `ART` **se lee por secciones**, y cada consumidor tiene la suya declarada. Es segregación de interfaz aplicada a un documento: nadie depende de lo que no usa.

```txt
Contrato de escala        -> Level Design   dimension maestra · huella · altura ·
                                            tabla de proporcion contra los assets
                                            que ya existen
Contrato de lectura       -> UI/UX          silueta en gris · separacion de color
                                            entre familias · contraste contra el
                                            terreno
Contrato de integracion   -> Programacion   archivo y ruta · bbox en metros ·
                                            z_min · origen · eje · nomenclatura ·
                                            transform sucio (idealmente vacio)
Contrato de costo         -> Produccion     objetos · caras · caras x instancias
                                            maximas simultaneas · relleno por
                                            clase con cada cascara justificada
```

Programación no necesita saber cómo se resolvió una junta. UI/UX no necesita la topología. **La ficha lo dice, no lo mezcla.**

---

## Contenido mínimo

Además de las cuatro secciones de arriba:

```txt
Las seis leyes    medidas, una por una, con su veredicto
Decisiones        y por que
Lo que salio mal  y con que se vio
```

La última no es autocrítica: **es lo que hace que el defecto no vuelva.** Las nueve reglas de construcción `RA-001` a `RA-009` salieron todas de ahí.

---

## Si el `ART` es una animación

Una secuencia no tiene malla, así que tres de las cuatro secciones cambian de contenido y ninguna desaparece:

```txt
Contrato de escala        -> la referencia maestra y su version, alto de la silueta,
                             linea de suelo, lienzo y pivot
Contrato de lectura       -> la accion en silueta, a la escala y sobre el fondo reales
Contrato de integracion   -> el manifiesto: orden, duracion por cuadro, loop, eventos,
                             entrada y salida, in-place o root motion
Contrato de costo         -> cuadros, lienzo y atlas
```

Y una sección más, obligatoria: **el nivel de validación alcanzado** —propuesta visual, secuencia validada, exportación validada o integración comprobada— con la salida de `animacion.py` que lo sostiene. Detalle en `RA-012`.

---

## Dónde aterriza

```txt
la ficha     <Proyecto>/07_Arte/ART-XXX.n_<Nombre>.md
el archivo   .blend / .glb / .fbx, donde el TL diga
```

Rige el **gate de existencia en disco**: lo que la ficha afirma terminado tiene que estar en disco, y se comprueba.

---

## Cuándo un `ART` no cierra

```txt
la malla no esta en ley             rebota al 03_Modelador con el hallazgo
un paso condicional no corrio y     es un hueco, no una omision
NO declaro su omision
un numero sin instrumento           el area estaria estimando
dos sillas se rebotan y no cierran  Pausado, y decide el owner
```

Un `ART` cerrado es insumo de Programación, que lo integra en el motor.

---

## Registro

Los artefactos de un proyecto **no se registran acá**. Viven en `06_Proyectos/<Proyecto>/07_Arte/` y se listan en el cuaderno de ese proyecto.

Este índice es el **contrato de salida** del área: qué produce, qué forma tiene, cómo se numera y cuándo está cerrado. No es un archivo.

---

## Regla

- Un `ART` no cierra sin estar medido: un asset que se afirma en ley y no se midió está estimado.
- La verificación de malla corre **después de emparentar**, o no prueba el asset que se va a exportar.
- Todo paso condicional que no corre **declara su omisión con su razón**.
- El contrato del cliente le gana a la convención interna, y se comprueba leyendo el archivo entregado.
- Toda excepción vive en `Herramientas/excepciones.txt` con su razón escrita.
