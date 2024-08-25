import pandas as pd
from io import StringIO

def load_sales_data(file) -> pd.DataFrame:
    """
    Carga los datos de ventas desde un archivo CSV.
    
    Args:
        file (UploadFile): El archivo CSV cargado a través de FastAPI.
    
    Returns:
        pd.DataFrame: Un DataFrame de Pandas con los datos de ventas cargados.
    """
    content = file.file.read().decode('utf-8')
    df = pd.read_csv(StringIO(content))
    return df

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia los datos de ventas eliminando valores nulos y corrigiendo formatos.
    
    Args:
        df (pd.DataFrame): El DataFrame de ventas sin limpiar.
    
    Returns:
        pd.DataFrame: El DataFrame de ventas limpio.
    """
    # Eliminar filas con valores nulos
    df.dropna(inplace=True)

    # Convertir columnas a los tipos adecuados
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['sales'] = pd.to_numeric(df['sales'], errors='coerce')

    # Eliminar filas con conversiones inválidas
    df.dropna(inplace=True)
    
    return df

def analyze_sales_data(df: pd.DataFrame) -> dict:
    """
    Realiza un análisis básico de los datos de ventas.
    
    Args:
        df (pd.DataFrame): El DataFrame de ventas limpio.
    
    Returns:
        dict: Un diccionario con los resultados del análisis.
    """
    # Ejemplo de análisis: total de ventas por día
    total_sales_by_day = df.groupby(df['date'].dt.date)['sales'].sum().to_dict()
    
    # Estadísticas descriptivas
    descriptive_stats = df['sales'].describe().to_dict()

    # Analizar tendencias (por ejemplo, crecimiento porcentual)
    df['daily_change'] = df['sales'].pct_change().fillna(0)
    daily_change_stats = df['daily_change'].describe().to_dict()
    
    return {
        "total_sales_by_day": total_sales_by_day,
        "descriptive_stats": descriptive_stats,
        "daily_change_stats": daily_change_stats
    }

def process_sales_data(file) -> dict:
    """
    Función principal para procesar los datos de ventas.
    
    Args:
        file (UploadFile): El archivo CSV cargado a través de FastAPI.
    
    Returns:
        dict: Un diccionario con los resultados del análisis de ventas.
    """
    df = load_sales_data(file)
    df = clean_sales_data(df)
    analysis_results = analyze_sales_data(df)
    
    return analysis_results