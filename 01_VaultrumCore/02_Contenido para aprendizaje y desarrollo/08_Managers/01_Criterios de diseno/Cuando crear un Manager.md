## Propósito dentro de Vaultrum

Este documento define criterios para decidir cuándo conviene crear un manager en un proyecto de videojuegos.

El objetivo es que una persona o una IA pueda tomar una decisión arquitectónica justificada, no automática.

Un manager puede ser útil para prototipar más rápido, centralizar responsabilidades y mantener orden.

Pero solo si existe una necesidad concreta.

La idea principal es:

```txt
Crear Manager
→ solo cuando hay responsabilidad administrable,
→ límites claros,
→ ciclo de vida definido,
→ y beneficio arquitectónico real.
```

---

## Criterio principal

Conviene crear un manager cuando existe una responsabilidad que necesita ser administrada de forma central, transversal o compartida.

Debe poder responderse:

```txt
¿Qué administra?
¿Por qué debe estar centralizado?
¿Quién lo usa?
¿Cuándo se inicializa?
¿Cuándo se limpia?
Qué sistemas coordina?
¿Qué no debería hacer?
```

Si esas preguntas tienen respuestas claras, el manager puede estar justificado.

Si no, probablemente todavía falta diseñar el problema.

---

## Crear un Manager por ciclo de vida

Un manager está justificado cuando una responsabilidad tiene ciclo de vida propio.

Ejemplos:

```txt
cargar assets al entrar a un nivel,
liberar assets al salir,
crear pools al iniciar gameplay,
limpiar pools al volver al menú,
inicializar audio global,
guardar datos al cerrar,
registrar sistemas actualizables,
reiniciar estado al comenzar partida.
```

Ejemplo:

```txt
AssetManager
→ carga recursos,
→ cachea referencias,
→ libera recursos.

PoolManager
→ crea objetos iniciales,
→ entrega objetos,
→ recibe objetos,
→ resetea objetos.
```

Criterio:

```txt
Si algo necesita inicialización, uso controlado y limpieza,
puede necesitar un manager.
```

---

## Crear un Manager por responsabilidad transversal

Conviene crear un manager cuando una responsabilidad cruza varios sistemas.

Ejemplos:

```txt
audio,
guardado,
assets,
input global,
eventos,
actualizaciones,
UI general,
flujo de niveles,
estado global de partida.
```

Ejemplo:

```txt
AudioManager
→ muchos sistemas quieren reproducir sonidos,
→ pero ninguno debería administrar toda la configuración de audio.
```

Otro ejemplo:

```txt
SaveManager
→ muchos sistemas aportan datos,
→ pero el proceso de guardado debería estar centralizado.
```

Criterio:

```txt
Si muchos sistemas necesitan usar la misma responsabilidad,
pero ninguno debería poseerla por completo,
un manager puede ser adecuado.
```

---

## Crear un Manager por coordinación

Conviene crear un manager cuando varios sistemas necesitan actuar en un orden determinado.

Ejemplo:

```txt
Inicio de nivel:
1. cargar datos,
2. cargar assets,
3. inicializar sistemas,
4. preparar UI,
5. iniciar estado de juego.
```

Esto puede justificar un `LevelManager`.

Pero el manager no debería hacer todo.

```txt
LevelManager
→ coordina.

AssetManager
→ carga assets.

UIManager
→ prepara interfaz.

GameManager
→ actualiza estado general.

Spawner
→ inicia oleadas.
```

Criterio:

```txt
Coordinar orden
→ sí.

Absorber responsabilidades
→ no.
```

---

## Crear un Manager por control de acceso

Un manager puede estar justificado cuando se necesita controlar cómo se accede a un recurso o servicio.

Ejemplos:

```txt
acceso a assets,
acceso a datos guardados,
acceso a configuración,
acceso a pools,
acceso a audio.
```

Ejemplo:

```txt
Sin AssetManager:
cada sistema carga assets como quiere.

Con AssetManager:
todos piden recursos mediante una API controlada.
```

Esto permite:

```txt
evitar duplicación,
evitar cargas repetidas,
controlar errores,
centralizar release,
medir uso,
y desacoplar gameplay de infraestructura.
```

---

## Crear un Manager por optimización

Algunos managers se justifican por rendimiento.

Ejemplos:

```txt
UpdateManager
→ reduce muchos Update dispersos.

PoolManager
→ evita Instantiate/Destroy constantes.

AssetManager
→ evita cargas duplicadas y assets innecesarios en memoria.

UIManager
→ evita actualizaciones innecesarias.

EventQueueManager
→ ordena procesamiento de eventos diferidos.
```

