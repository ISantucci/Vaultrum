## Definicion

Separacion model view consiste en dividir lo que el juego es de lo que el juego muestra.

```txt
Model
→ estado
+ reglas

View
→ representacion Unity
```

El modelo sabe cuanta vida tiene un enemigo, cuanto daño recibe y cuando muere.

La View sabe que hay un GameObject, un mesh, un animator y una barra flotante que reflejan eso.

```txt
El modelo decide.
La View muestra.
```

La separacion no es exclusivamente una optimizacion.

Pero una buena arquitectura permite optimizar sin romper comportamiento, y eso la vuelve una pieza de esta seccion.

```txt
Si EnemySystem es costoso,
deberia poder modificarse sin reescribir
UI, camara, input ni audio.
```

---

## Que problema ayuda a prevenir

Ayuda a prevenir:

```txt
Logica repartida por GameObjects.
Reglas de gameplay escritas dentro de la UI.
Sistemas imposibles de medir por separado.
Dependencias cruzadas entre gameplay, audio, UI y VFX.
Update por objeto sin control de frecuencia.
Optimizaciones que obligan a tocar media base de codigo.
```

Tambien previene un patron de acoplamiento muy comun.

```txt
La clase que dispara
tambien reproduce el sonido,
actualiza la municion en pantalla
y lanza el efecto de fogonazo.
```

Cambiar el disparo pasa a significar tocar audio, interfaz y efectos.

---

## Como funciona

El modelo es logica sin dependencia del engine.

```csharp
public class EnemyModel
{
    public int Health { get; private set; }
    public event Action<int> HealthChanged;

    public void TakeDamage(int amount)
    {
        Health -= amount;
        HealthChanged?.Invoke(Health);
    }
}
```

La View traduce ese estado a Unity.

```csharp
public class EnemyView : MonoBehaviour
{
    [SerializeField] private Image healthBar;

    public void Bind(EnemyModel model)
    {
        model.HealthChanged += OnHealthChanged;
    }

    private void OnHealthChanged(int value)
    {
        healthBar.fillAmount = value / 100f;
    }
}
```

La View no calcula daño.

El modelo no conoce la barra.

Sobre esa base se agrega la segunda idea: el gameplay emite un hecho y otros sistemas reaccionan.

```txt
WeaponFiredEvent
    ↓
AudioSystem
UISystem
VFXSystem
```

En vez de acoplar disparo, audio, interfaz y efectos en la misma clase, cada sistema se suscribe a lo que le importa.

```txt
Cada observer
→ ejecuta solamente cuando ocurre el evento
```

Ese criterio quedo consolidado en Capsule Survivor y Project Forge, donde los sistemas de gameplay dejaron de conocer a los sistemas de presentacion.

---

## Como aplicarlo en videojuegos

Candidatos claros a modelo:

```txt
Vida, daño y muerte.
Economia y costos.
Progresion y upgrades.
Estado de oleadas.
Inventario.
Reglas de construccion.
Timers de gameplay.
```

Candidatos claros a View:

```txt
Barras y numeros en pantalla.
Animaciones.
Particulas.
Sonido.
Camara.
Feedback de seleccion.
```

Ejemplo en un Tower Defense:

```txt
EconomyModel
    dinero y costos

TowerBuildSystem
    valida y aplica la construccion

TowerView
    instancia la torre en escena

HUD
    muestra el dinero restante
```

Y el flujo por eventos:

```txt
Jugador confirma construccion
→ TowerBuildSystem valida y descuenta
→ TowerBuiltEvent
→ HUD actualiza dinero
→ AudioSystem reproduce sonido
→ VFXSystem lanza el efecto de aparicion
```

Cada sistema hace una sola cosa y ninguno depende de los otros.

---

## Relacion con arquitectura

Se relaciona con:

```txt
Clases puras.
MonoBehaviour como puente.
Batch processing.
UI orientada a eventos.
Observer.
```

La separacion habilita el recorrido agrupado.

```txt
Modelos en una coleccion
→ un sistema los recorre
→ las Views reflejan el resultado
```

Y habilita control real sobre la actualizacion.

```txt
Quien actualiza
→ el sistema

Cada cuanto
→ decision explicita

En que orden
→ decision explicita
```

