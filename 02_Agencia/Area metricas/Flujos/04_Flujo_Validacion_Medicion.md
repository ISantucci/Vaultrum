## Propósito

El Flujo de Validación de Medición corre el instrumento en los tres puntos donde el área puede equivocarse sin darse cuenta —el plan, el dato y la lectura— y cierra cada modo con un veredicto medido.

Existe porque en esta área el error más caro no se ve: un evento duplicado, un entorno de prueba mezclado con el real o un KPI cambiado después de mirar producen informes perfectamente coherentes y perfectamente falsos.

---

## Entrada del flujo

Uno de tres documentos, según el modo:

```txt
plan      un MET-XXX.n terminado por el 02_Flujo_Plan_De_Medicion
dato      un CSV de eventos de una build, antes de que nadie lo lea
lectura   un MET-XXX terminado por el 03_Flujo_Lectura
```

---

## Transformación que realiza

- **Antes de confiar en el instrumento**, corre su prueba: `probar_metricas.py`.
- Sobre el plan: `metricas.py plan <ruta> --verificar`.
- Sobre el dato: `metricas.py datos <csv> --plan <MET-XXX.n> --verificar`, y declara el dato **legible**, **legible con salvedades** o **no legible**.
- Sobre la lectura: `metricas.py lectura <ruta> --verificar`, que además compara el KPI contra el del plan.
- Clasifica cada falla: de ley —rebota al agente dueño— o excepción legítima —se escribe con su razón—.
- Revisa a mano lo que el instrumento no alcanza, y lo rotula como juicio.

---

## Salida esperada / formato

```txt
## Medición                       comando y salida, textual
## Fuera de ley                   ley · detalle · a quién rebota
## Calidad del dato               legible / con salvedades / no legible, y por qué
## Fuera del alcance del instrumento   dicho como juicio
## Cierre                         Cerrado / Ajustar (a quién) / Pausado (qué falta)
```

Queda como el bloque de medición del `MET` que cierra.

---

## Criterios de aceptación

- el instrumento se probó en esta sesión antes de usarse,
- el veredicto sale del instrumento, no de una lectura del documento,
- cada falla tiene destino,
- lo juzgado a mano está separado de lo medido.

---

## Condiciones para avanzar

Avanza cuando el instrumento devuelve 0 en el modo que corresponde, o cuando cada falla restante está declarada como excepción con razón.

Queda **Pausado** cuando el dato no es legible y no hay otro: se declara qué se necesita —una build con el evento arreglado, un entorno separado, más jugadores—.

No debe avanzar si:

- el dato tiene duplicados o entornos mezclados sin limpiar,
- la lectura cambió el KPI del plan,
- el instrumento no corrió y se cerró "a ojo".

---

## Qué debe evitar este flujo

No repara el plan ni reescribe la lectura. No falla un documento por algo que la herramienta no prueba. No presenta juicio como medición.

---

## Resultado final

Tres puertas, cada una con su número: un plan que se puede implementar, un dato que se puede leer y una lectura que se puede entregar.
