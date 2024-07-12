from evidently.dashboard import Dashboard
from evidently.tabs import DataDriftTab

dashboard = Dashboard(tabs=[DataDriftTab()])
dashboard.calculate(reference_data, current_data)
dashboard.save("dashboard.html")


from evidently.dashboard import Dashboard
from evidently.tabs import DataDriftTab, ModelPerformanceTab

def monitor_model(reference_data, current_data, model):
    dashboard = Dashboard(tabs=[DataDriftTab(), ModelPerformanceTab()])
    dashboard.calculate(reference_data, current_data, model)
    dashboard.save("model_monitoring_dashboard.html")