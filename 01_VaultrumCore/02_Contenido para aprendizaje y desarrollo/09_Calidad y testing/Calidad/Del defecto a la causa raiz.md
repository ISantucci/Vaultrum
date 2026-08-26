## Que es

El recorrido completo de un defecto: desde que alguien lo ve hasta que el sistema aprende a no repetirlo.

```txt
se observa → se reporta → se clasifica → se arregla → se confirma → se protege → se entiende
```

Cortar el recorrido antes de tiempo es lo que produce los dos problemas clasicos: tickets que se cierran sin verificar, y el mismo defecto apareciendo por tercera vez con otro nombre.

---

## El reporte

Un reporte de defecto existe para que **otra persona** pueda entenderlo, reproducirlo, estimar su impacto y verificar el arreglo. Si no habilita las cuatro cosas, no es un reporte: es un aviso.

Campos minimos:

```txt
identificador
titulo observable y especifico
version o build, y rama o commit si aplica
plataforma y entorno
sistema o area afectada
precondiciones
pasos para reproducir, numerados
resultado esperado
resultado obtenido
reproducibilidad: siempre / intermitente / una vez
severidad
prioridad
evidencia
requisito o caso de prueba asociado
dueno
version del arreglo
resultado de la confirmacion
si necesita regresion
```

### El titulo

Es el campo que mas se lee y el que peor se escribe. Un buen titulo tiene contexto, accion y falla.

```txt
malos     "bug de inventario" · "no anda" · "problema al tirar cosas"
util      [Inventario][Descartar] el item se borra sin confirmacion al soltarlo fuera de la ventana
```

La diferencia practica: con el segundo, quien triagea decide sin abrir el ticket, y quien busca duplicados los encuentra.

### La evidencia

Segun el caso: captura, video, log, traza de error, captura del medidor de rendimiento, archivo de partida guardada, semilla, identificador de build, dispositivo, salida de la prueba.

Regla de la evidencia: **la minima que prueba el punto.** Cincuenta capturas no valen mas que una y un log; valen menos, porque nadie las mira.

### Lo intermitente

Un defecto que no se reproduce siempre no se descarta: se reporta como intermitente, con las condiciones bajo las que aparecio y cuantas veces de cuantos intentos. Los intermitentes suelen ser de tiempo, de orden, de concurrencia o de datos, y son exactamente los que llegan al jugador.

---

## El ciclo de vida

```txt
Abierto → Triado → En progreso → Listo para reverificar → Cerrado
```

Con ramas:

```txt
Reabierto     el arreglo no resolvio, o rompio otra cosa
Diferido      valido, se arregla mas adelante: exige version objetivo o riesgo aceptado
Duplicado     apunta al original
No se arregla decision explicita, con razon escrita
```

Cuatro reglas que sostienen todo lo demas:

```txt
quien programa NO marca cerrado: marca listo para reverificar
cierra quien verifico el arreglo, sobre una version identificable
si el arreglo falla, vuelve a abierto, no se discute en un comentario
diferir y no arreglar son decisiones con dueno y razon, no silencios
```

La primera es la que mas resistencia genera y la que mas defectos evita. Cambiar codigo no es lo mismo que resolver el problema.

---

## El triage

La reunion corta donde se decide que se hace con lo que aparecio. Participan quien verifico, quien es dueno tecnico del sistema y produccion cuando el impacto lo justifica.

Se decide, por defecto:

```txt
es valido
severidad
prioridad
dueno
se arregla ahora, se difiere, o no se arregla
bloquea la entrega o no
necesita regresion
necesita analisis de causa raiz
```

Un triage que solo asigna duenos no es un triage: es un reparto.

---

## Despues del arreglo

Dos pasos distintos y los dos obligatorios:

```txt
confirmacion   el defecto reportado, exactamente ese, no ocurre en la version que dice arreglarlo
regresion      lo que ya funcionaba alrededor sigue funcionando
```

Y una decision: si el defecto era grave o el sistema es fragil, el caso **entra a la suite de regresion**. Un defecto que se arreglo y no dejo prueba detras puede volver sin que nadie se entere.

No todo entra: una suite de regresion infinita deja de correrse. Entra lo que cumple el criterio de que volver a romperlo cueste mas que protegerlo.

---

## El analisis de causa raiz

Se activa cuando el defecto revela un problema de proceso, no solo de codigo:

```txt
un bloqueante o critico llego al jugador
hubo perdida o corrupcion de datos
una entrega fallo
el mismo defecto volvio
una regresion se repitio
un defecto caro que se podria haber visto mucho antes
```

Las seis preguntas:

```txt
1. que ocurrio, en orden de tiempo
2. por que el producto permitio ese comportamiento
3. por que el proceso no lo detecto antes
4. que senal habia y nadie miro, o no existia
5. que cambio previene la recurrencia
6. que prueba, regresion, herramienta o documento queda como resultado
```

La tercera es la unica que produce mejora. Las dos primeras arreglan **este** defecto; la tercera arregla la clase entera.

**No se buscan culpables: se busca el mecanismo de falla.** Un analisis que termina en el nombre de una persona no deja nada aprendido — la persona ya sabia, y la proxima vez va a ser otra.

Su salida no es un documento: es un cambio concreto. Un caso de regresion nuevo, una validacion automatica, un dato que ahora se valida al cargar, un paso que ahora corre solo. Si el analisis no deja nada que corra, no cambio nada.

---

## Regla final

```txt
Un ticket cerrado no es un defecto resuelto.

Un defecto esta resuelto cuando el arreglo se verifico,
lo que rompio quedo protegido, y el sistema sabe como no repetirlo.
```
