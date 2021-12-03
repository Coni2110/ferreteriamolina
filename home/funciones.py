import pandas as pd
import numpy as np

def aislar_datos(ventas,minimo,actual,proveedor):

    


    minimo['STOCK MINIMO']=minimo['STOCK MINIMO MATILDE']+minimo['STOCK MINIMO BULNES']+minimo['STOCK MINIMO BODEGA']
    actual['STOCK TOTAL']=actual['CASAMATRIZ']+actual['CASAMATRIZ']+actual['BODEGA']
    ventas['STOCK RECOMENDADO']=ventas['VENTAS'].div(10)
    ventas['STOCK RECOMENDADO']=round(ventas['STOCK RECOMENDADO'],0)
    merge=pd.merge(ventas,actual)
    merge=pd.merge(merge,minimo)
    merge=pd.merge(merge,proveedor)
    
    merge['COMPRA MINIMA']=  merge['STOCK TOTAL'] - merge['STOCK MINIMO'] 
    
    for dato in merge['COMPRA MINIMA']:
        if dato < 0:
            dato=0

    merge=merge[['CODIGO','DESCRIPCION','STOCK RECOMENDADO','STOCK TOTAL','STOCK MINIMO','COMPRA MINIMA','SUBCATEGORIA3','NOMBRE PROVEEDOR']]

    return merge

def explorar_datos(merge):


    merge['dif_mat']=merge['stock_mat'] - merge['min_mat']
    merge['dif_bul']=merge['stock_bul'] - merge['min_bul']
    merge['dif_bod']=merge['stock_bod'] - merge['min_bod']



    #merge_matu=merge[merge['dif_mat']<0]

    return merge

def articulos_bodega_criticos(df):
    df_critico_bodega=df[df['dif_bod']<0]

    df_critico_bodega=df_critico_bodega[['cod_art','stock_bod', 'dif_bod',]]
    return df_critico_bodega