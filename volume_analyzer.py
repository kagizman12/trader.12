# volume_analyzer.py

from tradingview_ta import TA_Handler, Interval
from config import VOLUME_SPIKE_MULTIPLIER

def analyze_volume(symbol):
    handler = TA_Handler(
        symbol=symbol,
        screener="turkey",
        exchange="BIST",
        interval=Interval.INTERVAL_1_DAY
    )

    try:
        analysis = handler.get_analysis()
        indicators = analysis.indicators

        current_volume = indicators.get("volume")
        avg_volume_5 = indicators.get("MA5")  # MA5 = 5 günlük hareketli ortalama (hacim dahil)

        if not current_volume or not avg_volume_5:
            return f"{symbol}: Hacim verisi eksik."

        if current_volume > avg_volume_5 * VOLUME_SPIKE_MULTIPLIER:
            return f"🔥 {symbol}: Hacim Patlaması! Volume: {current_volume}, Ort: {avg_volume_5}"
        elif current_volume < avg_volume_5 * 0.5:
            return f"⚠️ {symbol}: Çok düşük hacim. Volume: {current_volume}, Ort: {avg_volume_5}"
        else:
            return f"{symbol}: Hacim normal. Volume: {current_volume}, Ort: {avg_volume_5}"
    except Exception as e:
        return f"{symbol}: Veri alınamadı. Hata: {e}"
