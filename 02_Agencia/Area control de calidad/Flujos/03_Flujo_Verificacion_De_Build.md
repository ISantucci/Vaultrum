## Propósito

El Flujo de Verificación de Build responde una sola pregunta:

```txt
¿Vale la pena gastar horas probando esta build?
```

No intenta probar el producto. Comprueba que la entrada es testeable, y si no lo es, la rechaza antes de que el pase profundo consuma el día.

Existe porque un pase completo sobre una build rota produce cero información útil y agota el presupuesto de verificación de la iteración.

---

## Entrada del flujo

- la build congelada declarada en el intake,
- el entorno donde se va a ejecutar,
- el camino crítico del alcance: qué tiene que poder hacerse para que el pase tenga sentido.

---

## Transformación que realiza

Corre el conjunto mínimo, en orden, y con criterio de falla por ítem:

```txt
instala o actualiza
abre
la pantalla principal funciona
la entrada principal responde
el bucle principal se puede iniciar
el camino crítico del alcance no está bloqueado
no hay caída ni congelamiento inmediato
los logs no muestran una falla bloqueante evidente
guardar y cargar básico funciona, si aplica
```

En perfil Ligero el conjunto se acota al camino afectado, y eso se declara. En perfil Completo se suma la identidad de la build: que el paquete sea el que dice ser y que la versión sea única.

---

## Salida esperada / formato

```txt
## Build           identificador · rama o commit · plataforma · fecha · quién
## Checks          uno por línea, con resultado y evidencia cuando falla
## Bloqueantes     los que impiden el pase, con su identificador de defecto
## Decisión        Aceptada · Condicional · Rechazada
## Fundamento      por qué, con evidencia
```

Queda como el bloque instrumentado de verificación de build del `QA`.

---

## Criterios de aceptación

El flujo puede darse por cerrado cuando:

- todos los checks del perfil tienen resultado,
- cada falla tiene evidencia y un defecto asociado,
- la decisión está declarada,
- una build rechazada dice exactamente por qué.

---

## Condiciones para avanzar

**Aceptada** — el pase profundo empieza.

**Condicional** — la build es testeable en parte: se declara qué área queda sin poder probarse y el pase corre sobre el resto.

**Rechazada** — el pase no empieza. El área devuelve la build con los bloqueantes y su evidencia, y el `QA` cierra en **NO-GO** sin ejecutar el resto. No es un pase pendiente: es un pase que no se pudo hacer, y eso también es un resultado.

---

## Qué debe evitar este flujo

No crece. Una verificación de build que tarda dos horas dejó de ser una verificación de build: es un pase corto que ya no sirve para decidir rápido.

No arregla la build. Si falta un paso de compilación o un recurso, se devuelve.

No acepta una build "casi": los criterios bloqueantes no se negocian dentro de este flujo. Si alguien decide correr igual, es una decisión declarada de quien la toma, y queda escrita.

---

## Resultado final

Una decisión de cinco minutos que protege un día de trabajo, y una build que —cuando se acepta— vale la pena probar en serio.
