from django.shortcuts import render
from .resources import *
from home.models import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from pathlib import Path
from .funciones import *
import pandas as pd
from io import BytesIO
# Create your views here.

@login_required(login_url='/accounts/login/')
def Aplicacionhome(request):
        

    return render(request, "home.html")

@login_required(login_url='/accounts/login/')
def reporte(request):

    merge=pd.DataFrame()
    col=pd.DataFrame()
    
    if request.method == 'POST':

        ventas=pd.read_excel(request.FILES["ventas"])
        stock_actual=pd.read_excel(request.FILES["stock_actual"])
        stock_minimo=pd.read_excel(request.FILES["stock_minimo"])
        proveedor=pd.read_excel(request.FILES["proveedores"])
        reposicion=pd.read_excel(request.FILES["reposicion"])


        proveedor=proveedor.rename(columns={'COD_ART':'CODIGO'})
        ventas=ventas.rename(columns={ventas.columns[2]:'VENTAS'})



        merge=aislar_datos(ventas, stock_minimo, stock_actual, proveedor)
        merge['ULTIMO_PRECIO']=reposicion['ULTIMO PRECIO COMPRA']

       

        print(merge.columns)
        


        
        return render(request, 'reporte.html' ,{ 'merge': merge.to_html(classes=['table','table-responsive']) ,})


    return render(request, 'reporte.html' )

@login_required(login_url='/accounts/login/')
def traspaso(request):

    

    merge=pd.DataFrame()
    col=pd.DataFrame()
    
    if request.method == 'POST':

        stock_actual=pd.read_excel(request.FILES["stock_actual"])
        stock_minimo=pd.read_excel(request.FILES["stock_minimo"])

        merge=pd.merge(stock_actual, stock_minimo, on='CODIGO')

        merge['DIF_MAT']=merge['CASAMATRIZ'] - merge['STOCK MINIMO MATILDE']
        merge['DIF_BUL']=merge['SUCURSAL'] - merge['STOCK MINIMO BULNES']
        merge['DIF_BOD']=merge['BODEGA'] - merge['STOCK MINIMO BODEGA']

        merge=merge[['CODIGO','DESCRIPCION_x','DIF_MAT','DIF_BUL','DIF_BOD','CASAMATRIZ','SUCURSAL','BODEGA']]
        return render(request, 'traspaso.html' ,{ 'merge': merge.to_html(classes=['table','table-responsive']) ,})


    return render(request, 'traspaso.html' )

@login_required(login_url='/accounts/login/')
def ventas(request):
    pand=pd.DataFrame()


    if request.method == 'POST':
            


    
        pand=pd.read_excel(request.FILES["ventas"])




    return render(request, "ventas.html",{'df2':pand.to_html(classes='table')})