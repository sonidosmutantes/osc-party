Jam experimental vía mensajes OpenSoundControl (OSC) orientada al livecoding

Instrucciones para participar:

• Opción 1: Poder generar mensajes OSC de algún tipo (patterns, controles físicos, funciones, etc)

• Opción 2: Sonificar en base a mensajes OSC

• Opción 3: Generar visuales en base a OSC



La convención de los mensajes será algo así: /nombreusuario/tipomensaje

Un server se encargará de graficar el histórico de cada label como para dar una idea de que tipo de dato genera cada uno. Esto estará accesible vía http y en una pantalla.

Los productores enviarán mensajes a una dirección de broadcast (les llega a todos) en una red especialmente configurada. Por ejemplo: 5.0.100.255:4330

Habrá convertidores midi-osc y traductores de mensajes (oscmux)

Ver ejemplos: https://github.com/sonidosmutantes/osc-party/tree/master/examples



Envento en FB: https://www.facebook.com/events/1380354618721827/

# Live-Coding Argentina

Recomendaciones: 

• Enviar mensajes con un rate menor a 20Hz.

• Traer todo preparado como para poder cambiar rápidamente los mensajes que utilizaran los sonificadores/visuales.

• OpenStageControl