Con la logica repartida por GameObjects, ninguna de esas tres preguntas tiene una respuesta clara.

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
CPU
Frame Budget
```

Puede afectar tambien:

```txt
Memoria
```

por las estructuras de modelo que conviven con las representaciones de escena.

La separacion no optimiza sola.

```txt
Separar
≠
ir mas rapido
```

Lo que aporta es capacidad de intervencion.

```txt
Sistema aislado
→ medible por separado
→ reemplazable por separado
→ ajustable en frecuencia
→ testeable sin escena
```

Es la diferencia entre poder cambiar un algoritmo y tener que negociar con toda la base de codigo para hacerlo.

---

## Cuando conviene usarlo

Conviene cuando:

```txt
Las reglas de gameplay tienen peso propio.
Muchas entidades comparten la misma logica.
Hace falta medir o testear sistemas por separado.
La presentacion cambia mas seguido que las reglas.
Hay varios sistemas reaccionando al mismo hecho.
Se espera que el proyecto crezca.
```

Casos claros:

```txt
Economia y progresion.
Combate con reglas de daño.
Sistemas de oleadas.
Inventario y crafteo.
Cualquier gameplay con muchas entidades semejantes.
```

---

## Cuando NO conviene usarlo

No conviene cuando:

```txt
El comportamiento es puramente visual.
El objeto depende de componentes de escena todo el tiempo.
El prototipo es chico y va a descartarse.
La separacion agrega mas piezas que valor.
```

Ejemplo:

```txt
Un cartel que rota
→ puede ser un MonoBehaviour y nada mas.
```

Y hay un extremo que conviene evitar:

```txt
EnemyView
EnemyModel
EnemyLogic
EnemyData
EnemyAdapter

para un enemigo de prototipo.
```

Eso es sobrearquitectura, no separacion.

---

## Trade-offs

Ventajas:

```txt
Logica concentrada y no repartida por la escena.
Menos dependencias entre sistemas.
Control sobre que se actualiza y cuando.
Sistemas testeables sin escena.
Perfilado mas claro.
Presentacion reemplazable sin tocar reglas.
```

Costos:

```txt
Mas clases y mas archivos.
Sincronizacion entre modelo y representacion.
Mas diseño previo.
Indireccion adicional al leer el codigo.
Riesgo de estado duplicado.
```

---

## Riesgos de aplicarlo mal

El riesgo central es el estado duplicado.

```txt
El modelo guarda la vida.
La View guarda su propia copia para la barra.
Alguien actualiza una y no la otra.
```

A partir de ahi el juego tiene dos verdades y ninguna es confiable.

La pregunta que hay que poder responder de cada dato es una sola:

```txt
¿Quien es el dueño de este dato?
```

La respuesta debe ser un unico sistema.

```txt
Un dueño
→ escribe

Todos los demas
→ leen o reciben eventos
```

Otros riesgos:

```txt
Views que modifican el modelo directamente.
Modelos que conocen componentes de Unity.
Eventos emitidos aunque el dato no haya cambiado.
Views que no se desuscriben.
Views que nunca reciben el estado inicial.
Cadenas de eventos donde nadie sabe quien disparo que.
```

Ejemplo de riesgo real:

```txt
La View descuenta vida para animar el golpe
antes de que el modelo confirme el daño.

Resultado:
enemigos que se ven muertos y siguen vivos.
```

---

## Checklist de implementacion

```txt
¿Que parte es estado y reglas y que parte es representacion?
¿Quien es el dueño de cada dato?
¿Hay estado duplicado entre modelo y View?
¿La View modifica el modelo directamente?
¿El modelo depende de tipos de Unity?
¿Como se entera la View de un cambio?
¿La View recibe el estado inicial?
¿La View se desuscribe?
¿El evento se emite solo cuando el dato cambia?
¿Quien actualiza el modelo y cada cuanto?
¿Se puede optimizar el sistema sin tocar UI, camara, input ni audio?
¿Se puede testear el modelo sin escena?
```

---

## Regla final

El estado tiene un dueño y la pantalla es un espejo.

```txt
El modelo decide, la View refleja.
Un hecho, muchos observadores.
Si un dato vive en dos lugares, uno de los dos va a mentir.
```
