## Descripción

Un `SaveManager` administra guardado y carga de datos persistentes.

Su responsabilidad es coordinar el proceso de persistencia, no ser dueño absoluto de todos los datos del juego.

Debe diferenciar entre:

```txt
datos guardables,
estado runtime,
objetos de escena,
configuración,
progreso,
perfil.
```

---

## Qué problema resuelve

Resuelve problemas como:

```txt
guardar progreso,
cargar partida,
persistir configuración,
centralizar serialización,
evitar guardados dispersos,
controlar slots,
manejar errores de guardado,
coordinar datos de distintos sistemas.
```

---

## Cuándo conviene usarlo

Conviene cuando:

```txt
hay progreso persistente,
hay configuración guardable,
hay desbloqueos,
hay niveles completados,
hay inventario,
hay perfil de usuario,
hay slots de guardado,
varios sistemas aportan datos.
```

---

## Cuándo NO conviene usarlo

No conviene si:

```txt
el juego no guarda nada,
solo hay PlayerPrefs simples,
la persistencia es mínima,
o se quiere usar SaveManager para almacenar todo el estado runtime.
```

Tampoco debe crearse para ocultar falta de modelos de datos.

---

## Responsabilidades permitidas

Puede encargarse de:

```txt
guardar datos,
cargar datos,
validar existencia de guardado,
manejar slots,
serializar,
deserializar,
notificar éxito o error,
coordinar proveedores de datos guardables,
guardar configuración.
```

---

## Responsabilidades prohibidas

No debería:

```txt
decidir gameplay,
crear objetos de escena directamente,
modificar UI directamente,
manejar audio,
controlar niveles,
calcular progreso por sí solo si otro sistema lo posee,
guardar referencias directas a GameObjects,
ser dueño de todos los sistemas.
```

Regla:

```txt
SaveManager guarda datos.
No reemplaza los sistemas que producen esos datos.
```

---

## Relación con otras piezas arquitectónicas

Relaciones comunes:

```txt
GameManager
→ puede solicitar guardado global.

LevelManager
→ informa progreso de nivel.

AudioManager
→ configuración de volumen.

UIManager
→ muestra resultado de guardado.

Memento
→ puede capturar snapshots.

Sistemas guardables
→ exponen datos para guardar.
```

Un diseño sano puede usar interfaces:

```csharp
public interface ISaveable
{
    string SaveId { get; }
    object CaptureState();
    void RestoreState(object state);
}
```

Usar con criterio, no por decoración.

---

## Ciclo de vida

Flujo posible:

```txt
Initialize
→ cargar perfil o configuración.

SaveGame
→ pedir datos a sistemas.

LoadGame
→ restaurar datos.

SaveSettings
→ persistir configuración.

Shutdown
→ guardar si corresponde.
```

Debe manejar errores.

Ejemplos:

```txt
archivo inexistente,
formato inválido,
versión vieja,
permiso denegado,
datos corruptos.
```

---

## API mínima recomendada

```csharp
public interface ISaveManager
{
    bool HasSave(string slotId);
    void SaveGame(string slotId);
    void LoadGame(string slotId);
    void DeleteSave(string slotId);
}
```

Opcional:

```csharp
event Action<string> SaveCompleted;
event Action<string> SaveFailed;
event Action<string> LoadCompleted;
event Action<string> LoadFailed;
```

---

## Ejemplo aplicado a videojuegos

Juego con niveles desbloqueables:

```txt
LevelManager completa nivel.
ProgressSystem marca nivel completado.
SaveManager.SaveGame("slot_1").
SaveManager serializa progreso.
UI muestra “Guardado completado”.
```

SaveManager no decide si el nivel fue completado.

Solo guarda el dato que el sistema correspondiente produce.

---

## Errores comunes

```txt
guardar GameObjects directamente,
mezclar runtime con persistencia,
hacer que SaveManager decida gameplay,
no manejar versiones,
no manejar errores,
guardar desde muchos lugares sin coordinación,
usar strings mágicos sin control,
hacer UI directa desde SaveManager,
no separar configuración de partida.
```

---

## Checklist para IA/agente

Antes de modificar `SaveManager`:

```txt
¿Qué datos se guardan?
¿Quién posee esos datos?
¿SaveManager produce datos o los recolecta?
¿Hay slots?
¿Hay configuración separada?
¿Hay manejo de errores?
¿Hay versión de datos?
¿Se guardan referencias de escena por error?
¿Se notifica resultado por eventos?
¿Se evita lógica de gameplay?
```

---

## Regla final

`SaveManager` administra persistencia.

```txt
Sano:
guarda y carga datos claros.

Peligroso:
se vuelve dueño de todo el estado del juego.
```