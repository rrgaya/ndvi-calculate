# NDVI

NDVI (Normalized Difference Vegetation Index) ou Índice de Diferença
de vegetação normalizada é utilizado para analisar a saúde da cultura
agrícola. Após o processamento da imagem de satélite, regiões com pixels
com valores altos de NDVI significam alto vigor vegetativo (valores próximos
a 1.0). Regiões com pixels com valores baixos significam problemas de
produção agrícola (valores próximos a 0.0).

Regiões com pixels com valores baixos significam problemas de
produção agrícola (valores próximos a 0.0). A fórmula é simples, NDVI =
(NIR – RED) / (NIR+RED). No caso das imagens fornecidas, NDVI = (B4 –
B3) / (B4 + B3).

- Entrada: Imagem analítica no formato GeoTiff.
- Saída: Imagem GeoTiff NDVI processada.

$ python ndvi.py