## Descripción

Un `UIManager` coordina pantallas, paneles, navegación visual y actualización de interfaz.

No debería decidir gameplay.

La UI muestra estado y captura intención.

Los sistemas de gameplay validan, ejecutan y notifican resultados.

```txt
UI
→ muestra y solicita.

Gameplay
→ decide y ejecuta.
```

---

## Propósito dentro de Vaultrum

Este documento define cómo diseñar o auditar un `UIManager` sin convertir la interfaz en dueña del gameplay.

La UI suele ser una de las zonas donde más fácilmente se mezcla lógica visual con lógica de juego.

Por eso, un `UIManager` sano debe tener límites claros.

Regla base:

```txt
UIManager coordina interfaz.
No decide reglas de juego.
```

---

## Qué problema resuelve

Un `UIManager` puede resolver problemas como:

```txt
muchos paneles sin coordinación,
navegación de pantallas,
mostrar/ocultar UI,
actualización visual desde eventos,
evitar UI actualizada cada frame,
separar UI de gameplay,
centralizar referencias visuales de una escena,
mantener flujo visual claro.
```

Ejemplo:

```txt
Jugador pausa.
GameManager cambia estado.
UIManager muestra PauseMenu.
```

La UI representa el estado.

No decide si el juego realmente está pausado.

---

## Cuándo conviene usarlo

Conviene cuando:

```txt
hay múltiples pantallas,
hay HUD,
hay paneles modales,
hay menú de pausa,
hay feedback visual,
hay navegación compleja,
hay muchos elementos que reaccionan a eventos,
se quiere evitar que gameplay manipule UI directamente.
```

También conviene cuando hay varios controladores visuales y se necesita coordinación.

Ejemplos:

```txt
HUD,
PauseMenu,
UpgradePanel,
LevelSelect,
SettingsPanel,
WinScreen,
LoseScreen.
```

---

## Cuándo NO conviene usarlo

No conviene si:

```txt
la UI es mínima,
hay un único panel simple,
un controlador local alcanza,
o el UIManager va a absorber lógica de gameplay.
```

Tampoco debe ser un singleton global si solo controla UI de una escena.

Regla:

```txt
No crear UIManager global para resolver un botón.
```

---

## Responsabilidades permitidas

Puede encargarse de:

```txt
abrir paneles,
cerrar paneles,
navegar pantallas,
mostrar HUD,
ocultar HUD,
escuchar eventos visuales,
actualizar vistas,
coordinar animaciones UI,
hacer bind/unbind de vistas de escena,
mostrar feedback visual,
coordinar popups.
```

También puede administrar el estado visual de pantallas.

Ejemplo:

```txt
MainMenuScreen activo.
SettingsPanel cerrado.
PauseMenu abierto.
HUD oculto.
```

---

## Responsabilidades prohibidas

No debería:

```txt
calcular daño,
modificar economía directamente,
decidir si una torre puede comprarse,
crear enemigos,
guardar partida,
cargar assets de gameplay,
controlar niveles,
contener reglas de negocio,
ejecutar comandos sin pasar por una facade o sistema,
decidir victoria o derrota,
decidir si una acción es válida.
```

Regla:

```txt
UIManager no decide reglas.
UIManager representa estado.
```

---

## Relación con GameplayFacade

En proyectos con UI interactiva, una `GameplayFacade` puede ser una buena barrera entre UI y gameplay.

La UI captura intención:

```txt
Jugador toca botón de vender.
```

La facade interpreta esa intención hacia el sistema correcto:

```txt
UI
→ GameplayFacade.SellSelectedTower()
→ Command / BuildInvoker / Economy / Events
```

La UI no debería hacer:

```txt
UI
→ resta dinero
→ destruye torre
→ actualiza HUD
→ guarda historial
```

Regla:

```txt
La UI pide.
La facade coordina.
El gameplay decide.
```

---

## Relación con eventos

Un `UIManager` sano suele reaccionar a eventos.

Ejemplos:

```txt
MoneyChanged
HealthChanged
GamePaused
GameResumed
TowerSelected
TowerDeselected
LevelCompleted
WaveStarted
WaveEnded
UpgradePurchased
```

Flujo sano:

```txt
EconomySystem cambia dinero.
Emite MoneyChanged.
HUD actualiza texto.
```

Flujo peligroso:

```txt
HUD consulta dinero cada frame.
```

Regla:

```txt
La UI debería actualizarse cuando cambia el estado,
no preguntar todo el tiempo si cambió.
```

---

## Relación con GameManager

El `GameManager` puede emitir estados globales.

El `UIManager` puede representarlos.

Ejemplo:

```txt
GameManager.EndGame(Win)
→ GameStateChanged(Win)
→ UIManager.ShowScreen(WinScreen)
```

El `UIManager` no debería decidir por sí mismo que el jugador ganó.

---

## Relación con LevelManager

El `LevelManager` puede informar entrada, salida o progreso del nivel.

El `UIManager` puede mostrar esa información.

Ejemplo:

```txt
LevelManager.LevelEntered(Level1)
→ UIManager.ShowHud()
→ ObjectiveView muestra objetivos.
```

Separación:

```txt
LevelManager
→ sabe qué nivel está activo.

UIManager
→ muestra la información visual del nivel.
```

---

## Relación con AudioManager

El `UIManager` puede solicitar sonidos de interfaz o emitir eventos que el `AudioManager` escuche.

Ejemplo:

```txt
ButtonClicked
→ AudioManager.PlaySfx("ui_click")
```

Pero no conviene que `UIManager` administre música, volúmenes o SFX complejos.

Separación:

