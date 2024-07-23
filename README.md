
# Autómata Unidimensional - Regla 30

Este proyecto implementa un autómata celular unidimensional utilizando la Regla 30. El objetivo es generar y visualizar la evolución de un sistema complejo a partir de un patrón simple, proporcionando una herramienta educativa para entender los autómatas celulares.

## Descripción

La **Regla 30** es una regla de autómata celular unidimensional que fue introducida por el matemático Stephen Wolfram. Este software ilustra cómo patrones simples pueden evolucionar con el tiempo a partir de una celda activa. La visualización resultante ayuda a estudiar la dinámica y el comportamiento de los autómatas celulares.

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalados los siguientes paquetes de Python:

- `matplotlib`: para la visualización gráfica.
- `numpy`: para la manipulación de arrays y operaciones matemáticas.

Puedes instalar estos paquetes usando `pip` con el siguiente comando:

```bash
pip install matplotlib numpy
```
Puedes instalar estos paquetes usando `apt` con el siguiente comando en sistemas donde existen impedimentos de usar pip sin un entorno de python:
```bash
sudo apt install python3-matplotlib
sudo apt install python3-numpy
```

Puedes instalar estos paquetes usando venv para crear un entorno de python virtual donde dentro de este se instale las librerias

```bash
python3 -m venv env
source env/bin/activate
pip install matplotlib numpy
```



## Uso

1. **Clona el repositorio** o descarga los archivos del proyecto.
2. **Ejecuta el script** `main.py` usando Python:

   ```bash
   python main.py
   ```

3. **Visualiza el resultado**: El script generará una ventana con la visualización del autómata celular unidimensional utilizando la Regla 30.

## Configuración

El archivo `main.py` tiene las siguientes variables de configuración:

- `SIZE`: Tamaño de la fila de celdas. Ajusta este valor para cambiar el ancho de la visualización.
- `GENERACIONES`: Número de generaciones que se van a simular. Cambia este valor para ver cómo evoluciona el patrón a lo largo del tiempo.

```python
SIZE = 101  # Tamaño de la fila de celdas
GENERACIONES = 50  # Número de generaciones
```

## Contribuciones

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu feature (`git checkout -b feature-nueva`).
3. Realiza tus cambios y haz commits (`git commit -am 'Agrega nueva feature'`).
4. Envía un pull request (`git push origin feature-nueva`).

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Para preguntas o más información, puedes contactar a:

- **Autor:** Andrés Eduardo García Márquez
- **Correo electrónico:** andresgarcia0313@gmail.com
