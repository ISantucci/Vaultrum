## Descripción

Un `AudioManager` administra reproducción, configuración y control de audio.

Suele ser uno de los managers más justificados porque el audio atraviesa muchos sistemas.

Su responsabilidad debe mantenerse acotada al dominio de audio.

---

## Qué problema resuelve

Resuelve problemas como:

```txt
muchos sistemas reproduciendo audio por separado,
volumen global,
música entre escenas,
SFX,
mute,
mezcla de audio,
configuración persistente,
evitar referencias directas a AudioSource en todos lados.
```

---

## Cuándo conviene usarlo

Conviene cuando:

```txt
varios sistemas necesitan reproducir sonidos,
hay música de fondo,
hay configuración de volumen,
el audio persiste entre escenas,
hay múltiples canales,
hay feedback sonoro de UI o gameplay.
```

---

## Cuándo NO conviene usarlo

No conviene si:

```txt
hay uno o dos sonidos simples,
no hay configuración,
no hay música,
un AudioSource local alcanza,
o se quiere usar para manejar cosas ajenas al audio.
```

---

## Responsabilidades permitidas

Puede encargarse de:

```txt
reproducir música,
detener música,
cambiar música,
reproducir SFX,
controlar volumen,
mutear/desmutear,
administrar canales,
escuchar eventos para reproducir sonidos,
mantener configuración de audio.
```

---

## Responsabilidades prohibidas

No debería:

```txt
cambiar escenas,
decidir estados de juego,
guardar todo el juego,
modificar UI directamente,
calcular gameplay,
controlar niveles,
instanciar enemigos,
manejar input global.
```

---

## Relación con otras piezas arquitectónicas

Relaciones comunes:

```txt
GameManager
→ emite cambios de estado.

UIManager
→ puede solicitar sonido de botones.

EventQueueManager / eventos
→ notifican acciones relevantes.

SaveManager
→ puede guardar configuración de volumen.

AssetManager
→ puede cargar clips o bancos de audio.
```

El `AudioManager` puede escuchar eventos, pero solo para reaccionar con audio.

---

## Ciclo de vida

Puede ser persistente si la música o configuración atraviesan escenas.

Flujo posible:

```txt
Initialize
→ cargar configuración.

PlayMusic
→ reproducir pista.

PlaySfx
→ reproducir sonido.

SetVolume
→ cambiar configuración.

Shutdown
→ liberar recursos si corresponde.
```

Si persiste, evitar duplicados.

---

## API mínima recomendada

```csharp
public interface IAudioManager
{
    void PlaySfx(string sfxId);
    void PlayMusic(string musicId);
    void StopMusic();
    void SetMasterVolume(float value);
}
```

Opcional:

```csharp
void SetMusicVolume(float value);
void SetSfxVolume(float value);
void Mute();
void Unmute();
```

No agregar métodos ajenos al audio.

---

## Ejemplo aplicado a videojuegos

```txt
Enemy muere.
Evento EnemyKilled.
AudioManager escucha.
AudioManager.PlaySfx("enemy_killed").
```

Otro:

```txt
GameStateChanged(Win).
AudioManager cambia música a victoria.
```

Audio reacciona al juego.

No controla el juego.

---

## Errores comunes

```txt
hacer que AudioManager cambie escenas,
hacerlo singleton sin control de duplicados,
no separar música y SFX,
no guardar configuración correctamente,
exponer AudioSources internos,
no liberar clips si se cargan dinámicamente,
escuchar demasiados eventos no relacionados.
```

---

## Checklist para IA/agente

Antes de modificar `AudioManager`:

```txt
¿El cambio pertenece al audio?
¿Está escuchando eventos correctos?
¿Debe persistir entre escenas?
¿Evita duplicados?
¿Expone AudioSources internos?
¿Tiene configuración de volumen?
¿La API es mínima?
¿No está decidiendo gameplay?
¿Necesita AssetManager para clips?
```

---

## Regla final

`AudioManager` administra audio.

```txt
Sano:
reproduce, configura y reacciona.

Peligroso:
usa el audio como excusa para controlar flujo de juego.
```