```txt
UIManager
→ interacción visual.

AudioManager
→ respuesta sonora.
```

---

## Ciclo de vida

Un `UIManager` puede ser:

```txt
por escena,
por menú,
por HUD de gameplay,
por flujo global si la UI persiste.
```

Si es de escena, se crea y destruye con la escena.

Si persiste entre escenas, debe limpiar referencias visuales destruidas.

Métodos posibles:

```csharp
public void ShowScreen(string screenId);
public void HideScreen(string screenId);
public void ShowHud();
public void HideHud();
public void BindSceneViews();
public void UnbindSceneViews();
```

---

## UIManager persistente entre escenas

Un `UIManager` persistente puede ser útil si hay UI global.

Ejemplos:

```txt
pantalla de carga,
overlay global,
notificaciones globales,
menú persistente,
sistema de popups global.
```

Pero es riesgoso si guarda referencias a objetos de escena.

Riesgos:

```txt
referencias destruidas,
paneles duplicados,
eventos duplicados,
HUD viejo,
botones apuntando a objetos inexistentes,
errores al recargar escena.
```

Regla:

```txt
Si UIManager persiste, debe hacer bind/unbind de referencias de escena.
```

---

## API mínima recomendada

Ejemplo simple:

```csharp
public interface IUIManager
{
    void ShowScreen(string screenId);
    void HideScreen(string screenId);
    void ShowHud();
    void HideHud();
}
```

Para HUD específico, muchas veces conviene controladores separados:

```txt
HealthView
MoneyView
UpgradePanel
PauseMenu
LevelSelectView
```

No todo debe pasar por UIManager.

Regla:

```txt
UIManager coordina pantallas.
Las vistas específicas muestran datos específicos.
```

---

## Ejemplo aplicado a videojuegos

Tower Defense:

```txt
Jugador toca botón de torre.
UI captura intención.
GameplayFacade.TrySelectTower(towerId).
Si se puede, se habilita colocación.
GameEvents notifican dinero o selección.
HUD actualiza visualmente.
```

Correcto:

```txt
UI
→ GameplayFacade
→ Command / System
→ Events
→ UI actualiza.
```

Incorrecto:

```txt
UIManager resta dinero,
instancia torre,
actualiza economía,
guarda partida,
y reproduce audio.
```

---

## Ejemplo con upgrades

Flujo sano:

```txt
Jugador toca botón Upgrade.
TowerUpgradeRowUI captura click.
GameplayFacade.BuyUpgrade(upgradeType).
BuildInvoker ejecuta Command.
TowerUpgradeComponent aplica upgrade.
GameEvents emite TowerUpgraded.
UpgradePanel actualiza vista.
```

La UI no calcula si el upgrade es válido.

La UI no resta dinero.

La UI no modifica stats directamente.

---

## Errores comunes

```txt
meter gameplay en UIManager,
hacer singleton global innecesario,
actualizar UI cada frame,
referencias viejas al cambiar escena,
UIManager con demasiados paneles y reglas,
no separar vistas específicas,
botones llamando directamente a sistemas internos,
UI modificando economía,
UI instanciando objetos de gameplay,
UI decidiendo victoria o derrota.
```

---

## Señales de UIManager peligroso

Alertas:

```txt
UIManager tiene referencias a GameManager, AudioManager, SaveManager, LevelManager, Factory, Spawner y Economy.
UIManager tiene métodos como BuyTower, DealDamage, SaveGame o SpawnEnemy.
UIManager modifica dinero directamente.
UIManager instancia prefabs de gameplay.
UIManager tiene Update para refrescar todo.
UIManager decide si una acción es válida.
UIManager tiene lógica de negocio.
```

Señal crítica:

```txt
Si un botón de UI puede romper reglas de gameplay,
la UI está demasiado acoplada.
```

---

## Cómo optimizar UIManager

Evitar:

```txt
actualizar todos los textos cada frame,
buscar objetos UI constantemente,
usar FindObjectOfType en interacción,
reconstruir paneles enteros sin necesidad,
suscribirse a eventos sin desuscribirse,
mantener referencias de escena destruidas.
```

Mejor:

```txt
actualización por eventos,
vistas pequeñas,
bind/unbind claro,
referencias serializadas,
modelos de vista si el proyecto lo necesita,
separación entre intención y ejecución,
UI pooling si hay elementos repetidos.
```

Ejemplo:

```txt
Antes:
MoneyText se actualiza en Update.

Después:
MoneyChanged
→ MoneyView.UpdateValue(newAmount)
```

---

## Checklist para IA/agente

Antes de modificar `UIManager`:

```txt
¿El cambio es visual o de gameplay?
¿La UI está decidiendo reglas?
¿Debería pasar por una facade?
¿Se actualiza por eventos?
¿Hay referencias de escena?
¿Se limpian al cambiar escena?
¿Hace falta UIManager o controlador local?
¿La API sigue siendo chica?
¿Hay lógica que debería estar en otro sistema?
¿Se está usando singleton por comodidad?
¿Se están tocando prefabs o escenas?
```

Antes de implementar una feature UI:

```txt
¿Qué intención captura la UI?
¿Qué sistema valida esa intención?
¿Qué sistema ejecuta la acción?
¿Qué evento informa el resultado?
¿Qué vista muestra el resultado?
```

---

## Regla final

`UIManager` coordina interfaz.

```txt
Sano:
muestra estado,
coordina pantallas,
escucha eventos,
captura intención.

Peligroso:
decide gameplay,
modifica economía,
instancia objetos,
y se convierte en dueño del flujo.
```

La regla central:

```txt
UI captura intención.
Gameplay decide.
UI muestra resultado.
```