Pero la optimización debe estar conectada a un problema real.

```txt
No:
“Voy a crear UpdateManager por si acaso.”

Sí:
“Hay cientos de objetos con Update innecesario.
Medimos costo por frame.
Conviene centralizar y controlar frecuencia.”
```

---

## Crear un Manager por persistencia

Algunos managers deben sobrevivir entre escenas.

Ejemplos:

```txt
AudioManager
→ música continua entre escenas.

SaveManager
→ datos persistentes.

AssetManager
→ recursos compartidos.

GameManager
→ estado general si el flujo lo justifica.

UpdateManager
→ sistemas registrados globales si corresponde.
```

Pero persistencia no debe ser automática.

Un manager persistente debe tener reglas claras:

```txt
qué datos conserva,
qué referencias limpia,
qué referencias vuelve a vincular,
qué pasa al cambiar escena,
qué pasa al reiniciar partida.
```

Regla:

```txt
Persistir estado útil
→ válido.

Persistir referencias destruidas de escena
→ peligroso.
```

---

## Crear un Manager para prototipado

En prototipos, un manager puede ser útil para avanzar rápido.

Pero Vaultrum busca prototipos escalables, no prototipos descartables llenos de deuda innecesaria.

Un manager de prototipo debería tener:

```txt
nombre claro,
responsabilidad acotada,
API mínima,
comentarios sobre límites,
y una ruta clara de refactor si crece.
```

Ejemplo aceptable:

```txt
PrototypeGameFlowManager
→ coordina pantalla inicial, inicio de partida y pantalla final.
```

Pero debería evitarse:

```txt
PrototypeManager
→ hace todo.
```

---

## Relación con SOLID

Crear un manager puede ayudar a S - Single Responsibility Principle si extrae una responsabilidad dispersa y la centraliza de forma clara.

Ejemplo:

```txt
Antes:
cada sistema maneja audio por separado.

Después:
AudioManager administra audio.
Los demás sistemas solo solicitan reproducción.
```

Pero puede romper SRP si se convierte en centro de todo.

La decisión debe respetar:

```txt
SRP
→ una responsabilidad central.

ISP
→ API mínima.

DIP
→ dependencias claras y, si conviene, abstracciones.

OCP
→ posibilidad de extender sin modificar constantemente el núcleo.
```

Un manager no debería crearse si va a ser una interfaz gigante que todo el proyecto usa para todo.

---

## Criterio para IA/agente

Una IA puede proponer crear un manager si puede completar esta justificación:

```txt
Propongo crear [NombreManager] porque:

Problema detectado:
...

Responsabilidad central:
...

Sistemas involucrados:
...

Alternativas descartadas:
...

Por qué no alcanza una clase común:
...

Por qué no corresponde Factory/Facade/Pool/Event/StateMachine:
...

API mínima:
...

Responsabilidades prohibidas:
...

Riesgos:
...

Validación:
...
```

Si la IA no puede completar esa justificación, no debería proponer el manager todavía.

---

## Ejemplo aplicado a videojuegos

Supongamos un juego donde las torres, enemigos, UI y recompensas modifican o consultan dinero.

Mala solución:

```txt
GameManager
→ tiene métodos para todo:
AddMoney,
SpendMoney,
SpawnEnemy,
UpdateUI,
PlaySound,
SaveGame.
```

Mejor análisis:

```txt
La responsabilidad real es economía.

Posibles piezas:
EconomySystem
→ administra dinero.

GameEvents
→ notifica cambios.

UI
→ escucha cambios.

GameManager
→ coordina estado general, no cada operación económica.
```

Conclusión:

```txt
No siempre hace falta un manager nuevo.
A veces hace falta separar un sistema específico.
```

---

## Checklist para crear un Manager

Antes de crear un manager:

```txt
¿Hay problema concreto?
¿Hay responsabilidad central?
¿Hay ciclo de vida?
¿Hay acceso compartido?
¿Hay coordinación real?
¿Hay recursos compartidos?
¿Hay estado global limitado?
¿Hay beneficio de optimización?
¿La responsabilidad no pertenece a otra pieza?
¿La API puede ser pequeña?
¿Se puede definir qué NO hace?
¿Se puede probar o validar?
¿Se puede mantener SOLID?
```

---

## Regla final

Crear un manager es correcto cuando administra una responsabilidad real.

No cuando reemplaza el diseño.

```txt
Manager justificado
→ resuelve ciclo de vida, coordinación, acceso o estado compartido.

Manager injustificado
→ es una excusa para centralizar código sin criterio.
```