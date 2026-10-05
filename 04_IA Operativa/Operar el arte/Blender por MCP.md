# Blender por MCP

## Qué hace Vaultrum acá

Modela, verifica y renderiza en el Blender de la PC del owner. Es la superficie donde nació el Área de Arte: doce assets, nueve reglas y el instrumento `arte.py`, todo operado por esta vía.

## Con qué opera la IA

El servidor MCP de Blender conectado a la PC expone, entre otras, estas herramientas:

```txt
execute_blender_code          corre Python con bpy dentro de Blender. Lo que se devuelve
                              va en una variable `result`
get_objects_summary           la jerarquia de collections y objetos, sin capturas
get_blendfile_summary_*       datablocks, archivos faltantes, librerias enlazadas. Tienen
                              variantes _for_cli que leen un .blend sin abrir la interfaz
search_manual_docs            busqueda en el manual de Blender que viene con el servidor
get_python_api_docs           la documentacion de la API para un identificador exacto
render_viewport_to_path       render de la escena a un archivo
get_screenshot_of_*           capturas de la interfaz (caras: ver abajo)
```

Blender Lab publica un servidor MCP oficial (`73_Blender_Lab_MCP_Server`); también hay alternativas de la comunidad. Cuál está instalado lo dice el propio servidor; las reglas de abajo valen para cualquiera.

## Cómo se pone en marcha

```txt
1  Blender abierto en la PC (el servidor oficial pide 5.1 o posterior)
2  el complemento o servidor MCP activo en Blender
3  la app de escritorio de Claude abierta en esa PC, y la conversacion vinculada a ella
4  el .blend del proyecto guardado: la IA trabaja sobre lo que esta abierto
```

Si las herramientas de Blender no aparecen, no es un error de Vaultrum: Blender o el puente no están corriendo.

**Seguridad.** `execute_blender_code` corre código en la PC del owner, y el servidor oficial advierte que lo hace sin salvaguardas. Vaultrum no ejecuta nada que toque archivos fuera del proyecto, y guarda una copia del `.blend` antes de cualquier operación que no se pueda deshacer.

## Las reglas de operación

Medidas en `AiCare_Blender` sobre sesiones reales. Una sesión gastó **~20.7k tokens en Blender, y el 54% fueron capturas de pantalla**.

```txt
1  verificar por instrumento, mirar por render   la malla se prueba con arte.malla():
                                                 vuelve en ~300 caracteres. Una captura
                                                 no prueba nada que el instrumento no
                                                 pruebe mejor
2  renderizar el asset, no capturar la pantalla  Workbench a archivo: no compila shaders,
                                                 no depende de que la UI repinte. Tres
                                                 capturas seguidas volvieron rotas con
                                                 la ventana congelada: ~3.4k tokens de nada
3  si hay que capturar: el area, no la ventana   -29% por imagen, y en la misma llamada
                                                 forzar modo objeto y sombreado solido
4  el script grande va a disco                   todo asset de mas de ~150 lineas se
                                                 escribe antes de la primera ejecucion;
                                                 cada iteracion es una linea
5  el instrumento va adentro del build           exec de arte.py una vez por sesion, y
                                                 malla(leer_coleccion("X")) en una linea
6  la API se busca, no se adivina                search_manual_docs y get_python_api_docs
                                                 antes de escribir una llamada que no se
                                                 conoce: la API cambia entre versiones
```

## Dos trampas de la herramienta, y cómo las compensa la IA

Las leyes y el contrato del Área de Arte **no cambian**. Lo que la IA tiene que saber es dónde la herramienta exporta o mide distinto de lo que la ley dice, y compensarlo al operarla. Decisión del owner, 2026-10-04.

### El frente al exportar

El contrato del asset dice *mira a +Y*. Los exportadores de Blender no piensan todos igual:

```txt
glTF (.glb)   lleva el -Y de Blender al frente del formato (+Z de glTF). No tiene
              opcion de "adelante": solo export_yup. Un asset que mira a +Y sale
              MIRANDO PARA ATRAS
FBX           tiene axis_forward y axis_up: el frente se elige al exportar
```

Cómo se compensa:

```txt
1  el .blend no se toca      el asset sigue mirando a +Y, como dice el contrato
2  glTF                      se exporta desde una COPIA girada 180 grados en Z
                             alrededor del origen, con la rotacion aplicada; la
                             copia se borra despues. Origen y apoyo no cambian
   FBX                       axis_forward segun el contrato del cliente, sin girar nada
3  se verifica en el archivo la ley 6 (arte.entrega()) lee el archivo ENTREGADO: el
   entregado                 frente tiene que quedar donde lo espera el cliente
```

Si el cliente no declaró su convención, se pregunta antes de exportar. Si no hay a quién preguntar, se exporta en la convención del formato y se declara en el `ART`.

### Las normales que el instrumento no ve

La ley 1 dice *todo mira afuera*. `arte.malla()` lo mide con el **signo del volumen** de cada pieza, sin redondear: ve una pieza **entera** dada vuelta, y **no ve unas pocas caras invertidas**, que solo achican el volumen y lo dejan positivo. Tres caras al revés de quinientas pasan.

Cómo se compensa: sobre el asset armado —después de emparentar— y en la misma llamada que corre `arte.malla()`, la IA corre la prueba cara por cara:

```python
import bmesh
bm = bmesh.new(); bm.from_mesh(obj.data)
aristas_al_reves = sum(1 for e in bm.edges if e.is_manifold and not e.is_contiguous)
bm.free()
```

`is_contiguous` es falso en una arista cerrada cuyas dos caras tienen orientaciones opuestas, y cada cara dada vuelta deja todas sus aristas así. Las dos pruebas juntas cubren los dos casos:

```txt
signo del volumen       la pieza ENTERA mira adentro
aristas no contiguas    ALGUNAS caras miran al reves
```

El `ART` declara la ley 1 con las dos. Si `aristas_al_reves` da más de cero, la ley 1 **no** está en ley aunque `arte.malla()` diga que sí.

## Cómo pedírselo

```txt
modelar     "Modela <asset> para <proyecto>, familia <familia>. La mitad A esta cerrada.
             Referencia: <archivo>. Entrega la collection <Nombre> y el ART con las seis
             leyes medidas."
pasada      "Pasada sobre la collection <set>: medi el conjunto y reporta antes de tocar."
probar      "Probá el rig de <personaje> en estas poses: <lista>. Medi solapes en cada una."
render      "Render Workbench de <asset> desde la camara de juego, a <tamano>."
```

## Qué verifica y con qué

Leyes 1, 2 y 3 con `arte.malla()` sobre el asset **ya emparentado**; ley 4 con `arte.presupuesto()`; ley 5 con `arte.paleta()`; ley 6 con `arte.entrega()` leyendo el `.glb` o el `.fbx` exportado.

## Lo que no hace

No decide la dirección de arte. No aprueba un asset por cómo se ve en un render. No toca archivos fuera del proyecto.
