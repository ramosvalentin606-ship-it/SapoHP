# Para mi amor
Descomprime el proyecto y agrega tus recuerdos a media/. Usa JPG real para las tres fotos y MP4 con video H.264 y audio AAC para el clip. Conserva exactamente los nombres de media/LEEME.txt. Puedes probar el recorrido incluso mientras faltan archivos.

Personaliza CARTA, RECUERDOS (el último texto de cada fila es el pie de foto), RAZON, SECRETO y DESPEDIDA al comienzo de App.py. Guarda el archivo en UTF-8.

Para probar en tu computador abre la terminal en la carpeta donde está App.py:
```sh
python -m pip install -r requirements.txt
python -m streamlit run App.py
```

Para publicarla, sube el contenido descomprimido, incluidas media/ y .streamlit/, a un repositorio nuevo. En Streamlit Community Cloud crea una aplicación con ese repositorio, la rama que usaste y App.py como archivo principal. Las elecciones viven en la sesión del navegador. La pantalla de resumen pide una captura para compartirlas.
