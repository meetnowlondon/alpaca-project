"""
Storage callbacks for persisting user settings in localStorage
"""

from dash import Input, Output, State, callback_context as ctx, no_update
from webui.utils.storage import get_default_settings

def register_storage_callbacks(app):
    """Register storage-related callbacks"""

    # Callback to save settings to localStorage when they change
    @app.callback(
        Output("settings-store", "data"),
        [
            Input("ticker-input", "value"),
            Input("analyst-market", "value"),
            Input("analyst-social", "value"),
            Input("analyst-news", "value"),
            Input("analyst-fundamentals", "value"),
            Input("analyst-macro", "value"),
            Input("research-depth", "value"),
            Input("allow-shorts", "value"),
            Input("loop-interval", "value"),
            Input("market-hours-input", "value"),
            Input("trade-after-analyze", "value"),
            Input("trade-dollar-amount", "value"),
            Input("quick-llm", "value"),
            Input("deep-llm", "value")
        ],
        [
            State("settings-store", "data"),
            State("loop-enabled", "value"),
            State("market-hour-enabled", "value")
        ],
        prevent_initial_call=True
    )
    def save_settings(ticker_input, analyst_market, analyst_social, analyst_news,
                     analyst_fundamentals, analyst_macro, research_depth, allow_shorts,
                     loop_interval, market_hours_input,
                     trade_after_analyze, trade_dollar_amount, quick_llm, deep_llm,
                     current_settings, loop_enabled, market_hour_enabled):
        """Save settings to localStorage store"""

        # Get the trigger to check which input changed
        trigger = ctx.triggered[0]["prop_id"].split(".")[0] if ctx.triggered else None

        # Don't update if no trigger or if triggered by settings-store itself
        if not trigger or trigger == "settings-store":
            return no_update

        new_settings = {
            "ticker_input": ticker_input,
            "analyst_market": analyst_market,
            "analyst_social": analyst_social,
            "analyst_news": analyst_news,
            "analyst_fundamentals": analyst_fundamentals,
            "analyst_macro": analyst_macro,
            "research_depth": research_depth,
            "allow_shorts": allow_shorts,
            "loop_enabled": loop_enabled,
            "loop_interval": loop_interval,
            "market_hour_enabled": market_hour_enabled,
            "market_hours_input": market_hours_input,
            "trade_after_analyze": trade_after_analyze,
            "trade_dollar_amount": trade_dollar_amount,
            "quick_llm": quick_llm,
            "deep_llm": deep_llm
        }

        return new_settings
