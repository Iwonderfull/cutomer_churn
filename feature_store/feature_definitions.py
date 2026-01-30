from datetime import timedelta

from feast import Entity, FeatureService, FeatureView, Field, FileSource, Project, ValueType
from feast.types import Float32, Int32, String

project = Project(
    name="customer_churn",
    description="Проект для прогнозирования оттока клиентов",
    tags=dict(),
)

source = FileSource(
    path="/home/tii/datasets/customer_churn/telco-customer-churn-with-ts.parquet",
    name="customer_churn_data",
    created_timestamp_column="timestamp",
    # field_mapping=dict(event_timestamp="timestamp"),
    description="Customer churn source",
    owner="tii",
    tags=dict(purpose="test", team="ML"),
)

customer_entity = Entity(
    name="customer_entity",
    join_keys=["customerID"],
    value_type=ValueType.STRING,
)

cusotmer_churn_view = FeatureView(
    name="cutomer_churn_view",
    source=source,
    schema=[
        # Field(name="timestamp", dtype=UnixTimestamp),``
        Field(name="Churn", dtype=String),
        Field(name="Contract", dtype=String),
        Field(name="Dependents", dtype=String),
        Field(name="DeviceProtection", dtype=String),
        Field(name="gender", dtype=String),
        Field(name="InternetService", dtype=String),
        Field(name="MonthlyCharges", dtype=Float32),
        Field(name="MultipleLines", dtype=String),
        Field(name="OnlineBackup", dtype=String),
        Field(name="OnlineSecurity", dtype=String),
        Field(name="PaperlessBilling", dtype=String),
        Field(name="Partner", dtype=String),
        Field(name="PaymentMethod", dtype=String),
        Field(name="PhoneService", dtype=String),
        Field(name="SeniorCitizen", dtype=Int32),
        Field(name="StreamingTV", dtype=String),
        Field(name="StreamingMovies", dtype=String),
        Field(name="TechSupport", dtype=String),
        Field(name="tenure", dtype=Int32),
        Field(name="TotalCharges", dtype=Float32),
    ],
    entities=[customer_entity],
    ttl=timedelta(days=0),
    online=False,
    offline=True,
    description="Customer churn data",
    owner="tii",
    tags=dict(purpose="test", team="ML"),
)

service = FeatureService(
    name="customer_churn_service",
    features=[cusotmer_churn_view],
    owner="tii",
    tags=dict(purpose="test", team="ML"),
    description="Test service for cutomer churn forecasting",
)
